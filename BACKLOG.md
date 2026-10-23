# Completion backlog

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

## Eval hardening, 0.7.1

Version-Timestamp: 2026-10-23 11:31:41 UTC

- [x] Split rubrics: eight cases now have 3-4 weighted `llm` graders each; nine cases measured at `--runs 3 --ablation with-without` ($4.05).
- [x] Fix: `packaging-luxury-vs-value` gave no named faces or hex values because the tier recipes were reachable only through `atlas.py`; owner skill print-packaging-social. Before 0.00 (3 runs), after 1.00 (1 run).
- [x] Fix: `director-distinct-scored` failed `matrix` (no accessibility criterion, no reasons); owner skill design-director. Before 0.80, after 1.00 (1 run).
- [x] Fix: `critique-described-pricing` dropped scores and caps in conceptual critiques; owner skill design-critique. `scoring-gates` passes after the fix (1 run).
- [ ] Fix: `low-literacy-benefits-form` fails `level-standard`, `structure` and `help-channels` because answers drop the atlas numbers (grade 5-6, step count, ISO 24495-1); owner skill ux-design. Direct atlas link added: 0.33 to 0.50. Next: make them non-negotiables.
- [ ] Fix: `quebec-french-launch` fails `typography` and `fr-ca` (both arms) because web-design does not route to `atlas/markets/canada.md`; owner skill web-design.
- [ ] Decide: `tokens-dark-mode-contrast/tokens` wants light values that the prompt does not ask for. Either name them in the prompt or add a light-and-dark token table to `color/references/dark-mode.md`.
- [ ] Confirm the 0.7.1 single-run fixes with `--runs 3 --ablation with-without` before the next release.
- [ ] Harden or label as guards the no-lift cases: `pharma-promo-fair-balance` (1.00/1.00) and `email-dark-mode` (1.00/0.83).

## Design ops, 0.6.0

Version-Timestamp: 2026-10-20 11:00:00 UTC

- [x] Eval suite grown to 32 cases; the no-lift typography case replaced; maintainer eval loop skill with `summarize_eval.py`.
- [x] Parallel direction exploration and a five-member review panel as plugin agents.
- [x] `figma-workflow` skill and `compare_build.mjs` build-fidelity diff.
- [x] Spec radar (`tools/spec_radar.py`, `docs/SPEC-RADAR.md`) and a monthly scheduled review.
- [x] Private companion scaffold (taste profile, references, outcomes log) prepared outside this repository.
- [x] Full eval run (one per arm) and a targeted re-run after fixes: skill loading rose from 8/21 to 14/15 tracked runs (see RELEASE-060).
- [x] Harden the eight all-of rubrics that still fail strong answers into weighted graders, then `--runs 3` with ablation; fix skills one at a time with the eval loop (done in 0.7.1; see the evals README).
- [x] Make `pharma-promo-fair-balance` load a skill: web-design description change, fired 3/3 (0.7.1).
- [ ] Exercise `figma-workflow` against a live Figma file through the Figma MCP server; confirm plan limits marked "verify".
- [ ] Confirm the `visual-design-studio:<agent>` invocation name on each host; confirm Codex ignores agents cleanly.
- [ ] Attach the repository and GitHub connector to the monthly spec radar scheduled task so it can open PRs.
- [ ] Create the private `nmg-design-studio-private` repository and push the scaffold; run the calibration exercise.
- [ ] Bring `figma-workflow/references/no-connector.md` up to reference depth (written under time pressure).

## Claude-native design studio, 0.5.0

Version-Timestamp: 2026-10-20 02:05:00 UTC

