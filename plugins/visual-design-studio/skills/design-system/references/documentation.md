# Design system documentation

Version-Timestamp: 2026-10-20 02:08:24 UTC

Documentation is how the system is used. If a rule is not on the page where someone looks for it, it does not exist. Aim for pages people can scan in 30 seconds to answer "should I use this, and how?", with depth below the fold.

## Site structure

| Section | Contents |
| --- | --- |
| Get started | What the system is, who it serves, install for each platform, how to get help, how to contribute |
| Foundations | Color (roles, contrast rules, modes), typography (roles and scale), space and layout (scale, grid, breakpoints), radius and elevation, motion (durations, easing, reduced motion), iconography, accessibility principles, content and voice |
| Tokens | Generated reference of every semantic token with value per mode and brand, plus the naming convention and tier rules |
| Components | One page per component (template below) |
| Patterns | Assembled solutions: forms and validation, empty states, loading, navigation, data tables, onboarding, error recovery |
| Platforms | Web, iOS, Android notes where behavior or naming differs |
| Resources | Figma libraries, code packages, Storybook, changelog, roadmap, governance and RFCs |

## Component page template

1. **Name, status and version**: `Stable` / `Beta` / `Deprecated` badge, package version, links to Figma, Storybook and source.
2. **Overview**: one sentence on what it is for; a live example.
3. **When to use / when not to use**: with the alternative component named ("Use a Link for navigation").
4. **Anatomy**: numbered diagram of parts with their names (the same names as slots and Figma layers).
5. **Variants and sizes**: each with a short purpose statement.
6. **States**: default, hover, focus, pressed, selected, disabled, loading, error, empty, as applicable, shown side by side.
7. **Behavior**: interaction rules, responsive behavior, overflow and truncation, long and translated text, RTL.
8. **Content guidelines**: label length, capitalization, verb choice, error message patterns, with examples.
9. **Do and don't**: 2-6 pairs of real rendered examples with a one-line reason each.
10. **Accessibility**: role and semantics, keyboard table, focus management, screen reader announcements, target size, contrast notes, known limitations.
11. **Props / API**: generated from the source types (name, type, default, description), plus platform equivalents (SwiftUI, Compose).
12. **Tokens used**: component and semantic tokens it consumes, so theme authors know what changes it.
13. **Related**: components and patterns used with it.
14. **Changelog**: the entries for this component, generated from the release log.

Write in the imperative, keep each section short, and show rather than describe. Every example on the page is the real component rendered from the package, never a screenshot that can drift.

## Accessibility section example

Every component page carries a section in this shape (dialog shown):

| Key | Action |
| --- | --- |
| Tab / Shift-Tab | Move focus between controls inside the dialog; focus does not leave it |
| Esc | Close the dialog and return focus to the control that opened it |
| Enter | Activate the focused button |

- Role and name: `dialog` with `aria-modal="true"`, labelled by its title, described by its body when short.
- Screen readers announce the title and role on open; closing returns to the trigger.
- Target size: buttons at least 44x44px on touch layouts.
- Known limitations: list any, with the issue link.

## Do and don't format

Show each pair side by side, both rendered from the real component, with a one-line caption: "Do: one primary action per dialog." / "Don't: two primary buttons competing for attention." Use a green or red label plus a check or cross icon and the words Do and Don't, so the meaning does not depend on color.

## Storybook

- Storybook 10 (October 2025) is ESM-only; check the migration guide when upgrading older projects.
- One stories file per component with a story per variant, size and state, plus edge cases: long text, empty, error, RTL, dark mode, high contrast, compact density.
- **Accessibility addon** (`@storybook/addon-a11y`, axe-core): run on every story; configure the rules to fail CI on violations rather than only warn. Axe catches a portion of issues (missing names, contrast, ARIA misuse); keyboard and screen-reader behavior still need manual checks.
- **Interaction and component tests**: write play functions for keyboard paths (Tab, Enter, Esc, arrows) and run them in CI with the Storybook test runner or its Vitest integration.
- **Visual regression**: snapshot stories per mode and brand (Chromatic or a self-hosted Playwright screenshot job); review diffs in pull requests.
- Autodocs generate the props table; add MDX only for guidance that types cannot express.
- Use globals or toolbar controls for theme, brand, density and locale so reviewers can switch them on any story.

## Docs platform choice

| Option | Choose when |
| --- | --- |
| Storybook docs only | Engineering-led system, small team, components are the whole story |
| Static site (Astro Starlight, Docusaurus, Next.js) with embedded live components | Public or multi-team system that needs foundations, patterns and content guidance next to code |
| Hosted design-system doc tools (zeroheight, Supernova, Knapsack) | Design-led teams that want Figma embeds and non-developer editing; check token and code sync features and cost |

Keep docs in the same repository as the code where possible, so a pull request changes code, stories, docs and changelog together.

## Writing guidance that gets followed

- Lead with the decision: "Use one primary button per view."
- Give the number, in the form "Toasts stay 6 seconds; 10 when they contain an action" (an example of the form; set your system's own values).
- Show the failure: a don't example with the reason is worth three paragraphs.
- Name the alternative whenever you say "don't".
- Date anything platform-specific and link the source.

## Maintenance

- Docs build fails when a component lacks a page, a story or an accessibility section.
- Each release regenerates token tables, props tables and per-component changelogs.
- Review the top 10 most visited pages quarterly against support questions; the questions show what the docs fail to answer.
- Archive, do not delete, deprecated component pages until the removal release has shipped, with a banner pointing to the replacement.
