# rent-felix-1

Writer: claude-opus-5-5

## Call 1 prompt

I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

My task: Should I rent or buy this flat?

=== MY SITUATION ===
- The flat: 2-bed in Leeds, asking price £280,000. Leasehold, 115 years left.
- Service charge plus ground rent: £1,800 a year.
- I have £46,500 saved. A 15% deposit is £42,000; legal fees, survey and other buying costs are about £4,500. I'm a first-time buyer.
- Mortgage offer: 85% loan, 4.6% fixed for 5 years, 25-year repayment term. Assume the rate stays 4.6% after the fix.
- Renting the same kind of flat nearby costs £1,250 a month. Rents here have gone up about 3% a year.
- If I rent, my savings sit in an account paying 4% a year, and I'd save any monthly difference there too.
- Upkeep on a flat like this is usually about 1% of the price a year.
- Selling costs (agent and legal) are about 1.5% of the sale price.
- I expect to stay about 5 years, maybe 7.
- I don't know what prices will do. The last few years round here were roughly +2% a year.

## Call 1 reply

# Rent vs Buy: What a Professional Would Do, and a Rewritten Prompt

## (1) What a top professional would do that you're not asking for

You've asked a yes/no question. A good independent adviser or property analyst would reframe it as a set of narrower questions:

- **Compare net worth at exit, not monthly costs.** Both paths should start with the same cash, spend the same total each month, and invest whatever is left over. Then compare what you'd hold at year 5 and at year 7, after selling costs, mortgage payoff and tax. Your brief already leans this way. They'd make it strict.
- **Find the break-even price growth.** Rather than guess the future, they'd ask what annual growth makes buying and renting equal at 5 and 7 years. Then they'd judge whether that rate is plausible for this kind of flat. Leeds flats, especially newer city-centre stock, have often lagged houses.
- **Treat the lease as a financial risk.** They would read:
  - the ground rent review clause (does it double, or rise with RPI?);
  - the service charge history (£1,800 today says nothing about the trend);
  - the sinking fund balance and any planned major works (Section 20);
  - the cladding and fire-safety position (EWS1);
  - whether the next buyer's lender will be happy with the lease.

  115 years is fine. Escalating ground rent or an underfunded building is not.
- **Notice the liquidity problem.** £46,500 minus £42,000 minus £4,500 leaves £0. No emergency fund, no furniture money, no buffer for a boiler or a service charge spike. A professional would flag this before any return calculation. They'd also test whether a 10% deposit, or a cheaper flat, changes the answer.
- **Check the tax and scheme details:**
  - **Savings tax.** Interest at 4% on £46.5k is about £1,860 a year. That's above the £1,000 Personal Savings Allowance for basic-rate taxpayers, so part of the "rent" return is taxed unless it's held in an ISA.
  - **Lifetime ISA.** First-time buyers under 40 get a 25% bonus on up to £4k a year, for properties up to £450k. The account must be open 12 months before you use it for a purchase. That could favour renting for a year first.
  - **Stamp duty.** First-time buyer relief means £0 on £280k. Confirm your £4,500 doesn't include stamp duty.
- **Test the downside, not just the central case.** What if prices fall 10%? What if the rate at refix is 6%? What if service charges rise 8% a year? With a 15% deposit and 1.5% selling costs, a modest fall wipes out a large share of your equity.
- **Line the timing up with the mortgage fix.** Selling just before year 5 may trigger early repayment charges. Staying 7 years means two years on a rate nobody knows. "Assume 4.6% forever" is the assumption most worth stress-testing.
- **Price the non-financial side.** Renting gives flexibility. Since the Renters' Rights Act, it also gives more security of tenure. Owning gives control. A professional would name these trade-offs rather than leave them out.

## (2) The rawest material they'd start from

Instead of "prices went up about 2%" and "rents went up about 3%", they'd use:

