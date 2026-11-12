# cv-deeper-2

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

/deeper Give me feedback on my CV for this job.

=== JOB ADVERT ===
Senior Marketing Executive, Hartwell Outdoor (Bristol, hybrid)
We sell outdoor clothing online and through 14 shops.
Essential:
1. 3+ years in B2C marketing
2. Planning and managing paid social budgets (Meta, TikTok) of £20k+ a month
3. Reporting on campaign performance with GA4
4. Writing briefs for designers and agencies
5. Running email campaigns in Klaviyo or a similar tool
Desirable: experience in retail or outdoor brands; a team of 1-2 to manage.

=== MY CV ===
Sam Okafor
Bristol | sam.okafor@example.com | 07700 900123

Profile
Creative and hard-working marketer with a passion for brands people love. Strong team player with excellent communication skills.

Experience
Marketing Coordinator, Fernbrook Coffee Roasters (online and 3 cafes), Feb 2023 to now
- Responsible for social media
- Ran paid social campaigns on Meta and TikTok
- Sent the weekly newsletter in Klaviyo to 38,000 subscribers; open rate rose from 31% to 44% after I rewrote the subject lines
- Wrote briefs for our freelance designer for packaging and seasonal campaigns
- Recieved the company's "Bean of the Year" award in 2024

Marketing Assistant, Lumen Lighting (B2C e-commerce), Sep 2019 to Mar 2022
- Helped with campaigns
- Pulled weekly reports from Google Analytics for the marketing manager
- Supported the launch of the spring 2021 range, which sold out in 6 weeks
- Managed the intern for summer 2021

Education
BA Marketing, University of the West of England, 2019

Skills
Meta Ads Manager, TikTok Ads, Klaviyo, Google Analytics, Canva, Excel

## Call 1 reply

# /deeper: CV feedback for Hartwell Outdoor

**1. What would a top professional do that you haven't asked for?**
The field is recruitment for marketing roles, from the hiring manager's side. Two moves separate expert feedback from competent feedback:
- **Screen against the criteria, not the prose.** A hiring manager scores each of the 5 essentials as *evidenced*, *implied* or *missing*. Today, #2 (£20k+/month budget) and #3 (GA4) are missing or only implied, which is usually enough to get you rejected.
- **Separate what is true from what is written.** Each gap gets one of two fixes. Either you already have the evidence and it isn't on the page, so you rewrite. Or you don't have it, so you decide how to address it honestly instead of inflating it.

**2. What is the rawest material?**
I can only see your CV text and the advert. I can't read files in this reply, so I haven't checked your workspace. The primary sources underneath your bullets are:
- Meta and TikTok Ads Manager spend history, with monthly totals, ROAS and CPA
- GA4 property access, or any reports you built rather than pulled
- Klaviyo campaign reports, including clicks, revenue per recipient and list growth
- 1–2 real briefs you wrote
- What happened between Mar 2022 and Feb 2023

Missing: all of the above, plus the full Hartwell job description if it's longer than the advert.

**One belief this could disprove:** that the 31%→44% open rate came from your subject lines. Apple Mail Privacy Protection has inflated open rates since late 2021. A Hartwell interviewer may know this. Click rate and revenue per email from Klaviyo would show whether the gain is real.

**3. Methods and tools**
- **Requirements-to-evidence matrix:** each essential and desirable item against the exact CV line that proves it, with a rating.
- **Keyword/ATS check** against the advert's terms: GA4, paid social, budget, briefs, Klaviyo, B2C, retail.
- **Your ad account and Klaviyo exports**, to put real numbers in place of "responsible for" and "helped with".
- **A 6-second scan test:** what does the top third of page 1 tell a screener?

Skills and agents: I can't run shell commands or list installed skills and subagents from here, so I won't guess what's available. If you run this where commands work, I can search the open skills ecosystem with `npx skills find resume` (and `recruiting`). That downloads and runs the skills CLI from npm, so I'd only do it if you say yes, and I'd ask before installing anything.

