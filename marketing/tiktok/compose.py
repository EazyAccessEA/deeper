"""One HyperFrames project per short: the painted picture track, the voice, captions, type and the end card.

  python3 compose.py <short> [...]    writes <short>/index.html and assets; then `cd <short> && npm run render`

Inputs: art/<short>/picture.mp4 and shots.json (film.py), voice/<short>/*.wav and lines.json (voice.py),
scripts.json (copy). Every word on screen is code-set type, never generated. Captions carry every spoken line for
people watching muted; during an object shot the caption is deeper's own insertion, in red after a caret.
Text stays in TikTok's safe band: y 168-1330, x <= 940.
"""
import html, json, pathlib, shutil, subprocess
import numpy as np
import sys, wave

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[1]
FONTS = ROOT / "site/node_modules/@fontsource"
CLI = "hyperframes@0.8.173"
GAP = 0.35
END_HOLD = 2.0

FONT_FILES = {
    "sg-400.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-400-normal.woff2",
    "sg-600.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-600-normal.woff2",
    "sg-700.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-700-normal.woff2",
    "sg-500i.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-500-italic.woff2",
    "jbm-400.woff2": "jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff2",
}

CSS = """
@font-face { font-family: "Schibsted Grotesk"; font-weight: 400; src: url(assets/fonts/sg-400.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 600; src: url(assets/fonts/sg-600.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 700; src: url(assets/fonts/sg-700.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 500; font-style: italic; src: url(assets/fonts/sg-500i.woff2); }
@font-face { font-family: "JetBrains Mono"; font-weight: 400; src: url(assets/fonts/jbm-400.woff2); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; background: #ffffff; }
#root { width: 1080px; height: 1920px; position: relative; font-family: "Schibsted Grotesk", sans-serif; color: #141414; }
#pic { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }
.head { position: absolute; left: 72px; top: 184px; width: 860px; height: 104px; display: flex; align-items: center; }
.head p { font-weight: 700; font-size: 54px; line-height: 1.02; letter-spacing: -0.035em; }
.head code { font-family: "JetBrains Mono", monospace; font-size: 36px; background: #f4f5f6; border-radius: 8px; padding: 16px 20px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 860px; }
.cap { position: absolute; left: 60px; width: 880px; bottom: 600px; display: flex; justify-content: flex-start; }
.cap p { background: rgba(255,255,255,0.94); border-radius: 10px; padding: 18px 24px; font-size: 44px; line-height: 1.22; font-weight: 600; letter-spacing: -0.015em; box-shadow: 0 2px 18px rgba(0,0,0,0.08); }
.cap.ins p { color: #d0241b; font-style: italic; font-weight: 500; font-size: 50px; display: flex; gap: 16px; align-items: baseline; }
.cap.ins img { width: 34px; height: 34px; flex: none; transform: translateY(3px); }
.qs { position: absolute; left: 60px; width: 880px; top: 330px; display: flex; flex-direction: column; gap: 14px; }
.qs p { align-self: flex-start; background: rgba(255,255,255,0.95); border-radius: 10px; padding: 14px 22px; font-size: 46px; font-weight: 600; letter-spacing: -0.02em; box-shadow: 0 2px 18px rgba(0,0,0,0.08); }
.qs p span { color: #d0241b; font-weight: 700; margin-right: 14px; }
#end { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; background: #ffffff; }
#end .in { position: absolute; left: 88px; top: 430px; width: 840px; }
#end .mark { width: 500px; height: auto; }
#end .line { margin-top: 64px; font-size: 52px; line-height: 1.25; letter-spacing: -0.02em; font-weight: 600; }
#end .cmd { margin-top: 44px; background: #f4f5f6; border-radius: 8px; padding: 28px 30px; font-family: "JetBrains Mono", monospace; font-size: 33px; }
#end .then { margin-top: 28px; font-size: 40px; color: #5b5f66; }
"""


def esc(s):
    return html.escape(s, quote=True)


