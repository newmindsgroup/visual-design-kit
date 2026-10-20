---
name: figma-workflow
description: >-
  Runs the hands-on round trip between this kit and Figma through the official Figma MCP server: imports kit
  tokens as variables, builds variant components bound to them, pushes stylescapes or React screens into Figma,
  maps components with Code Connect, pulls frames back into code and prepares Dev Mode handoff, with a fallback
  when no Figma connector is available. Use when a task names Figma, a figma.com link, Dev Mode or Code Connect.
  Token and library architecture stay in design-system.
license: MIT
metadata:
  version-timestamp: "2026-10-20 10:35:33 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 10:35:33 UTC"
---

# Figma workflow

A good round trip leaves one source of truth (the DTCG tokens and the coded components), a Figma library that mirrors it exactly, and a screenshot proving each hop. Conventions for variables, styles, components and Code Connect live in [design-system's Figma reference](../design-system/references/figma.md); this skill is the procedure.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Direction of authority | Code and tokens lead; Figma mirrors | Exploration with no code: Figma first, then export once and flip authority |
| Skill gate | Load the matching figma skill before its tool, every session (table below) | Never skip; the skills carry API rules the tools assume |
| Target file | A file the user names; otherwise `create_new_file` after loading `figma-create-new-file` | Never write into a client file without its link in the brief |
| Token import | `tokens.py figma-script` output run once through `use_figma` | Plan or connector blocks it: [no-connector fallback](references/no-connector.md) |
| Collections | `Primitives` (modes Meridian, Ember; hidden, no scopes) and `Semantic` (Light, Dark, High contrast, aliases only) | Client brands replace the kit brands as Primitives modes |
| Components | Auto layout, every padding, gap, radius and fill bound to a variable; props named like the React props | |
| Reuse | `search_design_system` before creating anything | |
| Write size | Batch related, safely retryable work per `use_figma` call, as `figma-use` sizes it; one screenshot per finished phase | Split only at page boundaries or after a real failure |
| Verification | `get_screenshot` per finished phase, checked at 100%, every mode and brand | |
| Pull to code | Reuse `library/examples/react-system/` components and kit tokens; MCP code is a reference | |
| Fidelity proof | Figma frame PNG vs build with `compare_build.mjs` | |
| Unverified items | Plan limits and new Figma features marked "verify" | Confirm on figma.com pricing and help pages before quoting to a client |

## Skill gate

| Before calling | Load | Purpose |
| --- | --- | --- |
| `use_figma` (any write or scripted read) | `figma-use` | Plugin API rules, call sizing, recovery |
| Variables, component sets, theming in Figma | `figma-generate-library` with `figma-use` | Build order: foundations, then components |
| Pages, screens or composed UI in Figma | `figma-generate-design` with `figma-use` | Library discovery, section-by-section assembly, image capture |
| `get_code_connect_suggestions`, `send_code_connect_mappings`, `.figma.ts` files | `figma-code-connect` | Template format and publishing rules |
| `get_design_context` | `figma-design-to-code` | Screenshot target, asset handling, reuse rules |
| `create_new_file` | `figma-create-new-file` | File type and plan selection |
| Static HTML import, Code Layers | `figma-code-workflows` | Output choice: editable layers or runnable code |

If a listed skill is not available on the host, read the server's fallback (`skill://figma/<name>/SKILL.md`) before calling the tool.

## Workflow

1. **Confirm access.** Call `whoami`; note the plan and seat. Code Connect needs Organization or Enterprise and published components; mode counts per collection are plan-limited (verify on Figma's pricing page). If Figma tools are missing, switch to [the fallback](references/no-connector.md).
2. **Parse the link.** `figma.com/design/<fileKey>/<name>?node-id=1-2` gives `fileKey` and node `1:2`; a branch URL uses the branch key.
3. **Import tokens.** Run `python3 ../../library/scripts/tokens.py build`, then `tokens.py figma-script`, and pass the printed script to `use_figma`. It is idempotent; read the returned report (`created`, `updated`, `skipped`). Steps and post-import checks: [tokens and components](references/tokens-and-components.md).
4. **Finish foundations by hand.** Text styles bound to font variables, effect styles for shadows, grid styles, iOS and Android code syntax when native apps ship.
5. **Build components.** Variant sets whose properties match the React props (`variant`, `size`, `tone`), every state the coded component has, bindings checked with `get_variable_defs`. Order and naming: [tokens and components](references/tokens-and-components.md).
6. **Push a screen.** For a chosen stylescape or a React screen, capture a reference (`html_to_figma` for static HTML, `generate_figma_design` for a running app), rebuild it from library instances with `use_figma`, compare, then delete the capture. Details: [push and pull](references/push-and-pull.md).
7. **Connect code.** Map each published component to `library/examples/react-system/src/components/` with `.figma.ts` templates; the prop table is in [Code Connect map](references/code-connect-map.md).
8. **Pull a frame back.** `get_design_context` with a screenshot, map layers to existing components and tokens, build, then run `node ../design-critique/scripts/compare_build.mjs` against the exported frame.
9. **Hand off.** Mark frames Ready for dev only when states, breakpoints and annotations are complete; Dev Mode should show variables with code syntax and Code Connect snippets, not raw CSS.
10. **Inspect.** Screenshot every touched node in every mode. A script that returned without error is not a verified design.

## Naming conventions

- Variables: slash paths that mirror token names: `color/bg/surface-raised` is `--color-bg-surface-raised`. Never rename in Figma only.
- Components: PascalCase matching the React export (`Button`, `TextField`, `Badge`); properties lowercase like props (`size`), values like code values (`sm`, `md`, `lg`).
- Layers: roles, not defaults: `Label`, `Icon/Leading`, `Supporting text`; no `Frame 12`.
- Pages: `Cover`, `Foundations`, `Components/<Name>`, `Patterns`, `Screens/<Flow>`, `Archive`.
- Frames: `<Screen> / <width> / <theme>`, for example `Billing / 390 / Dark`.

## Decisions that change the answer

- **Plan tier.** Starter and Professional: no Code Connect, fewer modes; put brands in separate files or reduce modes, and hand off with Dev Mode variables only (verify current limits).
- **Existing client library.** Reconcile into it (the reconciliation path in `figma-generate-library`) instead of importing a parallel kit library; map client names to kit tokens in a table first.
- **Native apps.** Add iOS and Android code syntax and use `figma-swiftui` for SwiftUI in either direction.
- **Many brands.** Over five brands, consider extended collections (Enterprise, verify) rather than one mode per brand.
- **Images in the screen.** `use_figma` cannot fetch image URLs; run the `generate_figma_design` capture and copy its image fills, as `figma-generate-design` requires.

## Common failures

- Calling `use_figma` without `figma-use` loaded -> load it; most failed scripts break a rule it states.
- Hex values pasted into fills -> bind to semantic variables; `get_variable_defs` should list no raw colors.
- Semantic variables holding values instead of aliases -> re-run the import; never patch in Figma.
- Variant values that differ from code (`Primary` vs `primary`) -> rename in Figma to the code value, or map every value in Code Connect.
- Screens built from detached frames -> rebuild from library instances; detached screens drift on the next token release.
- Pulled code with absolute positioning and raw hex -> refactor to flex or grid and tokens before review.
- "Done" after one mode -> check Light, Dark and High contrast in both brands.

## References

- [Tokens and components](references/tokens-and-components.md): import, foundations, component build order, binding checks.
- [Push and pull](references/push-and-pull.md): stylescape or React screen into Figma; frame back to code; fidelity check.
- [Code Connect map](references/code-connect-map.md): react-system components to Figma properties, template example, publishing.
- [No connector](references/no-connector.md): token JSON export, development-plugin import, handoff package.
- [Figma conventions](../design-system/references/figma.md): variables, styles, auto layout, properties, libraries, Dev Mode.
- [Build fidelity](../design-critique/references/build-fidelity.md): thresholds and masks for `compare_build.mjs`.
- Deep process for client files: [Figma production](../../library/draft-skills/design-production-interface/references/figma.md), [stage handoff](../../library/draft-skills/design-stage-handoff/SKILL.md), [web fidelity](../../library/draft-skills/design-web-fidelity/SKILL.md).

Catalog IDs covered: production, handoff, web-fidelity, web-system-assembly, ui
