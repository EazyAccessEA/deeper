"""Pencil stages made from the colour frame itself, so every shot lines up with it pixel for pixel.

  python3 pencil.py <art/short/colour-N.png>   writes pencil-N.png next to it

The colour illustration already has graphite linework under its paint. A colour-dodge blend of the greyscale
against its blurred inverse keeps those lines and drops the paint; a light paper tone and grain finish it.
Shots in the film mix this pencil frame with the colour frame through per-object masks (scenes.json "regions").
"""
import sys, pathlib
import cv2
import numpy as np


def pencil(colour_bgr: np.ndarray) -> np.ndarray:
    grey = cv2.cvtColor(colour_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    blur = cv2.GaussianBlur(255 - grey, (0, 0), 14)
    dodge = np.clip(grey * 255 / np.maximum(255 - blur, 1), 0, 255)
    lines = 255 - (255 - dodge) * 1.35                       # firmer strokes
    rng = np.random.default_rng(3)                           # fixed grain, so a re-run gives the same frame
    grain = rng.normal(0, 3, grey.shape).astype(np.float32)
    paper = np.clip(np.minimum(lines, 250) + grain, 0, 255)
    tone = np.array([0.985, 0.99, 1.0], np.float32)          # graphite grey on cool white paper (BGR)
    return np.clip(paper[..., None] * tone, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1])
    out = src.with_name(src.name.replace("colour", "pencil"))
    cv2.imwrite(str(out), pencil(cv2.imread(str(src))))
    print(out)
