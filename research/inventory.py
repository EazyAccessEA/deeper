"""Builds research/content-inventory.csv: one row per section of impeccable.style and deeper.tools.

Sections split at h1-h3 and FAQ <summary> questions. Diátaxis type and reader are keyword rules
(below), so the CSV can be rebuilt and argued with; they are a first sort, not a reading.
Usage: python3 research/inventory.py <impeccable-html-dir> <deeper-dist-dir>
"""
import csv, re, sys
from html.parser import HTMLParser
from pathlib import Path

SKIP = {"nav", "header", "footer", "aside", "script", "style", "svg", "noscript"}
HEAD = {"h1", "h2", "h3", "summary"}


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Sections(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.inhead, self.sections = [], None, [["(intro)", []]]

    @property
    def skip(self):
        return any(s for _, s in self.stack)

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        cls = dict(attrs).get("class") or ""
        skipping = tag in SKIP or "sidebar" in cls or "toc" in cls.split()
        self.stack.append((tag, skipping))
        if not self.skip and tag in HEAD:
            self.inhead = tag
            self.sections.append(["", []])

    def handle_endtag(self, tag):
        if any(t == tag for t, _ in self.stack):
            while self.stack and self.stack.pop()[0] != tag:
                pass
        if tag == self.inhead:
            self.inhead = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.inhead:
            self.sections[-1][0] += data
        else:
            self.sections[-1][1].append(data)


def sections(html):
    p = Sections()
    p.feed(html)
    out = []
    for head, body in p.sections:
        head = " ".join(head.split())
        words = len(" ".join(body).split())
        if words or head:
            out.append((head or "(intro)", words, " ".join(body)))
    return out


READERS = [
    ("Claude Code user", r"claude code|/plugin|~/\.claude|\.claude/"),
    ("Cursor/Codex user", r"cursor|codex|copilot|gemini cli|windsurf|opencode|\.agents/"),
    ("Chat-app user", r"claude\.ai|chatgpt|chat app|\bpaste\b|project knowledge|custom instructions"),
    ("Non-developer / new to agents", r"new to|no design experience|don.t need (design|to)|beginner|getting started|first run|what (it|is) |plain english"),
    ("Skeptic", r"research|blind|judge|evidence|scor(e|ed|ing)|case stud|gallery|before and after|benchmark|tested"),
    ("Existing user", r"\bupdate\b|upgrade|uninstall|\bremove\b|\bpin\b|troubleshoot|not working|doctor|report (a|an)"),
    ("Phone visitor", r"email me|sign up|newsletter|remind me|send (it|this) to"),
]

PAGE_TYPE = [  # (url pattern, default Diátaxis type)
    (r"/tutorials/|/start/", "tutorial"), (r"/docs/.+", "reference"), (r"/docs/?$", "reference"),
    (r"/faq", "how-to"), (r"/changelog|/privacy|/legal|/patterns", "reference"),
    (r".*", "explanation"),
]
HEADING_TYPE = [
    (r"^(your first run|getting started|get started|try it|build something|improve an existing)", "tutorial"),
    (r"^(install|update|remove|pin|how do|how to|set up|configure|use\b|turn on|initiali[sz]e|by hand|any agent|in a chat|claude code, as)", "how-to"),
]


def classify(url, head, body):
    t = next(t for p, t in PAGE_TYPE if re.search(p, url))
    for p, ht in HEADING_TYPE:
        if re.search(p, head.lower()):
            t = ht
    if head.endswith("?") and t != "tutorial":
        t = "how-to" if re.match(r"(how do|how can|where do|can i)", head.lower()) else "explanation"
    text = f"{head} {body}".lower()
    if head in ("Read the full deeper prompt", "Compare the plain rewrite"):
        return t, "Non-developer / new to agents | Skeptic"
    readers = [name for name, p in READERS if re.search(p, text)]
    return t, " | ".join(readers) or "all"


def main(imp_dir, dist_dir):
    rows = []
    for f in sorted(Path(imp_dir).glob("*.html")):
        slug = f.stem
        url = "https://impeccable.style/" + ("" if slug == "home" else slug.replace("_", "/"))
        for head, words, body in sections(f.read_text(errors="ignore")):
            rows.append(("impeccable.style", url, head, words, *classify(url, head, body)))
    for f in sorted(Path(dist_dir).rglob("index.html")) + [Path(dist_dir) / "404.html"]:
        rel = f.parent.relative_to(dist_dir).as_posix()
        if rel == "subscribed":
            continue
        url = "https://deeper.tools/" + ("" if rel == "." else rel + "/") if f.name == "index.html" else "https://deeper.tools/404"
        for head, words, body in sections(f.read_text()):
            rows.append(("deeper.tools", url, head, words, *classify(url, head, body)))
    out = Path(__file__).with_name("content-inventory.csv")
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["site", "url", "heading", "words", "diataxis", "readers"])
        w.writerows(rows)
    print(f"{len(rows)} rows -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
