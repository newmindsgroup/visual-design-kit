---
type: llm
weight: 1
---

Passes only if the response does both:
- Gives dark-mode background and body-text values that avoid pure #000000 and #FFFFFF (off-black such as #111111 or #121212, off-white such as #F5F5F5 or #E8E8E8).
- Flags that the navy #1B2A4A CTA would nearly disappear on a dark background and fixes it (a lighter or inverted fill, or a light border), keeping the button as live text (a bulletproof or VML button, not an image).
Fails if the navy button is not addressed.
