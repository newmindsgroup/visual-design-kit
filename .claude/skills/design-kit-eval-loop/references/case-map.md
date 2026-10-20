# Case map

Version-Timestamp: 2026-10-20 10:31:13 UTC

Which eval cases to re-run after editing a skill, and where the knowledge each case's grader rewards lives in the kit. Paths are under `plugins/visual-design-studio/`. After any change to a skill `description`, also re-run every `no-fire-*` case.

| Case | Owner skill (edit this to fix) | Kit content the grader rewards |
| --- | --- | --- |
| `android-m3-nav-six-sections` | native-app-design | `skills/native-app-design/references/android-material3.md` (3-5 bar destinations, window size classes, `NavigationSuiteScaffold`) |
| `arabic-rtl-hero` | typography, web-design | `skills/typography/references/multiscript.md` (RTL, Arabic faces) |
| `brazil-pix-checkout` | ui-design (forms, checkout), design-director | `library/atlas/markets/brazil-portuguese.md` (Pix, copia e cola, installments, CPF, R$ format) |
| `critique-ai-tells` | design-critique | `skills/design-critique/references/ai-tells.md` |
| `critique-described-pricing` | design-critique | `skills/design-critique/SKILL.md` (evidence default: label prose-only critiques conceptual), `references/rubric.md` (gates, caps), `references/ai-tells.md` |
| `dataviz-nine-categories` | data-visualization | `skills/data-visualization/references/data-palettes.md` (6, 8 at most; Okabe-Ito; dark values) |
| `direction-genz-neobank-brazil` | design-director | `skills/design-director/SKILL.md` non-negotiables, `library/atlas/markets/brazil-portuguese.md` |
| `director-distinct-scored` | design-director | `skills/design-director/references/divergence.md` (3-of-6 distinctness), `references/scoring.md` (weights, sensitivity check) |
| `email-dark-mode` | print-packaging-social | `skills/print-packaging-social/references/email.md` (three client behaviors, `color-scheme`, `[data-ogsc]`) |
| `healthcare-portal-compliance` | ux-design, web-design | `library/atlas/industries/healthcare-provider.md` |
| `ios-tab-bar-seven-sections` | native-app-design | `skills/native-app-design/references/ios-hig.md` |
| `japan-vertical-editorial` | typography | `skills/typography/references/multiscript.md` (CJK), `library/atlas/markets/japan.md` (tategaki, kinsoku) |
| `kids-coppa-onboarding` | ux-design, native-app-design | `library/atlas/industries/kids-family.md`, `library/atlas/audiences/children-under-13.md` |
| `locked-brand-careers-site` | design-director | `skills/design-director/SKILL.md` (mandated direction: explore executions; existing-brand locks), `skills/color/references/contrast.md` |
| `low-literacy-benefits-form` | ux-design (content design) | `library/atlas/audiences/low-literacy-plain-language.md` (grade 5-6, ISO 24495-1) |
| `motion-bottom-sheet` | motion | `skills/motion/SKILL.md` defaults, `references/timing-and-easing.md` |
| `motion-reduced-motion-spec` | motion | `skills/motion/SKILL.md` (reduced motion, WCAG 2.2.2), `references/web-implementation.md` |
| `neurodivergent-focus-app` | ux-design, ui-design | `library/atlas/audiences/neurodivergent.md` (pressure patterns, COGA, personalization) |
| `no-fire-git-undo`, `no-fire-spreadsheet-formula`, `no-fire-sql-query` | every skill's `description` | None: no skill may load |
| `older-adults-medication-app` | ux-design, native-app-design | `library/atlas/audiences/older-adults.md` |
| `packaging-barcode-quiet-zone` | print-packaging-social | `skills/print-packaging-social/references/packaging.md` (GS1 sizes, 80% minimum, 11X/7X quiet zones) |
| `packaging-luxury-vs-value` | print-packaging-social, brand-identity | `library/atlas/tiers/luxury.md`, `library/atlas/tiers/value.md` |
| `pharma-promo-fair-balance` | web-design, design-director | `library/atlas/industries/pharma-biotech.md` (fair balance, ISI, OPDP) |
| `print-business-card-us` | print-packaging-social | `skills/print-packaging-social/references/print-production.md` |
| `qualifying-questions-vague-logo` | design-director, brand-identity | `skills/design-director/references/intake.md` |
| `qualifying-restraint-full-brief` | design-director | `skills/design-director/SKILL.md` (ask 0-1 when the brief answers the questions) |
| `quebec-french-launch` | web-design, ux-design | `library/atlas/markets/canada.md` (Bill 96, fr-CA, Law 25, QST) |
| `tokens-dark-mode-contrast` | color, design-system | `skills/color/references/dark-mode.md` (canvas L, elevation, accent step) |
| `tokens-light-dark` | color, design-system | `skills/color/references/dark-mode.md`, `library/tokens/` |
| `typography-bilingual-annual-report` | typography | `skills/typography/references/multiscript.md` (Arabic size and line-height, numerals, no tracking) |

Atlas entries are shared: after editing one, re-run every case whose row names it.
