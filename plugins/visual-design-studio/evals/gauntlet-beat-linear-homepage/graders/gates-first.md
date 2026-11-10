---
type: llm
weight: 3
---

Passes only if hard gates are checked before any comparison with the bar:
- Lists pass/fail gates run on our page each round before comparing: accessibility (WCAG 2.2 AA), the client's locked brand and tokens, licensing (fonts, images, components, nothing taken from Linear) and factual accuracy of claims. Performance budgets are an acceptable extra gate.
- States that a failed gate goes back to the builder without a comparison, and that winning the comparison never overrides a failed gate.
- Notices that #FCA311 orange body links on white fail WCAG text contrast (about 2.0:1 against the 4.5:1 minimum) and proposes a fix that respects the lock (for example navy links with an orange underline or non-text use of the orange, and raising an accessible variant with the brand owner). Any stated ratio must be close to 2.0:1. Orange on navy (about 7.9:1) passing is a plus.

Fails if gates are checked only at the end, or are absent.
