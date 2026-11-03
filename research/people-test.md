# People test: install and run deeper cold

One person per reader type, one session each, about 15 minutes. Print this page, or keep it open beside them.

## Who

| # | Reader | Find someone who | Device |
|---|---|---|---|
| 1 | Claude Code user | uses Claude Code most days | their laptop |
| 2 | Cursor or Codex user | codes with Cursor or Codex, not Claude Code | their laptop |
| 3 | Chat-app user | uses ChatGPT, Claude.ai or Gemini and never opens a terminal | their laptop |
| 4 | New to AI | has used a chatbot a few times at most | their laptop |
| 5 | Phone visitor | any of the above | their own phone |
| 6 | Skeptic | reviews tools or prompts for a living, or just doubts AI claims | any |
| 7 | Team lead | decides which tools a team uses | any |

Nobody who has seen deeper before.

## Before you start

- Open deeper.tools on their device. Don't show them anything else.
- Tell them: "This is a tool for AI assistants. Get it working and use it on something you'd actually ask an AI this week. Think out loud. I can't help, but I'll take notes."
- Start a timer.

## While they work

- Don't help, point or nod. If they're stuck for 3 minutes, write down where, then tell them the next step and carry on timing.
- Write down the first place they hesitate, scroll back or say "hm": the page and the exact line.
- The skeptic (6) and team lead (7) don't have to install it. Ask the skeptic, "Would you trust this? What would change your mind?" Ask the team lead, "How would you give your team the same version?"

## Record

| Field | Reader 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Got a first /deeper reply (yes or no) | | | | | | | |
| Minutes to that reply | | | | | | | |
| Route they took (chat or agent) | | | | | | | |
| First stuck point (page and line) | | | | | | | |
| Times you had to step in | | | | | | | |
| "What does it do?" in their words | | | | | | | |
| Would they use it again? | | | | | | | |

## Afterwards, ask

1. "In one sentence, what does deeper do?" Right if they say it rewrites the request and waits, and that it doesn't do the task itself.
2. "Was there a moment you nearly gave up? Where?"
3. "What did you expect to find that wasn't there?"

## Pass mark

- Readers 1 to 5 get a first reply within 10 minutes with no help. A run where you stepped in counts as a fail, even if they finished.
- Readers 1 to 5 answer question 1 correctly.
- Each stuck point turns into one row in `reader-matrix.json` and one fix. A fix that adds a page needs two readers stuck in the same place.

Send the filled table to hello@deeper.tools or drop it in `research/`, and the next round of changes starts from it.
