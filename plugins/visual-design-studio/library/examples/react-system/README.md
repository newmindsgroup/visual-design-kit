# React reference system

Version-Timestamp: 2026-10-20 03:35:12 UTC

The kit's reference implementation of a component system: sixteen accessible React components wired to the kit tokens (`library/tokens/dist/`), a specimen that shows every component in every state, and one composed screen (billing settings) that proves the parts work together. The `design-system` and `ui-design` skills point here when they need working code for a component API, a state matrix or a token mapping.

Stack: Vite 8, React 19.3, TypeScript 7, Tailwind CSS 4.3, Radix Primitives. Every color, size, radius, shadow, duration and easing comes from `tokens.css`; tests fail on raw colors, arbitrary Tailwind values, Tailwind's default palette and physical (left/right) utilities.

## Run it

Node 22.18 or later (the unit tests import TypeScript helpers through Node's built-in type stripping; Vite 8 itself needs 20.19+ or 22.12+). In an installed plugin, copy this folder to a working directory first; do not install dependencies inside the plugin.

```sh
npm ci
npm run dev          # specimen at http://127.0.0.1:5173/, composed screen at /billing.html
npm test             # token freshness, class lint, helpers, type-level prop tests (tsc)
npm run build        # dist/ (relative paths, works from any static host)
npm run preview
```

`?theme=dark|light|high-contrast`, `&brand=meridian|ember` and `&dir=rtl|ltr` set the display from the URL; the header switches them live and remembers the choice. Without either, the page follows the OS color-scheme and contrast settings.

Browser QA (Playwright and axe-core come from your own vetted QA environment, as in `../astro-motion/`):

```sh
npm run build
PLAYWRIGHT_MODULE=/path/to/node_modules/playwright \
AXE_SCRIPT=/path/to/node_modules/axe-core/axe.min.js \
CHROME_EXECUTABLE=/path/to/chromium \
npm run test:browser
```

`tests/browser.mjs` serves `dist/` itself (or uses `BASE_URL`), writes screenshots and `results.json` to `qa-output/` (gitignored) and checks:

- axe-core with the `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` and `wcag22aa` tags on both pages, at 1440 and 390px, in all six brand x theme contexts and in RTL (28 runs), plus no horizontal page overflow in each;
- dialog focus moves in, Tab and Shift+Tab stay inside, Escape closes and focus returns to the opener (with and without a `DialogTrigger`); confirmations start on the safe action and ignore outside clicks; overflowing bodies become a named, focusable region;
- tabs: arrow keys, Home, End, wrap, disabled tab skipped, arrows mirrored in RTL, Tab into the panel;
- Tab reaches every control on both pages (1440 and 390px) and every focused control shows a 2px or wider ring;
- checkbox, switch, radio, select (typeahead), tooltip (focus, Escape), toast (live region, F8, Undo), table sort (`aria-sort`, missing values last, end-aligned tabular numbers) and selection;
- billing flows: plan change with toast and Undo, error summary with focus and linked fields, banner action moving focus;
- `prefers-reduced-motion: reduce` turns every transition into 0.01ms and stops the skeleton and spinner animations (a baseline run confirms 120ms without it);
- no page errors, console errors or external requests (fonts are self-hosted).

## Files

| Path | What it is |
| --- | --- |
| `src/components/` | The system: one file per component plus `field.tsx` (label, hint, error, id wiring), `icons.tsx` (original stroke icons), `spinner.tsx`, `types.ts`, `index.ts` |
| `src/lib/` | `cx` and `variants` (props-to-class helper), sorting, controlled-state, overflow and ref helpers |
| `src/styles/tokens.css`, `tailwind.css` | Byte-for-byte copies of `library/tokens/dist/`; never edit |
| `src/styles/system.css` | The component layer: token-based default transition, keyframes, `focus-ring` utilities, preview-state variants, forced-colors fixes. Copy it with any component |
| `src/styles/fonts.css`, `src/fonts/` | Self-hosted OFL fonts for both brands, license next to each family |
| `src/specimen/`, `src/billing/`, `src/shared/` | Specimen page, composed billing screen, shared shell and sample data (invented workspace "Harbor Studio") |
| `scripts/sync-tokens.mjs` | Token copy and freshness check |
| `tests/` | `unit.test.mjs` (node:test), `props.typecheck.tsx` (type-level), `browser.mjs` (Playwright + axe), `static-server.mjs` |

## Token wiring

1. `scripts/sync-tokens.mjs` copies `../../tokens/dist/tokens.css` and `tailwind.css` into `src/styles/`. It runs before `dev`, `build` and `test`; `--check` exits 1 when a copy is stale (for CI); `TOKENS_DIST=/path` points it elsewhere. Outside the kit the source is missing and the committed copies are kept, so a copied project still builds.
2. `src/styles/index.css` imports, in order: `tailwindcss`, `tokens.css` (values, modes, brands), `tailwind.css` (`@theme inline reference` utility names that resolve to the token variables and reset Tailwind's palette, type scale, radii and shadows), `fonts.css`, `system.css`.
3. `data-theme` and `data-brand` live on `<html>`, set before first paint by the inline script in each HTML entry. Nested previews (the six tiles at the top of the specimen) set both attributes on a wrapper.
4. Components use the three tiers the token contract defines and never primitives (`--color-teal-600`):
   - component tokens through Tailwind's variable shorthand where they exist: `bg-(--button-primary-bg)`, `rounded-(--card-radius)`, `px-(--input-padding-x)`, `z-(--dialog-z)`;
   - semantic utilities for everything else: `bg-surface`, `text-muted`, `border-subtle`, `shadow-md`, `duration-fast`, `ease-standard`, `z-dropdown`;
   - the 4px spacing scale (`p-4`, `gap-2`), which `tailwind.css` maps to `--space-1`.
5. `system.css` points Tailwind's default transition duration and easing at `--duration-fast` and `--ease-standard` and builds every keyframe animation from duration tokens, so the tokens' reduced-motion block (every `--duration-*` becomes 0.01ms) covers all motion.

`tests/unit.test.mjs` enforces the wiring: the copies match the source, every `var(--x)` the code reads exists in the tokens or `system.css`, no hex or `rgb()`/`oklch()` literals appear, and every class string in the source compiles against the token theme (checked with Tailwind's own design system, about 1,400 class tokens) with no `[arbitrary]` values, palette colors or physical sides.

One deliberate deviation: placeholders use `text-muted` (`--color-fg-muted`) instead of `--input-placeholder` (`--color-fg-subtle`). `fg-subtle` on white measures 4.43:1 in Meridian light, and the Select shows its placeholder as real text that axe checks against 4.5:1.

## Component API conventions

Follows `skills/design-system/references/component-api.md`.

| Concept | Prop | Notes |
| --- | --- | --- |
| Emphasis | `variant` | Button `primary`, `secondary`, `ghost`, `danger`; Card `outlined`, `elevated`, `sunken`; Badge `subtle`, `outline` |
| Size | `size` | `sm` 32, `md` 40 (default), `lg` 48px on Button, TextField, Select; inputs and buttons in one row share it |
| Status color | `tone` | `neutral`, `accent`, `info`, `success`, `warning`, `danger` on Badge, Alert, Banner, toasts |
| Booleans | `disabled`, `required`, `loading`, `invalid`, `readOnly` | DOM names, positive phrasing |
| Values | `value`, `defaultValue`, `onValueChange` | TextField, Select, RadioGroup, SegmentedControl, Tabs; Checkbox and Switch use `checked`, `defaultChecked`, `onCheckedChange` like the DOM |
| Open state | `open`, `defaultOpen`, `onOpenChange` | Dialog, Select, Tooltip |
| Collections | `selectedKeys`, `defaultSelectedKeys`, `onSelectionChange`; `sort`, `defaultSort`, `onSortChange` | DataTable |
| Slots | `label`, `hint`, `error`, `description`, `startIcon`, `endIcon`, `startAdornment`, `endAdornment`, `actions`, `icon`, `badge`, `meta` | Rich content, not strings only |
| Composition | Compound parts | `Dialog`, `DialogTrigger`, `DialogContent`, `DialogBody`, `DialogFooter`, `DialogClose`; `Tabs`, `TabsList`, `TabsTrigger`, `TabsContent`; `Card`, `CardHeader`, `CardTitle`, `CardLink` ... |
| Polymorphism | `asChild` | Button (a link styled as a button), Card, CardTitle (pick the heading level) |
| Styling escape hatch | `className` | Merged onto the outermost element; `inputClassName` reaches the input. Prefer props over overriding classes: without `tailwind-merge`, conflicting utilities resolve by stylesheet order, not class order |
| Element access | `ref` | React 19 passes `ref` as a prop; no `forwardRef` |
| Styling hooks | `data-slot`, `data-state`, `data-variant` | Stable selectors for tests and overrides |
| Docs only | `data-preview-state="hover \| focus \| active"` | Renders interaction states statically through the custom variants in `system.css` |

Accessible names are part of the type: `iconOnly` buttons require `aria-label`, Checkbox requires `label` or `aria-label`, fields require `label`. `tests/props.typecheck.tsx` keeps those as compile errors. `variants()` recipes expose `.options` (for example `buttonStyles.options.variant`) so docs, tests and Figma mappings read the same option lists.

| Component | File | Primitive | Spec or reference |
| --- | --- | --- | --- |
| Button | `button.tsx` | native `button`, Radix Slot | `../component-specs/button.md` |
| TextField | `text-field.tsx` | native `input` | `../component-specs/text-field.md`, `ui-design/references/forms.md` |
| Select | `select.tsx` | Radix Select | `ui-design/references/components.md` |
| Checkbox | `checkbox.tsx` | Radix Checkbox | |
| Switch | `switch.tsx` | Radix Switch | |
| RadioGroup, Radio, RadioCard, SegmentedControl | `radio-group.tsx` | Radix RadioGroup | |
| Dialog | `dialog.tsx` | Radix Dialog | `../component-specs/dialog.md` |
| Tabs | `tabs.tsx` | Radix Tabs | |
| Toast (`ToastProvider`, `useToast`) | `toast.tsx` | Radix Toast | `ui-design/references/states-and-feedback.md` |
| Tooltip | `tooltip.tsx` | Radix Tooltip | |
| Card | `card.tsx` | `div` or `asChild` | |
| Badge | `badge.tsx` | `span` | |
| Alert, Banner | `alert.tsx` | `div` (optional `status` or `alert` role) | |
| DataTable | `data-table.tsx` | native `table` | `../component-specs/data-table.md` |
| EmptyState | `empty-state.tsx` | | |
| Skeleton, SkeletonText | `skeleton.tsx` | | |

## Accessibility guarantees

Target: WCAG 2.2 AA in all six brand x theme contexts, both directions, 1440 and 390px. Verified automatically in Chromium (see Browser QA); screen-reader and cross-browser passes are still required per project.

- **Keyboard** follows the WAI-ARIA Authoring Practices pattern for each component (keys listed on the specimen). Roving focus in radio groups, segmented controls and tabs; Escape closes dialogs, selects, tooltips and toasts; F8 reaches notifications.
- **Focus** is a 2px `--focus-ring-color` outline at 2px offset on `:focus-visible` (3px in high contrast), drawn inset where a scroll container would clip it. `scroll-padding-block` keeps focused elements clear of the sticky header (2.4.11).
- **Targets**: every control is at least 24x24px (`--size-target-min`; checkbox and radio draw a 20px mark inside a 24px button); on coarse pointers an `::after` extends sm and md controls to 44px (`--size-target-comfortable`).
- **Names and states**: visible labels linked with `for`; hint and error joined in `aria-describedby`; `aria-invalid`, `aria-busy`, `aria-sort`, `aria-current`, `aria-modal`; required fields set the native `required`.
- **Never color alone**: badges, alerts and toasts carry icon plus text; switches show a check mark when on; the mixed checkbox shows a dash; selected table rows also have a checked box.
- **Motion**: all transitions and animations come from duration tokens, which collapse to 0.01ms under `prefers-reduced-motion`; the spinner and skeleton pulse stop entirely.
- **RTL**: logical properties only (`ps`, `me`, `start-0`, `border-s`), enforced by the class lint; Radix receives the direction through `DirectionProvider`, so arrow keys and toast swipes mirror; directional icons (arrows, chevron-right) flip; numbers with units sit in `bdi`. The specimen's RTL toggle mirrors English copy, so punctuation lands at the start of lines; real RTL use needs translated content.
- **Forced colors**: parts drawn only with background color (switch thumb, radio dot, selected row) switch to system colors.
- **Not covered**: Safari and Firefox, Windows High Contrast themes beyond the forced-colors rules, VoiceOver, NVDA and TalkBack passes.

## Copy a component into a client project

The shadcn/ui model: you copy the source and own it. Use it for a single product or a prototype; for a system that serves several products, publish these files as a versioned package or a private shadcn-compatible registry so every product upgrades the same code (see `component-api.md`).

1. Prerequisites: React 19, Tailwind CSS v4 with `@tailwindcss/vite` (or PostCSS), and the client's token build using the kit contract names (`tokens.css` plus `tailwind.css`, generated by `library/scripts/tokens.py` from the client's DTCG files).
2. Copy `src/styles/system.css` and import it after the tokens, as in `src/styles/index.css`. Copy `src/lib/cx.ts` and `src/components/types.ts`.
3. Copy the component file and its local dependencies, and install its Radix package at the version pinned here:

   | Component | Also copy | npm package |
   | --- | --- | --- |
   | Button | `spinner.tsx`, `icons.tsx` (type only), `lib/refs.ts` | `@radix-ui/react-slot` |
   | TextField | `field.tsx`, `icons.tsx` | |
   | Select | `field.tsx`, `icons.tsx`, `text-field.tsx`, `lib/layer.tsx` | `@radix-ui/react-select` |
   | Checkbox, Switch | `field.tsx`, `icons.tsx` | `@radix-ui/react-checkbox`, `@radix-ui/react-switch` |
   | RadioGroup | `field.tsx`, `icons.tsx` | `@radix-ui/react-radio-group` |
   | Dialog | `button.tsx`, `icons.tsx`, `lib/layer.tsx`, `lib/use-overflow.ts` | `@radix-ui/react-dialog` |
   | Tabs | | `@radix-ui/react-tabs` |
   | Toast | `button.tsx`, `icons.tsx` | `@radix-ui/react-toast`, `@radix-ui/react-direction` |
   | Tooltip | `lib/layer.tsx` | `@radix-ui/react-tooltip` |
   | Card | | `@radix-ui/react-slot` |
   | Badge, EmptyState, Skeleton | | |
   | Alert, Banner | `button.tsx`, `icons.tsx` | |
   | DataTable | `checkbox.tsx`, `empty-state.tsx`, `skeleton.tsx`, `icons.tsx`, `lib/sort.ts`, `lib/use-controllable.ts`, `lib/use-overflow.ts` | (Checkbox's) |

4. Wrap the app once: `DirectionProvider` (RTL products), `TooltipProvider`, and `ToastProvider` if you use toasts (see `src/shared/shell.tsx`).
5. Replace `icons.tsx` with the client's icon set if it has one (keep 16, 20 and 24px from `--size-icon-*`), and `fonts.css` with the client's licensed fonts.
6. Copy `tests/unit.test.mjs` and keep the class lint, the variable check and the type tests running in CI; they catch the off-token values that copied code tends to collect.

## Figma Code Connect

Described here, not shipped: Code Connect files need the client's Figma node URLs.

- **Variables**: import `library/tokens/dist/figma-variables.json` with `library/tokens/figma-import.js` (see the tokens README). The `Primitives` collection has Meridian and Ember modes, `Semantic` has Light, Dark and High contrast, and every variable carries `codeSyntax.WEB` (`var(--color-bg-canvas)`), so Dev Mode shows the same names the components use.
- **Components**: build one Figma component set per component with property names identical to the props: Variant properties for enums (`variant`, `size`, `tone`), Boolean properties for toggles (`loading`, `disabled`, `iconOnly`), Instance swap for icon slots (`startIcon`, `endIcon`), Text for labels. Read the option lists from each recipe's `.options` so Figma and code cannot drift.
- **Mapping**: one `*.figma.tsx` per component next to the source, using `figma.connect(Button, "<component set URL>", { props: { variant: figma.enum("variant", { primary: "primary", ... }), size: figma.enum("size", ...), loading: figma.boolean("loading"), label: figma.string("label"), startIcon: figma.instance("startIcon") }, example: (props) => <Button ...>{props.label}</Button> })`, published with the Code Connect CLI (`figma connect publish`; confirm current syntax in Figma's docs). With the Figma MCP server, `add_code_connect_map` registers the same mapping; load the `figma-code-connect` skill first.
- **States**: Figma variants for hover, focus and pressed mirror `data-preview-state`; disabled, loading and invalid map to the real props.

## Dependencies

All versions are exact and were published at least two weeks before 2026-10-20; the lockfile was resolved with `npm install --before=2026-10-06`.

| Package | Version | Published |
| --- | --- | --- |
| react, react-dom | 19.3.0 | 2026-09-09 |
| @radix-ui/react-checkbox, -dialog, -direction, -radio-group, -select, -slot, -switch, -tabs, -toast, -tooltip | 1.3.12, 1.2.0, 1.1.5, 1.4.8, 2.3.8, 1.4.0, 1.3.8, 1.1.22, 1.2.24, 1.3.0 | 2026-10-05 |
| vite (dev) | 8.3.2 | 2026-10-01 |
| @vitejs/plugin-react (dev) | 6.1.2 | 2026-10-05 |
| tailwindcss, @tailwindcss/vite (dev) | 4.3.3 | 2026-07-16 |
| typescript (dev) | 7.0.2 | 2026-07-08 |
| @types/react, @types/react-dom (dev) | 19.3.0 | 2026-09-09 |

Fonts (OFL 1.1, Latin subsets from Fontsource 5.3.0): Schibsted Grotesk, Source Sans 3, JetBrains Mono (Meridian); Fraunces, Figtree, IBM Plex Mono (Ember). QA-only tools, not dependencies: Playwright and axe-core 4.10.2 (MPL-2.0).

Not included: combobox, menu, popover, date picker, pagination and virtualized tables. Build them on the same primitive layer (Radix) rather than mixing headless libraries.

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 03:35:12 UTC
