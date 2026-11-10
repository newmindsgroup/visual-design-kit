---
type: llm
weight: 3
---

Passes only if the response restyles the shadcn theme concretely:
- Changes radius, color and type first, through shadcn's CSS variables (`--radius`, `--primary`, `--background`, etc.) mapped to brand tokens, not by editing classes one by one. Noticing that shadcn derives its radius scale from `--radius` (so one change moves every corner), or that the radius scale must be replaced to use the brand's values, is a plus.
- Uses #1F5C4A as one accent with one job (the primary action, selected state) rather than coloring everything green; white on #1F5C4A is about 7.8:1 and #1F5C4A on #F6F1E7 about 6.9:1, so both pass 4.5:1. Any stated ratio must be close to these.
- Brings in a display face with a point of view (a serif to echo the wordmark is a good answer) and a text face for UI; keeps tabular figures for numbers.
- Keeps accessibility: input and control borders at 3:1, visible focus ring, dark mode handled through the same tokens.
- Ends with a render-and-review step (screenshots at several widths, a name-swap or AI-tells check).

Fails if it only says "customize the theme" without naming what changes, or swaps the gray default for a new default gradient.
