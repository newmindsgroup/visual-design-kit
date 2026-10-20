---
type: llm
weight: 3
---

Passes only if the response:
- Explains that clients behave differently: some render as coded and honor your own dark styles (Apple Mail with `prefers-color-scheme`), some partially invert, and some fully invert or remap colors (Gmail apps, Outlook), with a hedge that behavior changes by app version and must be tested.
- Gives the opt-in code: `color-scheme` and `supported-color-schemes` meta tags or CSS, a `@media (prefers-color-scheme: dark)` block with `!important` overrides, and Outlook.com's `[data-ogsc]` / `[data-ogsb]` selectors.
- Fixes the logo: a light-on-dark swap where supported, or a transparent PNG with a light outline/padded light container so the black logo does not vanish on a dark background.
- Avoids pure black and white in the dark palette (off-black such as #121212 and off-white such as #F5F5F5) and checks the navy CTA, which would disappear on a dark background (adds a border or lighter fill, keeps live text in a bulletproof button).
- Tells the user to test in real clients or Litmus/Email on Acid, including images-off.
