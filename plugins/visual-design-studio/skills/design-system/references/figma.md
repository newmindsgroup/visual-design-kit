# Figma: variables, components, libraries, Dev Mode and Code Connect

Version-Timestamp: 2026-10-20 02:08:24 UTC

Figma is the design-side mirror of the token source, never a second master. Tokens flow from `library/tokens/src/` to Figma variables; components in Figma mirror coded components and link to them with Code Connect. Figma plan limits and features change often: items marked "verify" come from Figma announcements or community reports rather than Figma's help center, which could not be reached from this environment on 2026-10-20.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Source of truth | DTCG files in the repository; Figma variables are imported or synced from them | Early exploration with no code yet: Figma first, then export once and flip authority |
| Collections | The kit's export: `Primitives` (modes are brands: Meridian, Ember; hidden from publishing, no scopes) and `Semantic` (modes Light, Dark, High contrast, aliasing primitives) | Client systems with many brands: brands in their own collection or extended collections |
| Variable naming | Slash groups mirroring token paths: `color/bg/surface-raised` for `--color-bg-surface-raised` | Never rename in Figma only |
| Scopes | Set on every variable; primitives get no scopes so they never appear in pickers | |
| Code syntax | Set WEB, iOS and ANDROID syntax on every semantic variable | |
| Typography | Text styles whose font family, size, line height and weight are bound to variables | |
| Effects and gradients | Effect styles (shadows) and color styles only for gradients | |
| Components | Auto layout everywhere, properties named exactly like code props | |
| Library files | Foundations, Components, Icons, Patterns as separate published files | Small team: one library file with clear pages |

## Variables

