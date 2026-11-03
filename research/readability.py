"""Flesch-Kincaid grade per page of visible prose (code, pre and nav stripped).

Usage: uv run --with textstat python3 research/readability.py <deeper-dist-dir> [impeccable-html-dir]
"""
import re, statistics, sys
from pathlib import Path
import textstat
sys.path.insert(0, str(Path(__file__).parent))
from inventory import sections


def prose(html):
    html = re.sub(r"<(pre|code|script|style)[\s\S]*?</\1>", " ", html)
    return " ".join(f"{h}. {b}" for h, _, b in sections(html))


def grade(f):
    t = prose(f.read_text(errors="ignore"))
    return round(textstat.flesch_kincaid_grade(t), 1), len(t.split())


dist = Path(sys.argv[1])
print("deeper.tools page              FK grade  words")
for f in sorted(dist.rglob("index.html")):
    rel = "/" + f.parent.relative_to(dist).as_posix().strip(".") + "/"
    if "subscribed" not in rel:
        g, w = grade(f)
        print(f"{rel.replace('//', '/'):30} {g:8} {w:6}")
if len(sys.argv) > 2:
    gs = [grade(f)[0] for f in Path(sys.argv[2]).glob("*.html") if "changelog" not in f.name]
    print(f"\nimpeccable.style, {len(gs)} pages: median {statistics.median(gs)}, range {min(gs)}-{max(gs)}")
