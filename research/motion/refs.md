# Motion references, measured 6 Nov 2026

Read with `document.getAnimations()` on the live home pages at 1440×900 in Chrome. The page was sampled at 0.3s, 1.2s and 3s after load, then after each of three 900px scrolls, once with `prefers-reduced-motion: no-preference` and once with `reduce`.
Script: `motion_refs.py`. Raw output: `refs-raw.json`. Durations and delays are in ms; easings are as the browser reports them.

Picks: Vercel, Stripe, Raycast and Cursor come from the styles.refero.design gallery. Linear isn't in that gallery's first page; it's included because its hero is a prompt being typed, the closest thing to what deeper does.

| Site | What moves | Duration | Delay / stagger | Easing | Loops | Under `reduce` |
|---|---|---|---|---|---|---|
| Vercel | one opacity fade | 1200 | 0 | linear | no | removed (1 → 0) |
| Stripe | demo graphics, started on scroll into view | 1420 | 4000 dwell | cubic-bezier(0.78, 0, 0.22, 1) | no | 62 → 12 animations |
| Stripe | chat demo sequence on scroll | 2260 | 0 | cubic-bezier(0.165, 0.84, 0.44, 1) | no | — |
| Stripe | link colour | 300 | 0 | cubic-bezier(0.25, 1, 0.5, 1) | no | — |
| Linear | hero text in (opacity + blur + translate) | 1000 | 400, 600, 850 | ease (0.25, 0.1, 0.25, 1) | no | 117 → 75: mostly kept |
| Linear | product frame in | 1500 | 1300 | cubic-bezier(0.455, 0.03, 0.515, 0.955) | no | kept |
| Linear | prompt caret blink | 1250 | 0 | steps(1) | infinite | kept |
| Linear | dot-grid "thinking" loops | 1600 / 2800 / 3200 | 0 | steps(1) | infinite | kept |
| Raycast | hero text fade-in-up | 1000 | 0, then 1000 | ease | no | 31 → 30: kept |
| Raycast | cards slide in | 700 | 100, +80 each | cubic-bezier(0.215, 0.61, 0.355, 1) | no | kept |
| Raycast | text carets blink | 1100 | 0 | steps(1) | infinite | kept |
| Cursor | entrance fades | 180–340 | 0, 570, 740 | ease-out | no | 13 → 11 |
| Cursor | shimmer / pulse on "working" text | 1600 / 2500 / 2000 | 0 | linear / (0.4, 0, 0.6, 1) | infinite | kept |
| deeper.tools (now) | headline blur-in | 800 | 100 | cubic-bezier(0.16, 1, 0.3, 1) | no | removed |

## What the numbers say

1. **A blinking caret is the shared sign for "a prompt".** Linear, Raycast and Cursor all use one, with a 1100–1250ms cycle and `steps(1)`, so it blinks instead of fading. They all loop forever. On a decorative caret, a blink that runs past 5 seconds with no way to pause it fails WCAG 2.2.2. **Ours doesn't blink at all.** Their caret is a text-cursor I-beam. Ours is a proofreader's ^, and a blinking ^ isn't a convention anyone knows (independent review, 6 Nov).
2. **Hero entrances take 1000ms with a 200–250ms stagger** (Linear, Raycast). UI feedback stays at 180–340ms (Cursor, Stripe links).
3. **Demos start when they come into view, not on load** (Stripe: a 4000ms dwell, then a 1420ms move).
4. **The leaders mostly ignore `prefers-reduced-motion`.** Linear keeps 75 of 117 animations and Raycast keeps 30 of 31. Only Vercel removes everything. We want to beat that, not copy it.
5. **Nobody's signature motion is a fade alone.** Each one acts out what the product does: Linear types a prompt, Stripe moves a payment, Cursor shimmers while it works. For deeper, the act is *insertion*.
