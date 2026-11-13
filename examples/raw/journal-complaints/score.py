"""Agreement, shares with 95% Wilson intervals, per-app shares, and the expert-gap test. Writes results.json."""
import json, math, pathlib
from collections import Counter

HERE = pathlib.Path(__file__).parent
BOOK = json.loads((HERE / "codebook.json").read_text())
SAMPLES = json.loads((HERE / "data/sample-ids.json").read_text())
# W5 maps to C9, but C9 also holds bans, ID checks, politics and water; see README Results for why its figure is not a privacy figure.
WARN = {"W1 sycophancy": ("C8", "P4"), "W2/W3/W6 wrong answers, over-reliance, health": ("C3", None),
        "W3 over-reliance": (None, "P6"), "W4 emotional dependence": (None, "P3"),
        "W5 privacy": ("C9", None), "W6 health": (None, "P5")}


def kappa(a, b):
    ids = sorted(a)
    n = len(ids)
    po = sum(a[i] == b[i] for i in ids) / n
    ca, cb = Counter(a[i] for i in ids), Counter(b[i] for i in ids)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return po, (po - pe) / (1 - pe)


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, round(100 * (c - h), 1)), round(100 * (c + h), 1)


out = {}
for pool in ("complaint", "praise"):
    a = json.loads((HERE / f"codes/claude-{pool}.json").read_text())
    b = json.loads((HERE / f"codes/gpt-{pool}.json").read_text())
    s = json.loads((HERE / f"codes/settled-{pool}.json").read_text())
    po, k = kappa(a, b)
    n = len(s)
    counts = Counter(s.values())
    ca, cb = Counter(a.values()), Counter(b.values())
    shares = {c: {"n": counts[c], "pct": round(100 * counts[c] / n, 1), "ci": wilson(counts[c], n),
                  "claude_n": ca[c], "gpt_n": cb[c]}
              for c in sorted(BOOK[pool], key=lambda c: -counts[c])}
    apps = {}
    for app in ("ChatGPT", "Claude", "Gemini", "Copilot"):
        ids = [r["id"] for r in SAMPLES[pool] if r["app"] == app]
        ac = Counter(s[i] for i in ids)
        apps[app] = {"n": len(ids), **{c: round(100 * ac[c] / len(ids), 1) for c in BOOK[pool] if ac[c]}}
    equal = {c: round(sum(apps[x].get(c, 0) for x in apps) / len(apps), 1) for c in BOOK[pool]}
    top, second = list(shares)[:2]
    out[pool] = {"n": n, "agreement_pct": round(100 * po, 1), "kappa": round(k, 3),
                 "verdict": "pass" if k >= 0.7 else "weak" if k >= 0.6 else "fail",
                 "top": top if shares[top]["ci"][0] > shares[second]["ci"][1] else f"tie {top}/{second}",
                 "shares": shares, "per_app": apps, "equal_weight_mean_pct": equal}
    print(f"\n== {pool}: n={n}  agreement {po:.1%}  kappa {k:.3f} ({out[pool]['verdict']})  top: {out[pool]['top']}")
    for c, v in shares.items():
        print(f"  {c:4} {v['n']:4} {v['pct']:5}%  CI {v['ci']}  claude {v['claude_n']:3} gpt {v['gpt_n']:3}  equal-weight {equal[c]:5}%  {BOOK[pool][c][:50]}")
    for app, v in apps.items():
        print(" ", app, v)

gap = {}
for w, (c, p) in WARN.items():
    row = {}
    if c:
        row["complaint_pct"] = out["complaint"]["shares"][c]["pct"]
        # "Rarely named" is about what reviewers write, not how often the harm happens.
        row["rarely_named"] = row["complaint_pct"] < 5
    if p:
        row["praise_pct"] = out["praise"]["shares"][p]["pct"]
    gap[w] = row
out["expert_gap"] = gap
print("\n== expert gap")
for w, r in gap.items():
    print(" ", w, r)
(HERE / "results.json").write_text(json.dumps(out, indent=1))
