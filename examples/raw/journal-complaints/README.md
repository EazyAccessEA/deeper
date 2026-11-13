# Journal test: what bugs people about AI assistants, and what doesn't

Pre-registered 13 November 2026, before any review was collected. This file, `codebook.json` and `collect.py` are frozen by the SHA-256 hashes in `FROZEN.txt`. After that, only the "Deviations" and "Results" sections may change.

## Question

When people who use AI assistant apps are unhappy enough to leave a 1- or 2-star review, what are they unhappy about? And when they're happy enough to leave 5 stars, do they praise the very things researchers warn about?

## Source

Apple App Store customer reviews, US store, through Apple's public review feed (`itunes.apple.com/us/rss/customerreviews/.../sortby=mostrecent/json`, pages 1 to 10, up to 500 most recent reviews per app). Four apps:

| App | App Store id |
|---|---|
| ChatGPT | 6448311069 |
| Claude by Anthropic | 6473753684 |
| Google Gemini | 6477489729 |
| Microsoft Copilot | 541164041 |

Why this source: it is where people who are not developers say what they think, and it is open to read. Reddit was planned and dropped before collection: its anonymous endpoints return 403, and logging in to get round that isn't something this study does. Hacker News and GitHub issues were dropped too, because their users are mostly developers and the journal's readers are anyone who uses an assistant.

Stored per review: our id, app, star rating, date, title, text, and Apple's review id. Usernames are not stored. `collect.py` fails if any stored field is named for or contains the reviewer's name.

(Correction, after the run: that check only looked at the id and date fields, never the title or text, so it could not catch a name a reviewer wrote into their own review. One review outside the sample does carry a first name, a town and health details. See Deviations 4.)

## Sample

- **Complaint pool:** every 1- and 2-star review collected. Random sample of 60 per app (all of them if fewer), seed 20261113. Target 240.
- **Praise pool:** every 5-star review collected. Random sample of 30 per app, same seed. Target 120.

## Coding

Each review gets exactly one label, its main subject, from the codebook in `codebook.json`: complaint codes C1 to C10 for the complaint pool, praise codes P1 to P8 for the praise pool. Where a review names two things, the one it spends most words on wins; on a tie, the first one named.

Two coders work independently and never see each other's labels:

- **Coder A:** a Claude model, given only the codebook and the reviews.
- **Coder B:** GPT through `codex exec` in an empty read-only folder, given the same.

Reviews go to each coder in batches, in a different random order for each coder.

Disagreements are settled by a third pass: a fresh Claude call that sees the review, the codebook and both labels, and must pick one of the two. The headline numbers use the settled labels, and the agreement figures are reported before settling.

## Pass marks, fixed now

- **Agreement:** Cohen's kappa between coders, reported separately for each pool. 0.70 or above passes. Between 0.60 and 0.70, the article reports the finding as weak. Below 0.60 is a fail: the article says the categories couldn't be coded reliably, and makes no ranking claim.
- **Top complaint:** a category is called "the top complaint" only if its 95% Wilson interval doesn't overlap the runner-up's. Otherwise the article calls it a tie between them.
- **Per app:** shares are also reported for each app. A pattern seen in only one app is described as one app's pattern.
- **Expert gap:** the expert-side list (what research and vendors warn users about) is written before the coded results are read, in `expert-warnings.md`. Each warning is mapped to a code. A warning is "quiet" if its code holds under 5% of complaints.

## Limits known in advance

- App Store reviews skew to the extremes and to mobile users. They are not a survey.
- One store, one country, a few days or weeks of reviews per app depending on volume. The busiest apps' 500 reviews cover the shortest time.
- Both coders are AI models. Kappa checks them against each other, not against people.
- The codebook was written by deeper's author before reading the sample, from general knowledge of what people complain about.

## Files

- `codebook.json`: the codes.
- `collect.py`: collection and sampling.
- `code.py`: the coding calls.
- `score.py`: kappa, shares and intervals.
- `data/`: the reviews and the samples.
- `codes/`: each coder's labels and the settled labels.
- `expert-warnings.md`: the expert side.

## Deviations

