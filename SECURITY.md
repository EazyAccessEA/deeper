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
npx skills add https://github.com/EazyAccessEA/deeper/tree/v1.1.2/skills/deeper
```

Release tags can't be moved or deleted once they're pushed. A repository rule blocks it.

Each release on GitHub lists the SHA-256 of its `SKILL.md`. deeper.tools publishes the hash of the latest release too, at [deeper.tools/skill-sha256.txt](https://deeper.tools/skill-sha256.txt). The site is deployed from Cloudflare, not from GitHub, so changing both the file and its hash takes two separate break-ins. Check the file you got against the site:

```bash
shasum -a 256 .claude/skills/deeper/SKILL.md
curl -s https://deeper.tools/skill-sha256.txt
```

The two hashes should match.

Read the skill before you install it. It's short.
