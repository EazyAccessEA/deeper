# 1.1.1: skills search without npx

The skills.sh security audit by Gen Agent Trust Hub rated 1.1.0 high risk. Three of its five findings cited one line in question 3, which offered to run `npx skills find <field>` and so download the skills CLI from npm. A fourth read the listed home-folder skill paths as data leaving the machine. 1.1.1 replaces that line: the skill lists the installed skills that fit, gives a search term to try at skills.sh, and runs nothing to find skills.

The pass mark was set before any run: in one blind pass with the same rubric and judge as the 1.1 test, 1.1.1 may score no more than 0.4 below the comparison on each measure, and add no more than 0.4 extra deliverables per task.

## Round 1: against the published 1.1 prompts (failed)

`v111.md` was judged blind against the published 1.1 prompts (`round1-*`). 1.1.1 came out 0.6 lower on expert method, 0.8 lower on raw material and 0.4 lower on checks. That fails the pass mark.

The change can't explain it. These runs use a plain chat setting with no installed skills, and no 1.1.1 reply mentions skills or searching, so the changed lines were never used. The gap is between a fresh model run and the one that was published.

## Round 2: with a fresh 1.1.0 run as the control (passed)

A fresh run of the unchanged 1.1.0 file (`v110.md`) was added, and all three were judged blind in one pass, with each version placed in each position (`round2-*`). Averages out of 5:

| | Published 1.1 | Fresh 1.1.0 | 1.1.1 |
|---|---|---|---|
| Expert method | 5.0 | 4.4 | 4.6 |
| Starts from raw material | 5.0 | 4.6 | 4.4 |
| Check outside the model | 4.0 | 4.0 | 3.8 |
| Kept to scope | 3.0 | 3.6 | 3.4 |
| Extra deliverables per task | 4.2 | 3.2 | 2.4 |

Against the fresh 1.1.0, every measure is within 0.2 and extra deliverables are lower, which passes. The judge picked the published prompt on two tasks, the fresh 1.1.0 on three and 1.1.1 on none. Two runs of the same 1.1.0 file differ by up to 0.6 here, so differences of that size between versions are within run-to-run noise.

## With shell tools offered

The chat setting never reaches the changed lines, so 1.1.1 was also run twice in Claude Code with shell tools offered, installed under the name `deeper111` so no other installed copy could answer (`tool-run1.md`, `tool-run2.md`). Neither run called `npx`. Both gave search terms for skills.sh ("book typesetting", "latex book design"). Local paths and the tester's name are redacted. Those sessions also loaded the tester's own global instructions, so they aren't clean of outside influence.

One earlier run with shell tools did call `npx skills find`. It was invoked as `/deeper` on a machine with an older copy of the skill installed under that name. Its log doesn't show which copy loaded, so it isn't counted either way.

It's one run per arm on five tasks, judged by a model.