**4. What would show the feedback is right?**
Someone who hires marketing executives, or a retail/e-commerce recruiter, does a blind 30-second screen of the CV against the 5 essentials.
- **Pass:** they mark all 5 as evidenced, and at least 3 have a number attached.
- **Fail:** any essential is marked "not shown", or they raise the 2022 gap or the budget size as an unanswered question.

You can run this today. A friend in hiring with the advert and a stopwatch is enough.

---

**Deliverable you asked for:** one set of feedback on your CV for this job. No rewritten CV.

```
Give me feedback on my CV for the Senior Marketing Executive role at Hartwell Outdoor (advert and CV below). Feedback only; don't rewrite the CV.

Work as an experienced hiring manager for B2C/retail marketing roles would:

1. Build a requirements-to-evidence matrix: each of the 5 essentials and 2 desirables against the exact CV line that proves it, rated Evidenced / Implied / Missing. Flag anything that would get the CV rejected at first screen, especially criterion 2 (£20k+/month paid social) and criterion 3 (GA4).

2. For every Implied or Missing item, tell me what evidence I'd need to pull from my own primary sources (Meta/TikTok Ads Manager spend history, GA4, Klaviyo campaign reports, past briefs) and ask me for it. Don't invent numbers. Where I may not have the evidence (e.g. budget below £20k/month), say how to address the gap honestly.

3. Challenge my headline claims against the raw data. In particular, tell me whether the 31%→44% open rate is likely inflated by Apple Mail Privacy Protection, and which Klaviyo metrics (click rate, revenue per recipient) would make the claim hold up in interview.

4. Run a keyword check against the advert's terms (GA4, paid social, budget, briefs, Klaviyo, B2C, retail) and a 6-second scan of the top third of page 1: what a screener sees, and what they miss.

5. Flag every passive verb ("responsible for", "helped with", "supported"), the unexplained Mar 2022–Feb 2023 gap, the generic profile, and errors such as "Recieved".

Order the feedback by impact on getting shortlisted, most important first.

Then give me a test I can run with someone outside this conversation: a hiring manager or retail recruiter does a blind 30-second screen against the 5 essentials. Pass = all 5 marked evidenced, with at least 3 backed by a number. Fail = any essential marked "not shown", or the budget or the 2022 gap raised as an unanswered question.

[paste advert and CV]
```

Worth knowing, not in this task: a rewritten CV, a cover letter that addresses the budget-size gap directly, and a prepared interview answer on the open-rate claim.

Shall I run it?

## Extraction

last fenced block

## Call 2 prompt

Give me feedback on my CV for the Senior Marketing Executive role at Hartwell Outdoor (advert and CV below). Feedback only; don't rewrite the CV.

Work as an experienced hiring manager for B2C/retail marketing roles would:

1. Build a requirements-to-evidence matrix: each of the 5 essentials and 2 desirables against the exact CV line that proves it, rated Evidenced / Implied / Missing. Flag anything that would get the CV rejected at first screen, especially criterion 2 (£20k+/month paid social) and criterion 3 (GA4).

2. For every Implied or Missing item, tell me what evidence I'd need to pull from my own primary sources (Meta/TikTok Ads Manager spend history, GA4, Klaviyo campaign reports, past briefs) and ask me for it. Don't invent numbers. Where I may not have the evidence (e.g. budget below £20k/month), say how to address the gap honestly.

3. Challenge my headline claims against the raw data. In particular, tell me whether the 31%→44% open rate is likely inflated by Apple Mail Privacy Protection, and which Klaviyo metrics (click rate, revenue per recipient) would make the claim hold up in interview.

4. Run a keyword check against the advert's terms (GA4, paid social, budget, briefs, Klaviyo, B2C, retail) and a 6-second scan of the top third of page 1: what a screener sees, and what they miss.

5. Flag every passive verb ("responsible for", "helped with", "supported"), the unexplained Mar 2022–Feb 2023 gap, the generic profile, and errors such as "Recieved".

Order the feedback by impact on getting shortlisted, most important first.

Then give me a test I can run with someone outside this conversation: a hiring manager or retail recruiter does a blind 30-second screen against the 5 essentials. Pass = all 5 marked evidenced, with at least 3 backed by a number. Fail = any essential marked "not shown", or the budget or the 2022 gap raised as an unanswered question.

