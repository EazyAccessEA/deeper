# rent-felix-2

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

# Rent or buy: what a professional would do, and a rewritten prompt

## (1) What a top professional would do that you're not asking for

An independent financial adviser who also understands leasehold property wouldn't ask "rent or buy?" They'd ask **"How much would prices have to rise for buying to win, and how likely is that for this specific flat?"**

- **Find the break-even price growth.** They'd calculate the annual price growth at which buying and renting leave you with equal net worth at year 5 and at year 7. Then they'd judge whether that rate is plausible. They wouldn't pick a single forecast like +2%.
- **Compare net worth fairly.** Both paths should have the same monthly spending. If buying costs more each month, the renter invests the difference, and the reverse if buying is cheaper. Buying costs include mortgage, service charge, ground rent and upkeep.
- **Stress-test, especially for falls.** City-centre flats in northern UK cities have often lagged houses and local averages, sometimes flat or negative in real terms. They'd model 0%, −10% and +4% alongside +2%.
- **Treat the lease as a financial liability.** Service charges often rise faster than inflation. They'd check:
  - Ground rent review or doubling clauses
  - Reserve fund health and any planned major works (Section 20 notices)
  - Cladding and fire-safety status (EWS1, Building Safety Act remediation)
  These decide whether the flat is mortgageable and sellable in 5 to 7 years.
- **Point out the cash buffer.** £46,500 saved minus £46,500 of buying costs leaves **zero emergency fund**. Many advisers would treat that as decisive on its own: delay, use a smaller deposit, or keep a buffer.
- **Use after-tax returns and the right accounts.** Interest at 4% may be taxable above your Personal Savings Allowance unless it's in an ISA. A Lifetime ISA (if you're under 40, for properties up to £450k) adds a 25% bonus, which changes both the "buy now" and "rent and wait" cases.
- **Check transaction details.** First-time buyer stamp duty relief should make SDLT nil at £280k under the current rules; confirm this. They'd also look at mortgage arrangement fees, early repayment charges if you sell during the fix, and the likely remortgage rate. After 5 years your loan-to-value falls, which usually means a better rate.
- **Weigh the non-financial side.** Moving flexibility versus security, especially as the Renters' Rights Act reforms (ending Section 21 "no-fault" evictions) change what renting is like.

## (2) The rawest material they'd start from

- **HM Land Registry Price Paid Data for this building and its postcode.** These are actual resale prices of flats in the block over 10+ years, not area averages.
- **The lease itself**, covering ground rent terms, review clauses, permitted use and subletting rights.
- **3 to 5 years of service charge accounts**, the current budget, the reserve fund statement, and the management pack (LPE1).
- **Fire risk assessment, EWS1 form and any remediation correspondence** for the building.
- **Let-agreed rents** for comparable flats (actual achieved rents, not asking rents), plus ONS rental price data for Leeds.
- **Your lender's ESIS/KFI document**, showing exact payments, fees and early repayment charges.
- **Your own tax band and income**, which set your after-tax savings return and your affordability if rates or service charges rise.

## (3) Methods and tools

- **A month-by-month net-worth model in a spreadsheet** (Excel or Google Sheets, using PMT and IPMT for the amortisation schedule). It tracks equity, mortgage balance, cumulative costs and the invested savings on both paths.
- **Break-even analysis**: solve for the house-price growth rate where the two paths finish equal, at year 5 and at year 7.
- **A sensitivity grid**: price growth against remortgage rate and service charge growth. Scenarios should include a −10% price shock, sale delays and special assessments for major works.
- **Optional Monte Carlo simulation** using the historical spread of Leeds flat price changes.
- **Cross-checks**: the HMRC SDLT calculator, the MoneyHelper mortgage calculator, and the UK House Price Index split by property type (flats versus all properties).

## (4) What would show the result is right, other than you or me

