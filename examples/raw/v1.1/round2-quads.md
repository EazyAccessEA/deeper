## T1
Original task: Write an Instagram caption for a jar of borage honey.

### Prompt A
```text
Write one Instagram caption for a jar of borage honey.

Before writing, ask me for, and build only from, the raw material: photos of this jar and its label, where and when it was harvested, who keeps the bees, how it tastes and pours (in my words or a customer's), any customer messages about it, and the account's last posts with their saves and comments. Do not invent harvest details, sensory claims, health benefits or numbers; if something is missing, ask.

Work like a food copywriter for a small producer: lead with one concrete, specific detail only this honey has (the blue borage flowers, the place, the beekeeper, the light colour or slow crystallisation if I confirm it), so the first line, the part visible before "more", stops the scroll on its own. Write in the voice of my existing posts. End with one plain action (where to buy, or a question people will answer). Hashtags: a few specific ones, after the caption.

Check before handing it over:
- The first line is under about 125 characters and makes sense without the rest.
- Every factual claim traces to something I gave you; mark any that does not.
- Read the caption aloud and to one person who buys from me; if they cannot say what makes this honey different from any other honey, it fails.

Deliver: the one caption, and the list of facts it relies on with their source.
```

### Prompt B
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

### Prompt C
```text
Write one Instagram caption for our jar of borage honey, the way a food copywriter who knows bees and the platform would.

Before writing, ask me for (and wait for) the raw material: the label and its exact wording, the producer's notes on where and when the borage was in flower and how the honey was extracted, any lab or pollen-analysis result, three or four real customer messages or reviews, our last 20 posts with their saves, shares and reach, and the photo this caption will sit under. Don't assume the honey is single-origin borage or "raw" until the label or the pollen report says so; if they don't, the caption must not claim it.

Method:
- Taste-led sensory language (colour, texture, flavour, crystallisation), anchored in one concrete fact about this harvest, not generic "liquid gold" lines.
- Put the hook in the first ~125 characters, before Instagram truncates with "more".
- Make every claim one the label or report supports; no health claims.
- Use 3 to 5 specific hashtags (borage honey, the region, the producer type), not 30 generic ones.
- One call to action that matches where people actually buy it.

No specialist skills or agents are available in this setting; work without them.

Verification:
- Every factual line traced to a document I gave you; any line without a source is cut.
- Character count of the hook stated, under 125.
- Write two variants for an A/B test on the account: post one, then the other a week later at the same time and day, and compare saves and shares per 1,000 reach. The better variant has to beat the account's median of the last 20 posts; if neither does, that counts as a fail.

Give me the caption, the variant, and the source for each claim.
```

### Prompt D
```text
Write an Instagram caption for a jar of borage honey I sell.

About the product (fill in what you can):
- Producer / brand: [name, small beekeeper or brand]
- Where it comes from: [region, farm]
- Taste and look: [e.g. pale, delicate, light floral, slow to crystallise]
- Jar size and price: [e.g. 250 g, £9]
- Where to buy: [link in bio / shop / market stall]
- Audience: [local foodies, gift buyers, honey enthusiasts]
- Brand voice: [warm and homely / clean and premium / playful]

What I want:
- One caption, 60–120 words. The first line has to work on its own, because Instagram cuts the rest off behind "more".
- Say something concrete about borage honey (the blue star-shaped flowers, the light colour, the mild taste) instead of generic "liquid gold" lines.
- Make no health or medical claims.
- End with one clear call to action that matches where people buy it.
- Put 5–10 relevant hashtags on a separate line at the end, mixing niche ones (#boragehoney) with broader ones.
- Use at most two emojis, or none if they don't suit the voice.

Then give me two shorter alternative opening lines I could swap in. If anything above is missing, make a sensible assumption and tell me what you assumed.
```

## T2
Original task: Evaluate the typesetting of my book manuscript and improve it. The inner margins look exceedingly large.