- **Types**: color, number, string, boolean. Use number for space, radius, sizes, border widths, opacity; string for font family names; boolean for visibility toggles in prototypes.
- **Collections and modes**: a collection groups variables that share modes. Modes per collection are plan-limited; community reports of a Figma staff announcement after mid-2025 put Professional at 10 and Organization at 20, with Enterprise higher (verify on Figma's pricing page). Starter plans support very few modes.
- **Aliasing**: semantic variables alias primitive variables, with a different alias per mode (`color/bg/canvas` points to `neutral/0` in Light and `neutral/950` in Dark). Keep the alias chain identical to the DTCG source.
- **Scoping** (shows variables only where they make sense):

| Variable group | Scopes |
| --- | --- |
| Background colors | Frame fill, Shape fill |
| Text colors | Text fill |
| Border colors | Stroke |
| Space | Gap (and padding) |
| Radius | Corner radius |
| Size | Width and height |
| Primitives | None (hidden) |

- **Code syntax**: WEB uses the CSS function form, `var(--color-bg-canvas)`; iOS and ANDROID use the generated platform names without a wrapper (for example `KitColor.bgCanvas`, `MaterialTheme.colorScheme.surface`). Dev Mode shows these to developers instead of hex.
- **Multi-brand**: either a Brand collection whose modes are brands (simplest), or **extended collections** that inherit a parent collection and override selected values per brand (announced at Figma's Schema 2025 for Enterprise; verify availability). Do not duplicate whole libraries per brand.
- **Import and export**: Figma announced native variable import and export in the DTCG format; rollout status was unclear in late 2025 (verify). Alternatives: a DTCG import plugin, the Variables REST API (reported to need an Enterprise plan; verify), or a `use_figma` script through the Figma MCP server.

## Importing the kit's tokens

1. Build: `python3 plugins/visual-design-studio/library/scripts/tokens.py build` writes [figma-variables.json](../../../library/tokens/dist/figma-variables.json): 2 collections and about 220 variables in the 2026-10-20 build (color, number and string, plus easing and timing values), each with scopes, a description, WEB code syntax and per-mode values or aliases (`{"alias": {"collection": "Primitives", "name": "color/neutral/50"}}`). Colors are 0-1 RGBA, numbers are px (rem x 16), times are seconds.
2. Import: load the `figma-use` skill, run `python3 plugins/visual-design-studio/library/scripts/tokens.py figma-script`, and pass the printed script to the Figma MCP `use_figma` tool in the target design file. The script ([figma-import.js](../../../library/tokens/figma-import.js)) is idempotent: it matches collections, modes and variables by name and updates them in place, so re-running after a token release keeps existing bindings. Native DTCG import or a plugin are alternatives where the plan allows.
3. Finish by hand what variables cannot hold (the file's `notExported` notes): text styles with line heights 110/125/150/165% and letter spacing -2/0/1/6%; effect styles for `shadow-sm` to `xl` from `tokens.resolved.json` (values differ per mode); layout grids with 16-32px gutters; frame widths at the breakpoints.
4. Add iOS and ANDROID code syntax if the project ships native apps (the export sets WEB only).
5. Verify in Figma: variable counts per collection match the export, every mode resolves, semantic values are aliases (not pasted colors), scopes and code syntax are present, and a specimen page shows the lint contrast pairs correctly in each mode and brand.
6. Record the token version in the library description. Re-import on every token release; never patch values in Figma.

## Styles vs variables

| Need | Use | Why |
| --- | --- | --- |
| Single color, number or string | Variable | Modes, aliasing, scoping, code syntax |
| Typography (family, size, weight, line height, letter spacing together) | Text style with bound variables | One-click application; values still come from tokens |
| Shadows and blurs | Effect style | Composite values |
| Gradients and image fills | Color style | Variables hold single colors |
| Layout grids | Grid style | Responsive frame setup |

## Auto layout conventions

- Every component and every screen section uses auto layout. Padding and gap bind to space variables (`space/2`, `space/4`), never typed numbers.
- Sizing: Hug for content-sized elements (buttons, chips), Fill for elements that stretch (inputs, cards in a grid), Fixed only for icons, avatars and media with a set ratio.
- Set min and max width on text containers to show wrapping and measure; use wrap for chip and tag groups.
- Absolute position only for overlays such as badges and close buttons.
- Name layers by role (`Label`, `Icon/Leading`, `Supporting text`), not `Frame 12`; layer names become Code Connect hooks and accessibility notes.
- Build responsive behavior into the component (fill containers, wrap, min widths) and show breakpoints as separate example frames, not separate components.

## Component properties

| Figma property | Use for | Code equivalent |
| --- | --- | --- |
| Variant | Mutually exclusive visual axes: `variant`, `size`, documented `state` | Enum prop |
| Boolean | Show or hide a part: `hasIcon`, `showHelperText` | Boolean prop or optional child |
| Instance swap | Swap a fixed part: the leading icon, an avatar | `icon` prop or element prop |
| Slot (where available) | Freeform content areas: card body, dialog content | `children` or named slot props |
| Text | Editable labels | String prop or children |

- Name properties exactly like code props (`size`, `variant`, `disabled`), with values matching code values (`sm`, `md`, `lg`).
- Keep variant counts down: size x variant x state multiplies quickly. Use booleans and instance swaps for parts, and interactive components (prototype hover and pressed) rather than separate published variants where possible.
- Include every state the coded component supports (default, hover, focus, pressed, disabled, loading, error, selected) so design and code reviews compare like with like. The component specs in `library/examples/component-specs/` list the expected states.

## Library publishing

- Separate files by layer: Foundations (variables, text and effect styles), Components, Icons, Patterns and templates. Product files consume libraries; they never copy components.
- Use branching (Organization and Enterprise) for changes that touch many components; review the branch like a pull request.
- Publish with release notes that name the version, added, changed, deprecated and removed items, and match the code changelog ([governance and versioning](governance-and-versioning.md)).
- Deprecate in place: move the component to a "Deprecated" page, prefix its name, describe the replacement, and keep it published until the code removal release.
- Watch library analytics for insertions, detachments and unused components; frequent detachment of one component means its API is missing something.

## Dev Mode

- Mark frames "Ready for dev" only when states, responsive examples and annotations are complete.
- Annotations carry what the canvas cannot: keyboard behavior, focus order, ARIA roles, truncation rules, motion specs, analytics events.
- Developers should see variables with code syntax and Code Connect snippets instead of generated CSS; generated CSS from layers is a reference, not production code.

## Code Connect

- Code Connect maps published Figma components to coded components so Dev Mode shows real usage snippets. As of Figma's code-connect repository README (checked 2026-10-20), **template files** (`ComponentName.figma.ts`) are the maintained approach; framework-specific parsers no longer receive updates. Integrations cover React and React Native, HTML (Web Components, Angular, Vue), SwiftUI and Jetpack Compose.
- Requires an Organization or Enterprise plan and a full Design or Dev Mode seat; components must be published to a team library.
- Map every variant value explicitly; an unmapped enum value renders as undefined.

```ts
// Illustrative, not run here. Button.figma.ts
// url=https://www.figma.com/design/<fileKey>/<fileName>?node-id=<nodeId>
import figma from 'figma'
const instance = figma.selectedInstance

const variant = instance.getEnum('variant', { Primary: 'primary', Secondary: 'secondary', Ghost: 'ghost' })
const size = instance.getEnum('size', { Small: 'sm', Medium: 'md', Large: 'lg' })
const label = instance.getString('label')
const disabled = instance.getBoolean('disabled')

export default {
  example: figma.code`<Button variant="${variant}" size="${size}" disabled={${disabled}}>${label}</Button>`,
  imports: ['import { Button } from "@kit/react"'],
  id: 'button',
}
```

Publish with the Code Connect CLI (`npx figma connect publish`) or create mappings through the Figma MCP server; review the snippet in Dev Mode for each variant.

## Working with the Figma MCP server and figma skills in Claude

| Task | Skill to load | Main MCP tools |
| --- | --- | --- |
| Create or edit anything in a file (variables, components, auto layout) | `figma-use` (always first) | `use_figma` |
| Build or reconcile a design system library from code | `figma-generate-library` with `figma-use` | `get_libraries`, `search_design_system`, `use_figma`, `get_variable_defs` |
| Map components to code | `figma-code-connect` | `get_code_connect_suggestions`, `get_context_for_code_connect`, `send_code_connect_mappings`, `get_code_connect_map` |
| Implement a Figma design in code | `figma-design-to-code` (required before `get_design_context`) | `get_design_context`, `get_screenshot`, `get_variable_defs` |
| Build screens from the library | `figma-generate-design` | `search_design_system`, `use_figma` |
| SwiftUI in either direction | `figma-swiftui` | as above |

- Always search the existing library (`search_design_system`) before creating components; reuse beats regeneration.
- Treat MCP output as a reference to adapt to the project's components and tokens, not production code.
- Reopen and screenshot the file after any scripted change and inspect variants, bindings and auto layout; a successful script run is not visual approval. The draft [Figma production workflow](../../../library/draft-skills/design-production-interface/references/figma.md) has the acceptance checks for client files.
