"""Exploratory, written after the main results were in: keyword counts across all collected 1-2 and 5 star reviews."""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
TERMS = {
    "limit": r"\blimit",
    "flattery": r"flatter|sycophan|agrees? with everything|what(ever)? (you|i) want(ed)? to hear|make you feel better|yes[- ]man|glaz|validat",
    "training on chats": r"train(s|ed|ing)? on|used? (my|our) (chats|conversations|data) to train|training data",
}
R = json.loads((HERE / "data/reviews.json").read_text())
pools = {"all": R, "1-2 stars": [r for r in R if r["rating"] <= 2], "5 stars": [r for r in R if r["rating"] == 5]}
for name, rows in pools.items():
    for k, p in TERMS.items():
        hits = [r for r in rows if re.search(p, r["title"] + " " + r["text"], re.I)]
        print(f"{name:9} {k:18} {len(hits):4} of {len(rows)}", [h["id"] for h in hits] if len(hits) < 8 else "")
