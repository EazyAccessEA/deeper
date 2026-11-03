# Security

deeper is a text file that AI agents follow with your agent's permissions. A change to it reaches everyone who installs or updates it, so security reports are taken seriously.

## Reporting a problem

Use GitHub's private form: [report a vulnerability](https://github.com/EazyAccessEA/deeper/security/advisories/new). Please don't open a public issue for anything an attacker could use.

Examples worth reporting:

- text in `skills/deeper/SKILL.md` that could make an agent run, download or send something without asking
- a way to change what `npx skills add EazyAccessEA/deeper` installs
- anything on deeper.tools that loads code from somewhere it shouldn't

deeper has one maintainer. Expect a first reply within 7 days.

## Installing a fixed version

`npx skills add EazyAccessEA/deeper` installs whatever is on `main` today. To install an exact release instead, name its tag:

```bash
npx skills add https://github.com/EazyAccessEA/deeper/tree/v1.1.1/skills/deeper
```

Each release on GitHub lists the SHA-256 of its `SKILL.md`, so you can check the file you got:

```bash
shasum -a 256 .claude/skills/deeper/SKILL.md
```

Read the skill before you install it. It's short.
