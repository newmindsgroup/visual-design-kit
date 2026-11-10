---
type: llm
weight: 3
---

Passes only if the response treats Linear's homepage as a concrete, fetchable bar:
- Names Linear's live homepage (linear.app or "Linear's homepage") as the single bar, rather than a category such as "best SaaS sites".
- Captures the real page (screenshots or a render, for example with the kit's `render_review.mjs` or a browser) and ours at the same viewports and settings (for example 390 and 1440 px, same height, device pixel ratio and color scheme), and compares the captures, not a memory or description of Linear.
- Splits the page into pieces judged separately (for example hero, type, color, imagery, motion, interaction, mobile) instead of judging the whole page at once.
- Keeps the bar captures for internal comparison only (not shipped, committed to a template or published). This point is a plus, not required.

Fails if it compares against a description of Linear from memory, or never captures both at matching viewports.