1. **13 November 2026, after App Store collection, before any coding or Reddit collection: Reddit added back as a second source.** Abu Aaliyah opened Reddit in their own logged-in browser, so it can be read without getting round a block. Read-only: nothing is posted, voted or changed. Method, fixed before collection: the `/new.json` listing of r/ChatGPT, r/ClaudeAI, r/GeminiAI and r/CopilotPro, read through that browser, posts from the last 30 days, title and body only, no usernames. Random sample of 40 posts per subreddit, seed 20261113. Reddit posts aren't all complaints, so the Reddit pool gets one extra code, **C0: not a complaint**, and its shares are worked out over the posts that aren't C0. Reddit is reported separately from the App Store, never pooled. Coding, settling and pass marks are as for the App Store pools.
2. **Reddit dropped again, the same day, before a single post was read.** The browser tool refused reddit.com as a restricted site. Getting round that refusal isn't something this study does either, so this study has one source: the App Store. Nothing from Reddit was collected.
3. **Complaint pool is 211, not 240.** Gemini had 31 one- and two-star reviews among its 500 most recent, so all 31 were taken. The other three apps gave 60 each.
4. **Review text is not published.** After the run, a review check found a first name, a town and medication details in one stored review, and Apple's review text isn't ours to republish. `data/reviews.json` and `data/samples.json` stay on the author's machine and are in `.gitignore`. The public folder has `data/sample-ids.json` (our id, app, Apple's review id, stars, date) with every code. `collect.py` can fetch again, but Apple's feed moves, so a re-run will get newer reviews. The article quotes a handful of reviews, each under 15 words, with no names.
5. **The GPT coder's model was not pinned.** `codex exec` used its default model on 13 November 2026. Coder A (Claude Sonnet 5.5) and the settler (Claude Opus 5.5) are Anthropic models, and one of the four apps is Anthropic's. The author builds tools on Claude.
6. **App id 541164041 was Microsoft's Bing app before it became Microsoft Copilot.** The 500 reviews collected are all from 11 October to 11 November 2026, after the change.
7. **Exploratory checks, done after the main results were in, not planned:** a keyword search (`keywords.py`, with its terms) and the author's reading of the C9 and C8 reviews. They are labelled as exploratory everywhere they're used.
8. **The settled labels are kept as coded,** even where reading them later suggests another code. Two C9 reviews (wrong canning information; a scam link) are arguably C3. Recoding after seeing the results would be moving the goalposts, so they're left alone and noted here.

## Results

Run on 13 November 2026. 2,000 reviews were collected: 623 with one or two stars and 1,210 with five. Coding needed no retries (`codes/log.txt` is empty). `python3 score.py` prints everything below from `codes/` and `data/sample-ids.json`. The settled labels are in `codes/settled-*.json`, and each coder's own labels are in `codes/claude-*.json` and `codes/gpt-*.json`.

**Date range per app:** ChatGPT 9 to 11 November, Gemini 8 to 11 November, Claude 15 October to 11 November, Copilot 11 October to 11 November. Copilot supplied 317 of the 623 low-star reviews.

**Agreement (pre-registered pass mark 0.70):**

| Pool | n | Agreement | Kappa | Verdict |
|---|---|---|---|---|
| Complaints | 211 | 85.3% | 0.832 | pass |
| Praise | 120 | 89.2% | 0.841 | pass |

**Complaints, settled labels, with 95% Wilson intervals:**

| Code | n | Share | Interval | Claude coder | GPT coder | Equal-weight mean of the 4 apps |
|---|---|---|---|---|---|---|
| C1 Limits and money | 44 | 20.9% | 15.9 to 26.8 | 41 | 48 | 19.1% |
| C10 Other | 32 | 15.2% | 11.0 to 20.6 | 30 | 31 | 17.6% |
| C5 App broken | 31 | 14.7% | 10.5 to 20.1 | 30 | 33 | 14.9% |
| C9 Trust in the company | 24 | 11.4% | 7.8 to 16.4 | 24 | 22 | 10.0% |
| C6 Got worse | 23 | 10.9% | 7.4 to 15.8 | 22 | 19 | 9.6% |
| C7 Ignores instructions | 19 | 9.0% | 5.8 to 13.6 | 20 | 18 | 9.9% |
| C3 Wrong or made up | 13 | 6.2% | 3.6 to 10.3 | 15 | 16 | 7.4% |
| C4 Forgets or loses things | 11 | 5.2% | 2.9 to 9.1 | 11 | 11 | 5.0% |
| C2 Refusals | 10 | 4.7% | 2.6 to 8.5 | 13 | 9 | 4.6% |
| C8 Tone | 4 | 1.9% | 0.7 to 4.8 | 5 | 4 | 2.0% |