### Prompt A
```text
Evaluate and improve the typesetting of my book manuscript the way a book typographer would. Same scope: the typesetting of this book, not a redesign or an edit of the text.

Start from the raw material, not a description of it. Ask me for and wait for: the source files (InDesign/Affinity/LaTeX/Word, with the fonts), the exported print PDF, the printer's or print-on-demand service's spec sheet (trim size, binding, page count, minimum gutter and safe-zone), and if possible a printed proof. We take as true that the inner margins are too large; check that claim against the binding. On a perfect-bound book, a thick spine eats part of the gutter, so a wide inner margin may be correct. Measure first, then decide.

Method:
- Build the page proportions deliberately. Use a canon (Van de Graaf / Tschichold or the classical 2:3:4:6 margin progression), adjusted for binding loss and page count, and make sure each spread reads as a single unit with the text blocks paired.
- Fix the measure at roughly 45 to 75 characters per line, set leading to the type size and measure, and hold a baseline grid across the book.
- Check the micro-typography: hyphenation and justification settings, rivers, widows and orphans, stacked hyphens, small caps and old-style figures where the text calls for them, real quotes and dashes, and optical margin alignment.
- Work inside the actual layout tool and its paragraph composer, not by eyeballing a PDF.

No specialist skills or agents are available in this setting; work without them.

Verification:
- Measure margins, gutter and measure in mm and characters on the PDF and report them against the printer spec and the chosen canon.
- Run a preflight (Acrobat Preflight or the printer's own checker) for fonts, bleed and safe zones.
- Get a printed proof copy. Pass: no text lost into the gutter when the book is opened normally, zero widows/orphans, no more than two consecutive hyphenated lines, no visible rivers on a random sample of 20 spreads, and the preflight clean. Any one of these failing is a fail.

Report what you found with numbers, what you changed and why, and what still needs my decision.
```

### Prompt B
```text
I'm going to paste in the typesetting details of my book manuscript. Please evaluate them and tell me how to improve them. My main complaint is that the inner margins (the gutter) look far too large.

Details (I'll fill these in):
- Format: [print book / PDF / ebook]
- Trim size: [e.g. 5.5 × 8.5 in, A5]
- Page count: [approx.]
- Binding: [paperback perfect-bound / hardcover / spiral]
- Tool used: [Word, InDesign, Affinity Publisher, LaTeX, Vellum, Atticus...]
- Current margins: inside [ ], outside [ ], top [ ], bottom [ ]
- Body font and size / leading: [e.g. Garamond 11/14]
- Printer or service: [KDP, IngramSpark, local printer]
- Genre: [novel, non-fiction, poetry...]
[Optionally paste a sample page's settings or describe what you see.]

Please:
1. Check whether my inner margin really is too large, given my page count and binding. Explain how gutter needs grow with page count, and give a recommended inside/outside/top/bottom set in the units I use. Mention my printer's minimum if you know it, and say so if you're unsure.
2. Check whether the problem is a setting mistake rather than the value itself. Common ones: mirrored margins not turned on, a gutter added on top of an already wide inner margin, or the spread viewed in the wrong way.
3. Review the rest of the typesetting: font and size, leading, line length (characters per line), justification and hyphenation, widows and orphans, paragraph indents vs. spacing, chapter openings, running heads and page numbers, front matter.
4. Give me a prioritised list of changes, most visible first, each with the exact setting to change and where to find it in my tool.

Don't invent measurements I haven't given you. If something you need is missing, ask me for it before making a recommendation that depends on it.
```

### Prompt C
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

### Prompt D
```text
Evaluate the typesetting of my book manuscript and improve it. I think the inner margins look too large.

Start from the source, not a screenshot: the typesetting file (InDesign, LaTeX, Word, Affinity or whatever I used), the exported PDF, the printer's or print-on-demand specs (trim size, page count, binding, paper, gutter/bleed requirements), and if possible a printed proof. Ask me for anything missing. Test my assumption: the inner margins may only look large on a screen spread; once the pages are bound, part of the gutter disappears into the spine, so they may be right or even too small for this page count and binding.

Work like a book typographer:
- Judge the page as a system: text block proportions and position on the double-page spread, the trim size, the gutter allowance for this binding and thickness, and margins measured in mm on the actual page, rather than shrinking one margin in isolation.
- Then the text itself: measure (characters per line, aiming at roughly 45-75), leading against type size, a baseline grid, hyphenation and justification settings (rivers, loose or tight lines, stacks of hyphens), widows and orphans, headings, folios and running heads, and consistent use of small caps, figures, quotes and dashes.
Use the layout program's own tools and preflight to measure and fix; don't eyeball.

Check:
- The printer's preflight passes (margins/safe area, gutter minimum, fonts embedded, resolution).
- Measured numbers before and after for margins, measure and leading, against the printer's minimums and the typographic ranges above.
- If a printed proof is possible, the open book shows the text block visually centred on the spread with no text lost into the gutter; text running into the fold is a fail.

Deliver: the evaluation, and the improved typesetting in the same file.
```

## T3
Original task: I need to sell my car, a VW Polo, and buy a new one, perhaps a Golf.

### Prompt A
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

