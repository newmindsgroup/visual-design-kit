---
type: llm
weight: 2
---

Passes only if the response picks one headless primitive layer for Svelte and says why:
- UI SDK (`@ui-sdk/svelte` with `@ui-sdk/core`) because it has an agent bridge (`createAgent`, snapshot/query/act, WebMCP `registerTools`), or Bits UI as the established Svelte option with the agent rules applied by hand. Either is acceptable when the trade-off is stated.
- If it picks UI SDK, it flags that UI SDK is in beta and says to pin an exact version (or wait for 1.0 or a version at least about two weeks old) for production work.
- It says to restyle the components with the product's own tokens rather than ship a library's default look.

Fails if it recommends hand-building the select, menus, dialog or switches, picks a React-only library for a Svelte app, or invents package names.
