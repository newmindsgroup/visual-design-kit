# Governance and versioning

Version-Timestamp: 2026-10-20 02:08:24 UTC

Governance decides who can change the system and how changes reach products without breaking them. Keep it as light as the organization allows: a two-person studio system needs a changelog and semver; a 40-team enterprise system needs RFCs, office hours and adoption metrics.

## Team and contribution models

| Model | How it works | Fits | Risk |
| --- | --- | --- | --- |
| Centralized | A core team builds and owns everything | Early systems, one product, strong design leadership | Bottleneck; products build around it |
| Federated | Product teams contribute; a small council reviews | Many products with capable designers and engineers | Inconsistent quality without clear review criteria |
| Hybrid (default) | Core team owns foundations and core components; product teams contribute patterns and candidates through a defined path | Most multi-product organizations and agency-run client systems | Needs a visible intake process |

For agency work, the studio usually runs the centralized model during the engagement and hands the client a hybrid model with named owners at handoff.

## Contribution path

1. **Check**: does an existing component or pattern solve it? Ask in the system channel or office hours.
2. **Propose**: open an issue with the problem, screenshots of 2-3 real product uses, and why existing parts fail.
3. **Triage** (weekly): accept as system work, accept as a product-local pattern, or decline with the alternative. Decide within 2 weeks.
4. **Design and build**: follow the component template (anatomy, states, accessibility contract, tokens, Figma and code together).
5. **Review**: design review, accessibility review (keyboard, screen reader, contrast, reduced motion), code review, docs review.
6. **Release** as `Beta` first if the API might change; promote to `Stable` after 2 products use it without changes.

Product-local is a valid outcome. Not everything belongs in the system; a component needs at least 2-3 genuine consumers.

## RFCs for significant changes

Use an RFC for anything breaking, any new foundation (a token tier, a new mode, a brand), or a change of tooling. Template:

- Summary (2-3 sentences) and motivation with evidence.
- Detailed design: API, tokens, Figma changes, platform impact.
- Migration: who is affected, codemod or manual steps, timeline.
- Alternatives considered and why rejected.
- Accessibility, performance and localization impact.
- Open questions; decision owner; comment window (usually 1-2 weeks).

Record the decision and link it from the changelog entry.

## Semantic versioning for a design system

| Change | Version bump | Examples |
| --- | --- | --- |
| Breaking | **Major** (x.0.0) | Removing or renaming a component, prop, token or CSS variable after its deprecation period; changing a prop's default; changing keyboard or focus behavior people rely on; layout-affecting size changes (control height, spacing scale); dropping a framework or OS version |
| Additive | **Minor** (0.x.0) | New component, variant, prop, token or mode; deprecating something (with an alias); visual refinements that do not change layout |
| Fix | **Patch** (0.0.x) | Bug fixes, accessibility fixes that restore documented behavior, docs corrections, token value corrections that stay within the documented intent |

- Version tokens, components and Figma libraries together under one release number when they ship together; if they ship separately, keep a compatibility table.
- Visual changes are product changes: a token value change that shifts every button's color is at least a minor with screenshots in the notes, even if no API changed.
- Kit rule (token contract): a published CSS variable is never renamed without a deprecation alias that lives for at least one minor version.

## Deprecation policy

1. **Announce** in the minor release: changelog entry, docs banner, Figma "Deprecated" page, and the replacement.
2. **Warn**: development-only console warning, lint rule or TypeScript `@deprecated` tag; aliases keep old token names working.
3. **Migrate**: provide a codemod or a find-and-replace table; offer office hours for large consumers.
4. **Remove** in the next major, no sooner than one minor release and typically 3-6 months after the announcement, longer for enterprise clients with slow release trains.

Never deprecate without a replacement or a stated reason why none is needed.

## Changelog

- Follow the Keep a Changelog structure: Added, Changed, Deprecated, Removed, Fixed, Security, per release with a date.
- Generate entries from pull requests (Changesets or conventional commits) and edit them for humans: say what changed for the person using it, with migration steps and before/after screenshots for visual changes.
- Mirror the summary in Figma library publish notes.

## Release cadence

- Patch as needed; minor every 2-4 weeks; major at most 1-2 times a year with a migration guide.
- Freeze periods around client launches; communicate them.
- Every release passes: token build and lint (`tokens.py build`, `lint`, `check`), unit and interaction tests, accessibility checks on every story, visual regression review, and docs build.

## Adoption and health metrics

| Metric | How to measure | Healthy signal |
| --- | --- | --- |
| Component coverage | Share of UI built from system components (code scan of imports vs custom components, or a screenshot audit) | Rising quarter over quarter toward a target the team sets per product |
| Token adherence | Hardcoded colors, sizes and spacings found by stylelint or ESLint rules | Falling toward zero in new code |
| Version lag | Products' installed version vs latest | Most products within one minor; none more than one major behind |
| Figma usage | Library analytics: insertions, detachments per component | Detach rate low and stable; spikes flag missing variants |
| Time to build | Time for a standard screen or feature using the system | Falling |
| Accessibility defects | Defects traced to system components | Falling; fixed in patches |
| Satisfaction | Short survey of designers and developers twice a year | Qualitative trends and top requests |

Report a few metrics consistently rather than many once. Pair numbers with stories from product teams.

## Common failures

- Breaking changes shipped as minors because "it's only visual".
- Deprecations that never complete, so the system carries three generations of components.
- A contribution process so slow that teams fork the system.
- Figma and code released on different schedules with no compatibility table.
