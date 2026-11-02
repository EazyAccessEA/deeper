# Blind test, 2 November 2026

Five tasks from real use, with names and project details taken out. Each was rewritten twice, once with no skill and once with /deeper, and judged blind.

## How it ran

1. `raw/tasks.md` holds the five tasks.
2. One agent rewrote each task as a better prompt, with no skill: `raw/baseline.md`.
3. A second agent ran /deeper on the same tasks, told it had no files, shell or installed skills. Its full replies are in `raw/deeper-full.md`; the final prompts alone are in `raw/deeper.md`.
4. A script shuffled each pair into A and B (`raw/pairs.md`) and kept the answer in `raw/key.json`.
5. A judge on a different model saw only `raw/pairs.md`. It scored four measures from 1 to 5 and picked a winner per task: `raw/judge.json`.

Both writers ran on Claude Opus 5.5 and the judge on Claude Sonnet 5.5.

## Results

| Task | Winner | Judge's reason, short |
|---|---|---|
| T1 Instagram caption for a jar of honey | /deeper | asks for the label, the pollen report and past posts; adds an A/B test, which is mild scope creep |
| T2 Book typesetting, margins too large | /deeper | works from the print PDF and printer spec, passes on preflight and a printed proof |
| T3 Sell a VW Polo, buy a Golf | /deeper | values the car from sold prices, models running costs, requires an inspection |
| T4 Move a Next.js app off Vercel | /deeper | asks for the repo and 30 days of logs, gates the switch on route diffs and a load test |
| T5 Tidy the Downloads folder | /deeper | finds duplicates by hash and checks no unique file is lost |

On T5 the skill could have stopped and called the task too small. It didn't: losing the only copy of a contract is a real risk, and the judge agreed.

## Limits

Five tasks is a small sample. One judge, and a model, though from a different model than the writers. The writers knew they were in a test. A person judging the pairs blind would be a stronger check; `raw/pairs.md` is ready for that.
