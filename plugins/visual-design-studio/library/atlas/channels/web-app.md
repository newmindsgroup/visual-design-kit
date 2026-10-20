---
id: channel.web-app
axis: channel
name: Web Application
aliases: [web app, saas app, dashboard, admin panel, portal, internal tool, product UI, browser app]
summary: Logged-in browser products where speed, density, state handling and keyboard flow decide the experience; design for repeated daily tasks, not first impressions.
tags: [saas, dashboard, app shell, tables, forms, productivity, components, states, keyboard, data]
pairs_with: [style.data-dense-utilitarian, style.corporate-modern, style.flat-material, style.dark-tech-developer, industry.saas-b2b, industry.developer-tools, industry.fintech-banking, audience.expert-power-users, archetype.sage, archetype.everyperson]
avoid_with: [style.maximalist-eclectic, style.art-nouveau-ornamental]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Web Application

## Formats and specs

| Item | Spec | Notes |
| --- | --- | --- |
| Viewport targets | Desktop 1280x720 minimum, 1440x900 primary, 1920x1080 wide; tablet 768-1024; phone 360-430 | Design the narrowest supported width first for mobile-capable apps |
| Breakpoints | 640, 768, 1024, 1280, 1536 px (kit tokens) | Switch shell at 1024: sidebar becomes drawer |
| App shell | Top bar 48-64px; sidebar 240-280px expanded, 56-72px collapsed; content max 1200-1440px; detail panel 360-480px | Persist collapsed state per user |
| Interactive performance | INP 200ms or less at p75; LCP 2.5s or less; CLS 0.1 or less | Interaction feedback within 100ms; skeleton after 300-400ms |
| Row and control heights | Table rows 32 (compact), 40 (default), 48 (comfortable); inputs and buttons 36-44px; touch contexts 44px+ | Offer a density toggle for expert users |
| Targets | 24x24 CSS px minimum (WCAG 2.2 AA 2.5.8); 44px for touch | Spacing can substitute when smaller |
| Text | 14px default UI text (13px compact tables), 16px minimum for mobile inputs (prevents iOS zoom); line-height 1.4-1.5 | Tabular numerals for data |
| Color | sRGB; semantic tokens with light, dark and high-contrast sets | Contrast 4.5:1 text, 3:1 UI and focus |
| File upload and export | Accept lists stated in UI; show max size; export CSV (UTF-8 with BOM for Excel), PDF, XLSX | Large exports run async with notification |
| Browser support | Evergreen Chrome, Edge, Safari, Firefox (last 2 versions) as a starting point | Confirm from the product's analytics |

## Structure and hierarchy

- **App shell:** persistent navigation (left rail for 6+ destinations, top tabs for 3-5), global search or command palette (Cmd/Ctrl+K), account and workspace switcher, notifications. Primary navigation holds 5-8 items; deeper structure lives in secondary nav or tabs.
- **Page anatomy:** title and primary action top-left and top-right; filters and view controls; the data region; contextual detail in a side panel. One primary button per view.
- **Information hierarchy:** summary metrics first, then trends, then detail tables. Put status and exceptions above averages.
- **Core patterns:** tables (sortable, sticky header, column resizing, bulk actions, virtualization above ~100 rows), forms (single column, labels above, inline validation on blur), wizards (3-6 steps with save-and-resume), dashboards (6-9 cards before scroll), settings (grouped, searchable), detail pages (summary, tabs, activity log).
- **State coverage is part of the design:** empty, first-run, loading, partial, error, offline, permission-denied, success, and long-content states for every view. See `ui-design` for patterns.

### Control and pattern defaults

