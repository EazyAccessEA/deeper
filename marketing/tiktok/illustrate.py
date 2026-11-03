"""Pencil-to-colour illustrations for the deeper shorts, through Harvalor's Runware key and image checks.

The metaphor: the sparse pencil sketch is the task without deeper; the full-colour scene is the task with it.
So the colour frame is made first, and the sketch is derived from it by a Kontext edit that erases what deeper
adds. Each erased object comes back in colour on its insertion beat, and the lines register because both
frames share one composition.

  python3 illustrate.py <short> [seed ...]   generate colour (one per seed) + its sketch, then check both
Every Runware job and its cost goes to runware_jobs.json. No people, no faces, no text in any frame.
"""
import base64, hashlib, io, json, pathlib, sys, uuid

import cv2
import numpy as np
import requests
from PIL import Image

HERE = pathlib.Path(__file__).parent
HARVALOR = pathlib.Path.home() / "Projects/Harvalor"
sys.path.insert(0, str(HARVALOR))
from engine import config  # noqa: E402  key from Harvalor's .env, never printed
from engine.imagine import imagelint  # noqa: E402  macOS Vision text and face probes

COLOUR_MODEL, EDIT_MODEL = "openai:gpt-image@2", "bfl:4@1"   # GPT Image 2 (held strict rules in the YouTube tests); FLUX.1 Kontext
SIZE = (1024, 1536)       # 2:3, the same shape as Kontext's 832x1248
BUDGET_USD = 10.0
OUT, LOG = HERE / "art", HERE / "runware_jobs.json"

STYLE = ("Editorial illustration on plain bright white paper. Hand-drawn graphite pencil linework stays visible "
         "under flat gouache colour, like a finished pencil drawing that has been painted. Soft blues, warm greys, "
         "muted greens and one red accent, with plenty of white paper. Any person is seen from behind or turned "
         "fully away: no face is ever visible. No text, no letters, no numbers, no logos; screens and papers show "
         "only abstract shapes and lines.")

SCENES = json.loads((HERE / "scenes.json").read_text())


def log(entry):
    jobs = json.loads(LOG.read_text()) if LOG.exists() else []
    jobs.append(entry)
    LOG.write_text(json.dumps(jobs, indent=1) + "\n")
    return sum(j.get("cost_usd") or 0 for j in jobs)


def spent():
    return sum(j.get("cost_usd") or 0 for j in json.loads(LOG.read_text())) if LOG.exists() else 0.0


def runware(task, label):
    if spent() >= BUDGET_USD:
        sys.exit(f"Budget of ${BUDGET_USD} reached; ask before spending more.")
    task = {"taskType": "imageInference", "taskUUID": str(uuid.uuid4()), "outputType": "URL",
            "outputFormat": "PNG", "includeCost": True, **task}
    r = requests.post(config.ENDPOINT, timeout=240, json=[task],
                      headers={"Authorization": f"Bearer {config.load_key()}"})
    body = r.json()
    if body.get("errors") or r.status_code >= 400:
        sys.exit(f"Runware error on {label}: {json.dumps(body)[:600]}")
    rec = next((d for d in body["data"] if d.get("taskUUID") == task["taskUUID"] and "imageURL" in d), None)
    if rec is None:
        sys.exit(f"Runware returned no image for {label}: {json.dumps(body)[:600]}")
    total = log({"label": label, "model": task["model"], "seed": task.get("seed"),
                 "task_uuid": task["taskUUID"], "cost_usd": rec.get("cost")})
    print(f"  {label}: ${rec.get('cost')}  (total ${total:.4f})")
    return requests.get(rec["imageURL"], timeout=120).content


