## T1

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

## T2

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

## T5

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
