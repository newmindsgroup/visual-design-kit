---
type: llm
weight: 2
---

Passes only if the color page lists approved text pairs with computed WCAG contrast ratios and flags the coral: white on #0F766E is about 5.5:1 (passes AA for body text); white on #F97361 is about 2.7:1 (fails 4.5:1 and the 3:1 large-text bar), so coral needs dark text (for example near-black at about 6.5:1) or is limited to non-text accents; teal and coral together are about 2.0:1 and must not carry text on each other. Ratios within 0.1 of these values pass.
Fails if it approves white text on the coral, or gives pairs without computed ratios.