**Top complaint, by the pre-registered rule: a tie.** C1's interval overlaps C10's, C5's and C9's. The pooled sample is stratified (Gemini 31, the others 60), so the per-app shares and the equal-weight mean are the fairer read, and they give the same order at the top. C1's lead rests on two events: 18 of the 44 C1 reviews are Copilot's, mostly new limits after its move to a new app, and ChatGPT's were mostly on 10 November, about paying to upload photos. Without Copilot, C1 is 26 of 151, 17.2%.

**Per app (percentage of that app's complaint sample):** Copilot C1 30.0, C6 28.3, C5 18.3, C4 13.3, so 58% of its complaints are limits or "got worse", one migration story split over two codes. Claude C9 26.7, mostly account bans and ID checks. Gemini C10 35.5 (n = 31). ChatGPT C1 20.0.

**Praise:**

| Code | n | Share | Interval | Claude coder | GPT coder |
|---|---|---|---|---|---|
| P8 Other or generic | 62 | 51.7% | 42.8 to 60.4 | 62 | 55 |
| P1 Gets things done | 31 | 25.8% | 18.8 to 34.3 | 30 | 33 |
| P3 Company and comfort | 8 | 6.7% | 3.4 to 12.6 | 9 | 10 |
| P6 Trust in its accuracy | 6 | 5.0% | 2.3 to 10.5 | 7 | 6 |
| P5 Advice for big decisions | 5 | 4.2% | 1.8 to 9.4 | 4 | 5 |
| P2 Learning | 4 | 3.3% | 1.3 to 8.3 | 4 | 5 |
| P7 Creative and fun | 4 | 3.3% | 1.3 to 8.3 | 3 | 5 |
| P4 Agrees and encourages | 0 | 0.0% | 0.0 to 3.1 | 1 | 1 |

Each coder used P4 once, on different reviews, and the settler overruled both. Of the five P5 reviews, two are about buying a car, two call it a life adviser, and one is about health. One of the six P6 reviews says the opposite of over-reliance ("use it as a tool and not as your only source").

**Expert gap.** "Rarely named" means under 5% of complaints. It measures what reviewers write about, not how often a harm happens, and harms that feel pleasant or go unnoticed would be rarely named whether or not they happen.

- **W1 sycophancy: rarely named.** C8 is 4 of 211, and on reading, none of the 4 is about flattery: two complain about the opposite, an assistant that argues back. Two reviews coded C3 do describe it, as lying to make you feel better or saying what you want to hear. Exploratory keyword search (`keywords.py`): 3 low-star matches of 623, two of them those same reviews and one a false hit. 0 of 120 five-star reviews praise agreeableness.
- **W2, W3, W6 wrong answers: 6.2% (3.6 to 10.3).** The interval crosses 5%, so it's neither clearly quiet nor clearly loud.
- **W5 privacy: the 11.4% is not a privacy figure.** C9 also holds bans, ID checks, politics, region blocks and water use. On reading, none of the 24 is about chats being used for training. Exploratory keyword search: 0 of 623 low-star reviews and 0 of 1,210 five-star reviews mention training on chats. Read honestly, W5 is rarely named.
- **W4 emotional dependence:** 8 of 120 five-star reviews (6.7%) praise it as a friend, companion or partner.

**Red-team review.** A separate agent read the folder before the article was written and checked the scripts. It confirmed the Wilson and kappa code, the hashes, and that the settler picked the Claude coder's label in 12 of 31 complaint disagreements and 8 of 13 praise disagreements. Its findings led to Deviations 4 to 8 and to the corrections above (C8's content, W5, the pooled-sample caveat, the P5 and P6 descriptions).
