# Weak spots — deeper.tools, 5 Nov 2026 (before)

Baseline: impeccable detector 0 findings at 375x812, 768x1024, 1280x800, 1440x900 (advisories only, files `before/impeccable-*.txt`). Screenshots: `before/*.png`.

| # | Weak spot | Where | Measurement (before) | Target (after) |
|---|---|---|---|---|
| W1 | No type scale | global | 13 distinct computed font sizes on home (13.6–41.6px in pane), no ratio | one modular scale (1.25 ratio, 7 steps) — every computed size on the page is a scale step |
| W2 | Mobile nav wraps; GitHub alone on line 2 | header, 375 | nav takes 2 rows (≈88px) above the h1 | one row at 375 |
| W3 | Install command breaks across 2 lines | hero, 375 | `npx skills add EazyAccessEA/deeper` wraps to 2 lines | one line at 375 |
| W4 | Hero has 4 trailing text links stacked under the command | hero | 4 separate lines after the CTA at 375 | 2 lines max |
| W5 | Example tabs wrap into 3 rows | markup, 375 | 3 rows of tabs | 1 row (scrolls sideways) |
| W6 | Questions grid: staggered offsets leave holes; h3 at 1.3rem barely above body | home | even items pushed 3rem; h3/body size ratio 1.22 | ratio ≥1.5 between item title and body; no holes |
| W7 | Every section is the same shape (h2, grey para, underlined link) | home lower half | 3 identical consecutive blocks | install + updates read as the close of the page, not repeats |
| W8 | Hero image top doesn't sit on the h1 cap line; floats | hero, 1440 | image top 92px vs h1 cap ≈ 100px (screenshot) | image top aligned to h1 cap height |
| W9 | Dark mode: hero photo is a bright white slab | hero, dark | brightness(0.86) of a white photo | photo recedes in dark (≤ surface luminance band) |
| W10 | Dark placeholder contrast | subscribe, dark | 4.1:1 | ≥4.5:1 |
| W11 | Inner pages centred, breaking the left lane the header sets | /start/ (and other .page) | h1 at x=268 vs logo at x=106 (1440) | content shares the logo's left lane |
| W12 | Browser surfaces unthemed | global | `::selection` default; no `accent-color`; scrollbar default | selection, caret, accent from Proof Red |
| W13 | Table header "No skill" wraps to 2 lines | evidence, 1440 | 2 lines | 1 line |
| W14 | Stragglers (one word last line) | /changelog/ ×3, /start/ ×1 | detector advisories: 4 | 0 |
| W15 | Insertion caret small against cap height | markup | caret 0.32em tall | caret height = x-height, apex reaches cap line feel |
