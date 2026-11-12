# cv-deeper-1

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
The field is recruitment screening for in-house marketing roles: a marketing hiring manager working with an experienced CV writer. Two moves separate their work from general advice:
- **They screen the CV the way Hartwell will.** That means one row per Essential and Desirable criterion, marked *evidenced*, *implied* or *missing*. Taste comes second.
- **They ask you for the missing facts instead of polishing the wording.** Your CV never states a monthly budget, never says GA4 (your "Google Analytics" from 2019–2022 was probably Universal Analytics), and shows only an intern for team management. It also leaves an 11-month gap (Mar 2022 to Feb 2023) unexplained.

An email specialist would add one more point. Since Apple's Mail Privacy Protection (2021), open rates are inflated, so "31% to 44%" may not convince a Klaviyo-literate reader. Click rate or attributed revenue would.

**2. What is the rawest material?**
Not your CV bullets, but the records underneath them:
- Meta and TikTok Ads Manager spend history
- GA4 properties or reports you built
- Klaviyo campaign stats (clicks and revenue, not just opens)
- The briefs you wrote
- Lumen's sales figures for the spring 2021 range
- Hartwell's full job description and person spec, if there is one

I can't see your workspace files from here, so please point me to any of these or paste the figures.
**One assumption this could disprove:** we're assuming you fail Essential #2 (£20k+/month). Your Ads Manager spend history might show you already meet it, or show the gap is bigger than it looks.

**3. Which methods and tools?**
- A requirements-to-evidence screening matrix, built the way a recruiter scores applicants.
- An ATS parse to check the CV is read correctly by an applicant tracking system. Jobscan is one option, or any résumé parser.
- Ads Manager spend exports, Klaviyo campaign reports and GA4 Explorations as the source of the numbers.
- A spellcheck. "Recieved" is misspelled.

None of these are in this conversation yet. I can't list your installed skills or subagents without running commands, which I haven't done. If you'd like, I can run `npx skills find recruitment` (and `npx skills find resume`). That downloads the skills CLI from npm, so I'll only run it if you say yes.

**4. What, other than us, would show the result is right?**
- **A blind 30-second screen by a real marketing hiring manager or recruiter** who scores the CV against the five Essentials.
  - **Pass:** all five marked *evidenced*, with numbers and dates.
  - **Fail:** any Essential marked *missing* or *unclear*, or the gap questioned without an answer.
- **An ATS parse.** It must pull out Meta, TikTok, GA4, Klaviyo and "briefs" under the right roles and dates.
- **A spellcheck** that finds zero errors.

**What your task asks you to end up with:** feedback on your CV for this job. One set of feedback, nothing else.

```
Give me feedback on my CV (pasted below) for the Senior Marketing Executive role at Hartwell Outdoor (advert pasted below). Work as a marketing hiring manager and an experienced CV writer would.

Method:
1. Build a screening matrix: one row per Essential (1-5) and Desirable criterion. Mark each as evidenced / implied / missing and quote the CV line it rests on. Flag specifically: no monthly paid-social budget stated (Essential 2 needs £20k+/month); "Google Analytics" rather than GA4 (Essential 3); management limited to one summer intern (Desirable); the unexplained Mar 2022 to Feb 2023 gap; vague bullets ("Responsible for social media", "Helped with campaigns"); the generic Profile; the "Recieved" typo.
2. Before suggesting wording, ask me for the raw figures behind each weak row: Meta/TikTok monthly spend and results from Ads Manager, any GA4 reporting I did, Klaviyo click rate and attributed revenue (open rates are inflated since Apple Mail Privacy Protection, so don't lean on 31%→44% alone), the scope of the briefs I wrote, Lumen spring 2021 sales numbers, and what I did during the gap. Don't invent or inflate numbers. If something is genuinely missing, say so and say how to address it honestly.
3. Run the CV through an ATS parser (e.g. Jobscan or another résumé parser) and report whether Meta, TikTok, GA4, Klaviyo and briefs are extracted against the right roles and dates.
4. Spellcheck the whole CV.

Give the feedback as: the matrix, then the fixes in priority order (biggest risk to being shortlisted first), with a suggested rewrite of each weak line based only on facts I've confirmed.

Check: the feedback passes only if, once applied, a marketing hiring manager or recruiter doing a blind 30-second screen would mark all five Essentials as evidenced with numbers and dates. It also needs the ATS parse to extract all five keywords correctly and zero spelling errors. Treat any Essential still marked missing or unclear, or an unexplained gap, as a fail, and say so plainly. Use any installed recruitment or résumé skills if present.
```

