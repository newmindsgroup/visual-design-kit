# Release notes

Version-Timestamp: 2026-09-27T13:51:25-04:00

## 0.8.0 Production layer: finished collateral, print, decks and motion

Version-Timestamp: 2026-10-27 12:00:00 UTC

The kit now produces finished files, not only directions and specs.

- **Collateral templates** (`library/examples/collateral/`): token-driven brand guidelines book, one-pager, case study, proposal cover, business card with bleed, social carousel and capabilities deck, in both kit brands. `print-packaging-social/scripts/render_collateral.mjs` renders screen PDFs and PNGs with layout and axe checks; `scripts/preflight_pdf.py` (standard library) reports boxes, bleed, fonts, image resolution, color spaces and output intent.
- **Print master and Canva twin.** `references/print-production-pipeline.md`: WeasyPrint (optional external CLI) for PDF/X with `device-cmyk()` and the printer's ICC profile; Playwright for accessible screen PDFs; Ghostscript documented only (AGPL). `references/canva-handoff.md`: brand template autofill, import and export limits, connector gate.
- **Decks** (`library/examples/deck-pptx/`): PptxGenJS, token-driven slide masters, a Canva-safe build and a PowerPoint-native build.
- **Motion** (`library/examples/motion-remotion/`, `library/scripts/lottie_build.py`): six Remotion compositions driven by tokens (logo reveal, kinetic type, lower third, 9:16 social, captions, Lottie in video) and a stdlib builder and validator for portable Lottie. `motion/references/production-pipeline.md` chooses the engine and sets accessibility gates. Remotion is source-available, not MIT; see `library/knowledge/ASSETS-LICENSES.md`.
- **Brand identity production:** `references/brand-book-production.md` and `references/identity-deliverables.md`; color specs beyond HEX/RGB are labeled nearest matches until proofed.
- **Asset licenses:** `library/knowledge/ASSETS-LICENSES.md` (icons, OFL fonts, CC0 and Pixabay audio, C2PA, non-MIT tools, provenance record).
- **Evals:** 10 production-layer cases (42 in total). **Codex:** `tools/check_codex_parity.py` (also in CI) and `docs/CODEX.md`.

Existing project pins are unaffected; adopt 0.8.0 deliberately.

## 0.7.1 Eval hardening and skill routing

Version-Timestamp: 2026-10-23 11:31:41 UTC

- **Weighted graders.** Eight eval cases that failed strong answers on one clause of an all-of rubric now have 3-4 weighted `llm` graders each, so partial credit is visible. Nine cases measured at three runs per arm: mean 0.67 with the plugin, 0.50 without (+0.17); a skill loaded in 27 of 27 with-plugin runs.
- **Routing fixes found by the split graders.** `print-packaging-social` links the tier token recipes and `ux-design` links the audience entries directly, since `atlas.py` needs a shell. `design-director` always scores accessibility, with a reason per criterion. `design-critique` keeps provisional scores and caps in conceptual critiques. `web-design` loads for above-the-fold and regulated (prescription drug, health, finance) pages and links the pharma-biotech entry.
- **Still open:** low-literacy numbers, Quebec French typography and a light-mode token question (see `BACKLOG.md`).

Existing project pins are unaffected; adopt 0.7.1 deliberately.

## 0.7.0 Research workspace methods merged

Version-Timestamp: 2026-10-23 16:19:27 UTC

The kit is now the single source of truth. Method work that had stayed in the original local research workspace joins the library.

- **Google Docs editorial design.** New `design-google-docs` draft skill and `google-docs-editorial` capability for native pageless document styling.
- **Logo brainstorming pilot.** Evidence, concept and critique loop (`design-logo-concepts/references/evidence-concept-critique.md`), `templates/logo-generation-brief.md`, a worked pilot example, and matching gates in logo concepts, refinement, evaluation, the logo study and identity handoff.
- **Photographic quality method.** `REALISM-REASSESSMENT.md`: a seven-step sequence for product and environment imagery (real product truth, photographic direction, one inspected hero still before adapting or animating). Linked from the media quality workflow.
- **Website methods.** Owner editing guidance, buyer decision density for content audits, `scripts/website_fixture.py` and the `examples/website-practice` form example with tests.
- **Research records.** `docs/research/` holds the sanitized decision register and knowledge gap audit.

