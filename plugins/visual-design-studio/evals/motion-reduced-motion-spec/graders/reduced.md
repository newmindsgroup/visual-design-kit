---
type: llm
weight: 3
---

Passes only if the response:
- Uses `prefers-reduced-motion: reduce` (CSS media query and the JavaScript matchMedia equivalent for scripted animation such as GSAP or View Transitions).
- Specifies a replacement per effect rather than deleting everything: parallax off (static image); section fade-ups become a short opacity-only fade (about 200ms or less) or an instant appearance; page transitions become a crossfade or instant swap (skip the View Transition or shorten it).
- Handles the background video: poster image or paused by default under reduced motion, and a visible pause control for everyone because autoplaying motion longer than 5 seconds needs pause, stop or hide (WCAG 2.2.2) regardless of the preference.
- Mentions flash safety (no more than three flashes per second, WCAG 2.3.1) or vestibular triggers (large-scale movement, zoom, parallax) as the reason.
- Gives concrete values: durations in ms, the token or variable approach (for example durations dropping to about 0.01ms), and keeps essential feedback (focus, hover, state changes) working.
