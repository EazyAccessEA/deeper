## T1

```text
Write one Instagram caption for our jar of borage honey, the way a specialist food copywriter would.

Before writing, ask me for and work only from the primary material: the jar's label, the photo the caption will go under, the beekeeper's harvest notes (where, when, which hives), the pollen analysis (melissopalynology) certificate if we have one, and our last 10-20 posts with their Instagram Insights (reach, saves, shares). Check the pollen analysis before calling it borage honey: if it doesn't show borage as the dominant pollen, say so and don't make the claim.

Method:
- Build the hook from one concrete, checkable sensory or origin fact about this honey (colour, taste, texture, crystallisation, the field it came from), not from adjectives.
- Put the hook and the reason to care inside the first 125 characters, the part that shows before "more" on a phone.
- Match the voice and length of our best-performing past posts by saves and shares, not by likes.
- Choose hashtags from Instagram's own search (post counts, recent top posts), a few niche ones over many broad ones.
- No health or medicinal claims (EU Regulation 1924/2006), and every floral-origin or regional claim must be backed by the label or the pollen analysis (EU Honey Directive 2001/110/EC).

Skills and agents: none are installed in this setting; if you're running somewhere that has copywriting or Instagram-caption skills, use them.

Checks, with pass marks:
- Paste the caption into a phone preview (or count characters) and confirm the hook and call to action sit before the truncation point. Fail if they don't.
- List every factual claim next to the document that backs it. Fail if any claim has no source.
- After posting, compare saves and reach against the median of our last 10 posts at 48 hours. Pass at or above the median; below it counts as a fail.

Deliverable: one caption, nothing else.
```

## T2

```text
Evaluate the typesetting of my book manuscript and improve it, the way a professional book typographer would. I think the inner margins are exceedingly large; treat that as a hypothesis to test, not a fact.

Start from the primary material, and ask me for anything missing: the print PDF and the source layout file (InDesign, Affinity, LaTeX or Word), the trim size, final page count, paper stock and binding method (perfect-bound, sewn, wire), and the printer's specification sheet (gutter/binding allowance, bleed, safe zone).

Method:
- Judge margins on two-page spreads, never single pages. Check whether the "large inner margin" is real or an artefact of viewing single pages or a binding offset. Then set the margins against a classical proportion (for example Tschichold/Van de Graaf, inner:top:outer:bottom near 2:3:4:6) adjusted for the binding loss at this page count and binding, using the printer's gutter allowance.
- Measure, don't eyeball: characters per line (target 45-75, about 66), leading relative to type size, baseline grid alignment across facing pages, widows, orphans, runts, rivers, consecutive hyphens, and stacked word breaks.
- Make the fixes in the layout file itself (master pages, paragraph styles, hyphenation and justification settings), not by hand on individual pages.

Tools: the layout software itself, Acrobat Preflight and Output Preview against the printer's spec, a ruler and a printed proof. Skills and agents: none are installed in this setting; if you're running somewhere that has typography or PDF skills, use them.

Checks, with pass marks:
- Preflight against the printer's profile: zero errors. Any error is a fail.
- A printed proof at 100% on the actual trim size, folded or bound as close to the final binding as possible: no text lost into the gutter on any spread, the text block visually centred on the open spread. Text in the gutter is a fail.
- A before/after table of the measurements above. Fail if any measure is outside the target range without a stated reason.
- If possible, a review by a book designer or the printer's prepress team.

Deliverables: an evaluation of the current typesetting, and the improved typesetting of the manuscript. Nothing else.
```

## T3

