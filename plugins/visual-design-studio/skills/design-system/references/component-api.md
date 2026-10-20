# Component API design

Version-Timestamp: 2026-10-20 02:08:24 UTC

A component's API is its real interface: the names designers see in Figma, developers type in code and screen-reader users experience as behavior. Design it once, name it the same everywhere, and document the accessibility contract as part of the API. A React reference implementation of the kit's components is planned at `library/examples/react-system/`; the component specs in `library/examples/component-specs/` (button, text field, dialog, data table) already define states and behavior.

## Prop naming defaults

| Concept | Name | Values or shape | Notes |
| --- | --- | --- | --- |
| Visual emphasis | `variant` | `primary`, `secondary`, `ghost`, plus `danger` if needed | One emphasis axis only |
| Size | `size` | `sm`, `md`, `lg` | Match token t-shirt names; `md` default |
| Semantic color (status components) | `tone` | `neutral`, `info`, `success`, `warning`, `danger` | Badges, alerts, toasts; not for buttons that already have `variant` |
| Booleans | `disabled`, `required`, `loading`, `selected`, `invalid` | true or false | Positive phrasing; align with DOM attribute names; no `noX` props |
| Controlled value | `value`, `defaultValue`, `onValueChange` | | Same trio for every input |
| Open state | `open`, `defaultOpen`, `onOpenChange` | | Dialogs, popovers, menus, disclosures |
| Selection | `selected`/`selectedKeys`, `onSelectionChange` | | Lists, tabs, tables |
| Events | `onX` with the domain verb | `onDismiss`, `onSubmit` | Do not leak DOM events where a value is meant |
| Content | `children` first; named slots (`icon`, `description`, `actions`) for structured parts | ReactNode | Strings-only `label` props limit rich content |
| Accessible name for icon-only controls | `aria-label` (required by type when there is no visible label) | string | Enforce in types and lint |
| Styling escape hatch | `className` (merged), `style` | | Never `color="#..."`; accept tokens or variants |
| Element access | `ref` | | React 19 passes `ref` as a prop; older React needs `forwardRef` |

Naming rule: if the same concept exists on two components, it has the same prop name and values on both. Write the vocabulary down in the docs and lint for it.

## Variants vs booleans

- Mutually exclusive options are one enum (`variant="danger"`), never several booleans (`primary`, `danger`) that can be combined into nonsense.
- Independent on/off features are booleans (`loading`, `fullWidth`).
- A boolean that changes structure (adds an icon slot, a description row) is often better as an optional slot: pass the content, and the part appears.
- Figma mirrors this exactly: Variant properties for enums, Boolean properties for toggles, Instance swap or Slot for parts (see [Figma](figma.md)).

## Composition and slots

| Pattern | Use when | Example |
| --- | --- | --- |
| Simple props | Fixed anatomy, few options | `<Badge tone="success">Paid</Badge>` |
| Named slot props | 1-3 optional parts in fixed positions | `<TextField label="Email" description="We never share it" endAdornment={<Icon />} />` |
| Compound components | Several parts with shared state, flexible arrangement | `<Tabs.Root><Tabs.List><Tabs.Trigger value="a">A</Tabs.Trigger></Tabs.List><Tabs.Content value="a" /></Tabs.Root>` |
| Render props or state data attributes | Consumers need state for styling | `data-state="open"`, `data-disabled` for CSS selectors |

Avoid configuration objects that encode a whole UI tree (`items=[{ type: "divider" }]`) except for genuinely data-driven components (tables, menus from data), and then also offer a composable version.

## Controlled vs uncontrolled

- Support both: uncontrolled with `defaultValue` for simple forms, controlled with `value` plus `onValueChange` when the app owns state.
- Never switch modes during a component's life; warn in development when `value` changes from undefined to defined.
- Change callbacks receive the new value (and optionally details), not a raw event, so the API stays identical on web and native.

## Polymorphism

| Approach | How | Tradeoff |
| --- | --- | --- |
| `asChild` (Radix-style Slot) | Component merges its props, handlers and ref onto its single child | Clean types, works with router links; the child must forward props and ref |
| `render` prop (Base UI, Ariakit style) | `render={<a href="/x" />}` or a render function | Explicit; similar outcome to `asChild` |
| `as` prop | `<Button as="a" href="/x">` | Familiar; types get heavy and slow in TypeScript |

Rule: semantics follow behavior. Navigation is a link (`<a href>`) even when it looks like a button; an action is a `<button>`. Polymorphism exists to keep the styling while using the right element.