- **A backtest.** Use Land Registry sales from this building. Would someone who bought a comparable flat there 5 to 7 years ago, and resold at recorded prices, have beaten renting under the same model?
- **Independent figure matching.** The model's monthly mortgage payment and stamp duty should match the lender's ESIS and the HMRC calculator to the pound.
- **The surveyor's valuation.** A down-valuation below £280k is hard evidence you'd be overpaying.
- **The solicitor's leasehold report.** It confirms or kills the service charge and safety assumptions.
- **A regulated independent financial adviser** reviewing the model's inputs.

---

## Rewritten prompt

```
I'm deciding whether to buy a specific leasehold flat in Leeds or keep renting.
Don't give me a single verdict based on one price forecast. Instead:

1. BUILD A NET-WORTH MODEL (month by month, years 0–7) comparing:
   - BUY: £280,000 flat, 15% deposit (£42,000), ~£4,500 buying costs,
     £238,000 repayment mortgage at 4.6% fixed for 5 years, 25-year term.
     Service charge + ground rent £1,800/yr; upkeep 1% of value/yr;
     selling costs 1.5% of sale price.
   - RENT: £1,250/month rising 3%/yr; savings of £46,500 earning 4%.
   Keep monthly outlay equal: whichever path is cheaper in a given month
   invests the difference at the savings rate. Report net worth after
   selling costs at year 5 and year 7.

2. SOLVE FOR BREAK-EVEN: what annual price growth makes buying and renting
   equal at year 5, and at year 7? Then judge how plausible that is for a
   Leeds FLAT specifically (flats vs all-property HPI), not Leeds overall.

3. SENSITIVITY GRID: price growth (−2%, 0%, +2%, +4%, plus a one-off −10%
   shock) × remortgage rate after year 5 (3.5%, 4.6%, 6%) × service charge
   growth (3%, 6%, 10%/yr). Flag which assumptions actually flip the answer.

4. CORRECT THE INPUTS I may have wrong:
   - Savings interest after tax (Personal Savings Allowance) vs held in an ISA.
   - Whether a Lifetime ISA applies to me (under-40, £450k cap) and how its
     25% bonus changes both "buy now" and "rent, save, buy later".
   - Confirm first-time buyer SDLT at £280k under current rules.
   - Mortgage arrangement fees and early repayment charges if I sell during
     the fix.
   - That buying uses ALL £46,500 and leaves no emergency fund: quantify the
     risk and show an alternative (e.g., smaller deposit / wait 12 months).

5. LEASEHOLD DUE DILIGENCE: list the exact documents I should obtain (lease,
   3–5 years of service charge accounts, reserve fund, LPE1 management pack,
   Section 20 notices, fire risk assessment, EWS1/cladding status) and the
   specific red flags in each that would change the decision or make the flat
   hard to sell or remortgage in 5–7 years.

6. VALIDATION: tell me how to check your result independently:
   - How to pull HM Land Registry Price Paid Data for this building/postcode
     and backtest: would a buyer here 5–7 years ago have beaten renting
     under this same model?
   - Which figures should match my lender's ESIS and the HMRC SDLT
     calculator exactly.
   - What a surveyor's valuation or solicitor's report would need to show
     to overturn your conclusion.

7. Finish with: the break-even numbers, the 2–3 assumptions that matter most,
   the non-financial trade-offs (flexibility vs security, Renters' Rights Act
   changes), and a conditional recommendation ("buy if X and Y hold; otherwise
   rent"). Show the formulas or a spreadsheet layout so I can rebuild it.
```

**Tip:** if you can get them, attach the service charge accounts and the Land Registry sold prices for the building when you use this prompt. Those two inputs will move the answer more than any of the assumptions above.

## Extraction

last fenced block

## Call 2 prompt

I'm deciding whether to buy a specific leasehold flat in Leeds or keep renting.
Don't give me a single verdict based on one price forecast. Instead:

1. BUILD A NET-WORTH MODEL (month by month, years 0–7) comparing:
   - BUY: £280,000 flat, 15% deposit (£42,000), ~£4,500 buying costs,
     £238,000 repayment mortgage at 4.6% fixed for 5 years, 25-year term.
     Service charge + ground rent £1,800/yr; upkeep 1% of value/yr;
     selling costs 1.5% of sale price.
   - RENT: £1,250/month rising 3%/yr; savings of £46,500 earning 4%.
   Keep monthly outlay equal: whichever path is cheaper in a given month
   invests the difference at the savings rate. Report net worth after
   selling costs at year 5 and year 7.

2. SOLVE FOR BREAK-EVEN: what annual price growth makes buying and renting
   equal at year 5, and at year 7? Then judge how plausible that is for a
   Leeds FLAT specifically (flats vs all-property HPI), not Leeds overall.

3. SENSITIVITY GRID: price growth (−2%, 0%, +2%, +4%, plus a one-off −10%
   shock) × remortgage rate after year 5 (3.5%, 4.6%, 6%) × service charge
   growth (3%, 6%, 10%/yr). Flag which assumptions actually flip the answer.

4. CORRECT THE INPUTS I may have wrong:
   - Savings interest after tax (Personal Savings Allowance) vs held in an ISA.
   - Whether a Lifetime ISA applies to me (under-40, £450k cap) and how its
     25% bonus changes both "buy now" and "rent, save, buy later".
   - Confirm first-time buyer SDLT at £280k under current rules.
   - Mortgage arrangement fees and early repayment charges if I sell during
     the fix.
   - That buying uses ALL £46,500 and leaves no emergency fund: quantify the
     risk and show an alternative (e.g., smaller deposit / wait 12 months).

5. LEASEHOLD DUE DILIGENCE: list the exact documents I should obtain (lease,
   3–5 years of service charge accounts, reserve fund, LPE1 management pack,
   Section 20 notices, fire risk assessment, EWS1/cladding status) and the
   specific red flags in each that would change the decision or make the flat
   hard to sell or remortgage in 5–7 years.

6. VALIDATION: tell me how to check your result independently:
   - How to pull HM Land Registry Price Paid Data for this building/postcode
     and backtest: would a buyer here 5–7 years ago have beaten renting
     under this same model?
   - Which figures should match my lender's ESIS and the HMRC SDLT
     calculator exactly.
   - What a surveyor's valuation or solicitor's report would need to show
     to overturn your conclusion.