def swish(path, seconds=0.8, seed=0, sr=48000):
    """A soft brush stroke: band-passed noise with a quick swell, the sound of the paint going on."""
    rng = np.random.default_rng(seed)
    n = int(seconds * sr)
    x = rng.normal(0, 1, n)
    spec = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / sr)
    spec *= np.exp(-((np.log(f + 1) - np.log(2600)) ** 2) / 0.7)        # centred near 2.6 kHz, soft sides
    x = np.fft.irfft(spec, n)
    t = np.linspace(0, 1, n)
    x *= np.sin(np.pi * t) ** 1.5 * (1 + 0.25 * np.sin(2 * np.pi * 9 * t))
    x = (x / np.abs(x).max() * 0.35 * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(x.tobytes())


def build(short):
    scripts = json.loads((HERE / "scripts.json").read_text())
    sc, end_line = scripts[short], scripts["_end"]
    shots = {s["name"]: s for s in json.loads((HERE / "art" / short / "shots.json").read_text())}
    order = json.loads((HERE / "art" / short / "shots.json").read_text())
    lines = json.loads((HERE / "voice" / short / "lines.json").read_text())
    pic_len = round(order[-1]["start"] + order[-1]["dur"], 3)

    d = HERE / short
    shutil.rmtree(d, ignore_errors=True)
    (d / "assets/fonts").mkdir(parents=True)
    (d / "assets/vo").mkdir()
    for out, src in FONT_FILES.items():
        shutil.copyfile(FONTS / src, d / "assets/fonts" / out)
    shutil.copyfile(ROOT / "brand/assets/mark.svg", d / "assets/mark.svg")
    shutil.copyfile(ROOT / "brand/assets/wordmark.svg", d / "assets/wordmark.svg")
    shutil.copyfile(HERE / "art" / short / "picture.mp4", d / "assets/picture.mp4")

    # When each spoken line starts: lines fill their shot in order, with GAP after each.
    groups = [("sparse", len(sc["sparse"])), ("sketch", len(sc["sketch"]))]
    groups += [(s["name"], 1) for s in order[2:2 + len(sc["objects"])]] + [("colour", 1)]
    starts, i = [], 0
    for name, n in groups:
        t = shots[name]["start"] + (0.25 if name == "sparse" else 0.1)
        for _ in range(n):
            starts.append(round(t, 2)); t += lines[i]["seconds"] + GAP; i += 1
    end_start = pic_len
    starts.append(round(end_start + 0.5, 2))
    total = round(max(end_start + 0.5 + lines[-1]["seconds"] + END_HOLD, end_start + 4.5), 2)

    media, clips, tweens = [], [], []
    media.append(f'<video id="pic" class="clip" src="assets/picture.mp4" muted playsinline data-start="0" '
                 f'data-duration="{pic_len}" data-track-index="0"></video>')
    for k, (l, t) in enumerate(zip(lines, starts)):
        shutil.copyfile(HERE / "voice" / short / l["file"], d / "assets/vo" / l["file"])
        media.append(f'<audio id="vo{k:02d}" class="clip" src="assets/vo/{l["file"]}" data-start="{t}" '
                     f'data-duration="{l["seconds"]}" data-volume="1" data-track-index="10"></audio>')
    for k, s in enumerate(order[2:]):
        swish(d / f"assets/swish{k}.wav", seed=k)
        media.append(f'<audio id="sw{k}" class="clip" src="assets/swish{k}.wav" data-start="{s["start"] + 0.03:.2f}" '
                     f'data-duration="0.8" data-volume="0.18" data-track-index="11"></audio>')

    def clip(id_, cls, start, dur, inner, track):
        clips.append(f'<div id="{id_}" class="{cls} clip" data-start="{start:.2f}" data-duration="{dur:.2f}" '
                     f'data-track-index="{track}">{inner}</div>')
        if start > 0:                                   # frame 0 is the thumbnail: what starts there is already on screen
            tweens.append(f'tl.fromTo("#{id_} > *", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "power2.out" }}, {start:.2f});')

    # Headline band: the launch line, then the command that does it, then the payoff.
    sp, sk, co = shots["sparse"], shots["sketch"], shots["colour"]
    clip("h0", "head", 0, sp["dur"], f"<p>{esc(sc['headline'])}</p>", 2)
    cmd = sc["request"][0].lower() + sc["request"][1:].rstrip(".?")
    size = min(36, int(800 / (0.62 * len(f"/deeper {cmd}"))))       # JetBrains Mono is ~0.6em wide: fit one line
    band = (f"<p>{esc(sc['band'])}</p>" if sc.get("band")          # a short that isn't a /deeper run names its point
            else f'<code style="font-size: {size}px">/deeper {esc(cmd)}</code>')
    clip("h1", "head", sk["start"], co["start"] - sk["start"], band, 2)
    clip("h2", "head", co["start"], co["dur"], f"<p>{esc(sc['payoff'])}</p>", 2)

    # Captions: every spoken line; deeper's insertion in red during its object shot.
    n_head = len(sc["sparse"]) + len(sc["sketch"])
    for k in range(len(lines) - 1):
        t, dur = starts[k], lines[k]["seconds"] + GAP * 0.8
        if n_head <= k < n_head + len(sc["objects"]):
            j = k - n_head
            clip(f"c{k}", "cap ins", t, dur,
                 f'<p><img src="assets/mark.svg" alt="" /><span>{esc(sc["objects"][j][1])}</span></p>', 3)
        else:
            clip(f"c{k}", "cap", t, dur, f"<p>{esc(lines[k]['text'])}</p>", 3)
        if "the expert's move" in lines[k]["text"]:     # the four questions land one by one as she names them
            qs = ["The expert's move", "The raw material", "The tools", "The check"]
            q0 = t + lines[k]["seconds"] * 0.42
            step = lines[k]["seconds"] * 0.58 / 4
            items = "".join(f'<p id="q{k}_{i}"><span>{i + 1}</span>{esc(q)}</p>' for i, q in enumerate(qs))
            clips.append(f'<div id="qs{k}" class="qs clip" data-start="{t:.2f}" data-duration="{dur + 0.3:.2f}" data-track-index="5">{items}</div>')
            for i in range(4):
                tweens.append(f'tl.fromTo("#q{k}_{i}", {{ opacity: 0, x: -16 }}, {{ opacity: 1, x: 0, duration: 0.22, ease: "power2.out" }}, {q0 + i * step:.2f});')

    end = (f'<div id="end" class="clip" data-start="{end_start}" data-duration="{round(total - end_start, 2)}" data-track-index="4">'
           f'<div class="in"><img id="wm" class="mark" src="assets/wordmark.svg" alt="deeper" />'
           f'<p id="e1" class="line">Free, for Claude Code, Codex and Cursor.</p>'
           f'<p id="e2" class="cmd">npx skills add EazyAccessEA/deeper</p>'
           f'<p id="e3" class="then">Then type /deeper and your task.</p></div></div>')
    tweens.append(f'tl.fromTo(["#wm", "#e1", "#e2", "#e3"], {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.35, stagger: 0.35 }}, {end_start + 0.1:.2f});')

    page = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      {chr(10).join('      ' + m for m in media)}
      {chr(10).join('      ' + c for c in clips)}
      {end}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join('      ' + t for t in tweens)}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
    (d / "index.html").write_text(page)
    (d / "package.json").write_text(json.dumps({
        "name": f"deeper-{short}", "private": True, "type": "module",
        "scripts": {k: f"npx --yes {CLI} {k}" for k in ("check", "render")} | {"dev": f"npx --yes {CLI} preview"}}, indent=2) + "\n")
    print(f"{short}: {total}s, picture {pic_len}s, {len(lines)} lines")


for s in sys.argv[1:]:
    build(s)