def data_uri(png: pathlib.Path) -> str:
    buf = io.BytesIO()
    Image.open(png).convert("RGB").save(buf, "JPEG", quality=95)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def registration(colour: pathlib.Path, sketch: pathlib.Path) -> float:
    """Share of the sketch's lines that sit within 4 px of a line in the colour frame."""
    def edges(p):
        g = cv2.cvtColor(np.array(Image.open(p).convert("RGB").resize(SIZE)), cv2.COLOR_RGB2GRAY)
        return cv2.Canny(cv2.GaussianBlur(g, (5, 5), 0), 40, 120) > 0
    s, c = edges(sketch), edges(colour)
    near = cv2.dilate(c.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
    return float((s & near).sum() / max(s.sum(), 1))


def check(png: pathlib.Path) -> dict:
    words, faces = imagelint.text_words(png), imagelint.face_count(png)
    return {"text": words, "faces": faces, "ok": words == [] and faces == 0}


def make(short: str, seed: int):
    sc = SCENES[short]
    d = OUT / short
    d.mkdir(parents=True, exist_ok=True)
    colour, sketch = d / f"colour-{seed}.png", d / f"sketch-{seed}.png"
    if not colour.exists():
        colour.write_bytes(runware({"model": COLOUR_MODEL, "width": SIZE[0], "height": SIZE[1],  # GPT Image takes no seed: the number only names the take
                                    "positivePrompt": f"{STYLE} {sc['colour']}"}, f"{short} colour {seed}"))
    if not sketch.exists():
        img = runware({"model": EDIT_MODEL, "seed": seed, "width": 832, "height": 1248,
                       "referenceImages": [data_uri(colour)],
                       "positivePrompt": ("Redraw this exact image as a loose, unfinished graphite pencil sketch on plain "
                                          "white paper: grey pencil lines only, no colour, no paint, no fills. Keep "
                                          f"{sc['keep']} in exactly the same place and size. Erase everything else and "
                                          "leave blank white paper where it was. No faces, no text.")},
                      f"{short} sketch {seed}")
        Image.open(io.BytesIO(img)).convert("RGB").resize(SIZE, Image.LANCZOS).save(sketch)
    # The plain request: the same sketch with deeper's additions removed, so its lines sit on the full sketch's.
    sparse = d / f"sparse-{seed}.png"
    if sc.get("erase") and not sparse.exists():
        img = runware({"model": EDIT_MODEL, "seed": seed, "width": 832, "height": 1248,
                       "referenceImages": [data_uri(sketch)],
                       "positivePrompt": (f"Remove {sc['erase']} from this pencil sketch, leaving plain white paper "
                                          f"where they were. Keep {sc['keep']} untouched. Change nothing else: every other line stays exactly where "
                                          "it is, in the same grey pencil.")},
                      f"{short} sparse {seed}")
        Image.open(io.BytesIO(img)).convert("RGB").resize(SIZE, Image.LANCZOS).save(sparse)
    report = {"colour": check(colour), "sketch": check(sketch), "registration": round(registration(colour, sketch), 3)}
    if sparse.exists():
        report |= {"sparse": check(sparse), "sparse_registration": round(registration(sketch, sparse), 3)}
    (d / f"report-{seed}.json").write_text(json.dumps(report, indent=1) + "\n")
    print(f"  {short} seed {seed}: {report}")




def colour_only(short: str, take: int):
    d = OUT / short
    d.mkdir(parents=True, exist_ok=True)
    out = d / f"colour-{take}.png"
    if not out.exists():
        out.write_bytes(runware({"model": COLOUR_MODEL, "width": SIZE[0], "height": SIZE[1],
                                 "positivePrompt": f"{STYLE} {SCENES[short]['colour']}"}, f"{short} colour {take}"))
    print(f"  {short} colour {take}: {check(out)}")


def sparse(short: str, take: int):
    """The plain request: the colour frame with deeper's additions edited out, then drawn in pencil."""
    from pencil import pencil
    sc, d = SCENES[short], OUT / short
    src, out = d / f"colour-{take}.png", d / f"sparse-{take}.png"
    clean = d / f"sparse-colour-{take}.png"
    if not clean.exists():
        clean.write_bytes(runware({"model": COLOUR_MODEL, "width": SIZE[0], "height": SIZE[1],
                                   "inputs": {"referenceImages": [data_uri(src)]},
                                   "positivePrompt": (f"The same illustration as the reference image: same place, same "
                                                      f"framing, same palette, same line style. Only change: remove "
                                                      f"{sc['erase']}, leaving what was behind them. Keep {sc['keep']} "
                                                      "exactly as they are. No faces, no text.")},
                                  f"{short} sparse {take}"))
    cv2.imwrite(str(out), pencil(cv2.imread(str(clean))))
    print(f"  {short} sparse {take}: {check(clean)}")


if __name__ == "__main__":
    step, short, *takes = sys.argv[1:]   # step: colour (GPT Image 2 frame only), kontext (old path), or sparse
    for t in takes or ["1"]:
        {"colour": colour_only, "kontext": make, "sparse": sparse}[step](short, int(t))
