"""The picture track of one short: successive shots in which colour paints itself into the pencil drawing.

  python3 film.py <short> <take>      writes art/<short>/picture.mp4 (1080x1920, 30 fps, silent) and shots.json

Shot list (each shot lasts as long as its voice lines in voice/<short>/lines.json, plus GAP after each line):
  sparse    first line over the finished colour scene (the hook), then cut to the plain request in pencil
  sketch    deeper's plan: the full pencil drawing, a cut
  <object>  one per region: punch in on it while its colour spreads in strokes over PAINT seconds
  colour    pull back while the rest of the frame paints in
Every frame is a function of its index (fixed noise seed), so a render is identical every time.
"""
import json, pathlib, subprocess, sys
import cv2
import numpy as np

HERE = pathlib.Path(__file__).parent
W, H, FPS = 1080, 1920, 30
PAINT = 0.8                      # seconds for colour to spread across one object
TOP = 300                        # the picture sits under a white band that carries the headline
GAP = 0.35                       # breath after each spoken line


def stroke_field(shape, seed):
    """A paint order in [0, 1]: diagonal sweep + soft noise + streaks along the stroke direction."""
    h, w = shape
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    sweep = (xx / w * 0.6 + yy / h * 0.4)
    noise = cv2.resize(rng.random((h // 64 + 2, w // 64 + 2)).astype(np.float32), (w, h), interpolation=cv2.INTER_CUBIC)
    streak = cv2.GaussianBlur(rng.random((h, w)).astype(np.float32), (0, 0), sigmaX=22, sigmaY=2)
    f = sweep * 0.55 + noise * 0.3 + (streak - streak.mean()) * 4 * 0.15
    return (f - f.min()) / (f.max() - f.min())


def reveal(field, mask, p):
    """Mask revealed up to progress p, with a 4% soft edge so strokes look wet rather than cut."""
    inside = field[mask > 0.5]
    if inside.size == 0:
        return mask
    lo, hi = inside.min(), inside.max()
    t = lo + (hi - lo) * p
    return mask * np.clip((t - field) / 0.04 + 0.5, 0, 1)


def frame_of(img, centre, zoom):
    """Crop around centre at zoom, fill the 1080-wide picture area below the headline band."""
    ih, iw = img.shape[:2]
    ph = H - TOP
    cw = iw / zoom
    ch = cw * ph / W
    cx = np.clip(centre[0], cw / 2, iw - cw / 2)
    cy = np.clip(centre[1], ch / 2, ih - ch / 2)
    m = np.float32([[W / cw, 0, -(cx - cw / 2) * W / cw], [0, W / cw, -(cy - ch / 2) * W / cw + TOP]])
    out = cv2.warpAffine(img, m, (W, H), flags=cv2.INTER_CUBIC, borderValue=(255, 255, 255))
    out[:TOP] = 255
    return out


def ease(t):
    return t * t * (3 - 2 * t)


def main(short, take):
    d = HERE / "art" / short
    scene = json.loads((HERE / "scenes.json").read_text())[short]
    colour = cv2.imread(str(d / f"colour-{take}.png")).astype(np.float32)
    pencil = cv2.imread(str(d / f"pencil-{take}.png")).astype(np.float32)
    sparse = cv2.imread(str(d / f"sparse-{take}.png")).astype(np.float32)
    ih, iw = colour.shape[:2]
    whole = (iw / 2, ih / 2)
    script = json.loads((HERE / "scripts.json").read_text())[short]
    said = [l["seconds"] + GAP for l in json.loads((HERE / "voice" / short / "lines.json").read_text())]
    n_sp, n_sk, n_ob = len(script["sparse"]), len(script["sketch"]), len(script["objects"])
    lines_of = {"sparse": said[:n_sp], "sketch": said[n_sp:n_sp + n_sk]}
    obj = said[n_sp + n_sk:n_sp + n_sk + n_ob]
    colour_dur = said[n_sp + n_sk + n_ob]
    shots = []
    # A cut on every spoken line: wide, then closer. The close sketch shot looks at where deeper's additions are.
    near = (iw / 2, ih * 0.42)
    added = tuple(np.mean([((r["box"][0] + r["box"][2]) / 2, (r["box"][1] + r["box"][3]) / 2) for r in scene["regions"]], axis=0))
    framings = {"sparse": [((1.0, 1.06), whole), ((1.35, 1.45), near)], "sketch": [((1.06, 1.0), whole), ((1.2, 1.32), added)]}
    for name, base in (("sparse", sparse), ("sketch", pencil)):
        subs = [dict(dur=dur, zoom=f[0], centre=(f[1], f[1]), base=base) for dur, f in zip(lines_of[name], framings[name] * 3)]
        if name == "sparse":             # open on the result: frame 0 is the finished colour scene, then cut to the sketch
            subs[0] |= dict(base=colour, zoom=(1.12, 1.0))
        shots.append(dict(name=name, dur=sum(lines_of[name]), base=base, subs=subs))
    painted = np.zeros((ih, iw), np.float32)
    for i, r in enumerate(scene["regions"]):
        m = cv2.imread(str(d / f"mask-{r['name']}.png"), 0).astype(np.float32) / 255
        new = np.clip(m - painted, 0, 1)
        x0, y0, x1, y1 = r["box"]
        c = ((x0 + x1) / 2, (y0 + y1) / 2)
        z = min(2.8, max(1.3, iw / (x1 - x0) * 0.7))
        shots.append(dict(name=r["name"], dur=max(obj[i], 1.6), before=painted.copy(), new=new, seed=i + 1,
                          zoom=(z * 0.92, z), centre=(c, c)))
        painted = np.maximum(painted, m)
    rest = np.clip(1 - painted, 0, 1)
    shots.append(dict(name="colour", dur=colour_dur + 0.6, before=painted.copy(), new=rest, seed=99,
                      zoom=(1.25, 1.0), centre=(shots[-1]["centre"][1], whole)))

    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p",
                           str(d / "picture.mp4")], stdin=subprocess.PIPE)
    timeline, t0 = [], 0.0
    for s in shots:
        n = round(s["dur"] * FPS)
        field = stroke_field((ih, iw), s["seed"]) if "new" in s else None
        bounds = np.cumsum([round(u["dur"] * FPS) for u in s.get("subs", [])])
        for k in range(n):
            t = k / max(n - 1, 1)
            if "subs" in s:                      # which sub-shot this frame is in, and how far through it
                j = min(int(np.searchsorted(bounds, k, side="right")), len(bounds) - 1)
                k0 = bounds[j - 1] if j else 0
                t = (k - k0) / max(bounds[j] - k0 - 1, 1)
                s["zoom"], s["centre"], s["base"] = s["subs"][j]["zoom"], s["subs"][j]["centre"], s["subs"][j]["base"]
            if field is None:
                img = s["base"]
            else:
                p = ease(min(1.0, (k / FPS) / PAINT))
                m = np.maximum(s["before"], reveal(field, s["new"], p))
                m = cv2.GaussianBlur(m, (0, 0), 3)[..., None]
                img = pencil * (1 - m) + colour * m
            z = s["zoom"][0] + (s["zoom"][1] - s["zoom"][0]) * ease(t)
            (ax, ay), (bx, by) = s["centre"]
            c = (ax + (bx - ax) * ease(t), ay + (by - ay) * ease(t))
            ff.stdin.write(frame_of(img.astype(np.uint8), c, z).tobytes())
        timeline.append(dict(name=s["name"], start=round(t0, 3), dur=s["dur"]))
        t0 += n / FPS
    ff.stdin.close()
    ff.wait()
    (d / "shots.json").write_text(json.dumps(timeline, indent=1) + "\n")
    print(f"{d / 'picture.mp4'}: {t0:.2f}s, {len(shots)} shots")


main(sys.argv[1], sys.argv[2])
