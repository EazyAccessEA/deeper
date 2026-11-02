# TikTok shorts for deeper

Six vertical shorts, 1080×1920. Every line on screen comes from a real /deeper run or the README's blind-test table. The `source` field in [shorts.json](shorts.json) says which.

To change a line, edit `shorts.json`, then run `python3 build.py` and render again (`cd car && npm run render`).

## Before posting

- **Link.** Put `https://deeper.tools/?ref=tiktok` in the bio. Signups from it are saved with source `tiktok`. TikTok only gives personal accounts a bio link at 1,000 followers; a business account gets one straight away. Until then, say "deeper.tools" out loud or in the caption.
- **Sound.** The files are silent. Add a quiet track in TikTok's editor. Business accounts can only use the Commercial Music Library.
- **Order.** Post the strongest hooks first: car, then vercel, then blind. One a day, so each gets its own 48-hour window.

## The six

| File | Hook on frame 0 | Caption | Hashtags |
|---|---|---|---|
| `renders/deeper-car.mp4` | Asking AI to sell your car? | My prompt was one line. Here's what a car dealer would have added. | #claudecode #aitools #promptengineering |
| `renders/deeper-vercel.mp4` | Leaving Vercel? Ask it like this. | The prompt a platform engineer would write before moving a Next.js app. | #nextjs #cloudflare #claudecode |
| `renders/deeper-blind.mp4` | We tested it blind. | Five real tasks, scored by a judge on another model. Every prompt is on GitHub. | #claudecode #codex #aitools |
| `renders/deeper-downloads.mp4` | Even this has an expert version. | "Tidy my Downloads folder" is where people lose the only copy of a contract. | #claudecode #macos #aitools |
| `renders/deeper-book.mp4` | "The margins look too big." Do they? | What a book typographer checks before touching a margin. | #selfpublishing #typography #aitools |
| `renders/deeper-scope.mp4` | Version 1.0 had a problem. | It kept adding work I hadn't asked for. 1.1 fixes that, and the numbers are public. | #claudecode #buildinpublic #aitools |

## What to read after 48 hours

TikTok Studio → the video → Analytics. Copy these into the table below.

- **Retention at 2 s.** From the retention curve. This tells you whether the hook worked. Under half means change the hook, not the video.
- **Watched full video (%).** Whether the payoff landed.
- **Profile views.** Whether people wanted more.
- **Signups.** Run this in `site/`:
  `npx wrangler d1 execute deeper-list --remote --command "SELECT date(created_at) d, COUNT(*) n FROM signups WHERE source='tiktok' GROUP BY d"`
- **GitHub views and clones.** Run `scripts/traffic-snapshot.sh`. If TikTok sends people there, it shows up among the referrers.

| Video | Posted | 2 s retention | Full watch % | Profile views | Signups (tiktok) |
|---|---|---|---|---|---|
| car | | | | | |
| vercel | | | | | |
| blind | | | | | |
| downloads | | | | | |
| book | | | | | |
| scope | | | | | |