- **HM Land Registry Price Paid Data** for this building and street: actual completed sales of comparable flats, and repeat sales of the same units, over 10 to 15 years.
- **ONS Price Index of Private Rents** for Leeds, plus current lettings of genuinely comparable flats (achieved rents, not asking rents).
- **The lease itself**, and the **LPE1 / management pack**: 3 to 5 years of service charge accounts, the current budget, the sinking fund, the major works schedule, and the EWS1 or fire-risk assessment.
- **The lender's ESIS (mortgage illustration):** exact fees, APRC, early repayment charges, and what the loan reverts to after the fix.
- **Bank of England mortgage rate series** (e.g., 85% LTV 5-year fixes) to see how far refix rates have actually swung.
- **Your own bank statements**, to set a real emergency-fund requirement.

## (3) Methods and tools

- **Model:** a year-by-year (or month-by-month) cash-flow model of both paths in a spreadsheet or Python. It needs a proper amortisation schedule (roughly £1,336 a month on £238k at 4.6% over 25 years). Surplus cash on either side is invested.
- **Analysis:**
  - break-even appreciation at 5 and 7 years;
  - a sensitivity "tornado" across price growth, refix rate, savings rate, service charge growth, rent growth and upkeep;
  - named scenarios (bear, base, bull);
  - optionally, a Monte Carlo simulation using Leeds flat price volatility estimated from Land Registry data.
- **Professional checks:** a RICS Level 2 or 3 survey, a solicitor's report on the lease, and the HMRC SDLT calculator.

## (4) What, other than you or me, shows the result is right

- **The lender's own figures.** The model's monthly payment and remaining balance at months 60 and 84 should match the ESIS or an amortisation statement.
- **The market.** The surveyor's valuation (does the flat value at £280k, or get down-valued?) and Land Registry resale prices for flats in the same building.
- **A backtest.** Use real Price Paid and rent-index data to check whether buying a comparable flat here 5 to 7 years ago would actually have beaten renting and saving.
- **Your solicitor's lease report.** It confirms or overturns the cost assumptions (ground rent escalation, service charge trend, major works).
- **Reproducibility.** A spreadsheet with every assumption in one input block, so a fee-only adviser could audit it.

---

## Rewritten prompt

> **Rent vs buy: a decision analysis for a specific leasehold flat in Leeds**
>
> Don't just tell me "rent" or "buy." Build a transparent model, find what the answer depends on, and tell me what to check before I commit.
>
> **Facts**
> - Flat: 2-bed, Leeds, asking £280,000. Leasehold, 115 years left. Service charge plus ground rent £1,800 a year (trend unknown).
> - Savings: £46,500. Deposit 15% = £42,000. Buying costs about £4,500. First-time buyer, so stamp duty should be £0; flag it if my £4,500 includes stamp duty.
> - Mortgage: £238,000, 4.6% fixed for 5 years, 25-year repayment.
> - Comparable rent £1,250 a month, historically rising about 3% a year.
> - Renting alternative: savings earn 4% a year. Any monthly cost difference is saved.
> - Upkeep about 1% of value a year. Selling costs 1.5%.
> - Horizon: 5 years, possibly 7. Local prices recently about +2% a year.
>
> **What I want**
> 1. **Like-for-like net worth comparison.** Model both paths month by month with identical total monthly outlay, the surplus invested on whichever side has it. Report net worth at years 5 and 7 after sale costs, mortgage payoff and tax on savings interest. Show results both with and without an ISA wrapper.
> 2. **Break-even.** Find the annual house price growth at which buying and renting are equal, at 5 and at 7 years.
> 3. **Sensitivity.** Rank the inputs by how much they move the answer: price growth, refix rate after year 5 (test 4.6%, 5.5%, 6.5%), savings rate, service charge growth (0%, 5%, 10% a year), rent growth, upkeep.
> 4. **Downside.** Show my equity, and whether I'd be in negative equity after selling costs, if prices fall 5%, 10% or 15% by year 5. State plainly that buying leaves me with roughly £0 in cash. Then show how the comparison changes if I keep a £6,000 to £10,000 emergency fund, for example with a 10% deposit at a likely higher rate (state the rate you assume).
> 5. **Timing and products.** Cover early repayment charge risk if I sell just before the fix ends. Assess whether renting for 12 months while using a Lifetime ISA (25% bonus, 12-month holding rule, £450k cap) improves the buy case enough to justify waiting.
> 6. **Leasehold risk.** List the specific lease and building documents I must obtain, and what result in each would change the decision: ground rent review clause, service charge accounts, sinking fund, Section 20 works, EWS1 and fire safety, onward-mortgageability.
> 7. **External checks.** Tell me exactly which outside sources would confirm or overturn your assumptions:
>    - Land Registry Price Paid Data for this building and street;
>    - the ONS rent index for Leeds;
>    - the lender's ESIS;
>    - the surveyor's valuation.
>
>    Also say what result from each would flip the conclusion. Where possible, sketch a backtest: would buying a comparable flat here 5 to 7 years ago have beaten renting?
>
> **Output**
> - One assumptions table, so everything can be changed in one place.
> - The year-5 and year-7 comparison.
> - The break-even growth rates.
> - A ranked sensitivity list.
> - A short conclusion in the form: "Buy is better only if X; rent is better if Y; before deciding, check Z."
> - Show the arithmetic, or give a spreadsheet layout I can rebuild and audit.

