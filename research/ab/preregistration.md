# A/B test pre-registration: deeper.tools home page (Red field)

Status: **draft, 5 Nov 2026. Not launched.** Nothing here may change after launch except the "Result" section.

## What counts as a conversion

deeper is free, so there is no sale. Candidates, with what we can measure today:

| Metric | Per-visitor? | Measurable today | Baseline today |
|---|---|---|---|
| Install-command copy click | yes | no (needs a logged event) | unknown |
| Email signup | yes | yes (D1 `signups`, `source` field) | 0 signups ever (production D1, 5 Nov) |
| GitHub star | no (can't tie to a visitor) | count only | 1 star (GitHub API, 5 Nov) |
| Real install | no (can't tie to a visitor) | count only | 1 install (skills.sh, 5 Nov) |

**Primary metric (confirmed by Abu Aaliyah, 5 Nov 2026):** share of page views that lead to a click on Copy on the install command, or "Copy the skill" on /start/. The unit is the page view, not the person, because the split stores nothing on the device. It's the closest signal to an install that can be counted per view, and the only one frequent enough to test.
**Secondary:** email signup rate. **Guardrails:** Lighthouse mobile performance ≥95, CLS <0.05, bounce of /start/ visits.

## Traffic, honestly

- GitHub: 20 views from 2 unique visitors in 14 days (traffic API, 5 Nov); referrers deeper.tools (1 unique), github.com (1).
- deeper.tools: Cloudflare Web Analytics is on (privacy notice; the CSP allows it). Its visit counts are in the Cloudflare dashboard, which wasn't reachable from this session. It can't count Copy clicks, so `/api/e` counting was added (worker.js, public/count.js, D1 `events`): deployed 5 Nov (version c43188a3). First reading: 3 page views, 0 copies, very likely all three from our own Lighthouse runs (the "Chrome-Lighthouse" user agent isn't in the bot filter). Left as is by decision (5 Nov). The baseline period starts on 6 Nov 2026, and the 5 Nov rows are excluded from analysis. Our own Lighthouse runs on the live site from now on will be counted, so we don't run them during the test.

## Sample size (power.py, two-sided, 80% power)

| Baseline | Lift to detect | 2 arms, α 0.05 | 5 arms, Bonferroni α 0.0125 |
|---|---|---|---|
| 5% | +50% | 2,942 visitors | 10,450 visitors |
| 5% | +100% | 870 | 3,090 |
| 10% | +50% | 1,372 | 4,875 |
| 2% | +50% | 7,652 | 27,175 |

Decision: five variants are **pre-tested with people** (five-second line-up, 5 developers each). Only the two that pass go live, 50/50.

## Hypotheses (one per variant)

| Variant | Hypothesis |
|---|---|
| V1 Headline-first | Because the promise is the product, the poster headline above the fold gets the most copies. (Control: the current D2.) |
| V2 Demo-first | Because developers trust proof over claims, leading with the marked-up example gets more copies than the headline. |
| V3 Evidence-first | Because sceptical developers want numbers, leading with "Best on 4 of 5 blind tasks" and the table gets more copies. |
| V4 Install-first | Because the action is one command, a hero that is almost only the command and Copy gets more copies. |
| V5 Wildcard: chat-first | Because many visitors have no terminal, leading with "Use it in ChatGPT, Claude.ai or Gemini" next to the command widens who converts. |

## Split and consent (compliance review, 5 Nov)

**Proposed: cookieless split.** `worker.js` picks a variant at random for each request and writes it into the served HTML. Nothing is stored on or read from the device, so PECR reg. 6 isn't engaged. Rows logged to D1 are `{variant, day, country}` for each page view and `{variant, day}` for each Copy click, with no IP, user agent or identifier, so they aren't personal data (UK GDPR Art. 4(1), Recital 26). The click beacon sends only the variant already in the HTML. A returning visitor may see a different variant, which adds noise but no bias.

Rejected: a `v` cookie. It needs consent unless the DUAA 2025 statistical exception applies, and that's unconfirmed for A/B assignment. Also rejected: `?v=` links, which only measure signups and tie the variant to a stored email.

Privacy notice to add before launch: "We sometimes show visitors one of two versions of the home page, picked at random each time. We count page views and clicks on the copy button by version, day and country. Nothing is stored on your device, and nothing we count can identify you." Before launch, check this against legislation.gov.uk and the ICO's Storage and Access Technologies guidance.

## Stopping rule

Run until each finalist reaches the planned sample (set once the baseline is measured). No peeking, no early stop except a guardrail breach. If the planned sample isn't reached in 8 weeks, the result is "no winner yet", not a winner.

## Analysis

Two-proportion z-test, two-sided, α 0.05, with the effect size and its 95% interval reported. Reviewed by an independent agent before any decision.

## Result

Not run.
