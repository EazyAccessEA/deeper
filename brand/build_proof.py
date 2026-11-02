"""Render the README proof image: a real request with deeper's insertions, in light and dark.

Every red phrase must appear word for word in examples/raw/deeper.md, or this script fails.
Needs Playwright with Chromium. Usage: python3 brand/build_proof.py
"""
import asyncio
import html
import pathlib
import re

from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
RAW = ROOT.parent / "examples/raw"
FONTS = ROOT.parent / "site/node_modules/@fontsource/schibsted-grotesk/files"
TASK_ID = "T2"
INSERTS = ["the exported print PDF", "Measure margins, gutter and measure in mm", "Get a printed proof copy"]

THEMES = {
    "light": dict(page="#FFFFFF", ink="#141414", muted="#5B5F66", red="#D0241B", rule="#E3E5E8"),
    "dark": dict(page="#0D1117", ink="#EDEDED", muted="#A3A3A3", red="#FF5A4E", rule="#30363D"),
}


def task_and_prompt():
    tasks = dict(l.split(": ", 1) for l in (RAW / "tasks.md").read_text().strip().splitlines())
    prompts = (RAW / "deeper.md").read_text()
    section = re.search(rf"## {TASK_ID}\s*\n(.*?)(?=\n## T\d|\Z)", prompts, re.S).group(1)
    for phrase in INSERTS:
        if phrase not in section:
            raise SystemExit(f'"{phrase}" is not in the real /deeper prompt for {TASK_ID}')
    return tasks[TASK_ID]


def page(task, t):
    face = lambda w, s: f"""@font-face {{ font-family: S; font-weight: {w}; font-style: {s};
      src: url("{(FONTS / f'schibsted-grotesk-latin-{w}-{s}.woff2').as_uri()}"); }}"""
    caret = '<span class="c"></span>'
    inserts = "".join(f' <ins>{caret}{html.escape(p)}</ins>' for p in INSERTS)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
      {face(500, 'normal')} {face(500, 'italic')} {face(400, 'normal')}
      body {{ margin: 0; background: {t['page']}; }}
      .card {{ width: 820px; padding: 8px 0 12px; box-sizing: border-box; font-family: S; }}
      .label {{ font: 400 22px S; color: {t['muted']}; margin: 0 0 22px; }}
      .req {{ font: 500 44px/1.3 S; letter-spacing: -0.02em; color: {t['ink']}; margin: 0; }}
      ins {{ text-decoration: none; color: {t['red']}; font-style: italic; margin-left: 0.25em; }}
      .c {{ display: inline-block; width: 0.42em; height: 0.32em; margin-right: 0.12em; vertical-align: -0.1em;
           background: {t['red']}; clip-path: polygon(0 100%, 50% 0, 100% 100%, 70% 100%, 50% 40%, 30% 100%); }}
      .foot {{ font: 400 22px S; color: {t['muted']}; margin: 34px 0 0; padding-top: 22px; border-top: 2px solid {t['rule']}; }}
    </style></head><body><div class="card">
      <p class="req">{html.escape(task)}{inserts}</p>
    </div></body></html>"""


async def main():
    task = task_and_prompt()
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, t in THEMES.items():
            pg = await b.new_page(viewport={"width": 820, "height": 400}, device_scale_factor=2)
            tmp = ROOT / f".proof-{name}.html"
            tmp.write_text(page(task, t))
            await pg.goto(tmp.as_uri())
            tmp.unlink()
            await pg.evaluate("document.fonts.ready")
            assert await pg.evaluate("document.fonts.check('500 44px S')"), "brand font did not load"
            await (await pg.query_selector(".card")).screenshot(path=str(ROOT / "assets" / f"proof-{name}.png"))
            print(f"proof-{name}.png")
        await b.close()


asyncio.run(main())
