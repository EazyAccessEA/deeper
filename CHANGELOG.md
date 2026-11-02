# Changelog

## 1.1.0 (2026-11-02)

- Same deliverables: the rewritten prompt asks for what the task asked for and nothing more, while keeping every method, source and check. Anything else an expert would add goes on one line, "Worth knowing, not in this task". In a blind test, scope rose from 2.8 to 4.0 and extra deliverables fell from 3.6 to 1.8 per task, with method, raw material and checks all at or above 1.0. Details in `examples/raw/v1.1/`.
- The skill now offers the `npx skills find` search and runs it only on your yes, since it downloads code from npm.
- SECURITY.md: private reporting, and how to install a pinned release.
- Plugin manifests carry the same version as the skill.

## 1.0.0 (2026-11-02)

First public release.

- Frontmatter now follows the open Agent Skills spec, so the skill loads in Claude Code, Codex, Cursor and the other agents the `skills` CLI supports. The Claude Code-only keys `disable-model-invocation` and `argument-hint` are gone; the description now says to run only on /deeper.
- No `$ARGUMENTS` placeholder. The task is read from what the user typed, so the text works in agents that don't substitute it, and in a plain chat.
- Stops in one line when a task is too small for depth to change anything.
- Question 2 asks for the raw material when the model can't read files.
- Question 3 names skill folders for several agents and says what to do without a shell.
- Question 4 asks for a pass mark set where the best in the field would set it, and what counts as a fail.