## Extraction

whole reply

## Call 2 prompt

# Rent vs Buy: What a Professional Would Do, and a Rewritten Prompt

## (1) What a top professional would do that you're not asking for

You've asked a yes/no question. A good independent adviser or property analyst would reframe it as a set of narrower questions:

- **Compare net worth at exit, not monthly costs.** Both paths should start with the same cash, spend the same total each month, and invest whatever is left over. Then compare what you'd hold at year 5 and at year 7, after selling costs, mortgage payoff and tax. Your brief already leans this way. They'd make it strict.
- **Find the break-even price growth.** Rather than guess the future, they'd ask what annual growth makes buying and renting equal at 5 and 7 years. Then they'd judge whether that rate is plausible for this kind of flat. Leeds flats, especially newer city-centre stock, have often lagged houses.
- **Treat the lease as a financial risk.** They would read:
  - the ground rent review clause (does it double, or rise with RPI?);
  - the service charge history (£1,800 today says nothing about the trend);
  - the sinking fund balance and any planned major works (Section 20);
  - the cladding and fire-safety position (EWS1);
  - whether the next buyer's lender will be happy with the lease.

  115 years is fine. Escalating ground rent or an underfunded building is not.
- **Notice the liquidity problem.** £46,500 minus £42,000 minus £4,500 leaves £0. No emergency fund, no furniture money, no buffer for a boiler or a service charge spike. A professional would flag this before any return calculation. They'd also test whether a 10% deposit, or a cheaper flat, changes the answer.
- **Check the tax and scheme details:**
  - **Savings tax.** Interest at 4% on £46.5k is about £1,860 a year. That's above the £1,000 Personal Savings Allowance for basic-rate taxpayers, so part of the "rent" return is taxed unless it's held in an ISA.
  - **Lifetime ISA.** First-time buyers under 40 get a 25% bonus on up to £4k a year, for properties up to £450k. The account must be open 12 months before you use it for a purchase. That could favour renting for a year first.
  - **Stamp duty.** First-time buyer relief means £0 on £280k. Confirm your £4,500 doesn't include stamp duty.
- **Test the downside, not just the central case.** What if prices fall 10%? What if the rate at refix is 6%? What if service charges rise 8% a year? With a 15% deposit and 1.5% selling costs, a modest fall wipes out a large share of your equity.
- **Line the timing up with the mortgage fix.** Selling just before year 5 may trigger early repayment charges. Staying 7 years means two years on a rate nobody knows. "Assume 4.6% forever" is the assumption most worth stress-testing.
- **Price the non-financial side.** Renting gives flexibility. Since the Renters' Rights Act, it also gives more security of tenure. Owning gives control. A professional would name these trade-offs rather than leave them out.

