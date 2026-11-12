# rent-deeper-1

Writer: claude-opus-5-5

## Call 1 prompt

You are an AI assistant with this skill installed:

<skill>
---
name: deeper
description: Rewrite a task into its deeper version (same scope, more expert) before doing it. Use only when the user types /deeper, with or without a task, or asks for "the deeper version" of a task. Do not use it on your own initiative.
license: Apache-2.0
metadata:
  version: "1.1.2"
  source: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models (13 October 2026), Depth section"
---

# /deeper: a deeper version of the task, not a bigger one

Adapted from the Depth section of Felix Rieseberg, "How to be more ambitious: A tutorial for
humans with models", 13 October 2026:
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

The task is whatever the user wrote with /deeper. If they wrote nothing, use the task currently
under discussion. If there is none, ask for the task in one line and stop.

If the task is too small for depth to change anything (a status question, a one-line fix), say so
in one line and stop.

Keep the scope the same size. Deeper means more expert, not more features. Don't start the work.
First answer these four, briefly and specifically for this task:

1. **What would a top professional in this field do here that I haven't asked for?** Name the
   field. Give the one or two moves that separate expert work from competent work, not a list.
2. **What is the rawest material they would start from?** Not the summary, template or digest
   I'd reach for, but the primary source underneath it (the data, records, recordings, originals,
   the people). If you can read files, check the workspace first. Say what's here, where it is,
   and what's missing. If you can't, ask me for it. Name one thing we take as true that this
   material could disprove.
3. **Which methods and tools would they use?** Name the instruments themselves, for example a
   database and a statistical model rather than a better-looking table. Models tend to change
   their vocabulary without changing their method. Say which of these tools are already here.
   Don't swap in a weaker tool just because it's to hand.
   Then the skills and agents for the field, if your environment has them. List the installed
   skills that fit (for example `.agents/skills`, `~/.claude/skills`, `~/.codex/skills`,
   `~/.cursor/skills`, enabled plugins) and the subagent types on offer. If you can run shell
   commands, offer to search the open skills ecosystem with `npx skills find <field>`, which
   downloads and runs the skills CLI from npm, and run it only if I say yes. Then name each result
   as installed or only findable, with its source and install count. If you can't run commands,
   say so rather than guessing. Ask before downloading or installing anything.
4. **What, other than you or me, would show the result is right?** A test, a measurement, a
   tool, a real audience, a domain expert. Prefer something that can be run straight away. A
   model grading its own work doesn't count. Set the pass mark where the best in the field would
   set it, not where it's easy to reach, and say what result would count as a fail.

Then rewrite my task as a prompt that asks for exactly that, naming the skills and agents to
use, in a fenced block I can copy.

**Same deliverables.** Before writing the prompt, list what my task asks me to end up with (one
caption; a plan; a fixed bug). The prompt asks for those and nothing else. Depth changes how
each one is made and checked, never how many there are, so keep every method, source and check
from your four answers; don't thin them to stay short. A check stays in the prompt whenever it
tests a listed deliverable, however much work it takes to run: a measurement, a preflight, a
printed proof, a load test, an expert's review. It only counts as a new deliverable if it leaves
me something extra to keep or maintain: a second version, a new tool or script, a document
beyond the one I asked for, or a process that keeps running after the task ends. Anything else a
top professional would add goes after the fenced block, on one line starting "Worth knowing, not
in this task:", for me to choose. Leave that line out if there's nothing to add.

End by asking whether to run it.

</skill>

The user typed:

/deeper Should I rent or buy this flat?

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

# /deeper: Rent or buy this flat in Leeds

**The task:** decide whether to rent or buy this flat, given your figures and a 5–7 year stay.
**Deliverable:** one recommendation (rent or buy) with the reasoning behind it. Nothing else.

### 1. What would a top professional do that you haven't asked for?

The field is independent financial planning, with UK residential conveyancing for the leasehold side. Two things separate expert work from competent work here:

