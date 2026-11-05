---
type: llm
weight: 3
---

Passes only if the reduced-motion behaviour is specified concretely:
- Under `prefers-reduced-motion: reduce`, either keep the scroll-to-frame mapping but remove smoothing and any autonomous movement, or replace the scrub with static stills (for example 3-4 key frames or the assembled poster) placed with the copy.
- The headline and "Reserve yours" button are visible in their final state without waiting for the scrub or for JavaScript (no content left at opacity 0 if scripts fail).
- Entrance motion for the headline becomes an instant change or a short opacity fade (about 200ms or less), and any looping motion has a pause control (WCAG 2.2.2).

Fails if reduced motion just disables the hero with no replacement content, or if the CTA only appears after scrolling the full animation.
