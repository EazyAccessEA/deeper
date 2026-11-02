# The 1.1 scope guard

1.0 tended to grow tasks. In a sample of 40 past runs, 33 asked for at least one deliverable the user hadn't. 1.1 adds a rule: the rewritten prompt asks for the same deliverables as the task, and anything else goes on one "Worth knowing, not in this task" line.

**Round 1.** The first wording of the rule (`first-guard*.md`) was judged against no skill and 1.0 (`round1-*`). Scope rose from 2.4 to 4.0, but method and checks fell. It treated some real checks, like a printed proof, as extra deliverables.

**Round 2.** The final wording (`final*.md`) separates a check that tests the deliverable from something new to keep. All four versions were judged blind in one pass (`round2-*`), so judge noise affects them equally. Averages out of 5:

| | No skill | 1.0 | First guard | Final 1.1 |
|---|---|---|---|---|
| Expert method | 2.6 | 4.6 | 4.2 | 5.0 |
| Starts from raw material | 1.8 | 4.8 | 5.0 | 5.0 |
| Check outside the model | 1.0 | 3.8 | 3.4 | 4.8 |
| Kept to scope | 2.2 | 2.8 | 4.4 | 4.0 |
| Extra deliverables per task | 3.2 | 3.6 | 0.6 | 1.8 |

The judge picked the final 1.1 on four of five tasks. It's one run on five tasks, judged by a model. The baseline and 1.0 prompts are the same files as in the parent folder.
