# Code Connect map for the react-system components

Version-Timestamp: 2026-10-20 10:35:33 UTC

Code Connect shows real component usage in Dev Mode instead of generated CSS. This file maps the kit's reference components in `library/examples/react-system/src/components/` to the Figma component properties they should have, so the library built in [tokens and components](tokens-and-components.md) connects without renaming. Background and plan requirements: [design-system's Figma reference](../../design-system/references/figma.md#code-connect).

## Requirements (as of 2026-10-20; verify on Figma's help center)

- Organization or Enterprise plan, a Design or Dev Mode seat, and components published to a team library. Free and Professional plans cannot use Code Connect.
- Template files only: `ComponentName.figma.ts` with a `figma.code` tagged template. Do not write `.figma.tsx` files or `figma.connect()` calls; that is the older parser-based format.
- Load `figma-code-connect` before `get_code_connect_suggestions` or `get_context_for_code_connect`.
- For type checking, add `@figma/code-connect/figma-types` to `compilerOptions.types` in `tsconfig.json`.

## Workflow

1. `get_code_connect_suggestions` on the library page (`fileKey`, `nodeId`, `excludeMappingPrompt: true`) lists published components without mappings.
2. `get_context_for_code_connect` per component (`clientFrameworks: ["react"]`, `clientLanguages: ["typescript"]`) returns the exact property names and every variant value.
3. Write `src/components/<name>.figma.ts` next to the component (or wherever `figma.config.json` `include` points). Map every variant value the context returned; an unmapped value renders as `undefined`.
4. Validate against the component's props type: never emit a prop the component does not accept.
5. Publish with the Code Connect CLI (`npx figma connect publish`, token in `FIGMA_ACCESS_TOKEN`) or through the MCP mapping tools (`send_code_connect_mappings`), then open Dev Mode on one instance of each variant and read the snippet.

## Property map

Figma property names are lowercase like the props; variant values are the code values, so `getEnum` maps identity pairs. Design-only properties (a `state` variant that draws hover or pressed) are not mapped.

| Component (file) | Figma variant properties | Booleans and text | Instance swaps and slots |
| --- | --- | --- | --- |
| `Button` (button.tsx) | `variant`: primary, secondary, ghost, danger. `size`: sm, md, lg | `label` (text), `loading`, `disabled`, `fullWidth` | `startIcon`, `endIcon` (`Icon/*`) |
| `Badge` (badge.tsx) | `tone`: neutral, accent, info, success, warning, danger. `variant`: subtle, outline. `size`: sm, md | `label` (text) | `icon` |
| `TextField` (text-field.tsx) | `size`: sm, md, lg | `label`, `hint`, `error` (text); `invalid`, `disabled`, `required` | `startAdornment`, `endAdornment` |
| `Select` (select.tsx) | none beyond states | `label`, `hint`, `error`, `placeholder` (text); `invalid`, `disabled` | none |
| `Checkbox` (checkbox.tsx) | none | `label`, `description`, `error` (text); `checked`, `invalid`, `disabled` | none |
| `Switch` (switch.tsx) | `labelPlacement`: start, end | `label`, `description` (text); `checked`, `disabled` | none |
| `Card` (card.tsx) | `variant`: outlined, elevated, sunken. `padding`: none, sm, md | `interactive` | content slot: `CardHeader`, `CardTitle`, `CardDescription`, `CardFooter` |
| `Alert` / `Banner` (alert.tsx) | `tone`: info, success, warning, danger. Layout is the component choice: `Alert` (inline) or `Banner` | `title` (text), dismissible | `actions` |
| `Tabs` (tabs.tsx) | none | tab label (text), `count` | `icon` |
| `Dialog` (dialog.tsx) | `size`: sm, md, lg. `role`: dialog, alertdialog | `title`, `description` (text); `closeButton` | body and footer slots |
| `EmptyState` (empty-state.tsx) | `size`: sm, md | `title`, `description` (text) | `icon`, `actions` |
| `DataTable` (data-table.tsx) | `density`: compact, default, comfortable | caption (text) | row and cell components |

Read each component's props type before writing its template: names above were read from the source on 2026-10-20 and the source wins if they differ.

## Template example: Button

```ts
// Illustrative, not run here. src/components/button.figma.ts
// url=https://www.figma.com/design/<fileKey>/<fileName>?node-id=<nodeId>
// source=src/components/button.tsx
// component=Button
import figma from 'figma'
const instance = figma.selectedInstance

const variant = instance.getEnum('variant', { primary: 'primary', secondary: 'secondary', ghost: 'ghost', danger: 'danger' })
const size = instance.getEnum('size', { sm: 'sm', md: 'md', lg: 'lg' })
const label = instance.getString('label')
const loading = instance.getBoolean('loading')
const disabled = instance.getBoolean('disabled')
const start = instance.getInstanceSwap('startIcon')
const startIcon = start && start.type === 'INSTANCE' ? start.executeTemplate().example : null

export default {
  example: figma.code`<Button variant="${variant}" size="${size}"${loading ? ' loading' : ''}${disabled ? ' disabled' : ''}${startIcon ? figma.code` startIcon={${startIcon}}` : ''}>
  ${label}
</Button>`,
  imports: ['import { Button } from "../components/button"'],
  id: 'button',
  metadata: { nestable: true },
}
```

Icons get their own templates (`Icon/Check` maps to `<IconCheck />` from `icons.tsx`) so the button's `startIcon` resolves through `executeTemplate()` instead of a hard-coded icon.

## Checks after publishing

- Every variant value of every mapped component shows a snippet in Dev Mode; none prints `undefined`.
- Snippets compile when pasted into the project (`npm test` in react-system runs `tsc` on prop types).
- Nested instances (icon in button, badge in card) render through their own templates.
- The `imports` line matches how the project imports components; replace the react-system path with the client's package (`@client/ui`) in client work.
- Unmapped components are listed in the library's README page with the reason (design-only, deprecated, planned).

## When the plan does not allow Code Connect

Put the import line and a usage snippet in each component's Figma description, keep property names identical to props, and link the component's documentation page. Dev Mode then shows the variables with WEB code syntax, which covers most of the handoff value without snippets.