7. Finish with: the break-even numbers, the 2–3 assumptions that matter most,
   the non-financial trade-offs (flexibility vs security, Renters' Rights Act
   changes), and a conditional recommendation ("buy if X and Y hold; otherwise
   rent"). Show the formulas or a spreadsheet layout so I can rebuild it.

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

# Buy vs Rent: 2-bed Leasehold Flat, Leeds (£280k)

**How these numbers were made:** I built a month-by-month model, years 0–7. Mortgage interest and savings interest compound monthly. Rent, service charge and upkeep step up once a year. I had no spreadsheet tool in this session, so the figures are hand-computed. If you rebuild them in a spreadsheet (layout in §8), expect differences of about ±£200, which is far smaller than any conclusion depends on.

**Answer in one line:** buying beats renting at year 5 only if the flat gains about **1.25%/yr**, and at year 7 about **0.9%/yr**. For a Leeds flat that is roughly the middle of plausible outcomes, so the decision depends on the leasehold documents and the valuation more than on any price forecast.

---

## 1. Net-worth model

### Assumptions (stated, not asked)

| Input | Value used | Note |
|---|---|---|
| Mortgage payment | **£1,336.43/mo** | PMT(4.6%/12, 300, 238,000) |
| Balance at month 60 / 84 | **£209,450 / £196,065** | Rate stays 4.6% after the fix (your instruction) |
| Service charge + ground rent | £1,800/yr, **+3%/yr** in base | You gave no growth rate; 3% is my base, tested up to 10% |
| Upkeep | 1% of value at start of each year | Falls if the price falls |
| Rent | £1,250, +3%/yr | Stepped annually |
| Savings rate | 4% gross, **no tax** | As if held in an ISA; see §4 |
| SDLT | £0 | First-time buyer relief, see §4 |
| Arrangement fee | Assumed inside the £4,500 | See §4 |
| ERC | None | Assumes you sell after the fix ends at month 60 |
| Purchase price | Equal to market value | If you overpay, every £5k overpaid costs about £4.9k at sale |

### Equal-outlay mechanics

Buying costs more every month, so the renter invests the difference.

| Year | Buy outlay/mo (mortgage + SC + upkeep) | Rent/mo | Renter invests/mo |
|---|---|---|---|
| 1 | £1,719.76 | £1,250.00 | £469.76 |
| 2 | £1,728.93 | £1,287.50 | £441.43 |
| 3 | £1,738.33 | £1,326.13 | £412.20 |
| 4 | £1,747.96 | £1,365.91 | £382.05 |
| 5 | £1,757.83 | £1,406.89 | £350.94 |
| 6 | £1,767.94 | £1,449.09 | £318.85 |
| 7 | £1,778.32 | £1,492.57 | £285.75 |

(Upkeep figures in the table use the +2% price path.)

### Results at +2%/yr price growth (your recent local trend)

| | Year 5 | Year 7 |
|---|---|---|
| Flat value | £309,143 | £321,632 |
| Less 1.5% selling costs | £304,506 | £316,808 |
| Less mortgage balance | −£209,450 | −£196,065 |
| **BUY net worth** | **£95,056** | **£120,743** |
| RENT: £46,500 compounded | £56,776 | £61,497 |
| RENT: monthly differences compounded | £27,424 | £37,253 |
| **RENT net worth** | **£84,201** | **£98,750** |
| **Buy minus rent** | **+£10,855** | **+£21,993** |

Cross-check on buyer equity at year 5: deposit £42,000 + principal repaid £28,550 + price gain £29,143 − selling costs £4,637 = £95,056 ✓.

The buyer's £4,500 purchase costs and roughly £4,600 selling costs add up to about **£9k of friction**. That friction is why short stays favour renting.

---

## 2. Break-even price growth

Solved by bracketing (the spreadsheet equivalent is Goal Seek).

| Horizon | Gap at 0% | Gap at 2% | **Break-even annual growth** |
|---|---|---|---|
| Year 5 | −£17,245 | +£10,855 | **≈1.25%/yr** (1.2% → −£655; 1.3% → +£763) |
| Year 7 | −£17,690 | +£21,993 | **≈0.92%/yr** (0.9% → −£425; 1.0% → +£1,553) |

Near break-even, each extra 1 percentage point of growth is worth about £14k by year 5 and about £20k by year 7.

**Realistic adjustments to the year-5 break-even:**
- A £999 arrangement fee on top of the £4,500 raises it to about 1.34%.
- Selling 2 months before the fix ends, with a 1% ERC, raises it to about 1.5%.
- Savings taxed outside an ISA (basic-rate taxpayer) lowers it to about 1.15%. For a higher-rate taxpayer it falls to about 0.95%.

### How plausible is ~1.25% for a Leeds flat?

1. **Your "+2% a year" is probably an all-property figure.** In UK HPI data, flats have consistently grown more slowly than houses since about 2016. Nationally, flats have roughly tracked or lagged inflation, so they have fallen in real terms. Northern city-centre flats in particular have had multi-year spells of flat nominal prices.
2. **Leeds city centre has a large build-to-rent and new-build pipeline.** That extra supply competes with resale flats. At £280k, this flat is well above the typical Leeds flat price. That suggests either a premium location (Chapel Allerton, Roundhay, Headingley) or a newer development.
3. **If it is a new build, the "−10% shock" is close to the base case.** New-build premiums of about 5–15% often disappear at first resale.
4. **Judgment:** 1.25% nominal means a real-terms fall of about 1–2%/yr, which is not a demanding hurdle. Even so, Leeds flats as a category have produced both above and below that over 5-year windows. Treat it as roughly a 50/50 call at year 5, tilting toward buying at year 7.
5. **Verify with data, not with me.** Pull UK HPI → Leeds → property type "Flat/maisonette" and compute rolling 5- and 7-year annualised growth (see §6). I could not access live data here.

---

## 3. Sensitivity grid (buy minus rent, £k)

The −10% shock is modelled as an immediate 10% fall after purchase, followed by +2%/yr.

### Year 5

The remortgage rate does not matter at year 5 because you sell at the end of the fix.

| Price path ↓ / Service charge growth → | 3% | 6% | 10% |
|---|---|---|---|
| −2%/yr | −43.2 | −43.8 | −44.7 |
| 0%/yr | −17.2 | −17.9 | −18.8 |
| **+2%/yr** | **+10.9** | **+10.2** | **+9.3** |
| +4%/yr | +41.3 | +40.6 | +39.8 |
| −10% shock, then +2% | −23.4 | −24.0 | −24.9 |

### Year 7

| Price path | RM 3.5%: SC 3% / 6% / 10% | RM 4.6%: SC 3% / 6% / 10% | RM 6.0%: SC 3% / 6% / 10% |
|---|---|---|---|
| −2%/yr | −48.2 / −49.6 / −51.8 | −52.8 / −54.2 / −56.4 | −58.8 / −60.2 / −62.4 |
| 0%/yr | −13.1 / −14.5 / −16.7 | −17.7 / −19.1 / −21.3 | −23.7 / −25.1 / −27.3 |
| **+2%/yr** | +26.6 / +25.2 / +23.0 | **+22.0** / +20.6 / +18.4 | +16.0 / +14.6 / +12.4 |
| +4%/yr | +71.3 / +69.9 / +67.7 | +66.7 / +65.3 / +63.1 | +60.7 / +59.3 / +57.1 |
| −10% shock | −8.3 / −9.7 / −11.9 | −12.9 / −14.3 / −16.5 | −18.9 / −20.3 / −22.5 |

Remortgage detail:
- At 3.5% the payment drops to £1,214.86 and the balance at month 84 is £194,459.
- At 6% the payment rises to £1,500.58 and the balance at month 84 is £197,921.

### What actually flips the answer

1. **Price growth is the only input that flips the sign.** Every row has the same sign in every column.
2. **A −10% shock is not recovered by year 7**, even with +2%/yr afterwards (−£12.9k).
3. **The remortgage rate moves the year-7 break-even** from about 0.7% (at 3.5%) to about 1.2% (at 6%), and up to about 1.4% with 10% service charge growth as well. It only matters near the break-even line.
4. **Ordinary service charge growth has a small direct effect**: at most −£1.5k at year 5 and −£3.6k at year 7. The real service charge risks are two things the grid cannot capture:
   - one-off major-works levies (Section 20 bills of £5–20k+);
   - high or fast-rising charges depressing the resale price and making the flat harder to sell. That feeds back into the price row, which does flip the answer.

---

## 4. Input corrections

### Savings tax
- **Personal Savings Allowance:** £1,000 of interest is tax-free for basic-rate taxpayers and £500 for higher-rate taxpayers.
- **Your exposure:** £46,500 at 4% earns about £1,860 in year 1, rising to about £3,400 by year 5. Outside an ISA you would pay roughly **£1.5k of tax over 5 years at basic rate, or about £4k at higher rate**.
- **Upcoming changes, as announced in the November 2025 Budget (check they went ahead):**
  - savings tax rates rise by 2 points from April 2027;
  - the cash ISA limit falls to £12k for under-65s from 6 April 2027, while the overall ISA limit stays at £20k.
- **What to do:** use your remaining 2026/27 allowance now, then the 2027/28 allowance, and you can shelter nearly everything.
- **Effect on the model:** my base assumes tax-free savings, which is the most favourable case for renting. Taxed savings make buying slightly better.

### Lifetime ISA
- **Rules:**
  - you must be aged 18–39 to open one;
  - contributions up to £4k/yr earn a 25% bonus (up to £1k/yr);
  - the home must be your first, cost ≤£450k (£280k ✓) and be bought with a mortgage;
  - **the account must have been open at least 12 months** before you use it;
  - other withdrawals carry a 25% charge, which costs you about 6.25% of your own money.
- **Status:** the government said in late 2025 it would consult on replacing the LISA with a new first-time-buyer product. Existing accounts keep their rules, but check the current position before opening one.
- **Buy now:** a LISA is useless unless you already hold one opened 12+ months ago. If you do, it adds up to £1k per year held, and you should tell me, because it changes the deposit maths.
- **Rent, save, buy later:** open a LISA now and pay in £4k before 5 April 2027 and £4k after 6 April 2027. That earns a **£2k bonus**, and the account becomes usable from about November 2027.

### SDLT
**£0 is confirmed.** Since 1 April 2025, first-time buyer relief gives 0% up to £300k and 5% from £300k to £500k, with no relief above £500k. Buying an existing lease raises no lease-premium complication. Without the relief (for example, a joint buyer who has owned before) you would pay **£4,000**.

### Arrangement fee and ERC
- **Arrangement fees** at 85% LTV are typically £0–£1,499, often £999. Check whether your £4,500 includes it.
- **Adding the fee to the loan** avoids the cash cost but you pay 4.6% interest on it for 25 years.
- **Early repayment charges** are usually tiered across a 5-year fix, for example 5/4/3/2/1%.
- **Example:** selling at month 48, with a balance of about £215,695 and a 2% ERC, costs **about £4.3k**. That alone raises the year-4/5 break-even by about 0.3 points.
- **Two ways to avoid it:**
  - **complete after the fix end date**;
  - **use portability**, which lets you move the mortgage to your next home.

### Emergency fund: buying uses all £46,500

**The risk:**
- your fixed housing cost is about £1,720/month;
- 3 months without income needs about £5.2k for housing alone;
- leasehold flats regularly bring surprise costs: special levies, insurance spikes, or a £5–15k Section 20 major-works bill;
- with no buffer, any of these goes on credit at 20%+ APR, or forces a sale.

**Alternative A: 10% deposit (90% LTV)**
- I assumed a rate of about 5.0%. Check this; it is typically 0.2–0.5 points above the 85% rate.
- Deposit £28,000 + costs £4,500 leaves a **£14,000 buffer**.
- Payment £1,473 vs £1,336; balance at month 60 £223,222 vs £209,450.
- Net cost: the gap at +2% falls from about +£10.9k to about +£5.1k, and the **year-5 break-even rises to about 1.65%**.
- You are also closer to negative equity: −2%/yr growth puts you at about 88% LTV at remortgage.

**Alternative B: rent 12 more months with a LISA**
- Assumes you save the same ~£470/month you would otherwise spend on owning.
- After a year you would have about £54k plus the £2k bonus, or **about £56k**.
- Buying at about £285.6k (after +2%) then leaves an **£8–9k buffer at 85% LTV**.

What waiting costs, at +2%:

| Item | Effect of waiting a year |
|---|---|
| A year of the flat's price gain | −£5.6k |
| Lower costs: renting is about £2.3k cheaper than owning's interest, service charge, upkeep and lost savings interest | +£2.3k |
| LISA bonus | +£2k |
| **Net** | **about −£1–2k** |

At ≤1.2% growth, waiting comes out ahead.

**This is the cheapest way to buy a buffer.**

---

## 5. Leasehold due diligence

| Document | What to check | Red flags that change the decision or hurt resale/remortgage in 5–7 yrs |
|---|---|---|
| **Lease** (and title, OC1/OC2) | Term (115 yrs ✓), ground rent amount and review clause, service charge %, repair split, alteration/sublet/pet/short-let clauses, forfeiture | Ground rent that doubles or is RPI-linked; ground rent >£250/yr (Housing Act AST problem, lenders refuse); ban on subletting (kills your plan B if you move); you being responsible for windows or structure; vague or uncapped service charge clauses. Ask how the £1,800 splits between ground rent and service charge. |
| **3–5 years of service charge accounts** (certified) and the current budget | Trend, insurance line, balancing charges, arrears | Rises above 6–8%/yr; insurance jumps (a building-safety signal); repeated year-end deficits; high arrears from other leaseholders, which you end up underwriting |
| **Reserve fund** and planned maintenance plan | Balance vs upcoming works | No reserve fund, or one too small for roof, lift or window replacement in the next 10 years. That means levies are coming. |
| **LPE1 management pack** (plus FME1 if the estate is shared) | Planned works, disputes, arrears, insurance, building safety answers | "Unknown" answers; tribunal cases; change of managing agent; recent or pending Right to Manage |
| **Section 20 notices** (past and pending) | Any consultation for works over £250 per flat | Any notice of intention issued: the cost lands on you, so negotiate a retention or a price cut |
| **Fire risk assessment** (and FRAEW / PAS 9980 if cladding) | Date, actions, completion | Outstanding "high" or "intolerable" actions; waking watch; assessment more than 2 years old |
| **EWS1 / cladding status** | EWS1 rating, Cladding Safety Scheme or developer remediation, Building Safety Act leaseholder deed of certificate (11m+ buildings) | B2 rating; remediation unfunded; missing deed of certificate. Any of these means some lenders refuse, so you cannot sell or remortgage. **Walk away unless resolved.** |
| **Buildings insurance schedule** | Premium, excess, commissions | Large excess, or cladding-related exclusions |

---

## 6. Validation

### HM Land Registry Price Paid backtest
1. Use the PPD search at landregistry.data.gov.uk/app/ppd, or download the full CSV from gov.uk "Price Paid Data".
2. Filter by the building's postcode (and neighbouring ones), property type = **F**, duration = **L**.
3. Match repeat sales of the same SAON/PAON (flat number + building) and compute annualised growth for pairs about 5–7 years apart, for example bought 2018–2020 and sold 2024–2026.
4. Run each pair through the same model, using the mortgage rates and rents of that period (fixes were about 2–2.5% in 2019–21, so take rent history from the ONS Price Index of Private Rents for Leeds). Ask whether that buyer beat renting.
5. Cross-check against UK HPI for Leeds flats (not all-property).
6. Caveat: PPD omits some non-market transfers, and a small building may give only a handful of pairs.

### Figures that should match exactly
- **Lender's ESIS:**
  - monthly payment £1,336.43, unless the fee is added to the loan;
  - total repayable about £400,929 over 25 yrs at a constant 4.6%;
  - the arrangement fee;
  - the ERC schedule;
  - the APRC (will differ from 4.6%).
- **HMRC SDLT calculator:** residential, first-time buyer, £280,000, existing lease → **£0**.

### What would overturn this conclusion
- **Valuation below price:** each £5k under price shifts the gap by about −£4.9k and may leave a deposit shortfall.
- **Survey:** structural or damp defects, or a short remaining life on the roof or lifts.
- **Solicitor's report:** an EWS1 issue, an escalating ground rent, a subletting ban, pending Section 20 works, or a low reserve fund.
- **Any of these** effectively moves you into the "shock" row of the grid.

---

## 7. Summary

**Break-even price growth:**
- **Year 5: ≈1.25%/yr**. With a £999 fee it is about 1.35%; selling inside the fix, about 1.5%; with a 10% deposit, about 1.65%.
- **Year 7: ≈0.9%/yr**, ranging from 0.7% (3.5% remortgage) to 1.4% (6% remortgage and 10% service charge growth).

**Assumptions that matter most:**
1. **Price growth for this specific flat.** Flats lag all-property figures, and a new-build premium is a real risk.
2. **How long you hold, and when you sell relative to the fix end.** About £9k of friction plus a possible ERC.
3. **Building and lease risk** (cladding, major works, ground rent terms). This drives both levies and saleability, which is where the "service charge" risk really sits.

**Non-financial trade-offs:**
- **Flexibility.** A renter can leave with 2 months' notice. Selling a leasehold flat takes 3–6+ months, and management packs cause delays.
- **Renters' Rights Act.** The main tenancy reforms commenced 1 May 2026 (check details):
  - no section 21 evictions;
  - periodic tenancies only;
  - one rent increase a year, which you can challenge at tribunal;
  - a right to request pets.
  - Renting is now more secure than the "insecure renter" stereotype. A landlord can still repossess to sell or move in, but only after 12 months and with 4 months' notice.
  - Possible upward pressure on rents as some landlords exit.
- **Security and control as a leaseholder.** You cannot be moved on. However, you are partly controlled by the freeholder and managing agent: pets, subletting and alterations depend on the lease.

**Conditional recommendation:**

> **Buy if** (a) the lease, LPE1, accounts, reserve fund, fire risk assessment and EWS1 come back clean (fixed ground rent ≤£250, no pending Section 20 works, no cladding liability, subletting allowed); **and** (b) the valuation is at or above £280k and local flat-only data supports roughly ≥1.5%/yr; **and** (c) you can keep a buffer of at least £6–10k, via a 90% LTV loan or by waiting about 12 months with a LISA; **and** (d) you are likely to stay past the fix end, ideally 7 years.
> **Otherwise rent**, keep savings in a cash ISA (plus a LISA if you're under 40 and still intend to buy), and revisit in 12 months.
> The cheapest risk-reducer is to **wait ~12 months with a LISA**: it costs about £1–2k at +2% growth and wins at lower growth.

---

## 8. Spreadsheet layout

Inputs in named cells: `g` (price growth), `R1` 4.6%, `R2` (remortgage rate), `s` (service charge growth), `i` 4%, `shock` (0 or −10%).

Rows: month `m` = 0…84. Row 0 holds the opening values: B = 238,000, M = 46,500, N = 0 (or your buffer).

| Col | Field | Formula (row for month m) |
|---|---|---|
| A | m | 0…84 |
| — | y | `=ROUNDUP(m/12,0)` (helper) |
| B | Balance | `=B_prev − F` |
| C | Rate | `=IF(m<=60, R1, R2)` |
| D | Payment | m 1–60: `=PMT(R1/12,300,-238000)`; m ≥ 61: `=PMT(R2/12,240,-B60)` |
| E | Interest | `=B_prev*C/12` |
| F | Principal | `=D−E` |
| G | Value | `=280000*(1+shock)*(1+g)^(m/12)` |
| H | Service charge/mo | `=1800/12*(1+s)^(y−1)` |
| I | Upkeep/mo | `=1%*G(at start of year y)/12` |
| J | Buy outlay | `=D+H+I` |
| K | Rent | `=1250*1.03^(y−1)` |
| L | Difference | `=J−K` |
| M | Renter pot | `=M_prev*(1+i/12)+MAX(L,0)` |
| N | Buyer pot | `=N_prev*(1+i/12)+MAX(−L,0)` |
| O | Buy net worth | `=G*(1−1.5%) − B + N − ERC` |
| P | Gap | `=O − M` |

**To solve for break-even:** use Goal Seek to set `P` at m = 60 (or 84) to 0 by changing `g`.

**To build the grid:** use a two-way Data Table over `g` × `R2`, with `s` as a third scenario set.

**Variants:**
- 10% deposit: set the loan to 252,000, the rate to about 5.0%, and opening N to 14,000.
- Savings tax: replace `i` with an after-tax rate, or subtract `tax = MAX(0, annual interest − PSA) × marginal rate` each April.

This is a model, not regulated advice. Run the final numbers past a whole-of-market mortgage broker, and have your conveyancer review the leasehold pack before you exchange.
