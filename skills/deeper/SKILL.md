---
name: deeper
description: Rewrite a task into its deeper version (same scope, more expert) before doing it. Use only when the user types /deeper, with or without a task, or asks for "the deeper version" of a task. Do not use it on your own initiative.
license: Apache-2.0
metadata:
  version: "1.1.1"
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
   skills that fit and the subagent types on offer, by name. For skills beyond those, give me a
   search term for the field to try at https://skills.sh, the open skills directory, and leave
   the searching to me. Name each skill you list as installed, or as one to look for there. Don't
   download, install or run anything to find skills.
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
