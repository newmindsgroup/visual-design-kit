---
type: llm
weight: 1
---

Passes only if the response does both:
- Requires direct labels or a legend in stack order, and does not rely on color alone (direct labels, patterns or separators, tooltips or a data table).
- Recommends checking the palette with a color-vision-deficiency simulation (for example deuteranopia and protanopia, with a named tool or the simulator in the design tool or browser) or a grayscale check.
Fails if it omits the color-vision-deficiency or grayscale check.
