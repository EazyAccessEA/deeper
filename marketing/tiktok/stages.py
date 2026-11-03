"""The successive shots of one short, from its colour frame, its pencil frame and its regions in scenes.json.

  python3 stages.py <short> <take>     writes art/<short>/stage-0.png ... and stages.jpg (a contact sheet)

stage 0  the plain request: sparse-N.png, a pencil frame of the colour frame with deeper's additions edited out
stage 1  deeper's plan: the full pencil drawing
stage 2+ one object painted per insertion, in scenes.json order
last     the whole frame in colour
Regions are [x0, y0, x1, y1] boxes on the 1024x1536 frame. Each object's mask is what changed between the
colour frame and the edit without deeper's additions, inside its box, so paint never lands on anything else.
"""
import json, pathlib, sys
import cv2
import numpy as np

HERE = pathlib.Path(__file__).parent
FEATHER = 7


def added(colour, before):
    """Where the colour frame differs from the edit with deeper's additions taken out: exactly what deeper adds."""
    diff = cv2.GaussianBlur(cv2.absdiff(colour, before).max(axis=2), (0, 0), 3)
    m = (diff > 28).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    return cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8)).astype(np.float32)


def inside(m, box):
    out = np.zeros_like(m)
    x0, y0, x1, y1 = box
    out[y0:y1, x0:x1] = m[y0:y1, x0:x1]
    return out


def mix(a, b, m):
    m = cv2.GaussianBlur(m, (0, 0), FEATHER)[..., None]
    return (a * (1 - m) + b * m).astype(np.uint8)


def main(short, take):
    d = HERE / "art" / short
    scene = json.loads((HERE / "scenes.json").read_text())[short]
    colour = cv2.imread(str(d / f"colour-{take}.png"))
    pencil = cv2.imread(str(d / f"pencil-{take}.png"))
    new = added(colour, cv2.imread(str(d / f"sparse-colour-{take}.png")))
    stages = [cv2.imread(str(d / f"sparse-{take}.png")), pencil]
    painted = np.zeros(colour.shape[:2], np.float32)
    for r in scene["regions"]:
        painted = np.maximum(painted, inside(new, r["box"]))
        cv2.imwrite(str(d / f"mask-{r['name']}.png"), (painted * 255).astype(np.uint8))
        stages.append(mix(pencil, colour, painted))
    stages.append(colour)
    for i, s in enumerate(stages):
        cv2.imwrite(str(d / f"stage-{i}.png"), s)
    thumbs = [cv2.resize(s, (256, 384)) for s in stages]
    cv2.imwrite(str(d / "stages.jpg"), np.hstack([np.pad(t, ((0, 0), (0, 8), (0, 0)), constant_values=255) for t in thumbs]))
    print(f"{len(stages)} stages -> {d}")


main(sys.argv[1], sys.argv[2])