### Prompt B
```text
Help me sell my VW Polo and buy my next car, perhaps a Golf, the way an independent car buyer's agent would. Same scope: one sale and one purchase, no fleet strategy.

Ask me for and wait for the raw material first: the Polo's V5C/registration document, full service history and MOT/inspection records, mileage, any finance outstanding, and photos of its condition; for the purchase, my real annual mileage, journeys and must-haves, and my budget including running costs. We take as true that a Golf is the right next car; test that against the numbers. Total cost of ownership may favour a different model, engine or age.

Method:
- Value the Polo from real sold prices for the same model, year, engine and mileage, not asking prices. Compare the trade-in and part-exchange offers (two or three instant-buyer quotes) with a private sale, net of the time and risk involved.
- Prepare it for sale: a short list of cheap fixes that raise the price, a complete document pack, and a safe handover (payment cleared before the keys go).
- For the purchase, work out a total-cost-of-ownership model over my expected holding period (depreciation, fuel, insurance group, tax, servicing, known faults for that engine and year), and compare the Golf against one or two alternatives.
- Before committing to any car, run a history check (finance, write-off, mileage) and an independent pre-purchase inspection. Negotiate on the out-the-door price, not the monthly payment.

No specialist skills or agents are available in this setting; work without them.

Verification:
- Sale: accept no offer below the median of comparable sold prices minus a stated margin for condition. If I go below that, write down why.
- Purchase: the history check is clean and the independent inspection is passed; the chosen car's TCO is lowest, or within 5% of lowest, among the candidates on my numbers. A car that fails either check is a no, whatever the price.

Give me a valuation with its sources, a sale plan, a TCO table, and a shortlist with reasons.
```

### Prompt C
```text
I want to sell my current car, a Volkswagen Polo, and buy a replacement, possibly a VW Golf. Help me plan both sides so I don't lose money or get rushed.

My situation (I'll fill in):
- Country / region: [ ]
- My Polo: year [ ], engine/fuel [ ], trim [ ], mileage [ ], gearbox [ ], condition and any faults [ ], service history [full / partial], outstanding finance [yes/no]
- Budget for the next car, including what I get for the Polo: [ ]
- Paying by: [cash / finance / lease]
- What I need the car for: [commute distance, family size, motorway vs city, parking]
- Must-haves: [ ]
- New or used: [ ]
- Timeline: [ ]

Please give me:
1. How to sell the Polo: the options (private sale, dealer part-exchange, online instant-buy services), with typical pros, cons and price gaps for each; how to estimate a realistic asking price myself; what paperwork and preparation I need; and how to avoid common scams in private sales.
2. Whether the Golf is a good fit for my needs and budget, which model years, engines and trims to look at or avoid, known issues to check, and two or three alternative cars worth comparing.
3. A checklist for viewing and test-driving a used car, plus what to check in its documents and history.
4. The order to do things in (sell first, buy first, or part-exchange) given my situation, and how to negotiate on both deals.

Be clear about which figures are rough estimates that I should check on local listing and valuation sites. Don't present a guessed price as fact. If my details are missing, ask the three or four questions that matter most before going deep.
```

### Prompt D
```text
Help me sell my VW Polo and buy the next car, perhaps a Golf. Ask me for what you need rather than assuming.

Raw material first, before any price: the Polo's registration document, service book and invoices, last inspection report, exact mileage, outstanding finance, known faults; then my real use (annual mileage, typical trips, passengers, parking, charging access) and my budget including running costs. Also live, comparable listings for my Polo (same model year, engine, trim, mileage, in my region) and for the candidate replacements. Test the assumption that the Golf is the right car: my usage figures may point to something else, or to keeping the Polo.

Work like a careful car buyer and seller:
- Sell: set the price from actual comparable listings and a dealer trade-in or instant-buy quote, not a single online valuation; compare private sale against trade-in net of time and risk; present the documented service history.
- Buy: compare candidates on total cost of ownership over the years I expect to keep it (purchase, depreciation, insurance, tax, fuel or charging, maintenance), check the specific engine and model year for known faults and recalls, and require an independent pre-purchase inspection and a vehicle history check before paying.
Use a spreadsheet for the cost comparison.

Check:
- The sale price sits within the range of at least five comparable listings, and the gap to the best trade-in quote is stated.
- The chosen car has a clean history check and passes an independent inspection; a failed inspection or an unexplained gap in history means walk away.
- The total cost of ownership of the chosen car is within my budget.

Deliver: a plan for selling the Polo, and a recommended replacement with the reasons.
```

## T4
Original task: Can we move our Next.js app off Vercel to Cloudflare?