[paste advert and CV]

=== JOB ADVERT ===
Senior Marketing Executive, Hartwell Outdoor (Bristol, hybrid)
We sell outdoor clothing online and through 14 shops.
Essential:
1. 3+ years in B2C marketing
2. Planning and managing paid social budgets (Meta, TikTok) of £20k+ a month
3. Reporting on campaign performance with GA4
4. Writing briefs for designers and agencies
5. Running email campaigns in Klaviyo or a similar tool
Desirable: experience in retail or outdoor brands; a team of 1-2 to manage.

=== MY CV ===
Sam Okafor
Bristol | sam.okafor@example.com | 07700 900123

Profile
Creative and hard-working marketer with a passion for brands people love. Strong team player with excellent communication skills.

Experience
Marketing Coordinator, Fernbrook Coffee Roasters (online and 3 cafes), Feb 2023 to now
- Responsible for social media
- Ran paid social campaigns on Meta and TikTok
- Sent the weekly newsletter in Klaviyo to 38,000 subscribers; open rate rose from 31% to 44% after I rewrote the subject lines
- Wrote briefs for our freelance designer for packaging and seasonal campaigns
- Recieved the company's "Bean of the Year" award in 2024

Marketing Assistant, Lumen Lighting (B2C e-commerce), Sep 2019 to Mar 2022
- Helped with campaigns
- Pulled weekly reports from Google Analytics for the marketing manager
- Supported the launch of the spring 2021 range, which sold out in 6 weeks
- Managed the intern for summer 2021

Education
BA Marketing, University of the West of England, 2019

Skills
Meta Ads Manager, TikTok Ads, Klaviyo, Google Analytics, Canva, Excel

Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make.

## Answer

# CV feedback: Sam Okafor, Senior Marketing Executive at Hartwell Outdoor

**Assumptions:**
- Today is Nov 2026, so Fernbrook (Feb 2023 to now) is about 3 years 9 months, and Lumen (Sep 2019 to Mar 2022) is about 2 years 6 months.
- Fernbrook sells mainly to consumers, not wholesale.
- The screen is a quick human read, possibly after an ATS keyword filter.

I haven't invented any figures. Wherever a number is needed, I've asked you for it.

---

## 1. Requirements-to-evidence matrix

| # | Criterion | Exact CV line | Rating | Screen risk |
|---|---|---|---|---|
| E1 | 3+ yrs B2C marketing | Dates; "Lumen Lighting (B2C e-commerce)"; "Fernbrook… (online and 3 cafes)" | **Evidenced** (about 6 yrs, but the screener must do the maths) | Low |
| E2 | Plan and manage paid social budgets (Meta, TikTok) of £20k+/month | "Ran paid social campaigns on Meta and TikTok" | **Implied** for the platforms. **Missing** for budget, planning and results | **High, likely knockout** |
| E3 | Campaign performance reporting in GA4 | "Pulled weekly reports from Google Analytics for the marketing manager" (Lumen, ended Mar 2022); Skills: "Google Analytics" | **Missing** | **High, likely knockout** |
| E4 | Briefs for designers and agencies | "Wrote briefs for our freelance designer for packaging and seasonal campaigns" | **Evidenced** for designers. **Missing** for agencies | Low–medium |
| E5 | Email campaigns in Klaviyo | "Sent the weekly newsletter in Klaviyo to 38,000 subscribers; open rate rose from 31% to 44%…" | **Evidenced**, with a number | Low at screen, medium at interview (see item 6) |
| D1 | Retail or outdoor brand | Fernbrook cafes; Lumen e-commerce | **Implied** for retail (physical sites, but cafes are not shops). **Missing** for outdoor | Low |
| D2 | Manage a team of 1–2 | "Managed the intern for summer 2021" | **Implied, weak**: one temporary report, five years ago | Low |

Three things would get this CV rejected at first screen:
- **E2**: no spend figure at all.
- **E3**: no mention of GA4. The only analytics work shown predates the switch to GA4.
- **The 11-month gap**, which turns a borderline CV into a "no".

At present, only one of the five essentials has a number attached.

