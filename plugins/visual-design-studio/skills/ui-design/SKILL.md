---
name: ui-design
description: >-
  Designs and specifies interface components, states and interaction patterns: forms, tables, navigation, dashboards,
  onboarding, auth and passkeys, pricing, checkout, search and filters, settings, empty, loading and error states,
  notifications, and AI chat and agent interfaces, all to WCAG 2.2 AA. Use when designing screens or components, writing
  a component spec or state matrix, choosing a pattern, building a chat or agent UI, or checking keyboard and
  accessibility behavior.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:04:32 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:04:32 UTC"
---

# UI design

Excellent UI is predictable, fast and calm: every control looks like what it does, every state is designed (not just the happy one), and people can finish the task with a mouse, a finger, a keyboard or a screen reader. Distinctiveness comes from the brand's tokens and composition, not from reinventing controls.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Control height | sm 32 / md 40 / lg 48px; md for desktop apps | Touch-first or older audiences: 48; dense expert tools: 32 with 24px minimum hit area |
| Target size | At least 24x24 CSS px (`--size-target-min`, WCAG 2.5.8); 44x44 for touch (`--size-target-comfortable`) | Never below 24 |
| Focus | 2px `--color-focus-ring` outline, 2px offset, on `:focus-visible`; never hidden by sticky UI (2.4.11) | High-contrast theme: 3px |
| Contrast | Text 4.5:1 (3:1 at 24px+ or 18.66px+ bold); borders, icons and focus 3:1 | High-contrast mode: 7:1 body text |
| Spacing | 4px base: inside controls `--space-2` to `--space-4`; between related items `--space-2`/`--space-3`; between groups `--space-6`/`--space-8` | Compact density: one step down |
| Radius | `--radius-md` (8px) controls and cards; `--radius-lg` (12px) dialogs and sheets; `--radius-full` pills and avatars | Style recipe says otherwise (Swiss: 0-2px; playful: 12-16px) |
| Type | Body `--font-size-md` (16px); dense apps `--font-size-sm` (14px); labels medium weight; `tabular-nums` for figures | Long reading: 18px, `--line-height-relaxed` |
| Elevation | `--shadow-sm` raised cards, `--shadow-md` menus and popovers, `--shadow-lg` dialogs; layers from `--z-*` | Flat styles: borders and tone instead of shadow |
| Motion | Hover and press `--duration-fast`; expand `--duration-moderate`; dialogs and sheets `--duration-slow` with `--ease-decelerate` in, `--ease-accelerate` out | `prefers-reduced-motion`: fade or none |
| Loading | Under 1 s: no spinner; 1-10 s: skeleton or inline spinner with text; over 10 s: determinate progress plus cancel | Known-fast actions: optimistic update |
| Primary actions | One primary button per region; labels are verb + object | Destructive confirm: the destructive button is the primary |
| Feedback surface | Inline for field and section issues; toast for transient confirmations with Undo; banner for persistent status; dialog only for decisions | Never put errors that need action in a toast |
| Forms | Single column, labels above, validate on blur, inline errors plus summary on submit | Very short inline forms (search, subscribe): one row |
| Tables | Text left, numbers right with tabular figures; rows 32/40/48px by density; sticky header | Under 640px: priority columns or card list |
| AI and agents | Stream output; Stop replaces Send; show sources; ask before any irreversible or external action | Fully read-only agents: no approval step |

## Workflow

1. **Collect the flow and states** from `ux-design` (flows with state IDs, content, requirements). If none exist, list the screens and their states first.
2. **Inventory existing components** in the client's system or the kit tokens (`../../library/tokens/dist/tokens.css`). Extend before inventing; use the `design-system` skill for token and API decisions.
3. **Pick patterns** from the references: [forms](references/forms.md), [navigation](references/navigation.md), [data-dense UI](references/data-dense-ui.md), [flows](references/flows.md), [AI interfaces](references/ai-interfaces.md).
4. **Specify each component**: anatomy, variants, sizes, the full state matrix, content rules, keyboard and ARIA, responsive behavior ([components](references/components.md)). Map every visual value to a semantic token.
5. **Design every state** with [states and feedback](references/states-and-feedback.md): empty, loading, partial, error, success, offline, permission.
6. **Use realistic content**: long names, 30-40% text expansion, large numbers, missing images, zero and one items, and 10,000 items.
7. **Render and inspect.** Build or mock the screen, screenshot at 375, 768 and 1280px in light and dark, and with keyboard focus visible; review with the `design-critique` skill and fix the generic-AI tells it lists.
8. **Accessibility pass** with the [WCAG 2.2 AA checklist](references/accessibility.md): keyboard walkthrough, screen reader spot check, zoom to 200% and reflow at 320px.
9. **Hand off** the spec, state matrix and token map; compare against the filled examples in `../../library/examples/component-specs/`.

## Decisions that change the answer