## Accessibility contracts (part of the API)

Base behavior on the WAI-ARIA Authoring Practices Guide patterns and test with real assistive technology.

| Component | Element or role | Keyboard | Focus and announcements |
| --- | --- | --- | --- |
| Button | `button` | Enter and Space activate | `aria-disabled` keeps it focusable when it must explain why; `loading` sets `aria-busy` and blocks duplicate activation |
| Link | `a[href]` | Enter | Visited and external indication where useful |
| Checkbox / Switch | `checkbox` / `switch` | Space toggles | Label click toggles; switch states are on and off, not checked text |
| Radio group | `radiogroup` with `radio` items | Arrow keys move and select; Tab enters and leaves the group | One tab stop |
| Select / Combobox | `combobox` with `listbox` | Arrow keys, typeahead, Enter selects, Esc closes | Active option via `aria-activedescendant` or roving focus |
| Menu | `menu` with `menuitem` | Arrows, Home and End, typeahead, Esc closes and returns focus | Not for site navigation (use a list of links) |
| Tabs | `tablist`, `tab`, `tabpanel` | Arrows move between tabs; automatic or manual activation documented | One tab stop for the list |
| Dialog | `dialog` with `aria-modal="true"` | Esc closes (unless destructive work is unsaved) | Focus moves in, is trapped, and returns to the trigger; title labels the dialog |
| Tooltip | `tooltip` | Shows on focus and hover; Esc dismisses | Never the only place for essential info; not on disabled controls |
| Toast | `status` or `alert` live region | Actions reachable by keyboard | Do not auto-dismiss toasts that contain actions in under 5 seconds; pause on hover and focus |
| Disclosure / Accordion | `button` with `aria-expanded` controlling a region | Enter and Space | Headings wrap the triggers |

Every component also guarantees: visible focus (2px or more, 3:1 contrast), target size at least 24x24 CSS px (44x44 for touch-first), no information by color alone, respects reduced motion, and works at 200% zoom and 320 CSS px width.

## Headless libraries

| Library | Frameworks | Strengths | Watch for |
| --- | --- | --- | --- |
| Radix Primitives | React | Mature primitives, `asChild`, wide adoption (shadcn/ui's original base) | Check current maintenance activity before adopting |
| React Aria Components (Adobe) | React | Deep accessibility and internationalization, mobile and screen-reader testing, date and number handling | More verbose API (`isDisabled`, `onPress`) |
| Base UI (MUI team) | React | Stable v1 since December 2025, `render` prop, actively developed | Newer; smaller ecosystem |
| Headless UI (Tailwind Labs) | React, Vue | Simple API, Tailwind-friendly, anchor positioning | Smaller component set |
| Ark UI | React, Solid, Vue, Svelte | Zag.js state machines shared across frameworks | Machine concepts to learn |
| Reka UI, Bits UI, Melt UI | Vue (Reka), Svelte (Bits, Melt) | Radix-like primitives outside React | Framework-specific |

Choose one primitive layer per system. Wrapping two libraries behind one API doubles the bugs.

## The shadcn/ui copy-in model

shadcn/ui is a CLI and registry that copies component source (Tailwind classes on a primitive layer, Radix or Base UI as of 2026 per its docs; verify) into your repository. You own the code.

| Benefit | Cost |
| --- | --- |
| Full control; no version lock on a component package | Upstream fixes do not arrive automatically; you diff and merge |
| Readable source, easy to theme with CSS variables | Each product that copies diverges unless you publish your own registry |
| Fast start for prototypes and small teams | Accessibility and quality are yours to maintain and test |

Default for a design system that serves several products: publish the system as a versioned package (or your own shadcn-compatible registry) so every product upgrades the same code. Use raw copy-in for a single product or a prototype.

## Cross-platform parity

Keep concept names aligned: a `variant="primary" size="lg"` button on web is a `.buttonStyle(.kitPrimary)` with a large control size in SwiftUI and a filled `Button` with the large size in Compose. Document the mapping per component; do not force web prop names into native APIs that have their own idioms.

## Common failures

- Prop sprawl: 25 booleans on a Card. Split into composable parts.
- Same idea, different names: `isOpen` on Modal, `visible` on Popover, `show` on Tooltip.
- Icon-only buttons without an accessible name, enforced nowhere.
- `disabled` used to hide unfinished features: remove them instead, or explain with `aria-disabled` and a reason.
- Components that accept raw colors or pixel values and bypass tokens.
