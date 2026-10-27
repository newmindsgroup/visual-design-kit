---
type: llm
weight: 2
---

Passes only if the response specifies a 3.5 x 2 in trim, 0.125 in bleed on all four edges (3.75 x 2.25 in with bleed), crop marks placed outside the bleed (offset at least the bleed distance so they never print inside it), and a PDF with a trim box equal to the finished size and a bleed box that includes the bleed. Equivalent routes pass: CSS `@page { size: 3.5in 2in; bleed: 0.125in; marks: crop; }` rendered with WeasyPrint, or an InDesign or Affinity export with marks and bleed.
Fails if the crop marks sit inside the bleed or trim, or no bleed is set.
