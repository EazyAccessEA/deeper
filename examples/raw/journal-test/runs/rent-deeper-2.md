# rent-deeper-2

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

# /deeper: Should I rent or buy this flat?

## 1. What would a top professional do that you haven't asked for?

**Field:** independent personal financial planning, with a leasehold conveyancer's eye.

- **Compare net worth when you leave, and find the break-even.** Work out your total wealth at year 5 and at year 7 under each option, with every pound accounted for. Then solve for the house-price growth rate at which buying and renting come out equal. The +2% figure stops being a guess you have to trust. The question becomes whether you think prices will beat X%.
- **Treat the lease and the cash buffer as risks, not footnotes.** £1,800 a year is this year's figure. What matters is how the service charge has moved, how ground rent is set to rise, the sinking fund, and any planned major works. Also, buying uses £46,500 of your £46,500, which leaves £0 for emergencies on day one.

## 2. The rawest material

I don't have file or shell access in this session, so I can't check your workspace. These are what's needed:

- **The lease:** the ground rent review clause (does it double, or follow RPI?), the service charge clauses, and any restrictions on letting.
- **The management pack (LPE1):** service charge accounts for the last 3–5 years, this year's budget, the sinking fund balance, planned or Section 20 major works, and fire-safety/EWS1 status.
- **The lender's KFI/ESIS:** product fee, early repayment charges and the official monthly payment. "4.6% fixed" alone isn't enough.
- **HM Land Registry Price Paid data** for this building and this postcode, flats only.
- **ONS Price Index of Private Rents** for Leeds.
- **Your tax band.** Interest of 4% on £46,500 is about £1,860 a year. That's above the £1,000 (basic rate) or £500 (higher rate) personal savings allowance, so renting's return is lower after tax.

**One belief this material could disprove:** "Prices here grow about 2% a year." That may be true of Leeds as a whole and false for flats, and especially for this development. Many Leeds flats have sold flat or below their earlier prices. Land Registry resales in the same building will show it.

## 3. Methods and tools

- **A year-by-year cash-flow model** (a spreadsheet or Python). It needs:
  - a real amortisation schedule, so the year-5 and year-7 loan balances are exact rather than estimated;
  - equalised outflows, so whichever option is cheaper each month invests the difference at 4% after tax;
  - rent rising 3% a year, plus upkeep, service charge, selling costs and ERCs.
- **Sensitivity analysis:** price growth from −2% to +5%, service charge growth, and the rate after the fix.
- **A break-even solver** for price growth at year 5 and at year 7.
- **Stamp Duty check:** first-time buyer relief makes a £280,000 purchase zero-rated. The model should confirm this, not assume it.
- **Skills and agents:** I can't list installed skills or subagents, or run `npx skills find personal-finance`, from here. If you're running this somewhere with shell access, I can search, but only if you say yes, and I won't install anything without asking.

## 4. What would show the answer is right, other than us

- **Reproduce the lender's figures.** The model's monthly payment must match the lender's KFI to within £1. The year-5 balance must match the lender's illustration (or an independent amortisation calculator) to within £10. If either is off, the model is wrong.
- **Hand-check year 1** line by line against bank-statement-style totals.
- **The recommendation must state its break-even growth rate** and say whether it survives ±1 percentage point. If the answer flips inside the plausible range and the write-up doesn't say so, that's a fail.
- **Outside review:**
  - a fee-only mortgage adviser looks over the numbers;
  - a leasehold solicitor reviews the lease and the LPE1;
  - a RICS Level 2 survey checks the flat itself.

## Deliverables your task asks for

One recommendation (rent or buy) with its reasoning.

