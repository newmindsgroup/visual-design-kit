# Case map

Version-Timestamp: 2026-11-10 03:20:00 UTC

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
| `sell-sheet-print-master-canva-twin` | print-packaging-social, design-director | `skills/print-packaging-social/references/print-production-pipeline.md`, `references/canva-handoff.md` |
| `business-card-crop-marks-minimums` | print-packaging-social | `skills/print-packaging-social/references/print-production.md`, `references/print-production-pipeline.md` |
| `brand-book-toc-color-systems` | brand-identity, color, design-system | `skills/brand-identity/references/brand-book-production.md`, `references/guidelines.md` |
| `logo-small-size-one-color-tests` | brand-identity | `skills/brand-identity/references/logo-design.md` |
| `social-spot-15s-vertical-spec` | motion, print-packaging-social | `skills/motion/references/production-pipeline.md`, `skills/print-packaging-social/references/social-formats.md` |
| `logo-animation-portable-lottie` | motion, brand-identity | `skills/motion/references/production-pipeline.md`, `references/lottie-and-rive.md`, `library/scripts/lottie_build.py` |
| `capabilities-deck-canva-safe-charts` | print-packaging-social, design-director | `skills/print-packaging-social/references/presentations.md` (Canva exception), `library/examples/deck-pptx/README.md` |
| `canva-handoff-recurring-collateral` | print-packaging-social, brand-identity, design-director | `skills/print-packaging-social/references/canva-handoff.md` |
| `client-video-asset-licensing` | motion, imagery, print-packaging-social | `library/knowledge/ASSETS-LICENSES.md` |
| `no-fire-ffmpeg-extract-audio` | every skill's `description` | None: no skill may load |

Atlas entries are shared: after editing one, re-run every case whose row names it.

## Native and reconstruction cases

Version-Timestamp: 2026-10-27 07:51:01 AST

| Case | Owner | Concrete evidence contract |
| --- | --- | --- |
| reconstruct-unknown-scale | reference-reconstruction | observation-to-spec: unknown scale and interactions stay unknown |
| reference-adapt-locked-brand | reference-reconstruction, design-system | project locks and state-complete gallery |
| icon-family-optical-and-native | icon-design | optical variants, semantic registry and compiled icon prerequisites |
| macos-project-locked-baseline | native-app-design | existing OS baseline, surfaces, keyboard and actual toolchain failures |

## Cinematic web cases (0.10.0)

Version-Timestamp: 2026-11-05 18:10:00 UTC

| Case | Owner skill (edit this to fix) | Kit content the grader rewards |
| --- | --- | --- |
| `cinematic-hero-spec-signature` | web-design | `skills/web-design/references/cinematic-landing.md` (one signature, first CSS rule), `references/landing-spec-template.md`, `references/cinematic-craft.md` (conflicts table: 12px labels, 1.2 s entrance, `preload="metadata"`), `skills/imagery/references/media-for-web.md` (poster budget), `library/knowledge/web-techniques/INDEX.md` (pause control, WCAG 2.2.2) |
| `lovable-builder-prompt-from-direction` | web-design, design-director | `skills/web-design/references/builder-prompts.md` (Lovable stack line, tokens in `index.css`, constraints last, verify), `skills/design-director/references/handoff.md` section 4, `skills/color/references/contrast.md` (accent button pair) |
| `scroll-video-hero-motion-budget` | web-design, motion | `library/knowledge/web-techniques/video-and-media.md` technique 7 (lerp 0.12, seek guard, frame cache, `-g` encode), `skills/imagery/references/media-for-web.md` (scrub clip budget), `skills/web-design/SKILL.md` and `references/performance.md` (Core Web Vitals, JS budget), `skills/motion/SKILL.md` (reduced motion) |

## UI libraries and reference-first cases (0.11.0)

Version-Timestamp: 2026-11-10 03:00:00 UTC

| Case | Owner skill (edit this to fix) | Kit content the grader rewards |
| --- | --- | --- |
| `ui-library-picks-shadcn-app` | ui-design | `skills/ui-design/references/component-libraries.md` (check package.json first, one primitive layer, mismatch map: Sonner, Vaul unmaintained, cmdk, NumberFlow `respectMotionPreference`), `references/states-and-feedback.md` (toast timing, no errors needing action in a toast, WCAG 2.2.1), `references/navigation.md` (visible command palette trigger) |
| `restyle-default-shadcn-dashboard` | ui-design, design-director, design-critique | `skills/design-director/references/reference-first.md` (evidence, components, motion), `references/handoff.md` section 4 (brief checklist: job and user, constraints, libraries, avoid list, AGENTS.md, small passes), `skills/ui-design/references/component-libraries.md` (restyle recipe, radius scale trap, `--input` to border-strong), `skills/design-critique/references/ai-tells.md` (AT-27, AT-28, AT-29) |

## Gauntlet loop case (0.12.0)

Version-Timestamp: 2026-11-10 03:20:00 UTC

| Case | Owner skill (edit this to fix) | Kit content the grader rewards |
| --- | --- | --- |
| `gauntlet-beat-linear-homepage` | design-critique | `skills/design-critique/references/gauntlet-loop.md` (named, fetchable bar captured at the same widths with `render_review.mjs`; pieces; hard gates before every comparison; blind binary `art-director` critic, fresh each round, single-context fallback; copy guard and name-swap; win-or-ceiling exit with stop-and-report; round log; hand-back to the rubric), `references/review-panel.md` (gauntlet row; conflict ladder: a locked color that fails as text is used as non-text), `references/accessibility-audit.md` and `skills/color/references/contrast.md` (#FCA311 on white about 2.0:1) |
