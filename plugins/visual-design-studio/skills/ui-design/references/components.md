# Components

Version-Timestamp: 2026-10-20 02:04:32 UTC

A component is specified when someone else could build it without asking a question: every part named, every state drawn, every size and token mapped, keyboard and screen reader behavior written down. The filled examples in the kit show the depth: [button](../../../library/examples/component-specs/button.md), [text field](../../../library/examples/component-specs/text-field.md), [dialog](../../../library/examples/component-specs/dialog.md) and [data table](../../../library/examples/component-specs/data-table.md).

## Anatomy

Name every part, then decide which are required, optional or conditional.

| Component | Parts |
| --- | --- |
| Button | Container, label, optional leading or trailing icon, optional busy indicator, focus ring, hit area |
| Text field | Label, optional hint, input container, value or placeholder example, optional prefix or suffix (unit, icon, clear button), character counter, error message, focus ring |
| Select / combobox | Label, trigger with value, chevron, listbox popup, options (with optional description, icon, check), group headings, empty result, loading row |
| Checkbox / radio | Box or circle, check or dot mark, label, optional description; group legend |
| Switch | Track, thumb, label; optional on/off text for clarity |
| Card | Container, media, eyebrow, title (the primary link), body, metadata, actions |
| Dialog | Scrim, container, title, body, actions, close button, focus trap boundary |
| Toast | Container, icon, message, optional single action, optional dismiss |

## State matrix

Every interactive component needs a decision for each state. Token names are the kit's semantic API.

| State | Trigger | Visual treatment (default recipe) | Notes |
| --- | --- | --- | --- |
| Rest | None | Base tokens, e.g. primary button `--color-accent-default` with `--color-fg-on-accent` | Must meet contrast at rest |
| Hover | Pointer over | `--color-accent-hover`; secondary: tint with `--color-accent-subtle` | Wrap in `@media (hover: hover)` so touch devices do not stick in hover |
| Focus-visible | Keyboard or programmatic focus | 2px `--color-focus-ring` outline, 2px offset | Distinct from hover; never `outline: none` without a replacement |
| Pressed / active | Pointer down, Space or Enter held | `--color-accent-active`; optional 1px translate or 0.98 scale over `--duration-fast` | No mutation on pointer-down (WCAG 2.5.2) |
| Selected / checked | Choice made | Fill or check mark plus a non-color cue | Expose `aria-pressed`, `aria-selected` or `checked` |
| Indeterminate | Partial selection in a group | Dash mark | Header checkboxes in tables |
| Disabled | Unavailable | `--color-fg-subtle` on `--color-bg-sunken`; no hover; cursor `not-allowed` | Exempt from contrast rules, but explain why nearby; consider `aria-disabled` so it stays focusable and discoverable |
| Read-only | Visible but not editable | No input border, value still selectable and copyable | Not the same as disabled |
| Loading / busy | Action in progress | Inline spinner replaces or follows the label; width locked | `aria-busy`; block repeat activation in the handler |
| Invalid / error | Validation failed | `--color-danger-border` border, icon plus message in `--color-danger-fg` | `aria-invalid="true"`, message linked with `aria-describedby` |
| Success / valid | Confirmed result | `--color-success-fg` icon and text | Use sparingly; do not mark every valid field green |
| Dragging | Item picked up | `--shadow-lg`, slight scale, placeholder slot | Provide a non-drag alternative (WCAG 2.5.7) |
| Visited | Link already followed | Optional muted color for content links | Not for navigation or buttons |

Combined states need explicit answers: selected + hover, selected + focus, error + focus (the focus ring stays visible on top of the error border), disabled + selected.

## Size scale

| Size | Height | Horizontal padding | Font size | Icon | Gap | Use |
| --- | --- | --- | --- | --- | --- | --- |
| sm | 32px | 12px (`--space-3`) | `--font-size-sm` (14px) | `--size-icon-sm` (16px) | `--space-1` | Dense tables, toolbars, filters |
| md | 40px | 16px (`--space-4`) | `--font-size-sm` or `--font-size-md` | `--size-icon-md` (20px) | `--space-2` | Default for desktop web and apps |
| lg | 48px | 20px (`--space-5`) | `--font-size-md` (16px) | `--size-icon-lg` (24px) | `--space-2` | Touch-first, marketing CTAs, older audiences |

Rules:

- Controls that sit in one row (input + button, select + button) share the same size.
- A 32px control still needs a 24x24 minimum target; for touch, extend the hit area to 44x44 with padding or a pseudo-element without changing the visual size.
- Icon-only buttons are square: 32, 40 or 48px.
- Text inputs on iOS need a font size of at least 16px or Safari zooms the page on focus.
- Similar scales appear in public systems: IBM Carbon uses 32/40/48px fields and buttons, Material 3 uses 40dp buttons with 48dp touch targets. Confirm current values in their docs if you are matching them.

## Density modes