```
Decide whether I should rent or buy this flat, and give me one recommendation with its reasoning. Do it the way an independent financial planner with leasehold expertise would.

Facts: 2-bed leasehold flat in Leeds, £280,000, 115 years left. Service charge + ground rent £1,800/yr. Savings £46,500. 15% deposit £42,000, buying costs ~£4,500. First-time buyer. Mortgage: 85% LTV, 4.6% fixed 5 yrs, 25-yr repayment, assume 4.6% after. Equivalent rent £1,250/month, rising ~3%/yr. Savings earn 4%/yr, and I'd invest any monthly difference. Upkeep 1% of price/yr. Selling costs 1.5%. Stay 5 years, maybe 7. Local prices ~+2%/yr recently.

Method:
1. Build a year-by-year cash-flow model (spreadsheet or Python) comparing my net worth at year 5 and year 7 under each option. Use a real amortisation schedule. Equalise outflows so the cheaper option invests the difference at 4% after tax (ask my tax band; apply the personal savings allowance). Include rent growth, upkeep, service charge, selling costs, any ERCs and product fees, and confirm first-time buyer stamp duty is £0.
2. Solve for the break-even house-price growth rate at year 5 and year 7. Run sensitivities: price growth −2% to +5%, service charge growth 0–8%/yr, post-fix rate 3.5–6.5%.
3. Ask me for, and use, the primary sources: the lease (ground rent review and service charge clauses), the LPE1 management pack (3–5 years of service charge accounts, sinking fund, planned/Section 20 works, EWS1), the lender's KFI, Land Registry Price Paid data for flats in this building/postcode, and the ONS private rents index for Leeds. Test the +2% assumption against Land Registry resales in this development.
4. Flag that buying leaves £0 cash buffer, and say what that means for the recommendation.

Checks (report each as pass/fail):
- Model monthly payment matches the lender KFI within £1; year-5 balance matches the lender's illustration or an independent amortisation calculator within £10.
- Year 1 hand-checked line by line.
- Recommendation states the break-even growth rate and whether it holds at ±1 percentage point; if it flips within the plausible range, say so plainly.
- List what a fee-only mortgage adviser, a leasehold solicitor and a RICS Level 2 survey must confirm before I act.

Deliverable: one rent-or-buy recommendation with reasoning, numbers at year 5 and 7, the break-even rate, and the check results. Nothing else.
```

Worth knowing, not in this task: a Lifetime ISA (the £280k price is under the £450k cap) adds a 25% bonus on up to £4,000 a year, but it must be open 12 months before you buy, which matters if you delay.

Shall I run it?

## Extraction

last fenced block

## Call 2 prompt

Decide whether I should rent or buy this flat, and give me one recommendation with its reasoning. Do it the way an independent financial planner with leasehold expertise would.

Facts: 2-bed leasehold flat in Leeds, £280,000, 115 years left. Service charge + ground rent £1,800/yr. Savings £46,500. 15% deposit £42,000, buying costs ~£4,500. First-time buyer. Mortgage: 85% LTV, 4.6% fixed 5 yrs, 25-yr repayment, assume 4.6% after. Equivalent rent £1,250/month, rising ~3%/yr. Savings earn 4%/yr, and I'd invest any monthly difference. Upkeep 1% of price/yr. Selling costs 1.5%. Stay 5 years, maybe 7. Local prices ~+2%/yr recently.

Method:
1. Build a year-by-year cash-flow model (spreadsheet or Python) comparing my net worth at year 5 and year 7 under each option. Use a real amortisation schedule. Equalise outflows so the cheaper option invests the difference at 4% after tax (ask my tax band; apply the personal savings allowance). Include rent growth, upkeep, service charge, selling costs, any ERCs and product fees, and confirm first-time buyer stamp duty is £0.
2. Solve for the break-even house-price growth rate at year 5 and year 7. Run sensitivities: price growth −2% to +5%, service charge growth 0–8%/yr, post-fix rate 3.5–6.5%.
3. Ask me for, and use, the primary sources: the lease (ground rent review and service charge clauses), the LPE1 management pack (3–5 years of service charge accounts, sinking fund, planned/Section 20 works, EWS1), the lender's KFI, Land Registry Price Paid data for flats in this building/postcode, and the ONS private rents index for Leeds. Test the +2% assumption against Land Registry resales in this development.
4. Flag that buying leaves £0 cash buffer, and say what that means for the recommendation.