### Prompt A
```text
Can we move our Next.js app off Vercel to Cloudflare? Answer that question, with a migration plan if the answer is yes.

Start from the code and the account, not the docs: package.json and the Next.js version, next.config, middleware, route handlers, which pages use SSR, ISR, static export, edge or Node runtime, image optimisation, and every Vercel-specific dependency (@vercel/* packages, KV, Postgres, Blob, Edge Config, cron, analytics, environment variables, domains). Pull the last month of Vercel usage and logs for traffic and function duration. Test the assumption that the app runs on Workers as is: Node-only APIs, native modules, bundle size limits or ISR behaviour may say otherwise.

Work like a platform engineer:
- Use the OpenNext Cloudflare adapter (@opennextjs/cloudflare) on Workers, not the older next-on-pages, and map each Vercel feature to its Cloudflare counterpart (R2 for blob and incremental cache, KV/D1/Hyperdrive, Cron Triggers, Images) or flag it as a blocker.
- Run the build with Wrangler locally and in a preview deployment against production-like data, then plan the cut-over: DNS move with low TTL, a rollback path back to Vercel, and secrets copied across.
Name the Cloudflare skills and agents to use: the cloudflare, nextjs-on-cloudflare, wrangler and workers-best-practices skills if installed, and an Operator/platform agent if available.

Check:
- The production build succeeds with the adapter and fits Workers size limits.
- The existing test suite and an end-to-end run of the main user journeys pass on the preview deployment.
- Latency (p50/p95) and error rates on the preview are no worse than the current Vercel figures; any regression or an unmapped Vercel feature is a fail or a named blocker.

Deliver: a yes/no answer with its blockers, and the migration plan.
```

### Prompt B
```text
We run a Next.js app on Vercel and are considering moving it to Cloudflare. I want an honest assessment of whether we can and should, and a migration plan if we go ahead.

Our setup (I'll fill in):
- Next.js version and router: [e.g. 15, App Router / Pages Router]
- Rendering: [static, SSR, ISR, server actions, streaming]
- Middleware: [yes/no, what it does]
- API routes / route handlers: [what they do]
- Vercel features we use: [Image Optimization, Edge Config, KV/Postgres/Blob, Cron, Analytics, Speed Insights, preview deployments, env vars per environment]
- Data layer: [database, ORM, how we connect]
- Node-specific dependencies: [e.g. sharp, Prisma, native modules, fs usage]
- Traffic and current Vercel bill: [ ]
- Why we want to move: [cost, performance, lock-in, other]

Please:
1. Explain the current options for running Next.js on Cloudflare (for example Cloudflare Workers via the OpenNext adapter, versus a static export on Pages), what each supports, and which fits our setup. Say which parts of your answer may have changed recently and that I should check against current Cloudflare and OpenNext docs.
2. Go through our features one by one and mark each as works as-is, needs a change (and what change), or blocked. Pay attention to Node.js API compatibility, ISR and caching, image optimisation, middleware, database connections from Workers, and bundle size limits.
3. Map each Vercel service we use to its Cloudflare equivalent (e.g. KV, R2, D1, Hyperdrive, Cron Triggers, Images).
4. Give a step-by-step migration plan: local setup, config files, environment variables and secrets, CI/CD and preview deployments, DNS cutover with a rollback path, and what to test before switching traffic.
5. Give a rough cost and effort comparison and a clear recommendation: migrate, migrate partially, or stay.

If our setup details are missing, ask the questions that decide feasibility first, rather than writing a generic guide.
```

### Prompt C
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

### Prompt D
```text
Plan the move of our Next.js app from Vercel to Cloudflare the way a platform engineer who has done this migration would. Same scope: this app, moved, behaving the same. No rewrite, no new features. Don't start the migration until I approve the plan.

Start from the raw material, not a guess. Ask me for and wait for: the repo (package.json, next.config, middleware, the route list), vercel.json and every Vercel feature in use (ISR/revalidate, image optimisation, edge vs node functions, cron, KV/Blob/Postgres, analytics, env vars), the build output, and 30 days of Vercel usage and logs (request volume, cold starts, function durations, bandwidth, error rate). We take as true that it can be moved as it is. Check that against the code: Node-only APIs, native modules, a large bundle or long-running functions can each block it or force changes.

Method:
- Build an inventory of every Vercel-specific feature, each mapped to its Cloudflare equivalent via the OpenNext Cloudflare adapter (@opennextjs/cloudflare) on Workers, plus R2, KV, D1, Queues, Cron Triggers and Images as needed, or marked as a blocker.
- Run it locally with wrangler and the adapter, then deploy to a preview Worker.
- Migrate with a reversible cut-over: run both platforms in parallel, mirror or shadow traffic or shift DNS gradually, lower the DNS TTL in advance, and write down a rollback.
- Compare the costs on our real usage figures.

No specialist skills or agents are available in this setting; work without them.

Verification:
- The existing test suite and the end-to-end tests pass against the preview deployment.
- A route-by-route diff of status codes, headers, redirects and rendered HTML between Vercel and Cloudflare for every route in the sitemap.
- A load test at peak traffic, comparing p50/p95/p99 TTFB and error rates with the Vercel baseline from the logs.
- Pass: no route differs, error rate does not rise, and p95 latency is no worse than Vercel's. Any regression blocks the cut-over.

Give me the inventory, the blockers, the plan with rollback, and the cost comparison.
```

