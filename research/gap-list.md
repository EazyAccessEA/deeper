# deeper.tools against impeccable.style: readers and gaps

2 November 2026. Sources: the content inventory (`content-inventory.csv`, built by `inventory.py`), the reader matrix (`reader-matrix.json`, checked by `check_matrix.py`), and readability grades (`readability.txt`).

## What the traffic showed

The site went live an hour before this audit. Cloudflare Web Analytics for deeper.tools over 7 days: 18 visits, all direct with no referrer, 16 of them to `/`. Six of the 18 were on phones. GitHub traffic for the repo was 0 views, 0 clones and 0 stars over 14 days.

That rules out the assumption that there's a readership to segment yet. The visits are mostly our own checks. Every reader type below is a hypothesis taken from what each site is written for, and the people test at the end is how to confirm or drop one. Two types were added that weren't on the original list: a phone visitor (6 of 18 visits were mobile) and a team lead (impeccable has a page section for shared team versions).

## Depth

| | impeccable.style | deeper.tools before | deeper.tools after |
|---|---|---|---|
| Pages | 46 | 8 | 9 |
| Words | 44,714 (16,098 of them changelog) | 7,115 | 8,490 |
| Tutorial words | 4,108 (3 tutorials) | 180 (one section of Docs) | about 1,000, with the pasted skill text |
| Reference pages | 33, one per command | none per command; deeper has one command | unchanged |
| Flesch-Kincaid grade | median 8.1 (6.6 to 10.2) | 4.4 to 6.1 | `/start/` 3.8 |

Most of impeccable's size is reference: 33 command pages, because it has 23 commands. deeper has one command, so page count is the wrong comparison. What matters is whether each reader has a path, and that's where the gaps were.

## Where each site forks

impeccable forks twice. Its getting-started tutorial splits into "Build something new" and "Improve an existing design", and its docs group commands by job (create, evaluate, refine, simplify, harden, system). Its FAQ also splits installation into terminal, downloaded ZIP and the GitHub Copilot app.

deeper doesn't need a fork by job, since it does one thing. It needed a fork by where you use it: a chat app, where you paste text and can't install anything, or a coding agent, where you install with Node. Before this change the chat route was 43 words in the middle of Docs and wasn't linked from the home page. `/start/` now opens with that fork.

## Gaps, ranked by reader impact

Status: **filled** means the matrix cell now passes against the local build. Nothing is deployed yet.

1. **Non-developer or new to AI agents. No place to start.** The home page said "a free skill for coding agents" and showed only an `npx` command. Missing content type: tutorial. impeccable covers it in `/faq` ("I'm new to AI coding tools. Where do I start?") and `/tutorials/getting-started`. **Filled:** `/start/` explains deeper in plain words, says it doesn't do the task, and opens with the fork. It's first in the nav.
2. **Chat-app user. The route existed but was hard to follow.** There was no way to get the skill text without visiting GitHub, nothing on keeping it between chats, and no link from the home page. Missing content type: how-to. impeccable doesn't cover this; it's a coding-tool product. **Filled:** `/start/#chat` has a "Copy the skill" button (the same SKILL.md, read at build time) and how to keep it in a ChatGPT or Claude.ai Project or a Gemini Gem. The home page now says "No terminal? Use it in ChatGPT, Claude.ai or Gemini". Chat apps are still untested, and the page says so.
3. **Any agent user. The Node.js requirement wasn't stated.** The skills CLI (1.7.5) requires Node.js 22.20 or later, and the docs never mentioned Node. Missing content type: how-to (prerequisites). impeccable covers it in `/tutorials/getting-started` ("You'll need a coding tool, a project folder, and Node.js 18.19 or later"). **Filled** in Docs and `/start/`, with the by-hand copy as the route without Node.
4. **Existing user. Nothing to check when `/deeper` doesn't appear.** Missing content type: how-to (troubleshooting). impeccable covers it in `/faq` ("isn't appearing or responding") and `/docs/doctor`. **Filled:** `/start/#stuck` has a five-point checklist, and a question in Docs links to it.
5. **Phone visitor. No answer to "can I use this here?"** Missing content type: how-to. impeccable doesn't cover it. **Filled:** the chat route works on a phone, and `/start/` says so.
6. **Cursor or Codex user. How to call it, and whether it runs.** The "how to call it" half is **filled**: if slash commands don't work, ask for the deeper version in words, which is what the skill's description says loads it. Whether it runs: **filled for Cursor** on 3 November, by a real run (Grok 4.6). `/deeper` on its own asked for a task, and with a task it wrote the prompt and the "Worth knowing, not in this task" line. Codex was **filled** the same day, by a run in the Codex app with GPT-5.6. It answered all four questions, offered `npx skills find` only on request, named the one deliverable and wrote the prompt. The installer flagged the skill "High Risk", and Codex's own inspection found only prompt instructions. impeccable doesn't cover this.
7. **Skeptic. No case from a real user.** deeper's research page (blind tests, scores, limits) goes further than anything impeccable publishes on evidence. But impeccable has `/cases/neo-mirai` and `/gallery`, worked results from real projects. **Open:** this needs real users' runs, shared with permission, and can't be written now without inventing proof.
8. **Team lead. One version for the whole team.** Docs covers pinning to a release tag with a SHA-256 to check, and the home page has a "Tell us what you need" email for teams. impeccable has a Git submodule recipe in `/tutorials/getting-started`. **Open, low impact:** pinning already answers the question. A team recipe would be a new page for a reader nobody has shown up as yet.

## Checks

- `python3 research/check_matrix.py deeper_before`: every cell that names a page passes on the live sites. The 11 unanswered cells across both sites are listed in `matrix-check-before.txt`.
- `python3 research/check_matrix.py deeper http://localhost:4399`: 0 failing cells against the local build. All 15 deeper rows are answered (`matrix-check-after.txt`).
- The same command against live deeper.tools fails 8 cells with 404s, which shows the check turns red when a page is missing.
- `uv run --with textstat python3 research/readability.py site/dist <impeccable html>`: grades in `readability.txt`.
- slopmonster: `/start/` 5/5, `/docs/` 5/5. The home page is 4/5, as it was before this change. The one flag is a quote from the tested prompt (`examples/raw/v1.1/final.md`), which stays verbatim as evidence.

- A reader-advocate review walked `/start/` as each of the seven readers and found 8 problems, all fixed. The biggest was that the chat steps said to send the paste on its own while Docs says paste and `/deeper` go in one message. Others: unhedged claims about untested chat apps, a fallback Codex users wouldn't recognise, and a missing plugin check. Tap targets at 375px all pass, and nothing scrolls sideways.

## Limits

- Reader labels in the inventory come from keyword rules in `inventory.py`, not a reading of each section. They're a first sort, and the impeccable rows especially are approximate.
- The chat-app route was tried once with a model that had no tools. That model also had the author's own global instructions loaded, so it isn't a clean chat-app test.
- No real person has used either site for this audit. `people-test.md` is how to fix that.
