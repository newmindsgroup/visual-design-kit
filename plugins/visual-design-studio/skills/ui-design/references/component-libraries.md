# Component libraries

Version-Timestamp: 2026-11-10 03:00:00 UTC

Use when an interface will be built in React (directly, or by another agent or a site builder) and you must decide which components to install instead of writing them by hand. Hand-built components are where AI-made UI shows: toasts that pile up, drawers that will not drag, command menus that break under the keyboard, numbers that jump. Libraries supply tested behavior; the brand's tokens supply the look.

Methods restated from Griffin Wooldridge's posts (credited in `NOTICE.md`); the mismatch list adapts Emil Kowalski's MIT-licensed `pick-ui-library` skill. Versions and licenses below were read on 2026-11-10.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| First step | Read `package.json` (and `components.json` for shadcn) and keep every UI library already installed | The installed library is unmaintained or fails the accessibility checks below: propose the change, do not churn it silently |
| Primitive layer | One per product: Radix Primitives (matches the kit's [React reference system](../../../library/examples/react-system/README.md)) or Base UI | Project already uses Base UI, React Aria or Headless UI: stay on it. Never wrap two primitive layers behind one API (`design-system` [component API](../../design-system/references/component-api.md)) |
| Most app components | shadcn/ui copied into the repo, on the chosen primitive layer | Multi-product design system: publish the components as a versioned package or a private shadcn-compatible registry |
| Specialists | Sonner for toasts, a drag-to-close drawer, cmdk for command menus, NumberFlow for changing numbers, input-otp for verification codes, `motion` only for springs, layout and exit animation | Plain hover and fade: CSS transitions with the kit duration and easing tokens |
| Designed components | At most one showpiece moment per page (one animated hero, one interactive background, one signature section) | A campaign microsite whose brief is the effect: still one primary effect per view |
| Styling | Restyle before anything ships: radius, color and type from the brand tokens (recipe below) | Never ship the library's default theme as the brand |
| Accessibility | Primitives own focus, keyboard and ARIA; designed components are audited before use | No exceptions for showpieces |

## The three kinds

| Kind | What it gives you | Use it for | Examples |
| --- | --- | --- | --- |
| Foundations | Behavior: focus management, keyboard support, ARIA, dismissal; little or no styling | Buttons, inputs, selects, dialogs, menus, tabs, popovers, tooltips: most of an app | shadcn/ui, Radix Primitives, Base UI |
| Specialists | One hard component done well | The details that make a product feel finished and that AI gets wrong by hand | Sonner, Vaul, cmdk, NumberFlow, input-otp, motion |
| Designed components | Finished, styled, usually animated pieces you copy into the repo | A moment you want people to notice | Beautiful UI (AI-native states), Magic UI, Aceternity UI, RareUI, the 21st.dev marketplace |

The kinds stack: foundations for the bulk, a specialist where one fits, and one designed piece where the page needs a moment.

## Verified versions and licenses (2026-11-10)

| Library | Kind | npm package | Version | License | Install | Source |
| --- | --- | --- | --- | --- | --- | --- |
| shadcn/ui | Foundation (copy-in) | `shadcn` (CLI) | 4.23.0 | MIT | `npx shadcn@latest init --base radix` (or `--base base`, `--base aria`), then `npx shadcn@latest add dialog` | npm; LICENSE.md in shadcn-ui/ui |
| Radix Primitives | Foundation | `@radix-ui/react-dialog` (one package per primitive; `radix-ui` 1.8.1 bundles them) | 1.3.1 | MIT | `npm i @radix-ui/react-dialog` | npm; LICENSE in radix-ui/primitives |
| Base UI | Foundation | `@base-ui/react` (the older `@base-ui-components/react` stopped at 1.0.0-rc.0) | 1.9.0 | MIT | `npm i @base-ui/react` | npm; LICENSE in mui/base-ui |
| Sonner | Specialist: toasts | `sonner` | 2.0.8 | MIT | `npx shadcn@latest add sonner` or `npm i sonner` | npm; LICENSE.md in emilkowalski/sonner |
| Vaul | Specialist: drawers | `vaul` | 1.1.2 (December 2024) | MIT | `npx shadcn@latest add drawer` on the Radix base | npm; its README says the repo is unmaintained |
| cmdk | Specialist: command menu, combobox | `cmdk` | 1.1.1 | MIT | `npx shadcn@latest add command` or `npm i cmdk` | npm; LICENSE.md in dip/cmdk |
| NumberFlow | Specialist: animated numbers | `@number-flow/react` | 0.6.2 | MIT | `npm i @number-flow/react` | npm; LICENSE.md in barvian/number-flow |
| input-otp | Specialist: verification codes | `input-otp` | 1.5.0 | MIT | `npx shadcn@latest add input-otp` or `npm i input-otp` | npm; LICENSE in guilhermerodz/input-otp |
| motion | Specialist: animation | `motion` | 14.11.1 | MIT | `npm i motion` | npm. The web technique recipes stay pinned at 14.4.0 until re-tested |
| Magic UI | Designed | none (shadcn registry `@magicui`) | registry | MIT (repo) | `npx shadcn@latest add @magicui/<component>` | LICENSE.md in magicuidesign/magicui; `@magicui` in shadcn's registry directory. Paid tiers: verify |
| Aceternity UI | Designed | none (shadcn registry `@aceternity`) | registry | verify (no public source repo found; old `aceternity-ui` CLI is MIT) | `npx shadcn@latest add @aceternity/<component>` | `@aceternity` in shadcn's registry directory. Free and paid components: verify on the site |
| RareUI | Designed | `rareui` (CLI) | 0.1.6 | MIT | `npx rareui add <component>` | npm; LICENSE in Codewithswappy/rareui |
| 21st.dev | Marketplace | `@21st-dev/cli` | 1.18.0 | CLI and marketplace code MIT; each component has its own author and license: verify per component | Copy the component or its agent prompt; the CLI also configures the 21st MCP | npm; LICENSE in serafimcloud/21st |
| Beautiful UI | Designed (AI-native) | none found | n/a | verify (site unreachable from the verification machine; no source repo found) | Copy code from the site | beautifului.dev |

The shadcn CLI options above were read from its source (`packages/shadcn/src/commands/init.ts`, commit 8ab2771, 2026-11-08); `--defaults` uses the Base UI base. Re-run `npm view <package> version license` before pinning in a client project.

## Check package.json first

1. List what is installed: primitive layer, toast, drawer, command menu, animation library, chart library.
2. Keep each one. A project on Radix Toast (the kit's React reference system uses it) keeps Radix Toast; do not add Sonner beside it. A project on react-window keeps it; flag a better option without swapping it.
3. Only for a gap, add a library from this page, on the same primitive layer as the rest.
4. Record each pick in the project's `AGENTS.md` (the kit repository's `project-starter/AGENTS.md.template` has an optional block for it) so every later prompt uses it.

## Mismatch map

Signs of a hand-built component and what replaces it. The first four rows adapt Emil Kowalski's `pick-ui-library` list (MIT); the rest are kit additions.

| You see | Replace with | Why |
| --- | --- | --- |
| Toasts built by hand, or with a modal library | Sonner (`npx shadcn@latest add sonner`); Base UI Toast on a Base UI project; keep Radix Toast where installed | shadcn deprecated its own Toast for Sonner on the Radix and React Aria bases; stacking, hover-expand, swipe and live regions are already solved |
| A `div` dropdown, menu or dialog with manual focus handling | The primitive layer's Menu, Popover or Dialog (Radix or Base UI, whichever is installed) | Focus trap, return focus, Esc, outside click, typeahead and ARIA roles |
| A number animated by re-rendering text (counters, prices, stats) | NumberFlow, formatted with `Intl.NumberFormat` options | Per-digit transitions without layout jumps; `respectMotionPreference` defaults to true |
| 1,000+ rows rendered at once | A virtualized list (Emil's list picks Virtuoso) with the rules in [data-dense UI](data-dense-ui.md) | DOM size and scroll performance |
| A bottom sheet that only opens and closes, with no drag or snap | shadcn Drawer: Base UI Drawer on the Base UI base, Vaul on the Radix base | Drag to close, velocity, snap points, scroll locking. Vaul is unmaintained (its README, checked 2026-11-10): for new work prefer the Base UI base or accept the risk in writing |
| A homemade Cmd+K palette that loses focus, ignores arrows or does not filter | cmdk (shadcn Command) | Filtering and sorting, arrow keys, grouped items, combobox semantics |
| Six separate inputs for a one-time code with hand-written focus jumping | input-otp (shadcn Input OTP) | Paste, `autocomplete="one-time-code"` autofill and one accessible field |
| A JavaScript animation library imported for a hover or fade | CSS transitions on `--duration-fast` and `--ease-standard` | Less JavaScript; the tokens' reduced-motion block already covers it |

## One showpiece per page

- One designed or animated moment per page makes it feel designed; several on the same page is the next generic AI look, where everything glows and moves and nothing leads ([AT-29](../../design-critique/references/ai-tells.md)).
- Place it where the page's main message is (usually the hero or the proof section), and keep every other section on foundations.
- Restyle it to the tokens like everything else, and give it a static fallback for reduced motion and a pause control for any loop over 5 seconds (WCAG 2.2.2).
- Product UI (dashboards, settings, forms) gets no showpiece. Its moment is a well-made state change: a toast, a number ticking over, an empty state.

## Restyle shadcn defaults with the kit tokens

Default shadcn styling is itself a recognizable AI look ([AT-27](../../design-critique/references/ai-tells.md)): neutral gray ramp, 10px base radius on everything, one sans family. Change radius, color and type first; they carry most of the personality.

Two traps, both checked with Tailwind CSS 4.3.5 on 2026-11-10:

- shadcn's `@theme inline` derives `--radius-sm`, `--radius-md` and `--radius-xl` from `--radius` with `calc()`, and Tailwind writes those formulas straight into `rounded-*` utilities. The kit's own `--radius-*` values never reach components unless you replace those lines.
- shadcn's `bg-accent` is a hover surface; the kit's own `tailwind.css` uses `bg-accent` for the brand accent. Use one naming layer per project: in a shadcn app, import the kit's `tokens.css` and keep shadcn's class names; do not also import the kit's `tailwind.css`.

```css
@import "tailwindcss";
@import "./tokens.css";              /* kit values, modes and brands */
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));

@theme inline {
  /* keep shadcn's --color-* lines; delete its --radius-* calc() lines */
  --font-sans: var(--font-family-body);
  --font-heading: var(--font-family-display);
}
@theme inline reference {
  --radius-sm: var(--radius-sm);
  --radius-md: var(--radius-md);
  --radius-lg: var(--radius-lg);
  --radius-xl: var(--radius-xl);
}
:root, [data-theme], [data-brand] {
  --radius: var(--radius-lg);
  --background: var(--color-bg-canvas);
  --foreground: var(--color-fg-default);
  --card: var(--color-bg-surface);
  --card-foreground: var(--color-fg-default);
  --popover: var(--color-bg-surface-raised);
  --popover-foreground: var(--color-fg-default);
  --primary: var(--color-accent-default);
  --primary-foreground: var(--color-fg-on-accent);
  --secondary: var(--color-bg-sunken);
  --secondary-foreground: var(--color-fg-default);
  --muted: var(--color-bg-sunken);
  --muted-foreground: var(--color-fg-muted);
  --accent: var(--color-accent-subtle);
  --accent-foreground: var(--color-accent-fg);
  --destructive: var(--color-danger-fg);
  --border: var(--color-border-subtle);
  --input: var(--color-border-strong);
  --ring: var(--color-focus-ring);
}
```

Then:

1. Delete shadcn's `.dark { ... }` block: the kit's `[data-theme="dark"]` and `prefers-color-scheme` rules switch every mapped variable. Set `data-theme` on `<html>`. `dark:` utilities fire only with an explicit `data-theme="dark"`, so put mode differences in tokens, not in `dark:` classes.
2. Map `--input` to `--color-border-strong`, not `--color-border-default`: in the Meridian light theme the default border is 1.51:1 on the canvas and the strong border 4.12:1, and input borders need 3:1 (WCAG 1.4.11).
3. Fix the destructive button's text. shadcn's destructive variant uses `text-white`; on the dark-mode danger color (#FF8382) white is 2.38:1. Use `text-(--color-fg-inverse)` (9.68:1 light, 7.43:1 dark) and confirm with `python3 ../../../library/scripts/color_tools.py contrast <fg> <bg>`.
4. Search the copied components for `var(--radius)` inside arbitrary values and replace them with the kit radius utilities.
5. Set the radius from the direction, not the library: Swiss or editorial 0-4px (`--radius-none`, `--radius-sm`), most products `--radius-md`, playful 12-16px. A tighter radius and a serif display face turn the same components from SaaS template into an editorial product.
6. Build a brand with `brands/<brand>.tokens.json` per `design-director`'s [handoff](../../design-director/references/handoff.md#2-turn-the-direction-into-tokens) and run `tokens.py lint`. Then render with `design-critique` and check that the name-swap test fails.

## Accessibility

- Prefer foundations and specialists for anything with focus or keyboard behavior: dialogs, menus, comboboxes, drawers, toasts. They are where hand-built code fails most.
- Toasts: keep the kit's rules in [states and feedback](states-and-feedback.md): never the only path to an action, pause on hover and focus, no auto-dismiss under 5 seconds when a toast holds an action. Sonner's defaults still need that review.
- Designed components: before shipping, check reduced motion (does the effect stop or simplify under `prefers-reduced-motion`?), text contrast over the moving background at its lightest frame, keyboard reachability and focus visibility of anything clickable, and a pause control for loops over 5 seconds. Add what is missing; many showpiece components ship without it.
- Command menus: a visible trigger as well as the shortcut, and every command reachable elsewhere ([navigation](navigation.md)).
- Re-run the [WCAG 2.2 AA checklist](accessibility.md) after restyling; theme changes break contrast more often than components do.

## Briefing a build agent

Name the libraries in the prompt ("shadcn/ui on Radix for base components, Sonner for toasts, cmdk for the command menu, NumberFlow for prices; do not build these by hand"), paste the token mapping above, and say which single section may carry a designed component. The rest of the brief follows `design-director`'s [handoff](../../design-director/references/handoff.md#4-prompts-for-generators-and-build-tools) and the [reference-first workflow](../../design-director/references/reference-first.md).

## Single-context note

Everything here works in one context, in Claude, Codex or any agent: read `package.json`, consult the mismatch map, install, restyle, render. Emil Kowalski's `pick-ui-library` skill (github.com/emilkowalski/skills, MIT) is optional and runs only when invoked by name (`disable-model-invocation: true`); this page covers its UI picks without installing it.
