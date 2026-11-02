# Changelog

## 1.0.0 (2026-11-02)

First public release.

- Frontmatter now follows the open Agent Skills spec, so the skill loads in Claude Code, Codex, Cursor and the other agents the `skills` CLI supports. The Claude Code-only keys `disable-model-invocation` and `argument-hint` are gone; the description now says to run only on /deeper.
- No `$ARGUMENTS` placeholder. The task is read from what the user typed, so the text works in agents that don't substitute it, and in a plain chat.
- Stops in one line when a task is too small for depth to change anything.
- Question 2 asks for the raw material when the model can't read files.
- Question 3 names skill folders for several agents and says what to do without a shell.
- Question 4 asks for a pass mark set where the best in the field would set it, and what counts as a fail.
