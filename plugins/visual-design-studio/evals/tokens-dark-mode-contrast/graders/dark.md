---
type: llm
weight: 3
---

Passes only if the response:
- Diagnoses with computed contrast ratios: brand blue #1D4ED8 on the dark surfaces is too low for text (about 3.1:1 on #000000 and about 2.6:1 on #1A1A1A) and #6B7280 on #1A1A1A is about 3.6:1, below 4.5:1.
- Replaces pure black with a near-black, slightly tinted canvas (for example OKLCH lightness about 0.15-0.20, or a hex like #0B0F12 to #121212) and builds lighter surfaces for elevation (stepwise lightness increases per level).
- Replaces pure white body text with an off-white (OKLCH L about 0.92-0.95 or a hex like #E2E9EF/#EDEDED), and gives a secondary-text value that reaches at least 4.5:1, with ratios shown.
- Uses a lighter, slightly desaturated step of the brand blue for links and accents on dark (and dark text on blue buttons, or a darker button fill with white text that passes), with ratios shown.
- Delivers semantic tokens (for example color.bg.canvas, color.bg.surface, color.fg.default, color.fg.muted, color.accent.default) with light and dark values, in DTCG JSON ($value/$type) or CSS custom properties.