Existing project pins are unaffected; adopt 0.7.0 deliberately.

## 0.6.2 Codex local work reconciled

Version-Timestamp: 2026-10-23 16:11:23 UTC

- **Persona workbench.** `design-persona-build` gains a complete reusable persona presentation: HTML, CSS and JS assets, `references/presentation.md` and `scripts/persona_workbench.py`, with URL lookup, source-language fallback and translated labels ([record](../../../docs/PERSONA-WORKBENCH.md)).
- **Typography and spacing receipt checks.** `scripts/composition_checks.py` validates a typography decision receipt against declared, format-specific thresholds; `typography` and `production-interface` library guidance link to it ([record](../../../docs/TYPOGRAPHY-SPACING-042.md)). Passing thresholds is not design approval.
- Built locally by Codex as editions 0.4.1 and 0.4.2 on an older base; rebased onto 0.6.1 with payload metadata regenerated by `tools/build_plugin.py`.

## 0.6.1 Prompt handoff and scoped spec radar

Version-Timestamp: 2026-10-20 17:00:00 UTC

- **Prompts for generators and build tools.** `design-director`'s handoff now has a step that turns the chosen recipe into prompts for image, video and UI-build tools. It hands off to the `prompt-engineering-expert` plugin (now listed in this marketplace) and falls back to `imagery`'s AI image generation reference.
- **Spec radar scope.** The monthly review covers only the United States, the Dominican Republic and the Caribbean, Spanish-speaking Latin America, platform specs, WCAG, ADA and Section 508 (`tools/spec_radar_scope.json`). In scope: 205 of 299 claims.

## 0.6.0 Design ops: agents, Figma, fidelity, evals

Version-Timestamp: 2026-10-20 11:00:00 UTC

- **Specialist agents.** `direction-explorer` builds one direction per position in parallel for `design-director`; `art-director`, `accessibility-auditor`, `copy-editor`, `brand-guardian` and `frontend-engineer` form the `design-critique` review panel with a score merge and conflict ladder. Hosts without plugin agents use the single-context fallback.
- **`figma-workflow` skill.** Token import as Figma variables (`tokens.py figma-script`), variant components bound to variables, stylescape and screen push, pull to code, Code Connect mapping, Dev Mode handoff and a fallback without a Figma connector.
- **Build fidelity.** `compare_build.mjs` diffs an approved design against the build (pixels and computed styles) at real widths, with masks and CI exit codes; `references/build-fidelity.md` sets thresholds.
- **Evals.** 32 cases; `typography-longform-defaults` (no lift) replaced by a bilingual annual-report case.

Existing project pins are unaffected; adopt 0.6.0 deliberately.

## 0.5.0 Claude-native design studio

Version-Timestamp: 2026-10-20 03:40:00 UTC

The kit becomes a native Claude plugin (Claude Code, claude.ai, Claude Desktop) while keeping Codex packaging, and shifts from process guidance to design knowledge Claude can apply directly.

- **16 registered skills.** `design-director` (brief to scored, rendered directions), 13 discipline skills with concrete defaults (brand identity, typography, color, layout, imagery, motion, UX, UI, web, native apps, design systems, data visualization, print/packaging/social), `design-critique` (render, score, revise) and `design-project-start` (client-project continuity). Always-on cost is about 2,900 tokens; each skill loads its body only when used.
- **Design Space Atlas.** 125 schema-validated entries: 37 styles, 32 industries, 17 markets, 10 audiences, 12 archetypes, 5 price tiers and 12 channels, with `scripts/atlas.py` to query, combine, validate and index them.
- **Design tokens.** DTCG source with light, dark and high-contrast modes and two brands; CSS, Tailwind v4, resolved JSON and Figma variable outputs; `scripts/tokens.py` lints 336 contrast pairs; `scripts/color_tools.py` (OKLCH ramps, WCAG, APCA) and `scripts/type_scale.py`.
- **Calibration and quality loop.** Twelve stylescapes across very different briefs, an AI-tells gallery, a render-review script, a React reference component system and 12 `claude plugin eval` cases.
- **Policy change.** "No universal numbers" statements in this library now point to defaults with documented override conditions.
- **Fixes found during integration.** Status border tokens raised to 3:1 (WCAG 1.4.11); the FORM/TIDAL index page no longer orphans headline words, falls back to another font for arrows, or uses undersized link targets.