---

## 2. Feedback ranked by impact on shortlisting

### 1. Paid social budget (E2) is invisible. This is the single biggest risk.
"Ran paid social campaigns" shows the platforms but none of the things the advert actually tests: **£ per month, planning, management, results**. A screener seeing a coffee roaster with 3 cafes will likely assume the spend was small. If nothing on the page says otherwise, that assumption stands.

**Evidence to pull:**
- **Meta Ads Manager**: Billing/Payment activity, or Ads Manager with the date range set to the last 24 months, broken down by month, showing the *Amount spent* column. Note the average monthly spend, the peak month, and the trend.
- **TikTok Ads Manager**: the same, using the Reporting tab with spend broken down by month.
- **Results**: ROAS, CPA or cost per purchase, purchases, and revenue for your best and typical months.
- **Ownership**: did you *set and allocate* the budget (split across platforms and campaigns, pacing, reallocation), or did you execute a budget someone else set?
- **Lumen**: did you touch paid spend there at all?

**Questions for you:** What were your average and peak combined monthly spends? Who decided the budget?

**If you're below £20k/month**, don't blur it. Specifically:
- Don't quote an annual figure in a way that reads as monthly.
- Don't add spend you didn't control.

Instead:
- State the real figure plainly and pair it with evidence of *management skill*: growth you scaled, efficiency held while scaling, testing structure, cross-platform allocation.
- Use the cover letter to address the gap in one sentence. Say how you'd step up, and point to your process rather than the size of the budget.

Hiring managers often flex on a number when the candidate is honest and strong on method. They rarely forgive a number that collapses under questioning.

### 2. GA4 (E3) is missing, and the only analytics evidence predates it.
Universal Analytics stopped processing data in July 2023. Your Lumen role ended in March 2022, so "Google Analytics" there was almost certainly Universal Analytics. A screener who knows this will mark E3 "not shown".

A second problem: "pulled weekly reports… for the marketing manager" describes data retrieval for someone else. The advert asks for *reporting on campaign performance*, which means analysis and conclusions.

**Evidence to pull from Fernbrook's GA4:**
- What you built: explorations, custom reports, key events/conversions you set up, UTM conventions, any Looker Studio dashboards.
- Who received it, and how often.
- One decision your reporting changed, such as moving budget from channel X to Y or cutting a campaign.
- Any GA4 certification (Google Skillshop).

**Questions for you:** Does Fernbrook use GA4, or Shopify/Klaviyo reporting only? What's one report you produced and what happened because of it?

**If you haven't used GA4 hands-on**, say so honestly. You can close the gap quickly and credibly by:
- getting the Google Analytics certification;
- working in Google's public GA4 demo account;
- listing both accurately as training, not as job experience.

### 3. The top third of page 1 hides your strengths (6-second scan).
**What a screener sees, in order:**
1. Name, **Bristol** (a plus: local for a hybrid role).
2. A profile with no facts in it.
3. "Marketing Coordinator", which is a title two rungs below "Senior Marketing Executive".
4. "Coffee Roasters".
5. "Responsible for social media", your weakest bullet, placed first.
6. "Meta and TikTok".
7. Possibly the 38,000 and 44%.

**What they miss:**
- That you have about 6 years in B2C. There's no total anywhere, so they must add up the dates.
- Any spend figure.
- GA4.
- Any commercial result (revenue, ROAS, sales).
- That Lumen was B2C e-commerce, which is below the fold.
- Your one sell-out launch, buried under "Supported".

**Profile:** "Creative", "hard-working", "passion", "team player", "excellent communication" could describe any applicant, and none of it maps to the advert. The profile is your most valuable space. It should carry the facts a screener is scanning for: years, sector, channels, budget, tools, and one result.

**Keyword check against the advert:**

| Term | On CV? | Note |
|---|---|---|
| GA4 | **No** | Only "Google Analytics". An ATS or strict screener won't match it |
| Paid social | Yes | Once, with no substance |
| Budget | **No** | Absent everywhere |
| Briefs | Yes | Designer only. "Agencies" is absent |
| Klaviyo | Yes | Twice, which is good |
| B2C | Yes | Once, Lumen only |
| Retail | **No** | Cafes are not framed as physical retail. "In-store" and "omnichannel" are absent |
| Also absent | n/a | "outdoor", "agency", "ROAS"/"CPA", "line manage" |

