# Navigation

Version-Timestamp: 2026-10-20 02:04:32 UTC

Navigation answers three questions on every screen: where am I, where can I go, and how do I get back. Choose the pattern from the number of destinations, the platform and how often people switch between them. The structure itself comes from `ux-design` [information architecture](../../ux-design/references/information-architecture.md).

## Pattern by destination count and platform

| Situation | Pattern | Notes |
| --- | --- | --- |
| 2-5 peer views of one object | Tabs or segmented control | Tabs switch content in place; keep labels 1-2 words |
| Marketing site, up to about 7 top-level items | Horizontal top navigation | Logo left (links home), primary CTA right, utility links (sign in, language) at the far right |
| Site with many categories and subcategories | Mega menu | Grouped columns with headings; opened by click or deliberate hover |
| Any site on phones | Menu button ("Menu" label plus icon) opening a drawer or full-screen panel | Keep the primary CTA and search visible outside the menu |
| Web app, about 5-15 destinations | Left sidebar, 240-280px expanded, 56-72px collapsed rail | Group under headings; pin favorites; collapse state remembered |
| Web app, more than 15 destinations or many objects | Sidebar groups plus global search and a command palette | Do not nest more than 2 levels in the sidebar |
| Native or mobile app, 3-5 top-level destinations | Bottom tab bar (iOS) or navigation bar (Android) | Labels always visible; more than 5: a "More" tab or a rail |
| Tablet and medium windows | Navigation rail, 3-7 destinations | Expands to a drawer or wider rail on large windows |
| Hierarchy 3 or more levels deep | Breadcrumbs | Current page last, not a link, `aria-current="page"` |
| Linear process | Stepper with step names | See [forms](forms.md) for multi-step rules |
| Long document | Table of contents, sticky on desktop, collapsible on mobile | Highlight the current section; links update the URL hash |
| Power users switching often | Command palette and keyboard shortcuts | Never the only way to reach a function |

Platform guidance changes: Apple's iOS 26 refresh changed tab bar appearance, and Material 3 Expressive (2025) favors navigation rails that expand over the classic drawer. Confirm the current Apple HIG and m3.material.io before native production; the `native-app-design` skill holds the details.

## Current location

- Mark the current destination with `aria-current="page"` (or `"step"`, `"location"`).
- Show it with more than color: a 2-4px indicator bar, a filled background (`--color-accent-subtle` with `--color-accent-fg` text), or heavier weight.
- Page H1 matches the navigation label.
- Keep navigation in the same place and order on every page (WCAG 3.2.3).

## Top navigation and mega menus

- 5-7 top-level labels of 1-2 words; the order follows the serial position effect (most important first and last).
- Use the ARIA disclosure pattern for site navigation (a button with `aria-expanded` controlling a list of links), not `role="menu"`, which is for application menus.
- Open on click or Enter. If hover opens it, add an intent delay of about 150-300ms and a close delay, so diagonal mouse movement does not close it.
- Esc closes and returns focus to the trigger; Tab moves through links in order.
- Mega menu content: 2-4 columns of grouped links with headings, optionally one promotional tile; no more than about 30-40 links in total.
- The header height on desktop is commonly 64-80px; on scroll it may condense to 56-64px. A sticky header must not hide focused elements (WCAG 2.4.11): set `scroll-padding-top` to the header height.

## Mobile menus

- A labeled menu button ("Menu" next to the icon) is found more reliably than an unlabeled hamburger icon.
- Opening the menu moves focus to the first item or the close button; Esc and the close button close it; focus returns to the menu button.
- If the menu covers the page, make it modal (trap focus, `inert` on the rest). If it pushes content, do not trap focus.
- Show the top tasks as large rows (48px+); collapse secondary groups into accordions.
- Do not hide core app destinations behind a hamburger: use a tab bar.

## App sidebars

- Order: primary workspace destinations, then object lists (projects, channels), then settings and help at the bottom.
- Section headings in `--font-size-xs` caps with `--letter-spacing-caps` or medium-weight sentence case.
- Collapsed rail shows icons with tooltips and keeps `aria-label`s; expanding is a user choice, remembered.
- Badges for unread counts cap at "99+".
- Width changes animate with `--duration-moderate` and `--ease-standard`, or not at all under reduced motion.

## Tabs

- ARIA tabs pattern: `role="tablist"`, `tab`, `tabpanel`; Left/Right arrows move between tabs, Home/End jump, Tab moves into the panel.
- Automatic activation (on arrow) when panels load instantly; manual activation (Enter or Space) when panels are slow.
- Overflowing tabs scroll horizontally with visible affordance, or collapse into a "More" menu; never wrap to two rows.
- Tabs that represent shareable views update the URL.

## Command palette

- Open with Cmd+K (macOS) or Ctrl+K (Windows, Linux), plus a visible button or search field showing the shortcut.
- Built on the ARIA combobox pattern: text input with a listbox of results; Up/Down move, Enter runs, Esc closes and returns focus.
- Empty query shows recent items and suggested actions; typing shows grouped results: navigation, objects, actions, help.
- Fuzzy matching on titles and synonyms; show the keyboard shortcut next to each action.
- Show about 7-10 results without scrolling; highlight matched characters.
- Optional scoped modes with a prefix (">" for commands) for experts.
- Every command is also reachable through visible UI.

## Keyboard shortcuts

- Show shortcuts in tooltips and menus, and list them all in a "?" dialog.
- Single-character shortcuts (like "j" and "k") must be possible to turn off or remap, or only work when a component has focus (WCAG 2.1.4).
- Common conventions: "/" focuses search, Cmd/Ctrl+K opens the palette, Esc closes, Cmd/Ctrl+Enter submits a composer.
- Never override browser and screen reader shortcuts.

## Skip links and landmarks

- First focusable element: "Skip to main content", visible on focus (WCAG 2.4.1).
- Landmarks: `header`, `nav` (with `aria-label` when there are several, such as "Main" and "Footer"), `main`, `aside`, `footer`.

## Search placement

- On content-heavy sites, show an open search field in the header on desktop; NN/g recommends a field wide enough for about 27 characters. On phones, a search icon that expands is fine.
- Search results and filters are covered in [flows](flows.md).

## URLs, history and back

- The URL reflects meaningful state: selected tab, filters, sort, pagination, open detail panel for shareable items.
- Browser Back undoes the last navigation, not the last micro-interaction; filtered lists restore scroll position.
- Deep links into authenticated areas return to the same place after sign-in.

## Responsive transformations

| Desktop | Tablet | Phone |
| --- | --- | --- |
| Top navigation with mega menu | Top navigation, condensed, or menu button | Menu button with drawer; CTA stays visible |
| App sidebar | Navigation rail | Bottom tab bar for 3-5 top destinations, drawer for the rest |
| Tabs | Scrollable tabs | Scrollable tabs, or a select for 6+ |
| Breadcrumbs | Breadcrumbs, middle levels collapsed | Single "Back to [parent]" link |
| Sticky table of contents | Collapsible table of contents at top | Collapsible "On this page" |

## Footer

Group links in 3-5 columns: product, company, resources, support, legal. Include contact, accessibility statement, privacy and cookie settings, and language or region switcher. On phones, stack columns or collapse them into accordions.