- **Compare net worth, and find the break-even.** Compare what you'd own at year 5 and at year 7 on each path, counting every cash flow. Instead of betting on one price forecast, work out the house-price growth at which buying and renting come out equal. Then judge whether this flat is likely to beat that rate. With 5% equity, 1.5% selling costs and leasehold costs, the break-even may be well above 0%.
- **Treat the lease as a financial instrument.** For a flat, the biggest risks are rarely the interest rate. They are:
  - ground-rent review clauses (for example, doubling),
  - how fast the service charge rises,
  - a thin sinking fund ahead of major works (section 20 bills),
  - cladding and fire safety (EWS1), which can make a flat hard to sell.
  
  Buying also uses all £46,500, leaving no emergency fund. That needs weighing.

### 2. What raw material would they start from?

**What's here:** only the figures in your message. You haven't given me any documents. I haven't checked your working folder, and I'd look there first if we run this.

**What's missing:**
- the lease itself
- the last 3 years of service charge accounts, the current budget, and the sinking fund balance
- any section 20 notices
- the management pack (LPE1)
- EWS1 status
- your mortgage illustration (ESIS)
- **HM Land Registry Price Paid data for flats in this postcode**
- live rental listings for comparable 2-beds

**Assumptions this could disprove:**
- **"+2% a year round here."** That figure most likely mixes houses and flats. In Leeds, flats, especially leasehold new-build-era blocks, have often grown much more slowly than houses, and some have stayed flat. If flats here grew at about 0%, the answer could flip.
- **"£1,800 stays £1,800."** The service charge accounts would show whether it does.
- **"Savings earn a clean 4%."** About £1,860 a year in interest exceeds the £1,000 Personal Savings Allowance for a basic-rate taxpayer, so the interest gets taxed unless it's held in an ISA.

### 3. Which methods and tools would they use?

- **A model:** a month-by-month cash-flow model in Python (pandas) covering:
  - a full amortisation schedule for the £238,000 loan at 4.6% over 25 years
  - both paths over 84 months
  - savings interest after tax
  - rent rising 3% a year
  - service charge and upkeep rising with inflation
  - net worth at months 60 and 84 after selling costs
- **Analysis on top of the model:**
  - a solve for the break-even growth rate
  - a sensitivity grid of price growth (−2% to +4%) against the post-fix mortgage rate
  - a simple Monte Carlo on price growth, using the spread in the local flat data
- **Data sources:** the Land Registry Price Paid / UK HPI flat series for Leeds, and the HMRC SDLT calculator. Under the first-time buyer rules since April 2025, the nil band runs to £300,000, so stamp duty on £280,000 should be £0. The calculator confirms this.
- **What's already available:** Python can run in this environment. The data sources are public downloads.

**Skills and agents:** I haven't listed installed skills or subagent types yet, so I can't name any that fit. I can check the usual skill folders. If you say yes, I can also search the open ecosystem with `npx skills find personal-finance`, which downloads and runs the skills CLI from npm. I'd report each result as installed or only findable, with its source and install count. I won't download or install anything without asking.

### 4. What, other than us, would show the result is right?

- **Mortgage maths:** the amortisation must match your lender's ESIS, or the MoneyHelper mortgage calculator, to within £5 on the monthly payment and £50 on the balance at month 60. If not, it fails.
- **Stamp duty:** the HMRC calculator confirms the figure.
- **Model reconciliation:** both paths must start with exactly £46,500. Each month, both must spend the same total, with the difference saved by whoever pays less. Any money that appears or disappears unexplained is a fail.
- **Robustness:** the recommendation must say whether it holds across the plausible growth range from the local flat data. If it flips inside that range and the answer doesn't say so, it fails.
- **Human review:** a solicitor's report on the lease, plus a whole-of-market mortgage adviser. You'd arrange both. I'd flag exactly what to ask them.

---