## (2) The rawest material they'd start from

Instead of "prices went up about 2%" and "rents went up about 3%", they'd use:

- **HM Land Registry Price Paid Data** for this building and street: actual completed sales of comparable flats, and repeat sales of the same units, over 10 to 15 years.
- **ONS Price Index of Private Rents** for Leeds, plus current lettings of genuinely comparable flats (achieved rents, not asking rents).
- **The lease itself**, and the **LPE1 / management pack**: 3 to 5 years of service charge accounts, the current budget, the sinking fund, the major works schedule, and the EWS1 or fire-risk assessment.
- **The lender's ESIS (mortgage illustration):** exact fees, APRC, early repayment charges, and what the loan reverts to after the fix.
- **Bank of England mortgage rate series** (e.g., 85% LTV 5-year fixes) to see how far refix rates have actually swung.
- **Your own bank statements**, to set a real emergency-fund requirement.

## (3) Methods and tools

- **Model:** a year-by-year (or month-by-month) cash-flow model of both paths in a spreadsheet or Python. It needs a proper amortisation schedule (roughly £1,336 a month on £238k at 4.6% over 25 years). Surplus cash on either side is invested.
- **Analysis:**
  - break-even appreciation at 5 and 7 years;
  - a sensitivity "tornado" across price growth, refix rate, savings rate, service charge growth, rent growth and upkeep;
  - named scenarios (bear, base, bull);
  - optionally, a Monte Carlo simulation using Leeds flat price volatility estimated from Land Registry data.
- **Professional checks:** a RICS Level 2 or 3 survey, a solicitor's report on the lease, and the HMRC SDLT calculator.

## (4) What, other than you or me, shows the result is right

- **The lender's own figures.** The model's monthly payment and remaining balance at months 60 and 84 should match the ESIS or an amortisation statement.
- **The market.** The surveyor's valuation (does the flat value at £280k, or get down-valued?) and Land Registry resale prices for flats in the same building.
- **A backtest.** Use real Price Paid and rent-index data to check whether buying a comparable flat here 5 to 7 years ago would actually have beaten renting and saving.
- **Your solicitor's lease report.** It confirms or overturns the cost assumptions (ground rent escalation, service charge trend, major works).
- **Reproducibility.** A spreadsheet with every assumption in one input block, so a fee-only adviser could audit it.

---

## Rewritten prompt

