---
type: llm
weight: 3
---

Passes only if the response:
- Pushes back on nine distinct hues: says categorical palettes stay legible up to about 6 (8 at most) colors, and that a stacked area with nine bands is hard to compare.
- Proposes at least two concrete alternatives: group the smaller lines into "Other" (top 5 + other), highlight one or two lines with the rest gray, small multiples, or a line chart or 100% stacked view for comparison.
- If it gives a palette, uses a colorblind-safe categorical set (for example Okabe-Ito or another named tested set) with hex values, and gives separate or adjusted values for dark mode with contrast against the dark background (at least 3:1 for graphical objects).
- Requires direct labels or a legend in stack order and not relying on color alone (patterns, labels, tooltips), and recommends a color-vision-deficiency simulation check.
Fails if it simply lists nine hex colors with no pushback.
