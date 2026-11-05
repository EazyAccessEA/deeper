# TikTok (@deepertools): operations plan

**Runs on:** Hermes in the `hermes` container on Hetzner for the planning and reporting. **You post from the TikTok app.**

## Why the agent doesn't post

Apps that haven't passed TikTok's audit can only post privately: only a handful of users a day, all on private accounts. TikTok's guidelines also say apps made only for internal use don't qualify for the audit. So a posting agent would never reach the public. The agent gets everything ready and you press Post.

## The job

Each day, tell you which short is next and give you the caption and hashtags from `marketing/tiktok/POSTING.md`. After 48 hours, ask you for the numbers, then add them to the report.

## Cadence

| When | What |
|---|---|
| Daily, 12:00 UK, for 6 days | Telegram: "Today: deeper-<name>.mp4", the caption, the hashtags, and "turn on Content disclosure → Your brand", which labels it Promotional content as TikTok expects for your own product. Order: car, cover, blind, downloads, book, honey |
| 48 h after each post | Telegram: asks for retention at 2 s, % watched in full and profile views from TikTok Studio |
| Mon, 08:00 | weekly report |

## API and access

- **None for posting.** The Content Posting API's `video.upload` scope (sends a video to your drafts) also needs an approved app. Revisit it if TikTok becomes a main channel.
- **No token is stored.** The agent reads only the repo and D1.

## Tools

- `marketing/tiktok/POSTING.md` and `renders/` from the repo. The agent sends the file's name, never the file itself.
- Signup counts for `tiktok` from a counts-only endpoint on the worker (see README). The container never gets a wrangler login or any access to the signups table.
- `scripts/traffic-snapshot.sh` for GitHub traffic on posting days.

## Alone, or with you

| The agent does it alone | You do it |
|---|---|
| reminders, captions, reports | posting, replying to comments, the profile |

## Cost

$0 for the API, $0 extra for compute, and a few model calls a week.

## Weekly report

For each short: the numbers you sent, signups with `source='tiktok'` in its first 48 hours, and how its 2-second retention compares with the others. POSTING.md says under half at 2 s means the opening frame needs changing.

## Dry run before going live

1. The agent sends today's reminder to Telegram. Pass: it arrives, and the file name and caption match POSTING.md word for word.
2. The agent asks the counts endpoint for `tiktok`. Pass: it returns a number (0 is fine) and nothing else.
3. No token exists to revoke. Check that the container has no TikTok credential: `grep -ri tiktok` over Hermes' secret store finds nothing.
