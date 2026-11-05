---
type: llm
weight: 3
---

Passes only if the response:
- Names exactly one signature idea for the hero (for example the movement footage itself, a ghost word behind the subject, or a masked headline rise) and builds the layout around it, with the copy placed opposite the centre-right subject.
- Gives real values, not adjectives: H1 size as `clamp()` with a rem term (or explicit sizes per breakpoint), line-height around 0.9-1.05, tracking around -0.02 to -0.05em, a sub max-width, CTA height of 44-48px, and colors as hex or token names.
- Sets the page background to the clip's edge color (black or a near-black such as #000 or #050505) on `html` and `body` as the first CSS rule, so nothing flashes white before the video loads.
- Includes real headline, sub and CTA copy (no lorem, no "Your tagline here") and no invented statistics.

Fails if the spec relies on words like "cinematic", "premium" or "smooth" without the numbers that produce them.