The 133-capability process library, templates and continuity contracts are unchanged and remain linked from the registered skills. Existing project pins are unaffected; adopt 0.5.0 deliberately.

## 0.2.1 public edition

Original kit files now have MIT licensing, with separate font and asset notices. Public setup uses the current payload checksum rather than obsolete archive instructions. Optional references require an independently supplied permitted local corpus. The package manifest describes public supervised evaluation and explicitly retains a publication review requirement and no production acceptance. Core design capabilities and example artwork are unchanged from 0.2.0. See [package readiness](../READINESS.md) and [current library setup](README.md).

The following entries are historical source-library records. Their internal-only status applies to those earlier candidates; current redistribution terms are [LICENSE](../LICENSE) and [NOTICE](../NOTICE.md). Historical test counts are not current execution claims.

## Earlier source-library checkpoint


Version-Timestamp: 2026-09-12T11:38:16-04:00

Status: candidate11, internal review only. This is a manually selected instruction library with local example code, not a production-certified plugin.

## Included scope

130 selectable capabilities cover research, creative direction, brand identity, typography, color, content, UX, websites, screen content, touchscreen workflows, media methods, production and quality review. The package contains314 payload files plus its manifest and checksums. No credentials, subscriptions, client assets or generated media are included.

## What changed

Candidate10 consolidated exact catalog-ID lookup and dependency/exclusion conflict rules, corrected team readiness, and current onboarding evidence. Directory names are not silently converted into IDs. Unresolved selections stay visible. Earlier candidates remain unchanged.

## Evidence and limits

Candidate09 has exact extraction and checksum evidence. Candidate08 passed all130 selectors, eleven JavaScript model tests and eight Python screen tests. The full source repository suite passed198 tests, which are not all distributed. Candidate11 must be judged from its own external verification receipt rather than inheriting those results.

Fresh Codex planning and recovery used candidate03. Claude Code staged writing and read-only recovery used candidate09 and required Codex-assisted ID repairs. These tests do not establish clean one-session execution or production acceptance for every capability. Focused Fable onboarding and motion reviews returned; their findings were addressed locally within recorded scope. Whole-library release review and supervised team acceptance remain open.

Internal source exercises include one completed OpenArt background job, schematic portrait/landscape compositions and a six-second H264 motion example. The motion example passed180-frame timing and local source-color checks, plus23 browser assertions and two value observations at1280/390 CSS pixels in desktop Chrome. These are not mobile-device, real-player or seamless-loop approval. Generated assets and private logs are excluded from this package. Source readiness does not transfer account access to another computer.

The packaged touchscreen fixture handles an actual unavailable-image error. It does not test video decoding or physical hardware. The private motion preview separately handles actual video-load failure and reduced motion; that preview is not bundled.

## Remaining acceptance

New-composition native editable export, photoreal glass, human motion/seam review, cross-player color compatibility, sustained hardware operation, whole-library release review and team acceptance remain open. Illustrator scripting last timed out. H264 sRGB transfer tagging needs target-player verification. No additional generation allowance is implied.

## Adopting project

1. Verify the archive source and exact hashes/membership before running code.
2. Read README.md and USAGE.md. Keep this library unchanged and use a separate project workspace.
3. Select exact capability IDs and record accepted inputs, missing facts and permissions.
4. Inspect actual outputs. A successful prompt or validator does not approve a design.
5. Report defects with sanitized reproduction details and exact file/version.

## Updates, rollback and sharing

Extract an update into a new folder. Compare manifests, then deliberately change the project's library pointer and record the version. Preserve accepted assets and the old folder. Roll back by restoring the prior pointer without deleting new evidence or replaying provider jobs.

The team destination/access and final release gates remain unresolved. Distribution status stays false. PowerPoint and backup remain deferred.

## Candidate11 corrections

Both65-entry contract reviews returned against candidate10. Candidate11 incorporates locally verified corrections: general media no longer depends on display discovery; touchscreen state ownership is explicit; shared audience, provider routing and handoff rules are aligned; active evidence and list-comparison limits are documented. The new general-media scope regression is included. The source suite passed199 tests after the routing change. Candidate11 checks are recorded separately. Reviews cover supplied entries and CLI, not every referenced document or production outcome.
