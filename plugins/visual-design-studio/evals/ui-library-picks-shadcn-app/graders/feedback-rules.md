---
type: llm
weight: 3
---

Passes only if the response fixes the behavior, not just the library:
- "Payment failed - Retry" must not rely on a disappearing toast: put the error and Retry inline at the cause or in a persistent banner (a toast may echo it), because an action that disappears fails people who need more time (WCAG 2.2.1).
- 2 seconds is too short: toasts last about 5-10 s, pause on hover and focus, and any toast with an action stays at least 5 s and its action is reachable elsewhere.
- Toasts use a polite live region (`role="status"`) or the library's equivalent; urgent errors use an alert pattern.
- Names at least one reduced-motion behavior: NumberFlow's `respectMotionPreference` (on by default) or a static price change under `prefers-reduced-motion`, and/or the drawer and toasts respecting it.
- The command menu has a visible trigger (button or search field showing the shortcut), not only Cmd/Ctrl+K.

Fails if the payment failure stays a 2-second toast with Retry as its only path.
