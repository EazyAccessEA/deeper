# TikTok shorts for deeper

Six vertical launch shorts, 1080×1920, 39–45 s each, voiced. Each opens on a finished colour illustration and cuts to a sparse pencil sketch: your plain request. Then `/deeper` runs, the four questions appear, and each part of the scene takes on colour as deeper's real insertion for that task is said. Every insertion comes from `examples/raw/v1.1/final.md`; the blind-test numbers come from the README.

## Files

`renders/deeper-<name>.mp4`: car, vercel, downloads, book, honey, blind.

To change a line or a picture, see "Rebuilding" at the end.

## Before posting

- **Link.** Put `https://deeper.tools/?ref=tiktok` in the bio. Signups from it are stored with source `tiktok`. A personal account only gets a bio link at 1,000 followers; a business account gets one straight away.
- **Sound.** The voice and soft brush sounds are in the file. Add a quiet music bed in TikTok's editor if you like, kept low under the voice. Business accounts can only use the Commercial Music Library.
- **Captions.** They're burned in. Turn off TikTok's auto-captions so they don't stack.
- **Order.** One a day, so each gets its own 48 hours: car, vercel, blind, downloads, book, honey.

## Captions and tags

| File | Caption | Hashtags |
|---|---|---|
| deeper-car.mp4 | My agent's version of "sell my car" was a sketch. Here's the one a dealer would draw. | #claudecode #aitools #promptengineering |
| deeper-vercel.mp4 | What a platform engineer asks before moving a Next.js app off Vercel. | #nextjs #cloudflare #claudecode |
| deeper-blind.mp4 | Five real tasks, scored by a judge on another model. Every prompt is on GitHub. | #claudecode #codex #aitools |
| deeper-downloads.mp4 | "Tidy my Downloads" is how people lose the only copy of a contract. | #claudecode #macos #aitools |
| deeper-book.mp4 | What a book typographer checks before touching a margin. | #selfpublishing #typography #aitools |
| deeper-honey.mp4 | deeper works on any task. Here it is on one Instagram caption. | #smallbusiness #copywriting #aitools |

## What to read after 48 hours

TikTok Studio → the video → Analytics:

- **Retention at 2 s**, from the retention curve. Under half means the opening frame isn't stopping people.
- **Watched full video (%).** Whether the colour reveal holds them to the end card.
- **Profile views.**
- **Signups.** In `site/`: `npx wrangler d1 execute deeper-list --remote --command "SELECT date(created_at) d, COUNT(*) n FROM signups WHERE source='tiktok' GROUP BY d"`
- **GitHub traffic.** Run `scripts/traffic-snapshot.sh`.

| Video | Posted | 2 s retention | Full watch % | Profile views | Signups (tiktok) |
|---|---|---|---|---|---|
| car | | | | | |
| vercel | | | | | |
| blind | | | | | |
| downloads | | | | | |
| book | | | | | |
| honey | | | | | |

## How they're made

| Step | Script | Tool |
|---|---|---|
| Colour scene, and the same scene with deeper's additions edited out | `illustrate.py colour|sparse <name> 1` | GPT Image 2 on Runware, through Harvalor's key and its Vision text and face checks |
| Pencil frames, matched pixel for pixel to the colour | `pencil.py` | OpenCV |
| One mask per insertion: what changed between the two scenes, inside that object's box | `stages.py <name> 1` | OpenCV |
| Voice, one file per line | `voice.py <name>` | VoxCPM2, from the YouTube project, with a designed voice (not a clone) |
| Each line checked against its text | `check_voice.py <name>` | Whisper large-v3, offline |
| Picture track: cuts per line, colour painting in strokes | `film.py <name> 1` | numpy and ffmpeg |
| Everything on screen and in the mix, laid on the picture | `compose.py <name>`, then `npm run render` in its folder | HyperFrames 0.8.173 |
| Loudness to −14 LUFS | ffmpeg `loudnorm` | |

Scene prompts and object boxes are in `scenes.json`; every spoken line and caption is in `scripts.json`. Runware costs per job are in `runware_jobs.json`.

## Rebuilding

The images, voice files, projects and renders are not in git. Rebuild a short with the steps above, in order.
