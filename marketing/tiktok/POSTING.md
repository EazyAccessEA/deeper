# TikTok shorts for deeper

Six vertical launch shorts, 1080×1920, about 40 s each, voiced, for anyone who uses an AI assistant. Each opens on a finished colour illustration ("Ask AI like an expert, and you get the full picture") and cuts to a sparse pencil sketch: the prompt most of us type. Then it says what deeper is in one sentence, the four things an expert thinks of appear, and each part of the scene takes on colour as deeper's real addition is said in plain words. It ends on "Get it free at deeper dot tools", with the three steps on screen: copy deeper's instructions at deeper.tools/start, paste them into ChatGPT, Claude or Gemini, type /deeper and your prompt.

Every addition comes from a real deeper run: `examples/raw/v1.1/final.md` for car, downloads, book and honey, and a fresh run on a cover-letter request for cover. The blind-test numbers come from the README.

## Files

`renders/deeper-<name>.mp4`: car, cover, blind, downloads, book, honey.

To change a line or a picture, see "Rebuilding" at the end.

## Before posting

- **Link.** Put `https://deeper.tools/?ref=tiktok` in the bio. Signups from it are stored with source `tiktok`. A personal account only gets a bio link at 1,000 followers; a business account gets one straight away.
- **Sound.** The voice and soft brush sounds are in the file. Add a quiet music bed in TikTok's editor if you like, kept low under the voice. Business accounts can only use the Commercial Music Library.
- **Captions.** They're burned in. Turn off TikTok's auto-captions so they don't stack.
- **Order.** One a day, so each gets its own 48 hours: car, cover, blind, downloads, book, honey.

## Captions and tags

| File | Caption | Hashtags |
|---|---|---|
| deeper-car.mp4 | "Sell my car" gets you a sketch. Here's the prompt a car dealer would write. | #chatgpt #aitips #promptengineering |
| deeper-cover.mp4 | What a hiring manager would ask your AI before it writes your cover letter. | #coverletter #jobsearch #chatgpt |
| deeper-blind.mp4 | Five real requests, asked plainly and with deeper, marked blind. Every one is public: github.com/EazyAccessEA/deeper | #chatgpt #aitools #ai |
| deeper-downloads.mp4 | "Tidy my Downloads" is how people lose the only copy of a contract. | #chatgpt #productivity #aitips |
| deeper-book.mp4 | What a book designer checks before touching a margin. | #selfpublishing #booktok #aitools |
| deeper-honey.mp4 | One honey caption, prompted the way a food copywriter would. | #smallbusiness #copywriting #chatgpt |

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
| cover | | | | | |
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
| Plain-language check: can someone who doesn't code explain it after one watch? | `teachback.py <label> [name]` | Codex, as a blind reader; answers in `teachback/` |
| Voice, one file per line | `voice.py <name>` | VoxCPM2, from the YouTube project, with a designed voice (not a clone) |
| Each line checked against its text | `check_voice.py <name>` | Whisper large-v3, offline |
| Picture track: cuts per line, colour painting in strokes | `film.py <name> 1` | numpy and ffmpeg |
| Everything on screen and in the mix, laid on the picture | `compose.py <name>`, then `npm run render` in its folder | HyperFrames 0.8.173 |
| Loudness to −14 LUFS | ffmpeg `loudnorm` | |

Scene prompts and object boxes are in `scenes.json`; every spoken line and caption is in `scripts.json`. Runware costs per job are in `runware_jobs.json`.

## Plain-language test

A Codex reader playing an adult who uses ChatGPT and doesn't code got only one short's words and answered: what is it, what does it do, who is it for, what would you do next. The first copy scored 17/24 ("who is it for" failed on 5 of 6: it read as a tool for coders). The current copy scores 23/24: cover's reader puts the expert part under "what is it" instead of "what does it do". Both slopmonster judges find no faults in any script. The "who is it for" pattern was widened twice during testing to accept right answers worded differently ("people who want … AI answers", "people using …"); both changes are marked in `teachback.py`. Answers for every round are in `teachback/`.

## Rebuilding

The images, voice files, projects and renders are not in git. Rebuild a short with the steps above, in order.