Checks (report each as pass/fail):
- Model monthly payment matches the lender KFI within £1; year-5 balance matches the lender's illustration or an independent amortisation calculator within £10.
- Year 1 hand-checked line by line.
- Recommendation states the break-even growth rate and whether it holds at ±1 percentage point; if it flips within the plausible range, say so plainly.
- List what a fee-only mortgage adviser, a leasehold solicitor and a RICS Level 2 survey must confirm before I act.

Deliverable: one rent-or-buy recommendation with reasoning, numbers at year 5 and 7, the break-even rate, and the check results. Nothing else.

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

# Rent-or-buy recommendation: 2-bed leasehold flat, Leeds, £280,000

## Recommendation: Rent for now. Don't buy this flat on these terms.

On your stated numbers, buying comes out ahead. The lead is small, though, and it depends on two things:

- **Price growth above about 1.1% a year** for a leasehold flat. Your +2% figure comes from the local market generally, not from resales in this development.
- **Using every pound you have**, with no money set aside for a Section 20 major-works bill.

At year 5 the result **flips to renting if growth is 1 percentage point below your assumption**. That is well within the plausible range for flats.

If renting, I wouldn't leave the £46,500 in a taxable savings account. A Cash ISA avoids the tax, and a Lifetime ISA adds a 25% government bonus if you open it at least 12 months before buying.

**What would change this to "buy":**
- Land Registry resales in this development show at least +1.5% a year.
- The management pack (LPE1) is clean: no planned Section 20 works, a funded sinking fund, and a service-charge history rising no faster than inflation.
- You can keep at least £10,000 in reserve, for example by negotiating the price down or saving for another 12 months.

## Key assumptions (I had no documents)

- **Tax:** basic-rate taxpayer. That means a £1,000 personal savings allowance, with interest above it taxed at 20%. No ISA is assumed.
- **Mortgage fees and exit charges:** product fee assumed to be inside the £4,500 buying costs. No early repayment charge (you sell at the end of the fix, or on the reversion rate at year 7). No remortgage fee.
- **Running costs:**
  - Service charge and ground rent grow 3% a year.
  - Upkeep is 1% of the current value.
- **Cash flows:** interest is credited yearly, and monthly contributions earn about half a year's interest.
- **Stamp duty:** first-time buyer relief makes it **£0** at £280k, since the relief covers up to £300k on purchases up to £500k. This passes.

## Model results (base case: +2% prices a year)

| | Year 5 | Year 7 |
|---|---|---|
| Flat value | £309,143 | £321,632 |
| Less 1.5% selling costs | £304,506 | £316,808 |
| Mortgage balance | £209,452 | £196,066 |
| **Buyer net worth** | **£95,050** | **£120,740** |
| **Renter net worth** (£46.5k plus monthly difference, 4% less tax) | **£82,350** | **£95,600** |
| Buy advantage | +£12,700 | +£25,140 |

**Mortgage figures:**
- Loan of £238,000 at 4.6% over 300 months gives a payment of **£1,336.42 a month** (£16,037 a year).
- Interest paid over 5 years is about £51,640.

**Year 1, checked line by line:**

| Item | Buyer | Renter |
|---|---|---|
| Mortgage | £16,037 | |
| Service charge and ground rent | £1,800 | |
| Upkeep | £2,800 | |
| Rent | | £15,000 |
| **Total outgoings** | **£20,637** | **£15,000** |

- The renter invests the £5,637 difference.
- Renter interest: £46,500 × 4% + £5,637 × 2% = £1,972.70.
- Tax: (£1,972.70 − £1,000) × 20% = £194.50.
- Renter's pot at end of year 1: £46,500 + £5,637 + £1,778 = **£53,915**.
- Mortgage after year 1: principal repaid £5,198, interest £10,839, balance £232,802.
- Buying costs more every year in all 7 years, so only the renter ever invests a difference.

