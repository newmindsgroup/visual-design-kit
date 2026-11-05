---
type: llm
weight: 3
---

Passes only if the performance budget is numeric and covers:
- Core Web Vitals at the 75th percentile: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less (designing for about 2.0 s LCP is a plus).
- The LCP element named (poster or headline) with a size target (for example a poster around 200 KB or less) and the video loading after first paint.
- Video weight targets for desktop and mobile (for example a few MB at 1080p and a lighter 720p or 960px mobile encode), and a memory or frame-count cap if a canvas frame cache is used.
- A JavaScript budget (for example about 150 KB compressed) or an explicit "no animation library needed" with the library weight stated.

Fails if the budget is qualitative ("fast", "optimized") without numbers.