- [x] Native Claude packaging (`.claude-plugin`) with a repository marketplace; versions synced with Codex packaging.
- [x] `claude plugin validate` passes locally and in CI; local install and enable observed in Claude Code 2.1.304.
- [x] Registered design-director, 13 discipline skills, design-critique and continuity skills with claude.ai-compatible frontmatter.
- [x] Design Space Atlas: 125-entry registry, schema, query/combine/validate/build tool, body-ID checks.
- [x] Replace "no universal numbers" guidance with defaults plus documented overrides.
- [x] CI for Python 3.9 and 3.13 suites, validators, atlas, tokens, payload integrity, Claude validation and example builds.
- [x] 12 `claude plugin eval` cases with a should-not-fire control.
- [x] Eval smoke tests (about $0.30): control case passes; the direction case exposed and then confirmed fixes for two design-director defects (reply language, specifics under concision).
- [x] Run the full eval suite with ablation within an agreed cost cap (done in 0.6.0 at one run per arm; see RELEASE-060).
- [x] Replace or harden eval cases that pass without the plugin (typography-longform-defaults) with cases that test kit-specific value.
- [ ] Token contract additions proposed during authoring: `--duration-reduced` (reduced-motion crossfade), `--ease-overshoot`, a `linear()` spring and stagger tokens; `--size-control-sm/md/lg` (32/40/48px); density tokens.
- [ ] Confirm claude.ai and Claude Desktop marketplace install in a receiving workspace; verify Codex install of 0.5.0.
- [ ] Native-speaker review of market entries and the Arabic, Japanese, Portuguese and Spanish stylescape copy.
- [ ] Re-verify every atlas statement marked "verify" against primary sources before relying on it for a client.
- [x] Second wave (shipped in 0.6.0): eval-driven improvement loop skill, parallel-agent divergence in design-director, specialist reviewer agents, Figma round-trip skill, design-to-build fidelity checks, scheduled spec and trend radar.
- [x] Private companion (scaffolded in 0.6.0; repository still to create): studio taste profile, licensed visual reference library and client outcome records, kept out of this public repository.

## Standalone and reference portability, 0.3.0

Version-Timestamp: 2026-09-27T14:35:39-04:00

- [x] Original applied method cards linked to existing capabilities for use without books.
- [x] Explicit standalone/local-library preflight, optional fallback and named-source evidence boundaries.
- [x] Fresh separate Codex session uses a method and produces a bounded plan without book/config access.
- [x] Verify authorized Drive folder access and complete bulk download in a signed-out browser on the authoring Mac.
- [x] Complete safe multi-ZIP import and verify all 723 received manifest entries after an observed Drive filename change.
- [x] Complete integrated tests, final pinned resume and independent review with no release blockers.
- [x] Publish 0.3.0 on main through PR 3 and verify an anonymous checkout, all 376 payload entries and standalone startup.
- [ ] Repair the pre-existing Unicode case-fold excerpt-offset edge case in a later bounded change.

See [edition evidence](docs/STANDALONE-030.md). A signed-out receiving context is verified separately from physical use on a different computer. Full source review, extraction gaps and native-host artifact acceptance remain scoped follow-up work.

## Current public distribution milestone

Version-Timestamp: 2026-09-27T13:51:02-04:00

The [0.2.1 public preparation](docs/PUBLIC-RELEASE-021.md) supersedes older distribution and installation instructions below. Use [INSTALLATION](INSTALLATION.md) and [VERIFIED-PIN](docs/VERIFIED-PIN.md) for current setup. Native host acceptance, real-project output and target-device validation remain separate work. The collection-specific reference milestones below describe an author-only historical corpus, not a public download promise.

## Historical first usable release backlog

The [design quality audit](docs/DESIGN-QUALITY-AUDIT-2026-09-16.md) adds an ordered pre-use improvement plan, including a reproduced handoff-check conflict, selection validation, continuity/link fixes and executed craft benchmarks. Its findings are recommendations, not completed implementations. Version-Timestamp: 2026-09-16 17:22:38 AST.

