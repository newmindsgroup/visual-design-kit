---
type: llm
weight: 1
---

Passes only if the response does both:
- Explains that clients behave differently: some render as coded and honor your own dark styles (Apple Mail with `prefers-color-scheme`), some partially invert (for example Outlook.com or some Outlook apps), and some fully invert or remap colors (Gmail apps, some Outlook builds), with a hedge that behavior changes by app version and must be tested.
- Tells the user to test in real clients or in Litmus or Email on Acid, including with images off.
Fails if it treats dark mode as one behavior across clients, or omits the images-off check.
