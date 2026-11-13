"""Collect recent US App Store reviews for four assistant apps and draw the frozen samples."""
import json, random, sys, time, urllib.request
from pathlib import Path

APPS = {"ChatGPT": 6448311069, "Claude": 6473753684, "Gemini": 6477489729, "Copilot": 541164041}
HERE = Path(__file__).parent
SEED = 20261113


def page(app_id, n):
    url = f"https://itunes.apple.com/us/rss/customerreviews/page={n}/id={app_id}/sortby=mostrecent/json"
    req = urllib.request.Request(url, headers={"User-Agent": "deeper-journal-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as f:
        return [e for e in json.load(f)["feed"].get("entry", []) if "im:rating" in e]


def main():
    reviews = []
    for app, app_id in APPS.items():
        for n in range(1, 11):
            for e in page(app_id, n):
                author = e["author"]["name"]["label"].strip()
                r = {
                    "id": f"{app}-{e['id']['label']}",
                    "app": app,
                    "apple_id": e["id"]["label"],
                    "rating": int(e["im:rating"]["label"]),
                    "date": e["updated"]["label"][:10],
                    "title": e["title"]["label"],
                    "text": e["content"]["label"],
                }
                # Gate A: no reviewer names stored, in any field.
                if len(author) > 3 and any(author.lower() in str(v).lower() for k, v in r.items() if k in ("id", "apple_id", "date")):
                    sys.exit(f"reviewer name leaked into {r['id']}")
                reviews.append(r)
            time.sleep(1)
    (HERE / "data/reviews.json").write_text(json.dumps(reviews, indent=1, ensure_ascii=False))

    rng = random.Random(SEED)
    samples = {"complaint": [], "praise": []}
    for app in APPS:
        low = [r for r in reviews if r["app"] == app and r["rating"] <= 2]
        high = [r for r in reviews if r["app"] == app and r["rating"] == 5]
        samples["complaint"] += rng.sample(low, min(60, len(low)))
        samples["praise"] += rng.sample(high, min(30, len(high)))
    (HERE / "data/samples.json").write_text(json.dumps(samples, indent=1, ensure_ascii=False))

    for app in APPS:
        mine = [r for r in reviews if r["app"] == app]
        dates = sorted(r["date"] for r in mine)
        stars = {s: sum(r["rating"] == s for r in mine) for s in range(1, 6)}
        print(app, len(mine), dates[0], dates[-1], stars)
    print({k: len(v) for k, v in samples.items()})


if __name__ == "__main__":
    main()