```
Decide whether I should rent or buy this flat. Deliverable: one recommendation (rent or buy) with its reasoning. Nothing else.

Inputs: 2-bed leasehold flat, Leeds, £280,000, 115 years left. Service charge + ground rent £1,800/yr. Savings £46,500. Deposit 15% = £42,000, buying costs ~£4,500, first-time buyer. Mortgage £238,000 at 4.6%, 25-year repayment, assume 4.6% throughout. Comparable rent £1,250/month, rising ~3%/yr. Savings earn 4%. Upkeep 1% of price/yr. Selling costs 1.5%. Horizon 5 years, possibly 7. Local prices roughly +2%/yr recently.

Method:
1. Check the workspace for the lease, service charge accounts and budget, sinking fund, section 20 notices, LPE1, EWS1 and the mortgage ESIS. List what's present and missing. Ask me for what's missing, and run with stated assumptions meanwhile.
2. Download HM Land Registry Price Paid / UK HPI data for FLATS in this Leeds postcode district (ask me for the postcode). Measure their actual annual growth and spread over 5 and 10 years. Test whether the "+2%/yr" assumption holds for flats.
3. Build a month-by-month Python (pandas) model over 84 months for both paths:
   - Buy: full amortisation, service charge, upkeep, sale at month 60 and 84 net of 1.5%.
   - Rent: rent rising 3%/yr. The £46,500 and any monthly difference earn 4%, taxed above the £1,000 Personal Savings Allowance (also show the ISA case).
   Both paths start with £46,500 and spend the same total each month.
4. Report net worth on each path at months 60 and 84. Solve for the break-even annual price growth. Show a sensitivity grid of growth −2% to +4% against post-fix rates 3.5–6.5%. Run a Monte Carlo on growth using the local flat data's spread.
5. Weigh the leasehold risks (ground rent review terms, service charge growth, major works, EWS1) and the loss of any emergency fund if buying.

Checks (all must pass):
- Monthly payment within £5 and month-60 balance within £50 of the lender ESIS or MoneyHelper calculator.
- SDLT confirmed via the HMRC calculator.
- Cash reconciles to the pound on both paths.
- State plainly whether the recommendation holds across the local flats' plausible growth range, and if not, what it hinges on.
- List the exact questions for my conveyancing solicitor (lease) and a whole-of-market mortgage adviser.

Use any installed personal-finance or data-analysis skills and a general-purpose subagent for the data download, if available.
```

Worth knowing, not in this task: if you're under 40, a Lifetime ISA adds a 25% bonus (up to £1,000 a year) for first-time buyers on homes up to £450,000. It only pays out after 12 months, so it would matter if you delay buying.

Shall I run it? And do you want me to search for skills with `npx skills find` first?

## Extraction

last fenced block

## Call 2 prompt

Decide whether I should rent or buy this flat. Deliverable: one recommendation (rent or buy) with its reasoning. Nothing else.

Inputs: 2-bed leasehold flat, Leeds, £280,000, 115 years left. Service charge + ground rent £1,800/yr. Savings £46,500. Deposit 15% = £42,000, buying costs ~£4,500, first-time buyer. Mortgage £238,000 at 4.6%, 25-year repayment, assume 4.6% throughout. Comparable rent £1,250/month, rising ~3%/yr. Savings earn 4%. Upkeep 1% of price/yr. Selling costs 1.5%. Horizon 5 years, possibly 7. Local prices roughly +2%/yr recently.

Method:
1. Check the workspace for the lease, service charge accounts and budget, sinking fund, section 20 notices, LPE1, EWS1 and the mortgage ESIS. List what's present and missing. Ask me for what's missing, and run with stated assumptions meanwhile.
2. Download HM Land Registry Price Paid / UK HPI data for FLATS in this Leeds postcode district (ask me for the postcode). Measure their actual annual growth and spread over 5 and 10 years. Test whether the "+2%/yr" assumption holds for flats.
3. Build a month-by-month Python (pandas) model over 84 months for both paths:
   - Buy: full amortisation, service charge, upkeep, sale at month 60 and 84 net of 1.5%.
   - Rent: rent rising 3%/yr. The £46,500 and any monthly difference earn 4%, taxed above the £1,000 Personal Savings Allowance (also show the ISA case).
   Both paths start with £46,500 and spend the same total each month.
