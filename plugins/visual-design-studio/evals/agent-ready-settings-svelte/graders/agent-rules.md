---
type: llm
weight: 3
---

Passes only if the response gives agent-ready rules that fit this screen:
- Unique accessible names: each row's controls carry the member's name ("Remove Jane Doe", "Role for Jane Doe"), one menu per row rather than one shared menu, and no two controls named only "Remove" or "Name".
- Removing a member needs a person's confirmation even when an agent starts it, and the gate sits on the control that commits the removal (the confirm button) with a specific sentence (who is removed and what they lose), not on the button that opens the dialog.
- The API key shown once is hidden from agents (or at least never readable by them), and secret fields can be filled but not read.
- App state and validation follow the components' change events or values, not only click or key handlers, so agent changes pass the same checks; refusing an agent change is possible.
- The page still works without WebMCP, and page text returned to an agent is treated as untrusted.

Fails if it lets an agent remove members or reveal the key with no person in the loop.
