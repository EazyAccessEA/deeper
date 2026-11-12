# Journal test: four ways to ask, run to finished answers

Pre-registered 11 November 2026, before any run. Everything in this file and in `fixtures/` is frozen by the SHA-256 hashes in `FROZEN.txt`, recorded before the first model call. After that, only the "Results" section may change. Failed calls (timeouts, empty output) are retried and logged in `runs/log.txt`. No call is re-run because of its content.

## Why this test exists

The earlier tests (`../v1.1/`, `../v1.1.1/`) had four weaknesses:

1. They scored rewritten prompts, not finished work.
2. The rubric mirrored deeper's own questions.
3. All of the writers and the judge were Claude models.
4. The final 1.1 wording was tuned on the same five tasks it was tested on.

The same prompt text also scored differently in two judging passes: 4.0 then 3.0 on scope, and 1.8 then 4.2 extras per task. This test is built to answer those points.

## Tasks

There are four everyday tasks. None was used when deeper was written or tuned. Each comes with the material a person would have to hand. All of that material is made up for the test, and names, numbers and companies are fictional.

| ID | Task | Fixture |
|---|---|---|
| cv | Give me feedback on my CV for this job. | `fixtures/cv.md` |
| rent | Should I rent or buy this flat? | `fixtures/rent.md` |
| complaint | Reply to this angry customer's email. | `fixtures/complaint.md` |
| downloads | Tidy my Downloads folder. | `fixtures/downloads.md` |

## Arms

The writer for every arm is Claude Opus 5.5. It runs through `claude -p` with Claude Code's global instructions, settings, hooks, plugins, MCP servers and tools turned off. The system prompt is the one line "You are a helpful assistant.", the nearest thing to a plain chat app.

Every arm's final call ends with the same line:

> Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make.

| Arm | Calls | Prompt |
|---|---|---|
| plain | 1 | the fixture (task line plus material) |
| persona | 1 | `Act as an expert <field>.` then the fixture. Fields are fixed here: cv "recruiter and CV writer"; rent "financial planner"; complaint "customer service manager"; downloads "IT support specialist" |
| felix | 2 | Call 1 is Felix Rieseberg's prompt, word for word from his article (below), then `My task:` and the fixture. Call 2 is the rewritten prompt it produced, then the fixture and the final line |
| deeper | 2 | Call 1 is `skills/deeper/SKILL.md` (1.1.1) installed as in `marketing/tiktok/deeper_runs.py`, with the user typing `/deeper` and the fixture. Call 2 works as for felix |

Felix's prompt, from <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/> (13 October 2026):

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

**Taking the rewritten prompt from call 1:** use the last fenced code block. If there is none, use everything after the last line that contains "prompt" and ends with a colon. If there is none of that either, use the whole reply. The rule used is logged for each run.

**Runs:** two independent runs of each arm on each task. That makes 4 tasks × 4 arms × 2 runs = 32 finished answers.

## Judging

There are two judges from different model families, each scoring every answer:

- **Claude Sonnet 5.5**, run with the same clean settings as the writer.
- **GPT**, through `codex exec` in a read-only, empty folder.

**How each judge sees the answers:**
- For each task, a judge sees the fixture, the checklist and all 8 answers.
- The answers are labelled A to H in a random order.
- Each judge gets its own order, from a seed recorded in `key.json`.
- The key stays in a separate file that judges never see.

**What each judge does:** marks every checklist item 1 (done) or 0 (not done), each with a reason of one sentence. Only what the answer actually does counts. Naming a method, tool or expert gets no credit. An answer that only asks questions, or only describes what it would do, scores 0 on any item it didn't carry out.

**Leak check:** before judging, each answer is searched for "deeper", "Felix", "Worth knowing", "top professional", "rawest material" and "Act as". Any hit is listed. Hits are not removed.

## Checklists (6 items per task, written before any run)

### cv
1. Checks the CV against at least 4 of the 5 essential requirements, by name, saying which ones the CV shows evidence for.
2. Says that the paid social budget requirement (£20k+ a month) is not evidenced. The CV gives no budget size.
3. Notices the unexplained gap between March 2022 and February 2023.
4. Rewrites at least two specific bullet points or the profile, using only facts that are in the CV. Invented numbers are marked as placeholders for the user to fill in.
5. Spots the misspelling "Recieved".
6. Puts the feedback in order of what matters most for this application, or clearly marks the top priorities.

### rent
Reference figures were computed before the runs by `reference_rent.py`. The monthly repayment is £1,336.43. With 2% growth a year, buying comes out ahead from year 3 and is about £12,000 better at 5 years. With 0% growth, break-even moves to year 13, so renting wins at 5 and 7 years.

1. Works out the monthly mortgage payment within 2% of £1,336.43, or states a figure within that range.
2. Compares the money position of buying against renting over the stated stay (5 or 7 years), with numbers for both.
3. Counts what the deposit and buying costs would have earned if invested, i.e. the opportunity cost.
4. Includes the service charge and ground rent, upkeep, and selling costs in the buying side.
5. Shows that the answer depends on house prices, with a number. For example, renting wins over 5 years if prices stay flat, or it gives a break-even.
6. Gives a clear recommendation tied to the stated assumptions, not "it depends" alone.

### complaint
1. Acknowledges all three failures specifically: the late delivery, the cracked leg, and the two missed callbacks.
2. Takes responsibility for the missed callbacks as the company's own failure, without blaming the carrier for them.
3. Offers a replacement or a full refund including delivery (£198.95), says the customer can choose, and says collection is free.
4. Keeps any extra gesture within £25, or says that more needs a manager. It doesn't promise compensation outside policy.
5. Gives a concrete next step with a time or date and a name (Priya), per the policy "Never promise a callback without a time and a name".
6. Does not ask for photos or other information the record shows was already given.