| Mode | Control height | Table row | Spacing step | Who |
| --- | --- | --- | --- | --- |
| Compact | 32px | 32px | One `--space-*` step down | Expert data tools, opt-in only |
| Default | 40px | 40px | Base | Most products |
| Comfortable | 48px | 48px | One step up | Touch-first, older adults, low-frequency users |

Implement with a `data-density` attribute on a container that overrides component-tier tokens. Let users choose density in data-heavy products and remember the choice. Never let compact mode drop targets below 24px or text below 12px.

## Buttons

- **Hierarchy:** primary (one per region), secondary, tertiary or ghost, destructive, link-style. Two primaries side by side means the decision was not made.
- **Placement:** in page forms, the primary button aligns with the left edge of the fields. In dialogs, follow the platform: macOS and Material put the confirming action last (rightmost); Windows puts it first, before Cancel, with both right-aligned. On the web pick one rule per product and keep it.
- **Labels:** verb + object, sentence case ("Create project"). Keep the label during loading and lock the width.
- **Destructive styling** (`--color-danger-*`) only on the final confirm, not on the button that opens the confirmation.

## Selection controls

| Need | Control |
| --- | --- |
| Independent on/off choices, or agreeing to terms | Checkbox |
| One of 2-5 options, all visible | Radio group |
| One of 2-5 views or modes, immediate effect | Segmented control |
| Setting that takes effect immediately | Switch (never inside a form that has a Save button) |
| One of about 6-15 options | Select |
| One of many, or searchable | Combobox with filtering |
| Several of many | Multi-select combobox or checkbox list with search |
| Filter tokens | Chips |

## Overlays

| Overlay | Use for | Do not use for | Behavior |
| --- | --- | --- | --- |
| Tooltip | Short supplementary text, names of icon buttons | Essential instructions, interactive content | Appears on hover and focus after a short delay (about 300-500ms is common); dismissible with Esc, hoverable, persistent while hovered (WCAG 1.4.13) |
| Popover | Small interactive content (pickers, filters, previews) | Long forms | Non-modal; Esc closes; focus moves in and returns to trigger |
| Menu | A list of actions or options from a button | Site navigation | ARIA menu button pattern; arrow keys move; Enter activates |
| Dialog | Decisions that block progress, short focused tasks | Success messages, long reading | Modal: focus trap, Esc closes (unless destructive data loss), focus returns to trigger; width 400-640px |
| Drawer / sheet | Detail panels, filters on mobile, secondary navigation | Critical confirmations | Side drawer 320-480px; bottom sheet on mobile with a drag handle and a close button |
| Toast | Transient confirmation of the user's own action | Errors that need action | See [states and feedback](states-and-feedback.md) |

Use the native `dialog` element or a proven headless library (Headless UI, Radix, React Aria) rather than hand-rolled focus management. Layers use `--z-dropdown`, `--z-sticky`, `--z-overlay`, `--z-modal`, `--z-toast`.

## Cards

- One primary link per card (the title), stretched over the card with a pseudo-element; secondary actions sit above that layer.
- Do not nest interactive cards inside interactive cards.
- Card everything only when items are truly separate objects; lists and tables are denser and easier to scan.
- Consistent media aspect ratios (16:9, 4:3, 1:1) across a grid.

## Icons

- Sizes 16, 20 and 24px (`--size-icon-sm`, `--size-icon-md`, `--size-icon-lg`), drawn on a pixel grid, stroke 1.5-2px, one family across the product.
- Label icons with text wherever space allows; icon-only buttons need an accessible name and a tooltip.
- Decorative icons get `aria-hidden="true"`.
- Never use emoji as interface icons.

## Theming through tokens

Components consume semantic tokens only, never primitives or raw hex values. A primary button maps to `--color-accent-default`, `--color-accent-hover`, `--color-accent-active`, `--color-fg-on-accent` and `--color-focus-ring`; a text field to `--color-bg-surface`, `--color-border-default`, `--color-border-strong` (hover), `--color-fg-default`, `--color-fg-subtle` (placeholder) and `--color-danger-border` (error). Brands (`data-brand`) and modes (`data-theme`) then work without component changes.

Nested radius rule: inner radius = outer radius minus the padding between them (a 12px card with 4px padding holds 8px inner elements).

## Spec template for a new component

```text
Name and ID:          C-xxx, version, owner
Purpose:              One sentence; when to use, when to use something else
Anatomy:              Parts, required/optional
Variants:             Emphasis, size, with/without icon
States:               Full matrix above, including combined states
Content rules:        Label length, truncation, wrapping, localization expansion
Tokens:               Every visual value mapped to a semantic token
Keyboard:             Keys and resulting behavior
Screen reader:        Role, name, state, description, announcements
Responsive:           Behavior at sm, md, lg breakpoints and in narrow containers
Motion:               Duration and easing tokens; reduced-motion behavior
Acceptance checks:    How to verify each requirement
```