### 4. The unexplained Mar 2022 to Feb 2023 gap.
Eleven months with nothing written invites the screener to fill it with the worst explanation. One honest line is enough, whether it was job search, travel, caring, health, study, or freelance work. You don't owe detail.

If you did anything relevant in that period, it may also be evidence: freelance clients, courses, a GA4 certification.

**Question for you:** What were you doing in that period, and is any of it marketing-relevant?

### 5. Passive, duty-based bullets with no outcomes.
These read as junior and give a screener nothing to tick:
- **"Responsible for social media"**: a duty, not an achievement. And it's your first bullet.
- **"Helped with campaigns"**: no campaign, no role, no result. This is the weakest line on the CV.
- **"Supported the launch of the spring 2021 range, which sold out in 6 weeks"**: a good result undercut by "Supported". What did *you* do? Also, how many units? A small stock run selling out is less impressive than it sounds, and an interviewer will ask.
- **"Pulled weekly reports… for the marketing manager"**: subordinate framing (see item 2).
- **"Sent the weekly newsletter"**: undersells it. Did you plan, write, segment, and test?
- **"Ran paid social campaigns"**: an active verb, but empty (see item 1).

**Evidence to pull:**
- Lumen launch: your specific tasks (email, social, copy, briefs?), units or revenue, and the channels you ran.
- Fernbrook social: follower growth, engagement, or any traffic or sales you can attribute, from native analytics or GA4.
- Lumen campaigns: name two you contributed to materially.

### 6. The open-rate claim (31% to 44%) won't survive a sharp interviewer as stated.
It's your only number, so it carries the CV at screen. But a retail email specialist will probe it.

**Apple Mail Privacy Protection (MPP):** Since iOS 15 (Sept 2021), Apple Mail preloads tracking pixels, so emails register as "opened" whether or not a human read them. Apple Mail often accounts for a large share of consumer opens. That has two consequences:
- **Your whole Fernbrook tenure is post-MPP**, so both 31% and 44% are inflated. The *rise* isn't automatically an MPP artefact. However, 44% on its own is unremarkable by post-MPP e-commerce standards.
- **The rise could have other causes**, all of which an interviewer will raise:
  - a shift in your list towards Apple Mail users;
  - list cleaning or sunset flows that suppressed unengaged subscribers (a smaller denominator raises the rate);
  - send-time changes;
  - seasonality, such as comparing January with the pre-Christmas period;
  - a change in how your Klaviyo reporting treats Apple privacy opens.
- **Subject-line A/B tests judged on opens are MPP-contaminated**, because machine opens ignore subject lines and dilute the signal.

**Klaviyo metrics that would make the claim hold up:**
- **Click rate** (unique clicks ÷ recipients): the cleanest proof that subject lines changed human behaviour.
- **Placed order rate.**
- **Revenue per recipient (RPR).** This is the metric a retail hiring manager cares about most.
- **Total attributed revenue.** Note whether it's click-based or open-based; open-based attribution is also MPP-inflated.
- **Unsubscribe and spam rates** staying flat, to show you didn't buy opens with clickbait.
- **Context**: the date ranges compared, number of sends averaged, list size at start and end, whether any list cleaning happened in the same window, and whether Klaviyo was showing or excluding Apple privacy opens (check your account's reporting settings).

**Questions for you:**
- Export campaign performance for the 3–6 months before your subject-line changes and the 3–6 months after.
- What did click rate and RPR do over the same windows?
- Did the list grow from below 38,000 on your watch? If so, that's a separate, stronger claim.

If clicks and RPR rose too, lead with those and keep opens as supporting detail. If they didn't, drop "after I rewrote the subject lines" as a causal claim.

### 7. Briefs (E4): agencies are missing, and there's no outcome.
**Questions for you:**
- Have you briefed any agency (creative, media, PR, influencer, photography, print)?
- Roughly how many briefs per year?
- Did the packaging or seasonal work you briefed have a measurable result (sales, sell-through, launch performance)?

Managing the freelance designer also counts as supplier management, which is useful for item 8.

### 8. Desirables are under-claimed.
- **Retail:** Fernbrook runs three physical sites plus online, close to Hartwell's 14 shops plus online. Did you run in-store promotions, POS, launches, or anything connecting online to the cafes? That's omnichannel evidence, and it's currently invisible.
- **Team:** "the intern for summer 2021" is thin and dated. How long was the internship? What did they deliver under you? Do you currently manage anyone, including freelancers and agencies? Day-to-day direction of the designer is relevant if described accurately as freelancer management, not line management.
- **Outdoor:** you have no evidence here, and you shouldn't fake it. Any genuine personal link (you hike, you're a customer) belongs in the cover letter, not the CV.