Worth knowing, not in this task: a fully rewritten CV, a cover letter that addresses the budget gap and the career gap directly, and interview prep for the likely "biggest budget you've managed" question.

Shall I run it? And do you want me to run the `npx skills find` search first?

## Extraction

last fenced block

## Call 2 prompt

Give me feedback on my CV (pasted below) for the Senior Marketing Executive role at Hartwell Outdoor (advert pasted below). Work as a marketing hiring manager and an experienced CV writer would.

Method:
1. Build a screening matrix: one row per Essential (1-5) and Desirable criterion. Mark each as evidenced / implied / missing and quote the CV line it rests on. Flag specifically: no monthly paid-social budget stated (Essential 2 needs £20k+/month); "Google Analytics" rather than GA4 (Essential 3); management limited to one summer intern (Desirable); the unexplained Mar 2022 to Feb 2023 gap; vague bullets ("Responsible for social media", "Helped with campaigns"); the generic Profile; the "Recieved" typo.
2. Before suggesting wording, ask me for the raw figures behind each weak row: Meta/TikTok monthly spend and results from Ads Manager, any GA4 reporting I did, Klaviyo click rate and attributed revenue (open rates are inflated since Apple Mail Privacy Protection, so don't lean on 31%→44% alone), the scope of the briefs I wrote, Lumen spring 2021 sales numbers, and what I did during the gap. Don't invent or inflate numbers. If something is genuinely missing, say so and say how to address it honestly.
3. Run the CV through an ATS parser (e.g. Jobscan or another résumé parser) and report whether Meta, TikTok, GA4, Klaviyo and briefs are extracted against the right roles and dates.
4. Spellcheck the whole CV.

Give the feedback as: the matrix, then the fixes in priority order (biggest risk to being shortlisted first), with a suggested rewrite of each weak line based only on facts I've confirmed.

Check: the feedback passes only if, once applied, a marketing hiring manager or recruiter doing a blind 30-second screen would mark all five Essentials as evidenced with numbers and dates. It also needs the ATS parse to extract all five keywords correctly and zero spelling errors. Treat any Essential still marked missing or unclear, or an unexplained gap, as a fail, and say so plainly. Use any installed recruitment or résumé skills if present.

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

# CV Feedback: Sam Okafor for Senior Marketing Executive, Hartwell Outdoor

**Verdict: fail as it stands.** In a 30-second screen, a recruiter would mark Essential 2 and Essential 3 as not met and would notice the unexplained gap. The fixes below can turn this into a pass, but only if your real figures support them. I haven't invented any numbers. Where a figure is needed, I've left a **[bracketed placeholder]** for you to fill from your own records.

### Assumptions and limits
- **No questions answered yet.** You asked me to proceed without them, so every rewrite uses only facts already in your CV. The questions I'd normally ask are listed at the end. Your answers fill the placeholders.
- **No ATS parser was run.** I can't upload to Jobscan or similar services from here, and doing so would send your name, email and phone number to a third party. Section 3 is a manual prediction of how standard parsers handle this layout. Before you apply, run the final version through Jobscan's free scan yourself.
- **No recruitment or résumé skills** were available in this environment, so this is a manual review.
- **Dates:** I've taken today as Nov 2026. That makes the Fernbrook role about 3 years 9 months, the Lumen role 2 years 6 months, and the gap Apr 2022 to Jan 2023 (about 10 months).

---

## 1. Screening matrix

| # | Criterion | Status | CV line it rests on | Screener's problem |
|---|---|---|---|---|
| E1 | 3+ years B2C marketing | **Evidenced** | "Lumen Lighting (B2C e-commerce), Sep 2019 to Mar 2022"; "Fernbrook… Feb 2023 to now" | About 6 years total, so the threshold is met. Fernbrook isn't labelled B2C, and "now" is informal. Minor issues only. |
| E2 | Paid social (Meta, TikTok), budgets £20k+/month | **Implied, threshold missing** | "Ran paid social campaigns on Meta and TikTok" | **No budget, no results, no "planned/managed".** This is the headline threshold in the advert. A screener can't assume £20k+, especially at a 3-café business. **Biggest risk.** |
| E3 | Reporting on campaign performance with GA4 | **Implied, weak** | "Pulled weekly reports from Google Analytics for the marketing manager"; Skills: "Google Analytics" | Says "Google Analytics", not GA4. It describes *pulling* reports for someone else, not *reporting on performance*. It's also dated 2019–22, when Lumen was almost certainly on Universal Analytics (UA stopped processing data in July 2023). Nothing about analytics at Fernbrook. |
| E4 | Writing briefs for designers and agencies | **Evidenced, partial** | "Wrote briefs for our freelance designer for packaging and seasonal campaigns" | Designers are covered. **Agencies are missing.** No volume or outcome is given. |
| E5 | Email campaigns in Klaviyo or similar | **Evidenced** | "Sent the weekly newsletter in Klaviyo to 38,000 subscribers; open rate rose from 31% to 44%…" | Tool, scale and frequency are clear. But open rate is the only metric, and it's inflated by Apple Mail Privacy Protection. An experienced manager will discount it. "Sent" also undersells planning and segmentation work. |
| D1 | Retail or outdoor brand experience | **Implied** | "online and 3 cafes"; "B2C e-commerce" | Online plus physical sites is a fair parallel to Hartwell's web plus 14 shops, but the CV never says so. No outdoor link. |
| D2 | Managing a team of 1–2 | **Implied, weak** | "Managed the intern for summer 2021" | One temporary report, five years ago. Nothing current. |
| – | Employment gap Mar 2022 to Feb 2023 | **Missing (unexplained)** | – | Screeners notice gaps of 6+ months. Without a line, they'll guess, and their guesses won't help you. |
| – | Profile | **Weak** | "Creative and hard-working marketer… Strong team player…" | No years, channels, tools, numbers or target role. It uses the prime 30-second space on claims that every CV makes. |
| – | Vague bullets | **Weak** | "Responsible for social media"; "Helped with campaigns" | Duties rather than outcomes, with no scope, channel or result. "Helped" reads as junior for a Senior role. |
| – | Spelling | **1 error** | "Recieved" | Should be "Received". |

---

## 2. Fixes in priority order

### Fix 1: State the paid social budget and results (Essential 2)
**Current:** "Ran paid social campaigns on Meta and TikTok"

**Rewrite, once you've confirmed the figures in Ads Manager:**
> Planned and managed paid social budget of **£[X]k/month** across Meta and TikTok; delivered **[ROAS / CPA / purchases / revenue]** over **[period]**.

**If your monthly spend is below £20k**, say so honestly. Don't round up. Show the scale you did manage and the efficiency you achieved:
> Managed **£[X]k/month** Meta and TikTok budget, owning plan, creative testing and weekly optimisation; improved **[CPA/ROAS] by [Y]%** over **[period]**.

Then mention the step up in your cover letter. Be aware that a strict screen may still mark E2 as *partially met*. That honest risk is better than a claim that falls apart at interview, where they'll ask about your spend and bid strategy.

### Fix 2: Evidence GA4 specifically (Essential 3)
**Rewrite, only if you've used GA4 at Fernbrook:**
> Built **[weekly/monthly]** campaign performance reports in **GA4** covering **[paid social, email, organic]**, used to **[reallocate budget / decide X]**.

**Lumen rewrite (accurate to the era):**
> Produced weekly Google Analytics (Universal Analytics) reports on campaign traffic and conversions for the marketing manager.

**If you've never used GA4,** E3 is genuinely missing. Don't relabel UA work as GA4. The honest fix is to complete Google's free GA4 training and Analytics certification, use GA4 on Fernbrook's site (or the demo account), and then list "GA4 (certified, [month year])". Until then, this row remains a fail.

**Skills line:** replace "Google Analytics" with "GA4" only if that's true. Otherwise use "Google Analytics (UA)", and add GA4 once certified.

### Fix 3: Explain the gap
Add one line between the two roles. Choose whichever is true:
> Apr 2022 – Jan 2023: Career break: **[travel / caring responsibilities / health / relocation / study / freelance]**.

If you did any freelance work, courses or certifications in that period, list them with dates, because they turn the gap into evidence. One honest line is enough. You don't owe more detail than that.

### Fix 4: Replace the Profile
The rewrite below uses only facts already in your CV. Brackets mark items to add once confirmed:
> B2C marketer with 6+ years across e-commerce and multi-site consumer brands. Plan and run paid social on Meta and TikTok (**£[X]k/month**), run Klaviyo email to a 38,000-subscriber list, and write creative briefs for designers. **[Report campaign performance in GA4.]** Looking to bring this to an omnichannel outdoor retailer.

### Fix 5: Rewrite the vague bullets
**"Responsible for social media"** becomes:
> Own organic social across **[Instagram / TikTok / …]**: **[posts per week]**, content calendar; grew followers / engagement **[from X to Y]** over **[period]**.

If you can't quantify this, merge it into the paid social bullet rather than keeping a duty line.

**"Helped with campaigns"** becomes:
> Coordinated **[number]** campaigns a year across **[email / paid / site]**, owning **[specific part, e.g. assets, scheduling, reporting]**.

Name the part you owned. "Helped" invites the question of who actually did the work.

### Fix 6: Strengthen the Klaviyo evidence (E5)
**Current wording is acceptable but over-relies on open rate.** Rewrite:
> Plan and send weekly Klaviyo campaigns to 38,000 subscribers. Click rate **[X% → Y%]**, Klaviyo-attributed revenue **£[Z]/[period]**. Rewrote subject lines, lifting open rate from 31% to 44% (MPP-affected).

If you've built flows (welcome, abandoned basket, post-purchase) or segmentation, add a bullet. That's Senior-level evidence.

### Fix 7: Add scope to briefs, and agencies if true (E4)
> Wrote **[number]** creative briefs for freelance designer **[and agencies: name type, e.g. photography / PR / media]** covering packaging and seasonal campaigns, including **[a measurable result, e.g. "spring range sold £X"]**.

If you've never briefed an agency, leave agencies out. Designers alone still meets most of the criterion.

### Fix 8: Make the Lumen launch yours
**Current:** "Supported the launch of the spring 2021 range, which sold out in 6 weeks"
> Supported the spring 2021 range launch (**[your part, e.g. email and social assets]**). The range of **[units / £ revenue]** sold out in 6 weeks.

### Fix 9: Management (Desirable)
Keep the intern line, but make it specific:
> Managed and set daily priorities for a summer intern (Jun–Aug 2021).

Add any current line management, freelancer management or mentoring at Fernbrook if it's true. Managing your freelance designer's workload and deadlines counts if you do it. Otherwise leave it as is. It's a Desirable criterion, not a gate.

### Fix 10: Polish
- "Recieved" → **"Received"**.
- "Feb 2023 to now" → **"Feb 2023 – Present"**.
- Add context to the award: *Received Fernbrook's "Bean of the Year" employee award (2024) for **[reason]***. Without a reason it reads as an in-joke.
- Label Fernbrook **"B2C coffee brand: online and 3 cafés"**. This makes E1 unambiguous and links to D1.

---

## 3. ATS parse (predicted, not run)

| Keyword | Where it appears now | Expected extraction | Issue |
|---|---|---|---|
| Meta | Fernbrook bullet; Skills | Likely correct (Fernbrook, Feb 2023–) | "Meta Ads Manager" parses fine |
| TikTok | Fernbrook bullet; Skills ("TikTok Ads") | Likely correct | – |
| GA4 | **Nowhere** | **Not extracted** | Jobscan-style keyword match will flag it missing. Fails until added truthfully. |
| Klaviyo | Fernbrook bullet; Skills | Likely correct | – |
| briefs | Fernbrook bullet | Likely correct | "Writing briefs" vs "Wrote briefs": most matchers stem these; add "creative briefs" to be safe |

**Other missing advert keywords:** budget, B2C (Fernbrook), campaign performance, agencies, retail, outdoor. Add only where true.

**Layout risks:**
- "Marketing Coordinator, Fernbrook Coffee Roasters (online and 3 cafes), Feb 2023 to now" on one line may merge the bracketed text into the company name. "to now" may not parse as a current role.
- Use this layout instead:
  - **Line 1:** Marketing Coordinator
  - **Line 2:** Fernbrook Coffee Roasters | Bristol
  - **Line 3:** Feb 2023 – Present
  - Put the description in the first bullet.
- Keep standard headings (Profile, Experience, Education, Skills), with no tables, columns or text boxes.

---

## 4. Spellcheck
- **Error:** "Recieved" → "Received". This is the only spelling error.
- **Style:** "cafes" → "cafés" (optional in UK usage, but be consistent); "now" → "Present".
- Everything else is correct, including "e-commerce", "Klaviyo", "TikTok" and "University of the West of England".

---

## Check result

| Requirement | Status now | After fixes |
|---|---|---|
| E1 evidenced with dates | Pass | Pass |
| E2 evidenced (£20k+/month) | **Fail** | Pass **only if** your real spend is £20k+; otherwise partially met |
| E3 GA4 evidenced | **Fail** | Pass **only if** you've genuinely used GA4; otherwise fail until certified/used |
| E4 evidenced | Pass (partial) | Pass |
| E5 evidenced with numbers | Pass (weak metric) | Pass |
| Gap explained | **Fail** | Pass once the line is added |
| ATS extracts all 5 keywords | **Fail** (GA4) | Pass if GA4 is added truthfully; confirm in Jobscan |
| Zero spelling errors | **Fail** (1) | Pass |

**Overall: FAIL now.** The CV can pass after the fixes, but the result depends on two facts only you can confirm: a monthly paid social spend of £20k or more, and real GA4 use.

---

## Questions to answer so I can finalise the wording
1. **Paid social:** Meta and TikTok spend per month, which months, and the results from Ads Manager (ROAS, CPA, purchases, revenue). Did you set the budget split, or did someone else?
2. **GA4:** Have you used it at Fernbrook? What did you report on, how often, and to whom? What decisions came out of it?
3. **Klaviyo:** Click rate before and after, attributed revenue, and any flows or segments you built.
4. **Briefs:** How many per year, which deliverables, and any agencies involved? Any results tied to them?
5. **Lumen spring 2021:** Units or revenue, and exactly what your role was.
6. **Gap (Apr 2022 – Jan 2023):** What you did, in one line.
7. **Organic social:** Platforms, posting frequency, and any growth or engagement numbers.
8. **Award:** What it was given for.
9. **Management:** Any current responsibility for people, including freelancers.