- [x] Assemble 130-capability library and single-entry Codex plugin candidate.
- [x] Add independent existing-brand/new-brand launch and sanitized feedback instructions.
- [x] Validate wrapper schema, payload hashes, archive and 19 packaged tests.
- [ ] Reconcile historical status prose inside the preserved library with a current supported-scope matrix; readiness override currently takes precedence for release status.
- [x] Verify Codex local installation, enabled-state readback and installed payload hashes.
- [x] Add project-level explicit startup entry and verify it in a separate folder without a path in the task prompt.
- [ ] Global automatic discovery remains limited by host skill-context truncation. Verify removal and upgrade behavior.
- [ ] Verify Claude Code explicit-path startup; implement native Claude plugin adapter only with supported discovery semantics.
- [x] Fresh Codex explicit-path read and selection for both brand modes, with project/feedback boundary checks.
- [ ] Run artifact generation, revision and resume for both brand modes. No real brand details needed for infrastructure checks.
- [ ] Resolve known local-model revision-fidelity and touchscreen-recovery failures using a qualified execution route. Do not route these autonomously to the failed local model.
- [ ] Validate dependency selection and exclusions during actual production, beyond planning fixtures.
- [ ] Finish independent release review and resolve findings on the final bytes.
- [ ] Publish a versioned release archive, digest, installation guide, limitations and rollback instructions.
- [ ] Consolidate the local research workspace to GitHub source mapping and a repeatable reviewed export/update process. Do not imply this curated snapshot is a complete workspace sync.

## Separate real-brand projects

- [ ] Owner creates existing-brand project and provides its first deliverable and authoritative assets there.
- [ ] Owner creates new-brand project and provides its offer, audience and first deliverable there.
- [ ] Each project pins the library version and records approvals, outputs and actual checks locally.
- [ ] A named teammate completes an assignment, revision and interrupted-session recovery.
- [ ] Feed sanitized observations back through review; test changes before adoption and opt projects into upgrades explicitly.

## Production and providers

- [ ] Inspect completed OpenArt motion for geometry, label, reflections and creative quality; resolve output dimensions and charge receipt. No additional generation allowance implied.
- [ ] Verify Higgsfield authentication and bounded generation when a scoped allowance is provided.
- [ ] Extend native editable/export tests as selected projects require: linked/perspective Photoshop work and richer motion editing remain unverified.
- [ ] Evaluate separate Figma CLI only for a demonstrated gap; desktop and official MCP have bounded fixture evidence.
- [ ] Discover and qualify After Effects, Premiere or InDesign only when a deliverable needs them.
- [ ] Verify actual display/player resolution, codecs, color, sustained playback and touchscreen recovery/accessibility on target hardware.
- [ ] Obtain human visual approval and relevant accessibility/audience acceptance of real deliverables.

## Optional and deferred

- [ ] Recover inaccessible research attachments if access becomes available; no paid libraries required for initial release.
- [ ] Implement cataloged design-system components when a real project selects them; inventory does not mean all components exist as code.
- [ ] Off-device backup: explicitly deferred.
- [ ] PowerPoint: explicitly deferred.

Do not add arbitrary skills or repeat successful tests merely to extend this list. Prioritize observed failures and usable project outcomes. Authentication, generation, technical validation, visual approval, installation and release are separate states.

## Reference portability and IDE follow-up

- [x] Owner confirmed Google Drive distribution and recipient local use; bundle staged in a dedicated Drive sync folder. Signed-out cloud download and local import are verified in 0.3.0.
- [x] Built relative-path catalog, permission records and checksum manifest for the selected sources.
- [ ] Resolve uncopied/restricted/unsupported references and inspect outstanding OCR/visual gaps where useful.
- [x] Verified staged bundle hashes and source/page retrieval from a separate local project folder.
- [ ] Verify cloud synchronization and a download on an independent receiving machine.
- [ ] Execute Cursor startup, artifact/revision and recovery acceptance.
- [ ] Execute Claude Code wrapper startup, artifact/revision and recovery acceptance.
- [ ] Keep optional reference access separate from kit installation; no blanket 100-percent knowledge claim.

## 0.2.0 quality implementation

The September 16 audit now has a [linked implementation and evidence record](docs/QUALITY-020-RELEASE.md). Track actual remaining gates there and in [RESUME](RESUME.md); do not re-open repaired gaps solely because this historical backlog lists them. Human preference, real project use and device tests remain distinct from kit implementation.

The eleven September 16 audit implementation items are complete in edition 0.2.0; [final evidence](docs/QUALITY-020-RELEASE.md) and [review disposition](docs/QUALITY-020-REVIEW.md) supersede their pending implementation status. Next acceptance is a separately scoped real project and its actual user/device review. Avoid creating another broad catalog expansion before observing a concrete unmet need.