### 9. Seniority signal.
Your title is "Marketing Coordinator" and the role is "Senior Marketing Executive". Your title won't change, but the bullets can show senior-level scope: owning budgets, owning channels, making decisions from data. That only works once items 1, 2, and 5 are fixed.

### 10. Errors and loose ends.
- **"Recieved"** should be **"Received"**. For a role that writes briefs and copy, a typo can be an instant reject for some screeners. It costs ten seconds to fix.
- **"Bean of the Year"** means nothing to an outsider. What was it awarded for, and out of how many staff? If it was for a result, the result is the bullet. If it was a culture award, it's low priority.
- **Skills**: "Google Analytics" is ambiguous. List GA4 only if item 2 confirms you've used it. Also, are there tools you use but haven't listed (Shopify, Looker Studio, Meta Business Suite)?
- There's no total-experience figure anywhere. Screeners shouldn't have to do date arithmetic.

---

## 3. Consolidated evidence request (reply with these)

1. Meta and TikTok monthly spend: average and peak over the last 24 months. Whether you set the budget. ROAS or CPA for typical and best months.
2. GA4: do you use it at Fernbrook? One report you built, who received it, and one decision it drove. Any certification.
3. Klaviyo: click rate, placed order rate, and RPR for comparable windows before and after the subject-line changes. List size at start and end. Any list cleaning in that window.
4. The Mar 2022 to Feb 2023 gap: what it was.
5. Lumen spring 2021 launch: your role, units or revenue.
6. Agency briefs: any? Plus the volume of designer briefs and their outcomes.
7. Fernbrook social results and any in-store/omnichannel work.
8. The intern's duration and output. Current freelancer or agency management.
9. What "Bean of the Year" was awarded for.

---

## 4. Blind 30-second screen test

**Who:** a hiring manager or recruiter in B2C or retail marketing who hasn't seen this conversation or your CV. Two or three testers is better than one.

**Setup:**
1. Give them the advert first and let them read it as long as they like.
2. Hand over the CV and time **30 seconds**, then take the CV away.
3. Don't tell them which criteria you're worried about. Don't explain or defend anything during or after.

**Scoring sheet** (they fill it in from memory, without the CV):

| Essential | Evidenced / Implied / Not shown | Backed by a number? (Y/N) |
|---|---|---|
| 1. 3+ yrs B2C | | |
| 2. Paid social £20k+/month (Meta, TikTok) | | |
| 3. GA4 reporting | | |
| 4. Briefs for designers/agencies | | |
| 5. Klaviyo email | | |

Then ask them:
- "What questions would you need answered before shortlisting?"
- "Shortlist: Y/N?"
- "What's the one thing you remember?"

**Pass:** all 5 marked Evidenced, with at least 3 backed by a number.

**Fail:** any of the following:
- any essential marked "Not shown";
- budget raised as an unanswered question;
- the 2022 gap raised as an unanswered question.

"Implied" on any essential also counts as not passing, because the pass bar is all five Evidenced.

**Prediction for the current version:** fail.
- E3 will likely be "Not shown" and E2 "Implied".
- Budget and the gap will probably both come up as questions.
- Only E5 carries a number.

Run the test on the current CV as a baseline, then again on your revised version with a *different* tester, so memory of the first version doesn't skew the result.
