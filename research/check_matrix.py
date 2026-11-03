"""Fails if any matrix cell's page is missing or doesn't contain its answer phrase.

Usage: python3 research/check_matrix.py [deeper|deeper_before] [deeper base URL]
The second argument lets the after-state run against a local build (astro preview).
"""
import json, sys, unicodedata
from pathlib import Path
from playwright.sync_api import sync_playwright

col = sys.argv[1] if len(sys.argv) > 1 else "deeper"
bases = {"impeccable": "https://impeccable.style", col: sys.argv[2] if len(sys.argv) > 2 else "https://deeper.tools"}
rows = json.loads(Path(__file__).with_name("reader-matrix.json").read_text())["rows"]
fold = lambda s: unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'").lower()

fails, gaps, cache = 0, [], {}
with sync_playwright() as p:
    page = p.chromium.launch().new_page()
    for r in rows:
        for site in ("impeccable", col):
            cell = r[site]
            if cell is None:
                gaps.append(f"  none  {site:13} {r['reader']}: {r['question']}")
                continue
            url = bases[site] + cell[0]
            if url not in cache:
                resp = page.goto(url, wait_until="domcontentloaded")
                # <details> answers are in the DOM but closed; textContent reads them anyway
                cache[url] = (resp.status if resp else 0, page.evaluate("document.body.textContent"))
            status, text = cache[url]
            ok = status == 200 and fold(cell[1]) in fold(text)
            fails += not ok
            print(f"{'PASS' if ok else 'FAIL'}  {site:13} {status} {cell[0]:28} {cell[1]!r}")
print("\nUnanswered cells:\n" + "\n".join(gaps))
print(f"\n{fails} failing cells")
sys.exit(1 if fails else 0)
