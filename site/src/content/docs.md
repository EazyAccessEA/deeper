# Docs

deeper is one skill file for coding agents. Type `/deeper` before a task and it rewrites the task the way an expert would ask for it, then stops so you can read it, change it and decide whether to run it.

## Install

### Any agent, with the skills CLI

```
npx skills add EazyAccessEA/deeper
```

The [skills CLI](https://github.com/vercel-labs/skills) is an open-source installer for agent skills. It asks which agents to install into, then copies or links the skill into each one's folder. Add `-g` to install it for your user rather than one project. Its install telemetry can be turned off with `DISABLE_TELEMETRY=1`. The CLI asks for Node.js 22.20 or later; `node --version` shows yours.

### Claude Code, as a plugin

```
/plugin marketplace add EazyAccessEA/deeper
/plugin install deeper@deeper
```

### By hand

Copy `skills/deeper/SKILL.md` from the repo into a folder named `deeper`:

- Claude Code: `~/.claude/skills/deeper/`
- Codex, Cursor and other agents that read the shared folder: `~/.agents/skills/deeper/`

### In a chat app

ChatGPT, Claude.ai and Gemini have no skills folder. Paste the contents of `SKILL.md` into the chat, then type `/deeper` and your task on the next line. With no files or shell to look at, the skill asks you for the raw material instead. [Start here](/start/#chat) has a copy button and how to keep it in a Project or Gem so you don't paste it every time.

### Where it's tested

Running deeper is tested in Claude Code, in Cursor with Grok 4.6 and in Codex with GPT-5.6. In Cursor, `/deeper` on its own asked for a task, and with a task it wrote the prompt and the "Worth knowing" line. In Codex it answered the four questions, named the one deliverable and wrote the prompt. Cursor and Codex were one run each, by hand. If you try it there, an [issue](https://github.com/EazyAccessEA/deeper/issues) saying how it went helps.

## Update, remove or pin

```
npx skills update deeper
npx skills remove deeper
```

`add` and `update` follow the main branch. To install an exact release instead, name its tag:

```
npx skills add https://github.com/EazyAccessEA/deeper/tree/v1.1.1/skills/deeper
```

Each [release](https://github.com/EazyAccessEA/deeper/releases) lists the SHA-256 of its `SKILL.md`, so you can check the file you got.

## Your first run

Check it's installed with `npx skills list`. In Claude Code, type `/` and deeper appears in the list of commands. Then give it a real task:

```
/deeper Can we move our Next.js app off Vercel to Cloudflare?
```

The reply opens with four short answers. This is the first of them from the blind test, word for word:

> **Top professional.** A platform engineer who has done this migration. They inventory every Vercel feature the app actually uses and map each one to Cloudflare (Workers via the OpenNext adapter) before answering, and they prove the answer by building and running the app on Cloudflare rather than reasoning about it.

Then it names what your task asks for, writes the prompt, and ends like this:

> **Your task asks for:** an answer to whether we can move, with what it would take.
>
> Worth knowing, not in this task: the migration itself (DNS cutover, rollback plan, CI/CD for preview deploys) and a cost comparison from real traffic.
>
> Shall I run it?

Nothing runs until you say so. The [full reply](https://github.com/EazyAccessEA/deeper/blob/main/examples/raw/v1.1/final-full.md) is in the repo.

## Use

- `/deeper <task>` deepens that task.
- `/deeper` on its own deepens the task already under discussion.
- If there's no task at all, it asks for one in a single line.

The skill's description tells the model to load it only when you type `/deeper` or ask for the deeper version. It stays out of the way the rest of the time.

## The four questions

### 1. Expert moves

What would a top professional in this field do here that you haven't asked for? The skill names the field first, then the one or two moves that separate expert work from competent work. A list of ten tips is the failure mode.

### 2. Raw material

What would they start from? Not the summary, template or digest, but what sits underneath it: the data, records, recordings, originals, people. If the agent can read files, it checks the workspace first and says what's there and what's missing. It also names one thing you take as true that the raw material could disprove.

### 3. Instruments

Which methods and tools would they use? The instruments themselves: a database and a statistical model, a profiler, a test suite. Models tend to change their vocabulary without changing their method, and this question is there to catch that.

It then lists the installed skills and agents that fit, by name. For skills beyond those, it gives you a search term to try at [skills.sh](https://skills.sh) and leaves the search to you. It doesn't download, install or run anything to find skills.

### 4. Outside check

What would show the result is right, other than you or the model? A test, a measurement, a real audience, a domain expert. Something that can run straight away is best. The pass mark goes where the best in the field would put it, and the answer says what counts as a fail.

## Same deliverables

Before writing the prompt, deeper lists what your task asks you to end up with, and the prompt asks for exactly that. Depth changes how each deliverable is made and checked, never how many there are. A check stays in however much work it takes to run, such as a load test or a printed proof. Anything that would leave you something extra to keep, like a second version, a new script or another document, goes on one line after the prompt: "Worth knowing, not in this task". You choose whether to do it.

Version 1.0 had no such rule and often grew tasks. The [research page](/research/) has the before and after.

## When it stops early

If a task is too small for depth to change anything, such as a status question or a one-line fix, it says so in one line and stops. In the blind test it chose not to stop on "tidy my Downloads folder", because losing the only copy of a contract is a real risk.

## Questions

### Does it do the work?

No. It writes the prompt and asks. To run it, say so.

### Does it send my files anywhere?

The skill itself sends nothing. It's a text file your agent reads, with no code and no network calls. Whatever your agent does with your files is up to the agent and your permissions.

### Why not make it do the work too?

Seeing the prompt first is the point. You catch a wrong assumption before it costs an hour of agent time.

### How is it different from be-ambitious?

Both build on the same article. deeper is the depth lens only: it writes the prompt and stops so you can edit it. be-ambitious also widens the goal and borrows from other fields, sets hard targets, then does the work. Use deeper when you want to see the prompt first. The README's [related skills](https://github.com/EazyAccessEA/deeper#related-skills) section covers a third, separate skill of the same name.

### Who makes it?

Eazy Access Ltd, as [EazyAccessEA](https://github.com/EazyAccessEA) on GitHub. The company details are in the [legal notice](/legal/). deeper is free and Apache 2.0 licensed.

### /deeper doesn't appear. What do I check?

Start a new session, then run `npx skills list`. [Start here](/start/#stuck) has the full checklist.

### How do I report a problem?

Bugs and questions: [open an issue](https://github.com/EazyAccessEA/deeper/issues). Anything private: hello@deeper.tools. Security problems, such as text in the skill that could make an agent run or send something without asking: use the [private report form](https://github.com/EazyAccessEA/deeper/security/advisories/new), not a public issue. [SECURITY.md](https://github.com/EazyAccessEA/deeper/blob/main/SECURITY.md) has the details.
