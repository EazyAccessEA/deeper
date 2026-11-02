## T1
Original task: Write an Instagram caption for a jar of borage honey.

### Prompt A
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

### Prompt B
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

### Prompt B
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

## T3
Original task: I need to sell my car, a VW Polo, and buy a new one, perhaps a Golf.

### Prompt A
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

## T4
Original task: Can we move our Next.js app off Vercel to Cloudflare?

### Prompt A
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

### Prompt B
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
