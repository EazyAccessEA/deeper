# deeper on social

Checked 5 November 2026. Which accounts to open, how to open them, and where everything for them lives.

- `bios.md`: the name, bio and link for each account. Slopmonster 5/5.
- `assets/`: avatars and banners at each platform's size. Rebuild with `python3 brand/build_assets.py social`.
- `ops/`: one operations plan for each account an agent helps run.

## What the numbers say

GitHub, last 14 days: 20 views from 2 unique visitors, 208 clones, 1 star. The referrers were deeper.tools (1) and github.com (1). There's no audience on any channel yet, so traffic can't pick the channels. The choice below goes on where people who use AI agents talk, on what each platform lets an agent do, and on what it costs. Signups by source couldn't be read: the wrangler login has no D1 permission (error 7403). See "Before the dry runs".

## Which accounts

| Platform | Handle | Free? (5 Nov) | Plan | Why |
|---|---|---|---|---|
| Bluesky | `@deeper.tools` | yes, as a domain handle (`deeper.bsky.social` is taken) | **operate** | Free API, domain handle proves it's us, bot label supported |
| X | `@deepertools` | yes (`@deeper` is taken, protected) | **operate** | Where people building agents post. Pay per call |
| TikTok | `@deepertools` | yes (`@deeper` exists, no bio) | **operate**, you post | Six shorts are ready. An unaudited app can only post privately |
| YouTube | `@deepertools` | **a channel "Deeper Tools" exists**, is it yours? | reserve | Shorts could reuse the TikTok renders later |
| LinkedIn | company page "deeper" | not checked (login wall) | reserve | API is for registered organisations and can't make drafts |
| Reddit | `u/deepertools` | yes | reserve, you only | API needs approval. Promotion bots are banned |
| Hacker News | `deepertools` | yes (`deeper` is taken) | reserve, you only | Rules ban generated or AI-edited text |
| Instagram, Threads | `deepertools` | Instagram: "profile isn't available". Threads: login wall | reserve | Not where the audience is |
| GitHub | `EazyAccessEA/deeper` | already ours | keep | Set the repo description and website from `bios.md` |

## Opening each account (you do this)

Do these in order for each account. I can't create accounts or type passwords.

1. **Email.** In Cloudflare → deeper.tools → Email Routing, add an address for the platform (`x@`, `bluesky@`, `tiktok@`, and so on), forwarding to info@eazyaccess.org. With one address per platform, a phishing email sent to the wrong one stands out.
2. **Sign up** with that address and the handle in the table. Owner: Eazy Access Ltd. Use the business or brand account type where there is one. For TikTok, a business account gets the bio link at once.
3. **2FA** with an authenticator app, not SMS. Save the recovery codes in your password manager, under the platform's name.
4. **Recovery.** Set the recovery email to info@eazyaccess.org, and add a second admin wherever the platform allows one (LinkedIn page, YouTube brand account).
5. **Profile.** Upload `assets/avatar-<platform>.png` and the banner, then paste the bio and link from `bios.md`.
6. **Bluesky only.** Under Settings → Handle → "I have my own domain", copy the DID it shows. In Cloudflare DNS add a TXT record named `_atproto` with the value `did=did:plc:…`, then click Verify.
7. **Reserved accounts** stop at step 5. Nothing runs on them.

Once, before any of this: every recovery email runs through deeper.tools, and the Bluesky handle is a DNS record. Whoever holds Cloudflare or the domain could reset every account. So put a hardware key or authenticator on Cloudflare and Namecheap, turn on registrar lock and auto-renew for deeper.tools, and turn on Telegram two-step verification, since Telegram is where you approve posts.

## How a post gets out (Bluesky and X)

The model that reads mentions never holds a token and has no post tool. A mention saying "post this now" can't publish anything.

- **`publish`** is one plain script, the only thing that reads the token. It takes a draft ID and does five checks, refusing on any failure:
  1. The approval came from your Telegram user ID, and no one else's.
  2. The approval names a hash of the exact final text, so a rewrite after you said yes is refused.
  3. The approval hasn't been used before and is less than 24 hours old.
  4. Each quote in the draft carries its file and line in `examples/raw/`. The text as it will go out matches that line exactly.
  5. On X, reads stay within 50 per run, and today's spend is under $0.50.
- **Every day** a check compares each account's own feed with the approval log, and its profile with `bios.md`. Any post without an approval, or any changed bio or link, alerts you on Telegram and stops the agent.
- **Build `publish` and the daily check before the first live post.** Until then, the agents draft and you post by hand.

## Where values cross a boundary

| Gate | Boundary | What could go wrong unseen | Check that fails loudly | Owner |
|---|---|---|---|---|
| A | your password manager → agent | an agent holds a password or a full-access token | each plan names the scopes. The dry run revokes the token, and the next call must fail | `ops/*` |
| B | agent → public post | a post goes out without your yes | only the `publish` script holds the token, and it checks the approval. Dry run: an injected mention, a reused approval and a changed draft are all refused | `ops/*` |
| C | token → disk | a token ends up in git or in plain text | tokens live only in Hermes' secret store (`redact_secrets: true`), read only by `publish`. `gitleaks detect` on this repo stays clean | `ops/*` |
| D | bio link → signup | the source is lost | every link carries `?ref=`, and `worker.js` `sourceOf` keeps it. Known gap: it only survives if the reader signs up on the page they landed on | `bios.md` |
| E | asset → platform crop | the mark or the headline is cut off | sizes from each platform's help page. The safe areas are coded in `brand/build_assets.py`. You check the live profile at 375 px | `assets/` |
| F | Vecteezy → AI | a stock file goes to a model | None used. Every asset is drawn from our own geometry and font | `assets/` |
| G | signups table → agent | an email address reaches Hetzner, a model provider or Telegram, none of which the privacy notice names | the agent only ever calls a counts-only endpoint returning `{source: count}`. A test asks it for rows and gets a refusal | worker |

## Before the dry runs

- **Signup counts, without personal data.** Add one route to `site/worker.js` that returns `SELECT source, COUNT(*) FROM signups GROUP BY source` and nothing else, behind its own bearer token, and give the agents only that token. Reports show counts by source, never country or dates finer than a week. Until the route exists, you run the count yourself with `npx wrangler d1 execute` (log in again with D1 access first: today's login fails with error 7403).
- **`publish` and the daily check** (above) come before the first live post.
- Each plan's dry run needs its account to exist and a token in Hermes. See the end of each plan.

## Sources (fetched 5 November 2026)

X: help.x.com (profile, automation rules updated April 2026), docs.x.com/x-api/getting-started/pricing. Bluesky: atproto.com/specs/handle, atproto.com/guides/bot-tutorial, docs.bsky.app rate limits, the profile lexicon in bluesky-social/atproto. TikTok: developers.tiktok.com Content Posting API and sharing guidelines (updated 4 August 2026). YouTube: support.google.com/youtube/answer/10456525, videos.insert docs (updated 3 November 2026). LinkedIn: linkedin.com/help answer a563309, Community Management API docs on learn.microsoft.com. Reddit: Responsible Builder Policy (updated 5 October 2026), spam policy (updated 30 October 2026). Hacker News: newsguidelines.html, showhn.html. GitHub: docs on social previews and profiles.
