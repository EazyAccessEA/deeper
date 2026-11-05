"""Makes the two Bricolage Grotesque files the site serves, from the installed @fontsource-variable package.

display.woff2  condensed (wdth 75), weight 700-800, optical size kept variable: headlines, big numbers. Preloaded.
text.woff2     normal width (wdth 100), weight 400-700, optical size kept variable: everything else.

The page needs only ASCII, Latin-1 and common punctuation, and splitting by width drops most of the
variation data, so the headline (the LCP element) waits for a small file instead of a 129 KB one.
Run from site/: python3 scripts/subset-fonts.py
"""
import io
import os

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

SRC = "node_modules/@fontsource-variable/bricolage-grotesque/files/bricolage-grotesque-latin-standard-normal.woff2"
OUT = "src/assets/fonts"
UNICODES = list(range(0x20, 0x7F)) + list(range(0xA0, 0x100)) + list(range(0x2000, 0x2027)) + [0x2030, 0x2039, 0x203A, 0x20AC, 0x2122, 0x2212]
CUTS = {
    "display": {"wdth": 75, "wght": (700, 800)},
    "text": {"wdth": 100, "wght": (400, 700)},
}


def reload(font):
    buf = io.BytesIO()
    font.flavor = None
    font.save(buf)
    buf.seek(0)
    return TTFont(buf, lazy=False)


os.makedirs(OUT, exist_ok=True)
for name, axes in CUTS.items():
    font = reload(instancer.instantiateVariableFont(TTFont(SRC, lazy=False), axes))
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga", "calt", "ccmp", "locl", "mark", "mkmk"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    opts.ignore_missing_unicodes = True
    s = subset.Subsetter(opts)
    s.populate(unicodes=UNICODES)
    s.subset(font)
    font.flavor = "woff2"
    path = f"{OUT}/{name}.woff2"
    font.save(path)
    print(f"{path}: {os.path.getsize(path):,} bytes")