## Break-even growth and sensitivities

**Break-even price growth:**
- **Year 5: about +1.1% a year.** At +1% (−1pp from base) renting wins by about £1,900, so **it flips**. At +3% buying wins by about £27,900.
- **Year 7: about +0.8% a year.** It holds at ±1pp: buying wins by about £4,700 at +1% and about £46,900 at +3%.

**Buy minus rent, by annual price growth:**

| Price growth | −2% | 0% | +1% | +2% | +3% | +5% |
|---|---|---|---|---|---|---|
| Year 5 | −£41,300 | −£15,400 | −£1,900 | +£12,700 | +£27,900 | +£59,300 |
| Year 7 | −£49,700 | −£14,500 | +£4,700 | +£25,100 | +£46,900 | +£94,400 |

**Service-charge growth, 0% to 8% a year:**
- Year 5: buy advantage ranges from +£13,300 down to +£11,700.
- Year 7: from +£26,400 down to +£22,700.
- Gradual growth barely matters. The real risk is a one-off Section 20 bill, which this model does not include.

**Rate after the fix, 3.5% to 6.5%:**
- This only affects year 7. Buy advantage ranges from +£29,700 down to +£17,100.
- At 6.5% the monthly payment rises to £1,562.

## Zero cash buffer

Buying uses £46,500 of your £46,500, leaving **£0**. Any of these would go onto expensive debt or force a sale:
- a Section 20 levy (often £2,000 to £15,000 or more for a flat)
- a boiler failure
- a gap in your income

A forced sale inside the 5-year fix would also trigger an early repayment charge. The renter keeps £46,500 or more, available at any time. That safety is worth paying for when buying is ahead by only about £210 a month in expected value and could easily be behind. This is the main reason the recommendation is "rent", not "buy".

## Check results

| Check | Result |
|---|---|
| Monthly payment matches the lender's Key Facts Illustration (KFI) within £1 | **FAIL (not yet verifiable).** No KFI was provided. My standard formula gives £1,336.42. |
| Year-5 balance matches the lender or an independent calculator within £10 | **PARTIAL.** £209,452 from the closed-form calculation, worked by hand without running code. Not yet compared with the lender's illustration. |
| Year 1 checked line by line | **PASS** (shown above). |
| Break-even rate stated, ±1pp tested, flip disclosed | **PASS.** Flips at year 5 (−1pp); holds at year 7. |
| Stamp duty confirmed at £0 | **PASS**, under current first-time buyer relief rules. |
| Primary sources used | **FAIL.** I haven't received the lease, the LPE1 pack, EWS1, the KFI, Land Registry data or the ONS rents index. The +2% assumption is **untested** against resales in this development. |

## What each professional must confirm before you act

**Fee-only mortgage adviser:**
- The KFI's payment, APR, product and valuation fees, and early repayment charge schedule.
- The reversion rate after the fix.
- Whether a 90% loan, which would leave you a buffer, beats 85% once all costs are counted.
- Lifetime ISA eligibility and timing.

**Leasehold solicitor:**
- **Ground rent:** the review clause, checked for doubling or RPI-linked increases and whether it is onerous for lenders.
- **Service charge:** the apportionment, the sinking-fund provisions, and any restrictions on letting or alterations.
- **Management pack (LPE1):** 3 to 5 years of service-charge accounts, the sinking-fund balance, planned and Section 20 works, any disputes, and buildings insurance.
- **Building safety:** an EWS1 form or the building safety position.
- **Lease extension:** the likely cost, given 115 years remain.

**RICS Level 2 survey:**
- The condition of the flat and the visible common parts, including roof, windows and damp.
- Any defects likely to lead to Section 20 works.
- Whether the valuation supports £280,000, checked against resales in this development.
