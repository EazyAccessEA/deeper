"""Score the journal test from judgements/ and key.json, per the readings in README.md.  python3 score.py"""
import json, pathlib, statistics as st

HERE = pathlib.Path(__file__).parent
key = json.loads((HERE / "key.json").read_text())
TASKS, ARMS, JUDGES = ["cv", "rent", "complaint", "downloads"], ["plain", "persona", "felix", "deeper"], ["claude", "gpt"]

score = {}   # (judge, task, arm, run) -> items done
items = {}   # (judge, answer name, item) -> 0/1
for j in JUDGES:
    for t in TASKS:
        data = json.loads((HERE / "judgements" / f"{j}-{t}.json").read_text())
        for lab, name in key[j][t].items():
            _, arm, n = name.split("-")
            marks = {i: int(v[0]) for i, v in data[lab].items()}
            score[(j, t, arm, n)] = sum(marks.values())
            for i, m in marks.items():
                items[(j, name, i)] = m

def mean(**f):
    return st.mean(v for k, v in score.items() if all(k[["judge", "task", "arm", "run"].index(x)] == y for x, y in f.items()))

print("Mean items done (0-6), all tasks, both judges:")
for a in ARMS:
    print(f"  {a:8} {mean(arm=a):.2f}   claude {mean(arm=a, judge='claude'):.2f}   gpt {mean(arm=a, judge='gpt'):.2f}")
print("\nBy task (both judges):")
print("  " + "".join(f"{a:>9}" for a in ARMS))
for t in TASKS:
    print(f"  {t:10}" + "".join(f"{mean(arm=a, task=t):9.2f}" for a in ARMS))

d = mean(arm="felix") - mean(arm="deeper")
print(f"\nfelix minus deeper: {d:+.2f} -> " + ("felix better" if d >= 1 else "deeper better" if d <= -1 else "tie (under 1.0)"))
for a in ARMS:
    for b in ARMS:
        if a < b:
            g = mean(arm=a) - mean(arm=b)
            print(f"  {a} - {b}: {g:+.2f}" + ("" if abs(g) >= 1 else "  (no difference)"))

pairs = [(items[("claude", n, i)], items[("gpt", n, i)]) for (j, n, i) in items if j == "claude"]
agree = sum(a == b for a, b in pairs) / len(pairs)
p1, p2 = st.mean(a for a, _ in pairs), st.mean(b for _, b in pairs)
pe = p1 * p2 + (1 - p1) * (1 - p2)
kappa = (agree - pe) / (1 - pe) if pe < 1 else 1.0
print(f"\nJudge agreement: {agree:.1%} of {len(pairs)} item scores, Cohen's kappa {kappa:.2f}"
      + ("  (below 0.4: too weak to support a ranking)" if kappa < 0.4 else ""))

print("\nItem pass rate by arm (both judges), per task:")
for t in TASKS:
    print(f"  {t}")
    for a in ARMS:
        row = [st.mean(m for (j, n, i), m in items.items() if n.startswith(f"{t}-{a}-") and i == str(k)) for k in range(1, 7)]
        print(f"    {a:8}" + "".join(f"{x:5.2f}" for x in row))
