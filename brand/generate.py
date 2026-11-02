"""Generate brand imagery with Runware. Prompts and seeds live in PLATES so every image can be remade.

Key: RUNWARE_API_KEY from the environment, or from the .env named by RUNWARE_ENV.
Usage: python3 brand/generate.py [plate-name ...]
"""
import json
import os
import pathlib
import sys
import urllib.request
import uuid

ENDPOINT = "https://api.runware.ai/v1"
MODEL = "runware:101@1"  # FLUX.1 [dev]
OUT = pathlib.Path(__file__).parent / "plates"

PLATES = {
    "pencil-space-b": dict(
        seed=7, size=(1344, 704),
        prompt=("Minimal overhead photograph: exactly one red pencil, alone, lying horizontally near the "
                "bottom right of a large sheet of bright white paper, tip pointing left. Everything else is "
                "empty white. Cool daylight, soft shadow under the pencil, no text, no marks, no second pencil."),
    ),
    "caret-macro": dict(
        seed=88, size=(1024, 1024),
        prompt=("Extreme macro photograph of a red pencil proofreader's caret mark on bright white paper, "
                "graphite-sharp edges, shallow depth of field, cool white light, minimal, no text."),
    ),
    "pencil-space-b": dict(
        seed=7, size=(1344, 704),
        prompt=("Minimal overhead photograph: exactly one red pencil, alone, lying horizontally near the "
                "bottom right of a large sheet of bright white paper, tip pointing left. Everything else is "
                "empty white. Cool daylight, soft shadow under the pencil, no text, no marks, no second pencil."),
    ),
    "caret-macro": dict(
        seed=88, size=(1024, 1024),
        prompt=("Extreme macro photograph of a red pencil proofreader's caret mark on bright white paper, "
                "graphite-sharp edges, shallow depth of field, cool white light, minimal, no text."),
    ),
    "pencil-space": dict(
        seed=61, size=(1344, 704),
        prompt=("Overhead photograph of exactly one single red pencil, only one pencil, lying diagonally across the right third of a sheet "
                "of bright white paper, sharpened tip pointing down-left, faint red pigment dust near the "
                "tip. The left two thirds are empty white space. Cool neutral daylight, soft shadow, "
                "minimal, no text, no letters, no writing, no beige."),
    ),
}


def key() -> str:
    if os.environ.get("RUNWARE_API_KEY"):
        return os.environ["RUNWARE_API_KEY"]
    env = os.environ.get("RUNWARE_ENV")
    if env and pathlib.Path(env).exists():
        for line in pathlib.Path(env).read_text().splitlines():
            if line.startswith("RUNWARE_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"')
    sys.exit("Set RUNWARE_API_KEY or RUNWARE_ENV")


def generate(name: str) -> pathlib.Path:
    p = PLATES[name]
    w, h = p["size"]
    task = {"taskType": "imageInference", "taskUUID": str(uuid.uuid4()), "model": MODEL,
            "positivePrompt": p["prompt"], "width": w, "height": h, "seed": p["seed"],
            "steps": 28, "numberResults": 1, "outputType": "URL", "outputFormat": "JPG",
            "includeCost": True}
    req = urllib.request.Request(ENDPOINT, data=json.dumps([task]).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {key()}"})
    with urllib.request.urlopen(req, timeout=180) as r:
        res = json.load(r)
    if res.get("errors"):
        sys.exit(f"{name}: {res['errors']}")
    data = res["data"][0]
    OUT.mkdir(exist_ok=True)
    dest = OUT / f"{name}.jpg"
    urllib.request.urlretrieve(data["imageURL"], dest)
    print(f"{name}: {dest} cost=${data.get('cost', '?')}")
    return dest


if __name__ == "__main__":
    for n in sys.argv[1:] or PLATES:
        generate(n)
