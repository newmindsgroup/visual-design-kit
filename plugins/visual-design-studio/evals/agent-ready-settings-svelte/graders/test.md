---
type: llm
weight: 1
---

Passes if the response includes a way to prove the screen is agent-operable: an automated test that lists every control by name and fails on unnamed ones and runs at least one agent action (for example UI SDK's `agent.snapshot()` and `agent.act()` in a Vitest or Playwright test), or a screen-reader walkthrough covering every control the task names.