> **Rent vs buy: a decision analysis for a specific leasehold flat in Leeds**
>
> Don't just tell me "rent" or "buy." Build a transparent model, find what the answer depends on, and tell me what to check before I commit.
>
> **Facts**
> - Flat: 2-bed, Leeds, asking £280,000. Leasehold, 115 years left. Service charge plus ground rent £1,800 a year (trend unknown).
> - Savings: £46,500. Deposit 15% = £42,000. Buying costs about £4,500. First-time buyer, so stamp duty should be £0; flag it if my £4,500 includes stamp duty.
> - Mortgage: £238,000, 4.6% fixed for 5 years, 25-year repayment.
> - Comparable rent £1,250 a month, historically rising about 3% a year.
> - Renting alternative: savings earn 4% a year. Any monthly cost difference is saved.
> - Upkeep about 1% of value a year. Selling costs 1.5%.
> - Horizon: 5 years, possibly 7. Local prices recently about +2% a year.
>
> **What I want**
> 1. **Like-for-like net worth comparison.** Model both paths month by month with identical total monthly outlay, the surplus invested on whichever side has it. Report net worth at years 5 and 7 after sale costs, mortgage payoff and tax on savings interest. Show results both with and without an ISA wrapper.
> 2. **Break-even.** Find the annual house price growth at which buying and renting are equal, at 5 and at 7 years.
> 3. **Sensitivity.** Rank the inputs by how much they move the answer: price growth, refix rate after year 5 (test 4.6%, 5.5%, 6.5%), savings rate, service charge growth (0%, 5%, 10% a year), rent growth, upkeep.
> 4. **Downside.** Show my equity, and whether I'd be in negative equity after selling costs, if prices fall 5%, 10% or 15% by year 5. State plainly that buying leaves me with roughly £0 in cash. Then show how the comparison changes if I keep a £6,000 to £10,000 emergency fund, for example with a 10% deposit at a likely higher rate (state the rate you assume).
> 5. **Timing and products.** Cover early repayment charge risk if I sell just before the fix ends. Assess whether renting for 12 months while using a Lifetime ISA (25% bonus, 12-month holding rule, £450k cap) improves the buy case enough to justify waiting.
> 6. **Leasehold risk.** List the specific lease and building documents I must obtain, and what result in each would change the decision: ground rent review clause, service charge accounts, sinking fund, Section 20 works, EWS1 and fire safety, onward-mortgageability.
> 7. **External checks.** Tell me exactly which outside sources would confirm or overturn your assumptions:
>    - Land Registry Price Paid Data for this building and street;
>    - the ONS rent index for Leeds;
>    - the lender's ESIS;
>    - the surveyor's valuation.
>
>    Also say what result from each would flip the conclusion. Where possible, sketch a backtest: would buying a comparable flat here 5 to 7 years ago have beaten renting?
>
> **Output**
> - One assumptions table, so everything can be changed in one place.
> - The year-5 and year-7 comparison.
> - The break-even growth rates.
> - A ranked sensitivity list.
> - A short conclusion in the form: "Buy is better only if X; rent is better if Y; before deciding, check Z."
> - Show the arithmetic, or give a spreadsheet layout I can rebuild and audit.

=== MY SITUATION ===
- The flat: 2-bed in Leeds, asking price £280,000. Leasehold, 115 years left.
- Service charge plus ground rent: £1,800 a year.
- I have £46,500 saved. A 15% deposit is £42,000; legal fees, survey and other buying costs are about £4,500. I'm a first-time buyer.
- Mortgage offer: 85% loan, 4.6% fixed for 5 years, 25-year repayment term. Assume the rate stays 4.6% after the fix.
- Renting the same kind of flat nearby costs £1,250 a month. Rents here have gone up about 3% a year.
- If I rent, my savings sit in an account paying 4% a year, and I'd save any monthly difference there too.
- Upkeep on a flat like this is usually about 1% of the price a year.
- Selling costs (agent and legal) are about 1.5% of the sale price.
- I expect to stay about 5 years, maybe 7.
- I don't know what prices will do. The last few years round here were roughly +2% a year.

Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make.

## Answer

# Rent vs buy: 2-bed leasehold flat in Leeds, £280,000

**Short answer:** On your numbers, buying comes out ahead, by about **£11,700 at 5 years** and **£23,600 at 7 years**. That lead is thin. It disappears if this flat's price grows by less than about **1.2% a year (5 years)** or **0.9% a year (7 years)**. Price growth matters far more than anything else in the model. Buying as planned also leaves you with **£0 in cash**, which I'd treat as a problem in its own right.

---

## 1. Assumptions (one place to change everything)