### downloads
1. Identifies at least 3 of the 4 likely duplicate "(1)" copies with the same size: Docker, Invoice-0412, holiday-photos zip, CV-2026.
2. Does not treat `budget.xlsx` and `budget (1).xlsx` as duplicates, since their sizes differ. It keeps both, or says to check before removing either.
3. Says the installer files (`.dmg`, `.pkg`) can go once the apps are installed.
4. Treats `P60-2025-26.pdf`, `passport-scan.jpg` and `tenancy-agreement.pdf` as documents to keep somewhere safe, not to delete. At least two of the three must be named.
5. Uses a reversible step before anything is gone for good: the Bin, a holding folder, or a dry run.
6. Notices that `tenancy-agreement.pdf.download` is an unfinished download, or that `holiday-photos.zip` duplicates the extracted folder.

## Readings, fixed now

- **Arm score:** the mean number of items done (0 to 6), averaged over 4 tasks × 2 runs × 2 judges.
- **Under 1.0:** two arms whose scores differ by less than 1.0 item are reported as no difference.
- **Felix against deeper:** if Felix's prompt scores 1.0 or more above deeper, article 1 says in its title that Felix's prompt did better. If they're within 1.0, it says they tied.
- **Judge agreement:** reported as percentage agreement and Cohen's kappa over all item scores. If kappa is below 0.4, the judges disagree too much to support any ranking, and the article says so.
- **Each task is reported separately as well.** A ranking that holds on only one task is described as holding on only one task.

## Limits known in advance

- Four tasks with two runs each is a small sample.
- The checklists were written by deeper's author, who knows what deeper asks for. They score actions, not vocabulary, to limit that bias, but it isn't removed.
- The writer is a Claude model, and one judge is a Claude model. The GPT judge is there to check that.
- The fixtures are made up, so real tasks would be messier.

## Files

- `fixtures/`: the four tasks.
- `reference_rent.py`: the reference figures.
- `run.py`: writer and judge calls.
- `FROZEN.txt`: the hashes.
- `runs/`: raw replies.
- `judgements/`: judge output.
- `key.json`: the answer key.
- `score.py`: scoring.

## Results

Run on 12 November 2026. There were 32 answers and 8 judging calls, with no failed calls. Before this section was written, the frozen files were checked against `FROZEN.txt` and all of them matched. `python3 score.py` prints everything below.

**Mean items done out of 6, across 4 tasks × 2 runs × 2 judges:**

| Arm | Both judges | Claude | GPT |
|---|---|---|---|
| plain | 5.81 | 5.88 | 5.75 |
| persona | 6.00 | 6.00 | 6.00 |
| felix | 5.69 | 5.62 | 5.75 |
| deeper | 5.56 | 5.50 | 5.62 |

**By the readings fixed in advance, no arm differs from any other.** The largest gap is persona against deeper, at 0.44 items, and the threshold was 1.0. Felix against deeper is +0.12, which counts as a tie.

**Judge agreement:** 97.4% of 192 item scores, Cohen's kappa 0.65. That's above the 0.4 floor.

**By task:**

| Task | plain | persona | felix | deeper |
|---|---|---|---|---|
| cv | 5.75 | 6.00 | 5.75 | 5.50 |
| rent | 6.00 | 6.00 | 6.00 | 6.00 |
| complaint | 5.50 | 6.00 | 5.00 | 4.75 |
| downloads | 6.00 | 6.00 | 6.00 | 6.00 |

### What it means

- **There's a ceiling effect.** Given the task and the material, the writer did nearly every checklist action whichever way it was asked. Of the 24 items, 20 were done by every answer, by both judges. The checklists were too easy for this model to show a benefit from any prompt, so the test can show "no difference here" but not "no difference anywhere".
- **Where answers missed, the two-step arms (felix, deeper) missed more often.** Every miss is in `judgements/`. The judges named three causes:
  - **Holding to scope against the checklist.** `cv-deeper-2` gave the feedback but no rewritten bullets. The judges called this asking for evidence instead of rewriting. A later read found the cause: deeper's own call-1 prompt said "Feedback only; don't rewrite the CV." So the miss on cv item 4 came from the scope rule, and the checklist item arguably asked for more than the task. Noted 12 November, after scoring.
  - **Placeholders instead of commitments.** `complaint-deeper-1` and `complaint-felix-2` left bracketed slots for the date and time.
  - **Dropping a policy option.** `complaint-deeper-2` and `complaint-felix-2` left out the replacement and offered a refund only.

  These come from 2 tasks and a handful of answers, below the 1.0 threshold, so they're a pattern to watch, not a finding.

### Deviations and notes

- **Extraction for the felix arm.** For 7 of 8 felix runs, the first-call reply put the rewritten prompt in a quote block under a heading such as "Your rewritten prompt". The pre-registered rule needed a fenced block or a line ending in a colon, so it fell back to "whole reply". Call 2 therefore received Felix's whole four-part analysis as well as the rewritten prompt, which a person using his prompt by hand probably wouldn't send. A later re-run that extracts only the quote block would be a separate check, labelled as added afterwards.
- **Skill version.** The Arms table calls the deeper arm 1.1.1. The file that ran, the one hashed in `FROZEN.txt`, has `version: "1.1.2"` in its metadata. The hash is the authority, and the label in the table is wrong.
- **Leak check.** One hit: "act as" in `rent-felix-2`, which turns out to be the phrase "Housing Act AST". It's a false positive.
