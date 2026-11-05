---
type: llm
weight: 3
---

Passes only if the response:
- Specifies a poster image for the video (WebP or AVIF, around 200 KB or less, or named as the LCP element) and a muted, playsinline, decorative video (`aria-hidden` or empty alt equivalent).
- Gives the looping video a visible pause control because it moves for more than 5 seconds (WCAG 2.2.2), independent of the reduced-motion setting.
- Gives a `prefers-reduced-motion` branch: the poster or a still frame instead of playback, and the entrance shown in its final state (or a short opacity fade).
- Specifies a lighter or different mobile behaviour: a smaller encode (for example 960px wide), `preload="metadata"`, or poster only on mobile data.

Fails if the video autoplays on every device with no poster, no pause control and no reduced-motion behaviour.
