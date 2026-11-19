# Agent-ready interfaces

Version-Timestamp: 2026-11-19 11:45:00 UTC

Use when an interface will be operated by AI agents as well as people: a browser agent filling a form, an in-app assistant changing settings, or a site that publishes tools to the browser through WebMCP. An agent finds controls the way a screen reader does, by role and accessible name. A screen that is ambiguous for a screen reader is ambiguous for an agent too. The difference is that an agent acts at speed, so the dangerous actions need a gate that a person answers.

This page is library-agnostic. The last section maps each rule to Vercel's UI SDK (`@ui-sdk/*`), which builds an agent bridge into its components. The rules and the benchmark below are restated from the UI SDK repository ([vercel-labs/ui](https://github.com/vercel-labs/ui), Apache-2.0, commit `e741e64`, read 2026-11-19; credited in `NOTICE.md`). No UI SDK code is bundled.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Names | Every control has a unique accessible name in its region: a visible label, a label part, or `aria-label` when there is no visible text | Two fields share a name only if a section heading or row text still tells them apart |
| Row actions | Give each control in a repeated row its own verb plus the row's text: "Open Water the plants", "Actions for Jane Doe" | Never: a bare row title on several controls collides |
| Dangerous actions | Delete, pay, send, publish, invite and anything irreversible or external need a person's confirmation, even when an agent starts them | Read-only agents: no gate needed |
| Secrets | Password, card, one-time-code and recovery fields can be filled by an agent but never read back | None |
| Hidden regions | Recovery codes, keys shown once and other people's personal data are hidden from agents entirely | None |
| State | App state follows the component's change events, never key or click handlers alone, so agent changes and keyboard changes go through the same checks | None |
| Validation | Validate the value, not the typing: browsers check `minLength` only while a person types, so use `pattern` or your own validation | None |
| Proof | Every agent-operable screen ships with a test that lists every control by name and changes each one the task names | Static marketing pages: the accessibility pass is enough |

## Name every control

- Names come from visible text first. Items, tabs and options are named by their text; an `aria-label` on an item is usually ignored.
- Match how agents search: a label matches every label that contains its words, so "Tip" collides with "Custom tip", and a "Delete" confirm button collides with a "Delete project" trigger. Give the confirming button text of its own ("Delete forever").
- Components that only support another still need a name or `aria-hidden="true"`: a shared tooltip, an avatar (`role="img"` plus `aria-label`), an accordion root with several sections, and an empty toast region.
- Labels inside a dialog differ from the page's: many agents still see the page behind an open modal.
- One menu per row, with a trigger named for that row. A shared menu has no name of its own.

These rules are the same ones a screen reader needs, so they also close WCAG 2.2 failures under 1.3.1, 2.4.6 and 4.1.2 ([accessibility](accessibility.md)).

## Gate what needs a person

Use the action classes in [AI interfaces](ai-interfaces.md#approvals-for-agent-actions). In the interface itself:

1. **Confirm.** Mark the control that commits the action, not the one that opens the dialog: opening a dialog is harmless, and gating the whole dialog gates Cancel too. Write the confirmation sentence for the person who will be asked, from app state: "Deletes the project Atlas and its 214 files", not "Are you sure?".
2. **Secret.** Mark fields whose value an agent may set but never read.
3. **Hidden.** Mark regions an agent must not see at all.
4. **Refuse in the change event.** The app can tell an agent's change from a person's and cancel it. A cancelled change still returns success from some bridges, so check the resulting value, not only the status.

Design the confirmation itself like any other decision dialog ([states and feedback](states-and-feedback.md)): what will happen, to what, whether it can be undone, a primary button that names the action and a Cancel.

## WebMCP and agent tools

- **What it is.** WebMCP lets a page register tools with the browser's built-in agent through `document.modelContext.registerTool`, so the agent calls the page's actions instead of reading and clicking the whole page. Browser support is still arriving: as of 2026-11-19 UI SDK's guide documents ChatGPT's built-in browser with a "site tools" permission (verify current support with `typeof document.modelContext?.registerTool` in the target browser). Pages must work without it.
- **What it saves.** UI SDK's own benchmark (Claude Sonnet through Claude Code, 2026-11-15, medians of 3 runs, one settings task with tabs, a 24-row member list, a confirm dialog and switches): browser tools took 16 to 19 tool calls and about 226k to 331k tokens across Base UI, Ark UI, Reka UI, Bits UI and UI SDK. UI SDK's three agent tools took 7 to 9 calls and 70k to 93k tokens, about 3 times cheaper. With browser tools, UI SDK cost the same as the other libraries. Vendor-reported; re-run `benchmarks/agent` in the repository before quoting it to a client.
- **Tool hints.** Read tools carry a read-only hint, and the tool that acts carries a consequential hint so the browser can ask the person first. Page content returned to an agent is untrusted: labels and text people typed can carry prompt injection, so never let page text authorize an action.
- **Double prompts.** Ask the person in one place. If the page's own permission check already asks, the browser registration should not ask again for the same step.

## With UI SDK

| Rule | UI SDK |
| --- | --- |
| Bridge | `createAgent({ allow })` from `@ui-sdk/<framework>/agent`, created once in client code (`"use client"` in Next.js) |
| Read and act | `agent.snapshot()`, `agent.query({ text, within, kind })`, `agent.act({ steps })`; `agentTools` gives the JSON Schemas for your own model |
| WebMCP | `registerTools(agent, { allow })`; does nothing without `document.modelContext` |
| Confirm | `data-agent-confirm="<sentence>"` on the committing control, for example `<AlertDialogClose value="confirm">` |
| Secret | `data-agent-secret` (password, card and one-time-code fields are secret already) |
| Hidden | `data-agent-hidden` |
| Refuse | In `onValueChange(value, details)`: `details.source === "agent"` and `details.cancel()` |
| Custom components | `definePrimitive({ ..., agent: { actions: [...] } })` with `closed`, `items`, `reveals`, `shown` or `secret` as needed |
| Only its parts are visible | Plain `<button>`, `<input>`, `<select>` and `<textarea>` are invisible to the bridge: use its `Button`, `Input`, `Select`, `Textarea` and `NumberInput` inside a `Field` |

Its skill (`npx skills@latest add vercel-labs/ui --skill ui-sdk`) includes an agent test to copy: snapshot every component, fail on any entry without a label, then run one `act` step per control the task names. Pick the library with [component libraries](component-libraries.md#ui-sdk-behaviors-for-five-frameworks) first; UI SDK is in beta.

## Other libraries

Radix, Base UI, React Aria, Ark UI, Reka UI and Bits UI have no agent bridge, but the naming, gating and state rules still apply. A browser agent reads their accessibility tree. Put the confirmation in the product flow (a confirm dialog with a specific sentence) rather than relying on the agent to ask. Mark secrets with the right `autocomplete` and `type` values, and keep hidden regions out of the DOM until a person reveals them.

## Review checklist

- [ ] Every control in a snapshot or the accessibility tree has a name a person would recognize, unique where it sits.
- [ ] Repeated rows give each control a verb plus the row's text.
- [ ] Every delete, pay, send, publish or invite is gated on the committing control, with a sentence built from app state.
- [ ] Secret fields can be filled, not read; hidden regions are hidden.
- [ ] App state follows change events; validation checks the value.
- [ ] An agent test or a screen-reader walkthrough covers every control the task names.
- [ ] The page works fully without WebMCP.
