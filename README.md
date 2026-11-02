# deeper

A skill that turns a task into the version an expert would ask for. Same scope, better method. It writes the prompt, then stops and asks before anything runs.

You type:

```
/deeper evaluate the typesetting of my book manuscript, the inner margins look too large
```

Before rewriting anything, it answers four questions about your task:

1. What would a top professional in this field do here that you haven't asked for?
2. What raw material would they start from? The data, files or originals, never a summary of them.
3. Which methods and tools would they use? Instruments, not vocabulary.
4. What would show the result is right, other than you or the model?

Then it hands you one rewritten prompt in a code block and asks whether to run it. On the margins task above, the plain rewrite asked you to describe your settings. The /deeper rewrite asked for the print PDF and the printer's spec, measured the margins against classic page canons and passed only after preflight and a printed proof.

## Install

### Any agent, with the skills CLI

```bash
npx skills add EazyAccessEA/deeper
```

The [skills CLI](https://github.com/vercel-labs/skills) asks which agents to install into. It knows about seventy agents, Claude Code and Codex among them. Add `-g` to install for your user rather than one project.

### Claude Code, as a plugin

```
/plugin marketplace add EazyAccessEA/deeper
/plugin install deeper@deeper
```

### By hand

Copy `skills/deeper/SKILL.md` into a folder named `deeper` in your agent's skills directory:

| Agent | Folder |
|---|---|
| Claude Code | `~/.claude/skills/deeper/` |
| Codex, Cursor and others that read the shared folder | `~/.agents/skills/deeper/` |

### In a chat app

ChatGPT, Claude.ai, Gemini and the rest have no skills folder. Paste the contents of `skills/deeper/SKILL.md` into the chat, then type `/deeper` and your task on the next line. The skill knows it may have no files or shell, and it asks you for the raw material instead.

## Use

- `/deeper <task>` deepens that task.
- `/deeper` on its own deepens the task already under discussion.
- If the task is too small for depth to matter, it says so in one line and stops.

It never starts the work. You read the rewrite, change what you like, and run it yourself or say "run it".

The skill's description tells the model to load it only when you type `/deeper` or ask for the deeper version, so it stays out of the way the rest of the time.

## Does it work?

A blind test on five real tasks from my own history, with project details stripped out: a product caption, book typesetting, selling a car, moving an app off Vercel, tidying a Downloads folder.

- One agent rewrote each task as a better prompt, with no skill.
- A second agent rewrote the same tasks with /deeper, in a plain chat setting with no files or tools.
- The pairs were shuffled into A and B, and a third agent on a different model scored them without knowing which was which.

/deeper won 5 of 5. Average scores out of 5:

| | No skill | /deeper |
|---|---|---|
| Expert method | 2.6 | 4.8 |
| Starts from raw material | 1.8 | 4.8 |
| Check outside the model, with a pass mark | 1.2 | 4.8 |
| Kept to the original scope | 4.2 | 4.0 |

Two things to weigh before you trust that. The judge is a model, and the skill itself says a model grading its own work doesn't count. And /deeper drifted on scope once: on the caption it added an A/B test nobody asked for. Every prompt, the answer key and the judge's reasons are in [`examples/`](examples/), so you can check them yourself.

I've used the skill about 230 times since October 2026. In roughly two of every three runs, my next message was "run it". Most of the rest were corrections to the rewrite, not rejections.

Tested so far in Claude Code. The install into Codex and Cursor folders is tested; running it inside those agents isn't yet. Reports welcome.

## Related skills

**The source.** The four questions are Felix Rieseberg's, from the Depth section of [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (13 October 2026). deeper turns that one prompt into a command, and adds the workspace check, the skills search and the stop rule.

**be-ambitious** (mine, not published) grew out of deeper. deeper is the Depth lens only. It reads the workspace, names the skills and agents to use, writes the prompt and stops. be-ambitious covers altitude, depth and range, adds hard targets, assumption checks and a list of what counts as finished, then does the work. Both insist on a check outside the model. Use deeper when you want to see and edit the prompt first. Use be-ambitious when you want the work done.

**[DannyMac180/skills@be-ambitious](https://github.com/DannyMac180/skills/tree/main/be-ambitious)** (MIT) is a separate skill built on the same prompt from the article. It behaves much like deeper: rewrite, then offer to run. It shares a name with my be-ambitious, which will need a new name if I ever publish it.

## Privacy

The skill sends nothing. It's a text file your agent reads, with no code and no network calls.

The skills CLI that installs it has its own anonymous install telemetry, which is where the install count on skills.sh comes from. Turn it off with `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1`. The site uses Cloudflare Web Analytics, which sets no cookies.

Those numbers answer one question: is deeper worth maintaining, and for which agents? `scripts/traffic-snapshot.sh` saves the repo's GitHub traffic to `data/traffic.csv` each day, because GitHub only keeps 14 days.

## The site

[deeper.tools](https://deeper.tools) is the docs and demo site. Its source is in `site/`, built with Astro. Every score on it is read from `examples/raw/` at build time, so the site can't drift from the evidence.

```bash
cd site && npm install && npm run dev
```

It runs on Cloudflare as static files. To publish a change: `cd site && npm run build && npx wrangler deploy`.

## Licence

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
