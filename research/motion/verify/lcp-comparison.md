# Home page LCP, with and without the motion (6 Nov 2026)

After the motion went live (version b462de8a), Lighthouse mobile measured home-page LCP at 1.74–1.81 s, above the 1.6 s pass mark. To see whether the motion caused it, the previous build (no motion) was uploaded as version 6eacf04a. It was deployed at 0% traffic, so only requests carrying the header `Cloudflare-Workers-Version-Overrides: deeper="6eacf04a-…"` reached it. Both builds were then measured on the same edge, alternating runs. Lighthouse 12, default mobile simulation.

| Run | Old build (no motion) | Motion build |
|---|---|---|
| 1 | 1847 | 1762 |
| 2 | 1855 | 1772 |
| 3 | 1846 | 1750 |
| 4 | 1901 | 1751 |
| Median | **1851 ms** | **1757 ms** |

Every run scored perf 0.99. The motion build is about 95 ms faster, probably because the 128px blur-in it replaced is gone. The motion didn't cause the result above 1.6 s: under today's conditions the old home page was over 1.6 s too. /start/, which this work didn't touch, measured 1.59–1.62 s on the same day. In the real (unsimulated) load, the headline paints at about 0.3 s.

The split was removed straight after the runs: production is b462de8a at 100%.