```text
Help me sell my VW Polo and buy its replacement, possibly a Golf, the way an experienced car dealer or independent buyer's agent would.

Keep the two deals separate: price the Polo and the replacement independently so a trade-in can't hide a poor discount, and decide which car to buy from my actual use and total cost of ownership, not from the model name.

Start from the primary material, and ask me for what's missing: the Polo's registration documents (in Germany, Zulassungsbescheinigung Teil I and II), exact model year, engine, trim, mileage, service book, last inspection (HU/TÜV) report, accident and repair history, and what's wrong with it. For the replacement: my real usage (km per year, typical trips, passengers, luggage, parking, fuel receipts) and my budget. Test whether "a Golf is the right replacement" holds against that usage data, and say plainly if it doesn't.

Method and tools:
- Value the Polo from comparable listings of the same spec on mobile.de and AutoScout24 (or the local equivalents), plus a DAT/Schwacke valuation, plus at least two binding instant-buy offers as the price floor.
- For the purchase, compare candidates in a total-cost-of-ownership spreadsheet over my planned holding period: price, expected depreciation, insurance quotes, vehicle tax, fuel, servicing.
- For any used candidate: a VIN/history check and an independent pre-purchase inspection (DEKRA, TÜV, ADAC or a trusted independent garage).
- Use a standard written sale contract (for example the ADAC private-sale contract) for both deals.

Skills and agents: none are installed in this setting; if you're running somewhere that has relevant skills or agents, use them.

Checks, with pass marks:
- Polo sale: agreed price at or above the best binding instant-buy offer and within the range of comparable listings after typical negotiation. Selling below the best binding offer is a fail.
- Purchase: price at or below the median of comparable listings for that spec, independent inspection passed, TCO computed. Buying a used car without an independent inspection is a fail.

Deliverables: the Polo sold and a replacement car bought. Nothing else.
```

## T4

```text
Tell me whether we can move our Next.js app off Vercel to Cloudflare, and what it would take, the way a platform engineer who has done this migration would.

Start from the primary material: the repository. Read package.json (exact Next.js version and every @vercel/* dependency), next.config, vercel.json, middleware, every route handler and page that sets `export const runtime`, and any use of ISR/revalidate, next/image, cron jobs, Vercel KV/Blob/Postgres, Edge Config, analytics or OG image generation. Also the Vercel project settings and environment variables, recent build logs, and our usage and bill. If any of these isn't available to you, ask me for it. Test the assumption that the app has no hidden Vercel dependencies, and the assumption that Cloudflare would cost less, against this material.

Method and tools:
- Build a feature inventory: every Vercel feature we actually use, mapped to its Cloudflare equivalent through the OpenNext adapter (@opennextjs/cloudflare) on Workers, or marked "no equivalent" with the workaround.
- Check compatibility of our Next.js version with the adapter, Node APIs under the `nodejs_compat` flag, and the Worker bundle size limit on our plan.
- Prove it rather than reason about it: build the app with @opennextjs/cloudflare, run it locally in workerd with the adapter's preview command, then deploy it to a throwaway workers.dev preview.

Skills and agents: none are installed in this setting, and I can't run commands here; if you're running somewhere that has Cloudflare, Wrangler or Next.js skills and a shell, use them.

Checks, with pass marks:
- Our existing test suite (unit and end-to-end) passes against the Cloudflare preview. Any failure that passes on Vercel is a fail.
- A route-by-route comparison of the preview against Vercel production: status codes, redirects, headers, cache behaviour and rendered output. Any unexplained difference is a fail.
- The compressed Worker bundle is under the plan's size limit.
- Every Vercel feature in the inventory has a working mapping or an accepted workaround. An unmapped feature means the answer is "not yet", with the blocker named.

Deliverable: a yes / no / not yet answer with what it would take, backed by the inventory and the checks above. Tear down the preview afterwards. Nothing else.
```

## T5

```text
Tidy my Downloads folder, the way a careful sysadmin or records manager would: look at everything before moving anything, and make every step reversible.

Start from the folder itself, not from impressions. If you can't read it, ask me for a listing (`ls -laR ~/Downloads` plus `du -sh ~/Downloads/*`). Build an inventory: every file with type, size, date added, and on macOS where it was downloaded from (the kMDItemWhereFroms attribute via `mdls`). Test the assumption that the folder is mostly junk: check what actually takes the space (usually a few large files) and which files exist nowhere else.

Method and tools:
- Find exact duplicates by content hash (`shasum` or jdupes), not by name.
- Triage each file by where it belongs, not by extension: installers (.dmg, .pkg) for apps already installed go to the Trash; documents and originals that exist only here go to their proper home folders; anything uncertain goes to a "To review" folder.
- Use Finder and the Trash, never `rm`. Nothing is permanently deleted.
- Show me the proposed moves as a list and get my yes before executing them.

Skills and agents: none are installed in this setting, and I can't run commands here; if you're running somewhere that has a shell, use it.

Checks, with pass marks:
- Account for every file: the count before must equal kept + moved + trashed. Any file unaccounted for is a fail.
- Zero files permanently deleted; everything trashed is restorable. A permanent deletion is a fail.
- Before/after size and file count for Downloads.
- I spot-check 10 randomly chosen moved files and find each where you say it is.

Deliverable: a tidied Downloads folder. Nothing else.
```
