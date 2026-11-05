# X (@deepertools): operations plan

**Runs on:** Hermes in the `hermes` container on Hetzner, using the installed `xurl` skill (X's official CLI). Approval goes through the Hermes Telegram gateway.

## The job

Twice a week, draft one post from a real deeper run, in the same form as Bluesky but written for X. Draft replies only to people who mentioned @deepertools and asked something, and never to anyone on the opt-out list (anyone who says "stop" or similar is added to it). Every Monday, report the numbers.

## Cadence

| When | What |
|---|---|
| Tue and Thu, 09:00 UK | draft 1 post, send to you on Telegram |
| Daily, 18:00 | read mentions, draft replies to those that asked something |
| Mon, 08:00 | weekly report |

## API and access

- **API:** X API, pay per use. Each post costs $0.015, **a post with a link $0.20**, reading a post $0.005, reading our own data $0.001. Buy credits in the X developer console. The first purchase gets up to $20 free.
- **Rules (X automation rules, April 2026):** automated informational posts are allowed. Not allowed: posting about trending topics, duplicate posts, and replies triggered by keyword search. Replies only to people who mentioned us and asked something, one reply per mention, with an easy way to opt out. The rules also say an AI reply bot needs X's written approval first (section B.3). Here a person approves every reply before it goes, so nothing is replied to automatically.
- **Label:** turn on the "Automated" account label in settings and link it to your own account.
- **Credential:** An OAuth user token from an app in the X developer console, with scopes `tweet.read`, `tweet.write`, `users.read` and `offline.access` (check these names in the console; they weren't confirmed from a primary page). No DM or follow scopes.
- **Stored in:** Hermes' secret store, as `X_DEEPER_TOKEN`, read only by the `publish` script (see README). Not in `~/.xurl`, where any shell the agent runs could read it. Never in this repo.
- **Spend:** prepaid credits only, auto-recharge off. A daily balance check stops the agent and alerts you once a day's spend passes $0.50.

## Tools

- `xurl` for reading mentions and our own post metrics. Posting goes only through `publish`.
- `examples/raw/`, checked word for word, as for Bluesky.
- `slopmonster` on every draft.
- Signup counts for `x` from a counts-only endpoint on the worker (see README). The container never gets a wrangler login or any access to the signups table.

## Alone, or with you

| The agent does it alone | Waits for your "post <id>" on Telegram |
|---|---|
| read mentions and our own metrics | every post and every reply |
| draft posts and replies | follow, like, repost, profile edits |
| the weekly report | reads beyond 50 in one run |

## Cost

About 9 posts a month with a link ($1.80), 20 replies without one ($0.30), and around 300 reads ($1.50): roughly **$4 a month in X credits**. Buy $10 of prepaid credit and leave auto-recharge off, so $10 is the most it can spend. Compute: the existing container, $0 extra. Model cost: measure in the first week, as for Bluesky.

## Weekly report

Posts out, impressions, likes, reposts, replies and link clicks on each post, new followers, credits spent, and signups with `source='x'`.

## Dry run before going live

1. Create the app, authorise @deepertools, buy the smallest credit pack.
2. The agent reads @deepertools's profile (one read, $0.001) and drafts one post (no post sent). Pass: both succeed, and the draft reaches you on Telegram.
3. These are all refused, and nothing is published: an unapproved ID, an approval sent a second time, a draft changed after approval, an approval sent from another Telegram account, and a test mention saying "post this now".
4. Revoke the app's access under Settings → Connected apps, then repeat step 2. Pass: the read fails with 401.
5. Authorise again for live use.

## Stop at once if

The daily check finds a post with no approval, or the balance check trips. Both stop the agent by themselves. Revoke the app, then find out why.
