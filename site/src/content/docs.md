# Docs

deeper is one skill file. It turns a task into the version an expert would ask for, then stops so you can read it, change it and decide whether to run it.

## Install

### Any agent, with the skills CLI

```
npx skills add EazyAccessEA/deeper
```

The [skills CLI](https://github.com/vercel-labs/skills) asks which agents to install into, then copies or links the skill into each one's folder. Add `-g` to install it for your user rather than one project.

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

ChatGPT, Claude.ai and Gemini have no skills folder. Paste the contents of `SKILL.md` into the chat, then type `/deeper` and your task on the next line. With no files or shell to look at, the skill asks you for the raw material instead.

## Use

- `/deeper <task>` deepens that task.
- `/deeper` on its own deepens the task already under discussion.
- If there's no task at all, it asks for one in a single line.

The reply has four short answers, then one prompt in a code block, then a question: run it? Nothing runs until you say so. Edit the prompt first if you like.

The skill's description tells the model to load it only when you type `/deeper` or ask for the deeper version. It stays out of the way the rest of the time.

## The four questions

### 1. Expert moves

What would a top professional in this field do here that you haven't asked for? The skill names the field first, then the one or two moves that separate expert work from competent work. A list of ten tips is the failure mode.

### 2. Raw material

What would they start from? Not the summary, template or digest, but what sits underneath it: the data, records, recordings, originals, people. If the agent can read files, it checks the workspace first and says what's there and what's missing. It also names one thing you take as true that the raw material could disprove.

### 3. Instruments

Which methods and tools would they use? The instruments themselves: a database and a statistical model, a profiler, a test suite. Models tend to change their vocabulary without changing their method, and this question is there to catch that.

It then lists the installed skills and agents that fit. If it can run commands, it searches the open skills ecosystem with `npx skills find <field>` and marks each result as installed or only findable. It asks before installing anything.

### 4. Outside check

What would show the result is right, other than you or the model? A test, a measurement, a real audience, a domain expert. Something that can run straight away is best. The pass mark goes where the best in the field would put it, and the answer says what counts as a fail.

## When it stops early

If a task is too small for depth to change anything, such as a status question or a one-line fix, it says so in one line and stops. In the blind test it chose not to stop on "tidy my Downloads folder", because losing the only copy of a contract is a real risk.

## Questions

### Does it do the work?

No. It writes the prompt and asks. To run it, say so.

### Does it send my files anywhere?

The skill itself sends nothing. It's a text file your agent reads. Whatever your agent does with your files is up to the agent and your permissions.

### Why not make it do the work too?

Seeing the prompt first is the point. You catch a wrong assumption before it costs an hour of agent time.

### How is it different from be-ambitious?

See [related skills](https://github.com/EazyAccessEA/deeper#related-skills) in the README.
