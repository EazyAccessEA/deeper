"""Reference figures for fixtures/rent.md, computed before any run. python3 reference_rent.py"""
P, dep, buy_costs, r, n = 280000, 42000, 4500, 0.046 / 12, 300
loan = P - dep
pay = loan * r / (1 - (1 + r) ** -n)


def wealth(years, growth=0.02, inv=0.04, rent0=1250, rent_g=0.03):
    """Buyer: sale price less 1.5% selling costs less mortgage left. Renter: deposit and buying costs invested,
    plus each month's difference between owning costs (mortgage, £1,800/yr charges, 1%/yr upkeep) and rent."""
    bal, renter, rent = loan, dep + buy_costs, rent0
    for m in range(years * 12):
        if m and m % 12 == 0:
            rent *= 1 + rent_g
        bal -= pay - bal * r
        renter = renter * (1 + inv / 12) + (pay + 1800 / 12 + P * 0.01 / 12 - rent)
    return P * (1 + growth) ** years * 0.985 - bal, renter


def breakeven(growth):
    return next((y for y in range(1, 26) if wealth(y, growth)[0] > wealth(y, growth)[1]), None)


if __name__ == "__main__":
    print(f"monthly mortgage £{pay:,.2f}")
    for y in (5, 7):
        b, rn = wealth(y)
        print(f"{y} years at 2% growth: buy £{b:,.0f}, rent £{rn:,.0f}, buy minus rent £{b - rn:,.0f}")
    for g in (0.0, 0.02, 0.04):
        print(f"break-even at {g:.0%} growth: year {breakeven(g)}")
