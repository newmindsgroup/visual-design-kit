---
type: llm
weight: 1
---

Passes only if the response does both:
- Replaces pure black with a near-black, slightly tinted canvas (for example OKLCH lightness about 0.15-0.20, or a hex in the range #0B0F12 to #121212) and builds lighter surfaces for elevation (stepwise lightness increases per level).
- Replaces pure white body text with an off-white (OKLCH L about 0.92-0.95, or a hex like #E2E9EF or #EDEDED) and gives a secondary-text value that reaches at least 4.5:1, with ratios shown.
Fails if the canvas stays #000000 without an OLED justification, or the new text values have no ratios.
