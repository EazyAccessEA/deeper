# Sample size per arm for a two-sided two-proportion z-test (normal approximation).
from statistics import NormalDist
from math import ceil
z = NormalDist().inv_cdf
def n_per_arm(p1, lift, alpha=0.05, power=0.8):
    p2 = p1 * (1 + lift)
    za, zb = z(1 - alpha / 2), z(power)
    pbar = (p1 + p2) / 2
    num = (za * (2 * pbar * (1 - pbar)) ** 0.5 + zb * (p1 * (1 - p1) + p2 * (1 - p2)) ** 0.5) ** 2
    return ceil(num / (p2 - p1) ** 2)
print("baseline  lift   2 arms (a=.05)   5 arms (Bonferroni a=.0125, 4 comparisons)")
for p in (0.02, 0.05, 0.10):
    for lift in (0.2, 0.5, 1.0):
        two = n_per_arm(p, lift); five = n_per_arm(p, lift, alpha=0.05/4)
        print(f"{p:>6.0%}  {lift:>5.0%}   {two:>7,}/arm = {2*two:>8,}   {five:>7,}/arm = {5*five:>9,}")
