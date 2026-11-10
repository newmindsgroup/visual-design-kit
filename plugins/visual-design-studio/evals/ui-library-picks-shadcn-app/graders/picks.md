---
type: llm
weight: 3
---

Passes only if the response picks one library per need and stays on the installed stack:
- Toasts: Sonner, installed through shadcn (`npx shadcn@latest add sonner`) or `npm i sonner`, replacing the hand-rolled array. Saying shadcn's own Toast is deprecated in favor of Sonner is a plus, not required.
- Drawer: shadcn's Drawer (built on Vaul on the Radix base), or Vaul directly. A note that Vaul's README says it is unmaintained, with the trade-off stated, is a plus. Switching the whole app to Base UI just for the drawer fails; Base UI's Drawer is acceptable only as an explicit, reasoned alternative.
- Command menu: cmdk, through shadcn's Command component or directly.
- Animated price: NumberFlow (`@number-flow/react`) with currency formatting via `Intl.NumberFormat` options, or an equivalent that animates digits without re-rendering text. Using the already-installed `motion` for this is acceptable only if it explains how digits transition; re-rendering the text with a fade does not count.

Fails if it recommends building any of the four by hand, adds a second toast library beside Sonner, or adds a second primitive layer (Base UI, Headless UI, React Aria) beside Radix without saying why.
