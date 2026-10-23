---
type: llm
weight: 1
---

Passes only if the response gives the opt-in code: `color-scheme` and `supported-color-schemes` meta tags or CSS, a `@media (prefers-color-scheme: dark)` block with `!important` overrides, and Outlook.com's `[data-ogsc]` and/or `[data-ogsb]` selectors.
Fails if any of the three is missing.