4. Report net worth on each path at months 60 and 84. Solve for the break-even annual price growth. Show a sensitivity grid of growth −2% to +4% against post-fix rates 3.5–6.5%. Run a Monte Carlo on growth using the local flat data's spread.
5. Weigh the leasehold risks (ground rent review terms, service charge growth, major works, EWS1) and the loss of any emergency fund if buying.

Checks (all must pass):
- Monthly payment within £5 and month-60 balance within £50 of the lender ESIS or MoneyHelper calculator.
- SDLT confirmed via the HMRC calculator.
- Cash reconciles to the pound on both paths.
- State plainly whether the recommendation holds across the local flats' plausible growth range, and if not, what it hinges on.
- List the exact questions for my conveyancing solicitor (lease) and a whole-of-market mortgage adviser.

Use any installed personal-finance or data-analysis skills and a general-purpose subagent for the data download, if available.

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

# Recommendation: Buy, but only if the lease checks clear and you keep a cash buffer

At the +2%/yr you've seen locally, buying leaves you about **£14k better off at 5 years and £27k at 7 years**. Prices only need to grow about **1.1%/yr (5 years) or 0.7%/yr (7 years)** for buying to break even.

Two things could reverse this:

1. **Flat prices stagnate or fall.**
2. **A leasehold surprise hits while you have no savings left.** Your £46,500 goes exactly on the deposit (£42,000) and costs (£4,500), leaving £0.

**What I couldn't do.** No file, web or code tools were available in this session. So I could not:
- read your workspace documents,
- download the Land Registry or UK HPI flat data, or
- run the pandas model or a computed Monte Carlo.

The figures below are worked by hand from standard formulas. Treat them as close estimates.

## Core numbers (4.6% throughout, basic-rate taxpayer)

| | Month 60 | Month 84 |
|---|---|---|
| **Buy**: sale value at +2%/yr, less 1.5% costs | £304,505 | £316,808 |
| Mortgage balance | £209,452 | £196,065 |
| **Buy net worth** | **£95,052** | **£120,743** |
| **Rent net worth**, savings taxed above £1,000 allowance | £81,327 | £93,292 |
| Rent net worth, ISA case (all savings tax-free) | £83,005 | £96,127 |
| Break-even price growth (taxed / ISA) | 1.06% / 1.18% a year | 0.69% / 0.83% a year |

**Monthly costs:**
- Mortgage payment: **£1,336.44**. Your lender's ESIS or the MoneyHelper calculator should match this within pennies.
- Total cost of owning: £1,719.77 a month (mortgage, £150 service charge and ground rent, £233.33 upkeep).
- The rent path spends the same total. The gap between owning costs and rent goes into savings: £469.77 a month in year 1, falling to £227.20 in year 7 as rent rises.
- Both paths reconcile: buying uses £42,000 + £4,500 = £46,500 on day one, and the rent path starts with the same £46,500.

**Stamp duty is £0.** First-time buyer relief covers purchases up to £300k on properties up to £500k. Please confirm with the HMRC calculator.

## Buy minus rent (£k): price growth vs rate after the fix

The rate after the fix only affects months 61–84, so the month-60 result is the same at every rate.

| Growth/yr | Month 60 (any rate) | Month 84 at 3.5% | at 4.6% | at 5.5% | at 6.5% |
|---|---|---|---|---|---|
| −2% | −41.5 | −45.3 | −49.9 | −53.7 | −58.0 |
| −1% | −28.5 | −27.7 | −32.3 | −36.1 | −40.4 |
| 0% | −15.0 | −8.9 | −13.6 | −17.4 | −21.6 |
| +1% | −0.9 | +11.0 | +6.3 | +2.5 | −1.7 |
| +2% | +13.7 | +32.1 | +27.5 | +23.6 | +19.4 |
| +3% | +28.9 | +54.5 | +49.8 | +46.0 | +41.8 |
| +4% | +44.8 | +78.2 | +73.6 | +69.8 | +65.5 |

