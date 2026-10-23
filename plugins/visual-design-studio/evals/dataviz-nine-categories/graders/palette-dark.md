---
type: llm
weight: 1
---

Passes only if any palette the response gives uses a named, tested colorblind-safe categorical set (for example Okabe-Ito, or another named tested set such as Tableau 10 colorblind or IBM) with hex values, AND handles dark mode against a stated dark background with the 3:1 graphical-object minimum (WCAG 1.4.11): either separate or adjusted dark values with their contrast, or an explicit statement that the light values already clear 3:1 on that named background, with the colors that do not (for example black) swapped for a light value.
Fails if the colors are unnamed or unsourced, or dark mode reuses or inverts the light values with no stated background and no 3:1 check.