| Pattern | Default |
| --- | --- |
| Data table | 40px rows, 40px sticky header, right-aligned tabular numerals, truncate with tooltip, page sizes 25 / 50 / 100, selection checkbox column 40px |
| Form | Labels above at 14px medium, field height 36-40px, help text 12-13px muted, error text below the field with icon, form width 480-640px, primary action bottom-left or bottom-right consistently |
| Dialog | Widths 480 (small), 640 (medium), 880 (large); max height 90vh; focus trap; Esc closes; primary action right |
| Toast | 5-8s, up to 2 stacked, `aria-live="polite"`, undo action on reversible changes |
| Empty state | Icon or illustration, one-line explanation, one primary action, optional link to docs |
| Dashboard grid | 12 columns, cards at least 280px wide, one headline metric per card, consistent time-range control |
| Search and filters | Debounce 200-300ms; show active filters as removable chips; keep results count visible |

## Craft defaults

- 4px base spacing; compact density uses 8-12px gaps, comfortable 16-24px. Use a restrained neutral palette with one accent; reserve red, amber and green for status and always pair with an icon or text.
- Type: a neutral UI sans (Inter, IBM Plex Sans, Geist, Public Sans) at 14px with 500/600 weights for labels; mono (JetBrains Mono, IBM Plex Mono) for IDs and code. Consider a distinctive display face only on empty states and onboarding.
- Motion: 120-200ms for hover, menus and toggles; 200-320ms for panels and dialogs; `cubic-bezier(0.2, 0, 0, 1)`; no decorative motion in data regions; reduced-motion removes slides.
- Feedback: optimistic updates with undo toasts (5-8s) for reversible actions; confirm dialogs only for destructive, irreversible actions, naming the object being deleted.
- Keyboard: every action reachable, logical tab order, documented shortcuts (a "?" overlay), focus returned after dialogs close.
- Errors: say what happened, what is preserved, and how to fix it; keep user input on failure.
- Dark mode is a first-class theme: re-derive surfaces and borders rather than inverting; check chart colors in both.

## Production and handoff

- Build from a design system (`design-system` skill): tokens, component API, Storybook or equivalent, and state matrices. Components follow the kit examples in `library/examples/component-specs/` (button, text field, dialog, data table).
- Figma: auto-layout with variables mapped to tokens; Code Connect links where components exist in code; annotate states, validation rules and keyboard behavior.
- Frameworks: React with Next.js, Remix or Vite SPA; Radix, React Aria or Headless UI primitives for accessible behavior; TanStack Table or similar for grids.
- Specify analytics and feature flags per interaction; define loading budgets (data under 2s p75 for primary views) and pagination or virtualization limits.
- Internationalization: pseudo-localize at 140% length, support RTL layout mirroring where markets require it, store and display times in explicit time zones.
- Enterprise concerns: SSO and roles in the information architecture, audit log views, data export, admin consoles. WCAG 2.2 AA and VPAT (ACR) documentation are frequent procurement requirements.

## QA checklist

- [ ] Every view has empty, loading, error, offline and long-content states.
- [ ] Keyboard-only run completes the top 5 tasks; focus ring visible on every interactive element.
- [ ] Screen reader pass (VoiceOver and NVDA) on table, dialog, form errors and live regions.
- [ ] Contrast 4.5:1 text, 3:1 UI in light, dark and high contrast; no status by color alone.
- [ ] Layout holds at 1280, 1024, 768 and 390 widths and at 200% zoom.
- [ ] 10,000-row and 1-row data sets tested; long names, RTL strings and emoji do not break layout.
- [ ] Destructive actions confirm or offer undo; session timeouts warn and preserve work.
- [ ] Performance: INP under 200ms on a mid-range laptop with throttled CPU.

## Reference anchors

- Apple Human Interface Guidelines (macOS and iPadOS sections) and Material Design 3 for interaction patterns
- IBM Carbon, Atlassian Design System, Shopify Polaris, GitHub Primer: public design systems with dense product patterns
- Linear and Notion as references for command palettes, keyboard flow and speed-as-brand
- Jakob Nielsen's 10 usability heuristics and Nielsen Norman Group research on tables and dashboards
- Edward Tufte and Stephen Few for dashboard clarity