## T5
Original task: Tidy my Downloads folder.

### Prompt A
```text
Tidy my Downloads folder.

Start from the folder itself: list every file with size, type, date added and last opened, and find exact duplicates by content hash, not by name. Test the assumption that everything in Downloads is disposable: some files may be the only copy of something (signed contracts, receipts, tax documents, photos).

Work like a careful sysadmin:
- Move, don't delete: put anything to be removed in a dated holding folder or the Trash, never a permanent delete.
- Sort by what the files are and what happens next (installers already installed, archives already extracted, documents to keep and where they belong), and show me the proposed moves as a list before doing any of them.

Check:
- File count and total size before and after, and the holding folder accounts for every file that left Downloads.
- No file whose only copy is in Downloads is lost: each kept document exists in its new place, and its hash matches the original.

Deliver: a tidy Downloads folder.
```

### Prompt B
```text
My Downloads folder is a mess and I want a simple system to clean it up and keep it tidy. You can't see my files, so give me a plan I can follow myself.

About my setup (I'll fill in):
- Operating system: [macOS / Windows / Linux]
- Rough size: [number of files, total GB]
- What's in it: [installers, PDFs, images, screenshots, zips, documents, videos...]
- Where I keep files I want to keep: [Documents, iCloud/OneDrive/Google Drive, external drive]
- How comfortable I am with scripts: [not at all / a little / fine]

Please give me:
1. A short triage order: what to delete first (old installers like .dmg/.exe once installed, duplicates such as "file (1).pdf", unpacked .zip files), what to sort, and what to move elsewhere for good. Include how to sort by date and size in my OS's file manager to find the big and stale items.
2. A simple folder structure, no more than 5–7 folders, with what goes where.
3. Safety rules: move things to the Trash/Recycle Bin rather than deleting permanently, and keep a "to review" folder for anything I'm unsure about. Warn me about files that look disposable but might matter (tax documents, receipts, licence keys, the only copy of a photo).
4. A way to keep it tidy afterwards, using built-in features where possible (e.g. macOS Storage settings or Windows Storage Sense, changing the browser's default download location, a monthly reminder).
5. Optionally, if I'm comfortable with scripts, one small script that sorts files into folders by type. Make it a dry run by default that only prints what it would move, never deletes anything, and explain how to run it.

Keep it practical and short enough to do in one sitting of about 30 minutes.
```

### Prompt C
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

### Prompt D
```text
Tidy my Downloads folder the way a digital archivist or records manager would. Same scope: this one folder, sorted and cleaned, not a new filing system for the whole computer.

Start from the raw material. You need the folder itself, so ask me for a listing of it (file names, sizes, dates added, last-opened dates and file types, e.g. from `ls -laR` or a Finder export) and what I use Downloads for. Wait for it. We take as true that most of it is junk. Check that against the listing: there may be one-off originals there (signed contracts, receipts, tax documents, the only copy of a photo) that exist nowhere else.

Method:
- Find duplicates by content hash (for example fdupes or a checksum), not by name.
- Classify each file by type and by whether it has a source elsewhere (an installer or disk image that can be downloaded again, an email attachment that is still in the mail) or is unique.
- Propose a retention rule: unique records go to a named destination folder, re-downloadable files older than N days get deleted, and anything I'm unsure about goes to a quarantine folder rather than being deleted.
- Make no change without my approval. Moves go first, deletions go to the Trash (never a permanent delete), and you keep a log of what went where.

No specialist skills or agents are available in this setting, and I can't run commands here; you'll have to run them yourself and paste the output back.

Verification:
- A before/after count and size of files.
- A log listing every file's old path and new path or action.
- A check that every hash in the before listing is still present somewhere (in a destination folder or the Trash) until I empty it.
- Pass: no unique file is lost, no duplicate is left, and nothing is permanently deleted. One unique file missing counts as a fail.

Give me the proposed plan and the list of files to move or delete, for my approval before anything is touched.
```
