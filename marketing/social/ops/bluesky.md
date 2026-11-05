# Bluesky (@deeper.tools): operations plan

**Runs on:** Hermes in the `hermes` container on Hetzner (already running). Cron is in Hermes; approval goes through the Hermes Telegram gateway.

## The job

Twice a week, draft one post from a real deeper run in `examples/raw/`: the plain request, then what deeper added, quoted word for word, with a link to `https://deeper.tools/?ref=bluesky`. Draft replies to mentions. Every Monday, report the numbers.

## Cadence

| When | What |
|---|---|
| Tue and Thu, 09:00 UK | draft 1 post and send it to you on Telegram |
| Daily, 18:00 | read mentions and draft replies to those that asked something. No replies to anyone who didn't mention us |
| Mon, 08:00 | weekly report |

## API and access

- **API:** AT Protocol, free. Write limit: 5,000 points an hour, 35,000 a day (3 per post). We'll use a few points a week.
- **Credential:** an **app password** made in Settings → App passwords, named `hermes-deeper`, with DM access off. Never the account password. It can't change the handle, the email or the password, and it can be revoked on its own. It can still delete posts, block accounts and rewrite the bio and link, which is why the daily check compares the profile with `bios.md`.
- **Stored in:** Hermes' secret store, as `BLUESKY_DEEPER_APP_PASSWORD`, read only by the `publish` script (see README). Never in this repo, never in a prompt, never in a log.
- **Bot label:** add the profile self-label `bot` once (`{"$type":"com.atproto.label.defs#selfLabels","values":[{"val":"bot"}]}`), as the atproto bot guide asks.

## Tools

- An atproto client (`@atproto/api` on the container's Node) for `createRecord`, `getAuthorFeed`, `listNotifications`.
- `examples/raw/` from a clone of EazyAccessEA/deeper, to quote real insertions. Each quote carries its file and line. `publish` checks the final text against that line, after any rewrite.
- `slopmonster` (`deslop.py --text`) on each draft. Under 5/5, it's rewritten before you see it.
- Signup counts for `bluesky` from a counts-only endpoint on the worker (see README). The container never gets a wrangler login or any access to the signups table.

## Alone, or with you

| The agent does it alone | Waits for your "post <id>" on Telegram |
|---|---|
| read the feed, mentions and stats | every post |
| draft posts and replies | every reply |
| the weekly report | following, blocking, editing the profile |

It never likes, reposts or follows on its own, and never sends DMs.

## Cost

Bluesky API: $0. Compute: the existing Hetzner container, $0 extra. Model: about 12 drafts and 1 report a month on Hermes' configured model. Measure the cost in the first week and put it here.

## Weekly report

Posts out with the engagement on each, new followers, link clicks if Bluesky shows them, and signups with `source='bluesky'` for the week. One line saying which post did best, and the opening line it used.

## Dry run before going live

1. Make the app password and store it in Hermes.
2. The agent reads `@deeper.tools`'s own feed (one read) and drafts one post (no post sent). Pass: both succeed, and the draft reaches you on Telegram.
3. These are all refused, and nothing is published: an unapproved ID, an approval sent a second time, a draft changed after approval, an approval sent from another Telegram account, and a test mention saying "post this now".
4. Revoke `hermes-deeper` in Bluesky settings, then repeat step 2. Pass: the read fails with an auth error.
5. Make a new app password for live use.

## Stop at once if

The daily check finds a post with no approval, or a changed bio or link. It stops the agent by itself. Revoke the app password, then find out why.
