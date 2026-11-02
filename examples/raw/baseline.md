## T1

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

## T3

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

## T4

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

## T5

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