- **Platform.** Web follows these defaults. iOS and Android follow platform conventions through the `native-app-design` skill. Shared public touchscreens and kiosks use the touch drafts below (attract loops, idle reset, privacy between users).
- **Audience.** Run `python3 ../../library/scripts/atlas.py query "<audience and product>"`. Expert power users: compact density, keyboard shortcuts, command palette, bulk actions. Older adults and low-literacy audiences: 48px controls, 18px text, fewer options per screen, explicit labels on every icon. Children: large targets, no dark patterns, parental gates.
- **Style.** The chosen atlas style changes radius, borders, shadow and motion. Read its *Token recipe*; do not let component-library defaults leak in.
- **Industry.** Finance and health: confirmation screens summarizing amount, recipient and consequences before irreversible actions. AI products: transparency about what the model did and why.
- **Density and data volume.** Under 50 rows: simple table; thousands: virtualization, saved views, server-side filtering.
- **Tier.** Premium and luxury: fewer elements per screen, more space, slower motion; value tiers: clarity and speed over ornament.

## Common failures

- The generic AI look: 16px radius and a drop shadow on every card, indigo-to-pink gradients, emoji as icons, centered everything. Fix: apply the style recipe and use shadow only for real layers.
- Disabled buttons with no explanation. Fix: keep the button enabled and validate on submit, or show the reason next to it.
- Placeholder text as the only label. Fix: visible label above the field.
- Spinner for every wait. Fix: skeletons for content, inline progress for actions, nothing under 1 s.
- Errors in disappearing toasts. Fix: inline error at the cause; toast only for confirmations.
- Modal dialogs for non-decisions. Fix: inline expansion, side panel or a new page.
- Missing focus styles or focus hidden under a sticky header. Fix: `:focus-visible` ring plus `scroll-padding-top`.
- Status shown by color alone. Fix: icon plus text plus color.
- Input and button in the same row at different heights. Fix: share the size token.
- Icon-only buttons without accessible names. Fix: `aria-label` and a tooltip.
- Center-aligned numbers in tables. Fix: right-align with tabular figures.
- Chat UIs that hide sources, cannot be stopped, or let an agent act without consent. Fix: [AI interfaces](references/ai-interfaces.md).

## References

- [Components](references/components.md): anatomy, state matrix, size scale, density modes, overlays, token mapping.
- [Forms](references/forms.md): layout, labels, input types and autocomplete, validation timing, multi-step forms.
- [Navigation](references/navigation.md): patterns by destination count and platform, mega menus, command palette, shortcuts.
- [Data-dense UI](references/data-dense-ui.md): tables, filtering, bulk actions, virtualization, dashboards.
- [States and feedback](references/states-and-feedback.md): response-time limits, skeletons, empty states, errors, toasts versus banners versus dialogs, notifications.
- [Flows](references/flows.md): onboarding, authentication with passkeys and MFA, pricing, checkout, search and filter, settings, account deletion.
- [AI interfaces](references/ai-interfaces.md): chat and agent UI, streaming, citations, tool calls, approvals, artifacts, memory and handoff.
- [Accessibility](references/accessibility.md): WCAG 2.2 AA checklist with numbers and ARIA keyboard patterns.
- Atlas: `python3 ../../library/scripts/atlas.py query "expert dashboard for logistics, dense"`; `combine <style> <industry> <audience>` before choosing density and tone.
- Filled component specs with full state logic: [button](../../library/examples/component-specs/button.md), [text field](../../library/examples/component-specs/text-field.md), [dialog](../../library/examples/component-specs/dialog.md), [data table](../../library/examples/component-specs/data-table.md), and the [selection guide](../../library/examples/component-specs/selection-guide.md).
- Deep process for client projects: [UI system](../../library/draft-skills/design-ui-system/SKILL.md) and the [component inventory](../../library/inventory/ui.md).
- Shared public touchscreens and kiosks: [touchscreen design](../../library/draft-skills/design-touchscreen-design/SKILL.md), [information architecture](../../library/draft-skills/design-touch-information-architecture/SKILL.md), [interaction patterns](../../library/draft-skills/design-touch-interaction-patterns/SKILL.md), [states and copy](../../library/draft-skills/design-touch-states-copy/SKILL.md), [forms](../../library/draft-skills/design-touch-forms/SKILL.md), [action reliability](../../library/draft-skills/design-touch-action-reliability/SKILL.md), [offline](../../library/draft-skills/design-touch-offline/SKILL.md), [media](../../library/draft-skills/design-touch-media/SKILL.md), [product discovery](../../library/draft-skills/design-touch-product-discovery/SKILL.md), [configurators](../../library/draft-skills/design-touch-configurators/SKILL.md), [product education](../../library/draft-skills/design-touch-product-education/SKILL.md), [phone and staff handoffs](../../library/draft-skills/design-touch-handoffs/SKILL.md), [usability testing](../../library/draft-skills/design-touch-usability-testing/SKILL.md), [device validation](../../library/draft-skills/design-touch-device-validation/SKILL.md).
- Related skills: `ux-design` (flows, research, content), `design-system` (tokens, component APIs), `data-visualization` (charts in dashboards), `native-app-design`, `web-design`, `design-critique`.

Catalog IDs covered: ui, touchscreen-design, touch-information-architecture, touch-interaction-patterns, touch-states-copy, touch-forms, touch-action-reliability, touch-offline, touch-media, touch-product-discovery, touch-configurators, touch-product-education, touch-handoffs, touch-usability-testing, touch-device-validation