## Does the recommendation hold across plausible growth?

**Not fully.** It holds at roughly +1%/yr or more. It flips at 0% or below.

I couldn't measure your postcode's flat data. Nationally, flats have grown more slowly than houses over the last decade, and some Leeds flat stock (especially city-centre new-builds) has been weak. If local flats' 5-year growth has averaged about +2% with a spread of 2–3 points, buying wins in very roughly 60–65% of outcomes. That is an illustration, not a computed Monte Carlo.

The decision mainly hinges on two things:
1. **Flat prices in your postcode district specifically.** Send me the postcode and I'll test the +2% figure.
2. **The leasehold costs described below.**

## Leasehold and liquidity risks (the real weak points)

- **No emergency fund.** A major-works bill, boiler, job gap or repair would go straight onto debt. Fix this by:
  - asking about a 90% loan, which frees about £14k at a slightly higher rate, or
  - saving £10–15k first.
- **Service charge growth and major works.** A £10k section 20 bill (the legal notice for big shared repairs) would wipe out most of the 5-year advantage at +2% growth.
- **Ground rent.** If the lease has doubling or RPI-linked reviews, resale and future mortgages can be impaired.
- **EWS1 (cladding fire-safety form).** If the building is over 11m or has cladding and the form is missing or rated B2, the flat may be hard to sell or remortgage.
- **115 years left is fine.** No lease extension is needed within 7 years.

## Assumptions

- Prices change at a constant annual rate.
- Upkeep is fixed at 1% of the purchase price (£2,800/yr).
- Service charge is flat at £1,800/yr.
- Rent rises 3% once a year.
- Savings earn 4% compounded monthly. Interest above £1,000 is taxed at 20%. A higher-rate taxpayer would do worse renting, which favours buying.
- The ISA case assumes everything is sheltered from tax. In reality you can only add £20k a year.
- There is no early repayment charge, since you sell at or after the end of the 5-year fix.
- All documents were treated as missing. Please send: the lease, service charge accounts and budget, sinking fund (the building's repair reserve) balance, any section 20 notices, the LPE1 (the managing agent's information form), the EWS1, the ESIS, and your postcode.

## Questions for your conveyancing solicitor

1. What is the ground rent split, and what are the exact review terms (doubling, RPI-linked, escalation dates)?
2. What were the service charges for the last 3 years, what is this year's budget, and what was the year-on-year increase?
3. What is the sinking fund balance, and is there a planned-works schedule?
4. Are there any past, current or proposed section 20 notices, or disputes about the service charge?
5. Is an EWS1 needed? If so, what is its rating, and what is the cladding or fire-safety remediation status? Does the Building Safety Act's leaseholder protection apply, and is there a qualifying lease deed of certificate?
6. Who is the freeholder and who is the managing agent? Are there any restrictions on subletting, alterations or pets? Is it insured, and with what excess?
7. Is the lease length acceptable to all major lenders?
8. Has a statutory lease-extension or collective-enfranchisement (buying the freehold) claim been made?

## Questions for a whole-of-market mortgage adviser

1. Can you confirm the £1,336.44 monthly payment and a month-60 balance of about £209,450 from the ESIS?
2. What are the best 90% loan-to-value rates, so I can keep a roughly £14k buffer, and what would that cost over 5 years?
3. What are the early repayment charges and portability terms if I move in year 4–5?
4. Are any fees added to the loan?
5. Does the lender have criteria for leasehold, ground rent or EWS1 that could block a future remortgage?
6. What would the reversion (standard variable) rate be, and what are the realistic options when the fix ends?