| Input | Base value | Note |
|---|---|---|
| Price | £280,000 | |
| Deposit / loan | £42,000 / £238,000 | 85% LTV |
| Buying costs | £4,500 | Stamp duty assumed £0. First-time buyer relief covers up to £300k, so make sure the £4,500 doesn't include any stamp duty. |
| Mortgage | 4.6%, 25 years, repayment | 4.6% after the fix as well (your instruction; tested in section 5) |
| Monthly payment | **£1,336** | £16,037 a year |
| Service charge + ground rent | £1,800 a year, flat | Trend unknown; tested in section 5 |
| Upkeep | 1% of current value a year | £2,800 in year 1 |
| House price growth | +2% a year | |
| Selling costs | 1.5% of sale price | |
| Rent | £1,250 a month, +3% a year | |
| Savings rate | 4% | Base case is untaxed (as if in an ISA); taxed case shown separately |
| Equal outlay | Renter saves (buyer's costs − rent) each year | |
| Method | Annual steps, contributions earn half a year's interest | Exact mortgage amortisation; accurate to about ±£500 |

Not modelled: contents insurance (both sides pay it), furniture, moving costs, and capital gains tax (none applies to your main home).

---

## 2. Year-by-year cash flows

| Year | Buyer's costs (mortgage + charges + upkeep) | Rent | Renter saves extra | Renter's pot (end of year) |
|---|---|---|---|---|
| 0 | | | | 46,500 |
| 1 | 20,637 | 15,000 | 5,637 | 54,110 |
| 2 | 20,693 | 15,450 | 5,243 | 61,622 |
| 3 | 20,750 | 15,914 | 4,836 | 69,020 |
| 4 | 20,808 | 16,391 | 4,417 | 76,286 |
| 5 | 20,868 | 16,883 | 3,985 | **83,402** |
| 6 | 20,929 | 17,389 | 3,540 | 90,349 |
| 7 | 20,990 | 17,911 | 3,079 | **97,104** |

---

## 3. Net worth at exit

| | Year 5 | Year 7 |
|---|---|---|
| Flat value (+2% a year) | £309,142 | £321,633 |
| Less selling costs (1.5%) | −£4,637 | −£4,824 |
| Less mortgage balance | −£209,450 | −£196,065 |
| **Buyer's net worth** | **£95,055** | **£120,744** |
| **Renter's net worth (ISA, untaxed)** | **£83,402** | **£97,104** |
| Buy ahead by | **+£11,650** | **+£23,640** |
| Renter, savings taxed (basic rate, £1,000 allowance) | about £81,800 | about £94,500 |
| Buy ahead by (taxed case) | about +£13,200 | about +£26,200 |

How much savings tax matters:
- As a basic-rate taxpayer, you'd pay roughly £1,600 (5 years) to £2,600 (7 years) in tax on the renter's interest.
- As a higher-rate taxpayer, the allowance drops to £500 and the rate is 40%, so the tax is roughly double.
- Savings tax rates are also due to rise by 2 percentage points from April 2027 (announced in the 2025 Budget).
- If you rent, use ISAs. The £46.5k fits within about 2 to 3 years of ISA allowances, but check the current cash ISA limit.

The mortgage figures can be checked against the lender's ESIS document: £1,336 a month, about £209,450 owed after 60 months, about £196,070 after 84 months, and roughly £51,600 of interest paid in the first 5 years.

---

## 4. Break-even house price growth

This is the annual growth at which buying and renting end up equal:

| Horizon | Break-even (savings untaxed) | Break-even (savings taxed, basic rate) |
|---|---|---|
| 5 years | **about 1.2% a year** | about 1.1% a year |
| 7 years | **about 0.9% a year** | about 0.8% a year |

Calculation for 5 years: the buyer needs (renter's £83,402 + mortgage £209,450) ÷ 0.985 = a sale price of £297,300. That is 1.0618 times £280k over 5 years, or 1.2% a year.

So the real question is whether this particular flat will beat about 1.2% a year. Leeds flats, especially newer city-centre blocks, have often grown more slowly than Leeds houses. Your "+2% locally" figure may describe houses rather than flats. Section 8 explains how to check.

---

## 5. Sensitivity, ranked by effect on the buy advantage

| Rank | Input | Change tested | Effect on buy advantage, 5 years | 7 years |
|---|---|---|---|---|
| 1 | **Price growth** | ±1 point a year | **±£15,000** | **±£22,000** |
| 2 | **Building shocks** | One-off major works bill (Section 20) | −£5k to −£20k or more, plus harder to sell | same |
| 3 | **Upkeep** | 0.5% instead of 1% | +£7,500 | +£10,500 |
| 4 | **Refix rate after year 5** | 5.5% / 6.5% | n/a | −£3,800 / −£8,000 |
| 5 | **Savings rate** | ±1 point | ∓£3,300 | ∓£5,000 |
| 6 | **Rent growth** | 5% / 1% a year | +£3,300 / −£3,100 | +£6,000 / −£5,500 |
| 7 | **Savings tax** | ISA vs taxed | £1,600 to £3,200 | £2,600 to £5,200 |
| 8 | **Service charge growth** | 5% / 10% a year | −£900 / −£2,000 | −£1,800 / −£4,300 |

Notes on the refix rate:
- At 5.5%, the payment rises to about £1,441 a month. At 6.5%, it rises to about £1,562 a month.
- Buying still wins at 7 years in both cases (about +£19.8k and +£15.6k).

Notes on upkeep:
- 1% of value is generous for a flat. The structure, roof and common parts are covered by the service charge.
- 0.5% is probably more realistic, so the base case slightly understates the case for buying.

Notes on service charges:
- The direct cost of rising charges is small.
- The real risk is that charges rising 8 to 10% a year make the flat harder to sell and lower its value. That shows up in rank 1, not here.

---

## 6. Downside: prices fall by year 5

| Price change by year 5 | Your equity after selling | Renter's pot | Buy vs rent |
|---|---|---|---|
| +2% a year (base) | £95,055 | £83,402 | +£11,650 |
| 0% (flat) | £66,350 | £83,402 | **−£17,050** |
| −5% | £52,560 | £83,402 | −£30,800 |
| −10% | £38,770 | £83,402 | −£44,600 |
| −15% | £24,980 | £83,402 | −£58,400 |

- Negative equity after selling costs starts at about a **24% fall**. That is unlikely but possible for flats. It doesn't stop you living there, but it does trap you when you want to sell or remortgage.
- The risk is lopsided. Each 1 point a year of growth moves the result by about £15k, and a flat price over 5 years already puts you £17k behind renting.

**Liquidity:** £46,500 − £42,000 − £4,500 = **£0**. Before you'd even moved in, you would have no buffer for a broken boiler, a service charge demand, job loss, or furniture.

**The alternative: a 10% deposit with a cash buffer.** I've assumed a 4.9% rate (+0.3 points for 90% LTV; get a real quote).

| | 15% deposit | 10% deposit |
|---|---|---|
| Loan | £238,000 | £252,000 |
| Monthly payment | £1,336 | about £1,459 |
| Cash kept | £0 | **£14,000** |
| Buy ahead at year 5 | +£11,650 | **about +£7,500** |

The buffer costs about £4,000 over 5 years. The rate gap is what matters here: at a 0.5-point gap the buffer costs about £6,000, and at 0.2 points about £3,000. You could also get a smaller cushion, say £6k to £8k, by putting down about 12 to 13%, where lenders' pricing bands allow it.

---

## 7. Timing and products

**Early repayment charges.** A 5-year fix usually charges 1 to 5% of the balance if you leave early. If you sell in year 5 before the fix ends, that could be £2k to £4k, about a third of the base-case advantage. Fixes can usually be moved to your next home ("ported"), so check the porting terms in the ESIS. Better still, time any sale for after the fix ends.

**Waiting a year to use a Lifetime ISA.**
- Opening one now and paying in £4k this tax year and £4k after 6 April 2027 could earn **£2,000 in bonuses** by about November 2027.
- If you're still leaving Leeds in 5 years, waiting means owning for only 4 years. That cuts the buy advantage from about £11.7k to about £6.6k, a loss of about £5k, which is more than the £2k bonus.
- Prices rising another 2% while you wait would cost you more again.
- Withdrawing from a LISA for anything other than a home purchase costs 25%, which is more than the bonus.
- **Verdict:** not worth waiting for in the base case. It is worth it if you expect flat prices, or if you're waiting anyway, for example because the lease or building checks are slow. If you do open one, check that the government hasn't changed the LISA rules; reforms have been under discussion.

---

## 8. Leasehold and building checks: what would change the decision

| Document | What kills or reprices the deal |
|---|---|
| **Lease: ground rent clause** | Doubling every 10 to 25 years, or tied to RPI with no cap. Lenders and buyers avoid these, which hurts resale. |
| **Service charge accounts (3 to 5 years) and current budget** | Rises above about 5 to 8% a year, or unexplained jumps |
| **Sinking fund balance** | Small or empty in an older block, meaning large one-off bills are likely |
| **Section 20 notices and planned major works** | Any notice issued or planned works: get a figure and negotiate the price down |
| **EWS1 and fire risk assessment** (blocks over 11m, cladding) | No EWS1, a B2 rating, or remediation not yet done |
| **Management pack (LPE1)** | Disputes, arrears, insurance excess or claims history |
| **Your solicitor's lease report** | Anything that makes the flat hard to mortgage for the next buyer |
| **Surveyor's valuation** (RICS Level 2 or 3) | A valuation below £280k: renegotiate. Don't make up the gap from your own pocket. |

Remember that flats are taking longer to sell than houses, so allow extra time to sell.

**External sources to confirm or overturn my assumptions:**

1. **HM Land Registry Price Paid Data** for this building and street, ideally repeat sales of the same flats over 10 to 15 years.
   - Below 1% a year: the case for buying falls apart (break-even is 1.2%).
   - **Backtest:** buy a flat in this block 5 to 7 years ago at its recorded price, sell at a recent comparable price, and run section 3 again. If that past buyer would have lost to renting, weight this heavily.
2. **ONS Price Index of Private Rents (Leeds)** and actual achieved rents. If comparable flats let for £1,100 rather than £1,250, buying loses about £9k.
3. **The lender's ESIS:** check £1,336 a month, the balances above, the early repayment charges, the porting terms, and the reverting rate.
4. **Bank of England data on 85% LTV 5-year fix rates:** shows how much refix rates have actually moved, as a basis for the section 5 tests.

---

## 9. Conclusion

**Buying is better only if:**
- this flat (not Leeds houses) grows by more than about **1.2% a year** over 5 years, or about 0.9% over 7;
- the lease and building checks come back clean; and
- you don't have to sell during the fix.

**Renting is better if:**
- the Land Registry data shows flats in this block flat or falling in price;
- the lease has escalating ground rent;
- there's cladding or major-works exposure; or
- you might move within 4 years.

**Before deciding, check:**
1. Land Registry repeat sales for the building.
2. The lease and management pack.
3. That stamp duty really is £0.
4. A 90% LTV quote, so you can keep about £10k to £14k in cash.

My view: if those checks are clean and the local flat price history is about 2% a year, buy, but with a **10% deposit and a cash buffer** rather than putting every pound into the deal. The ~£4k cost is cheap insurance against being forced to sell or take on debt.

---

## Spreadsheet layout to rebuild and audit

- **Sheet "Inputs":** one cell for each row of the section 1 table.
- **Sheet "Model":** one row per month (1 to 84) with these columns:
  - Month
  - Rate (4.6% to month 60, then the refix rate)
  - Payment, using `PMT` (recalculated at month 61 on the remaining balance and term)
  - Interest
  - Principal
  - Balance
  - Service charge (monthly, growing yearly)
  - Upkeep (1% × value ÷ 12)
  - Value (`price*(1+g)^(m/12)`)
  - Buyer's total cost
  - Rent (growing yearly)
  - Renter's extra saving (= buyer's total cost − rent)
  - Renter's pot (= previous × (1+4%/12) + extra saving)
- **Outputs:**
  - At months 60 and 84: buyer's net worth = value × 0.985 − balance; renter's net worth = pot − tax.
  - Use **Goal Seek** on g to make the two equal (break-even).
  - Use a **Data Table** on g, refix rate, upkeep and savings rate for the sensitivity tests.
