---
type: llm
weight: 1
---

Passes only if the response diagnoses with computed contrast ratios (within about 0.2 of these values):
- Brand blue #1D4ED8 as text on the dark surfaces is too low: about 3.1:1 on #000000 and/or about 2.6:1 on #1A1A1A (at least one stated).
- #6B7280 on #1A1A1A is about 3.6:1, below 4.5:1.
Fails if it says "low contrast" without computed ratios, or the ratios are wrong.
