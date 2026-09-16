# Design quality and readiness audit

Version-Timestamp: 2026-09-16 17:27:10 AST

Status: audit and proposed implementation order. Findings are not implemented by this report. The pinned plugin remains unchanged.

## Recommendation

Strengthen the existing workflows and prove their output before expanding the catalog. The kit already covers the major design disciplines. Its greatest opportunity is making good art direction, detailed craft, revision fidelity and honest acceptance happen reliably in actual projects.

The target is purposeful, brand-specific, carefully finished design. No detector or model setting can certify that work does not look AI-generated. Ultra was used as requested; this audit does not establish that it outperforms another effort level. The deliverable still needs strong inputs, suitable tools, actual rendering, comparison and human judgment.

## Scope and evidence

Audited repository: `newmindsgroup/visual-design-kit`, local baseline `39cc800`. Reviewed the wrapper, catalog, dependency graph, relevant craft skills, templates, starter packs, reference integration and validation code. This was a targeted audit, not a claim that all 130 capabilities were executed or every book was read.

Two independent audit workers were launched with `gpt-6-astra` and `ultra` reasoning at the user's explicit request. One assessed creative craft and one assessed package, routing and acceptance connections. The parent reconciled findings with files and reproduced the material validator defect. This does not mean the parent runtime was changed by prose.

Primary method: `project-skill-audit`, SHA-256 `cc8b7621d231732c389e93b3cf6868fc065dd9a2a449640d944c47ca14553eaf`; routing method: `model-governor`. The classifier recommended Astra Low; the explicit user instruction authorized Ultra for the two independent passes. Work used the existing Codex environment, local read-only inspection and public primary-source documentation. No books, client records or assets were uploaded to another service for this audit.

Fresh checks:

- All 322 payload entries match their manifest in both the repository and installed `visual-design-studio/0.1.0` cache. Both manifest digests are `dcca91274b676de49a0d4ee086aa7f4d6264c7ce8428cb259cdd0123c6683e4e`.
- Codex configuration marks `visual-design-studio@visual-design-team` enabled. This session's supplied skill catalog does not expose its starting entry. Installation does not establish automatic invocation.
- All 130 catalog entries exist. No missing dependencies or cycles were found. The plugin exposes one starting skill; the remaining entries are selected reference workflows.
- Six repository reference-utility tests, nine library Python tests and eleven JavaScript behavior tests passed, 26 in total. These test bounded behaviors, not visual excellence.
- An initial attempt to discover library tests from the repository root failed with `ModuleNotFoundError: No module named 'scripts'`. Running from the documented library directory passed. This is not presented as a product defect.
- Two additional negative probes found that a completed handoff can pass with contradictory passed/failed or passed/pending checks for the same criterion. Details follow.
- Visually inspected the existing fictional photographic correction and one historical touchscreen fallback screenshot. In the parent reviewer's judgment, the photograph has a more credible photographic treatment than a schematic fixture. This is one visual judgment, not human acceptance or multi-brand/motion proof. The fallback screenshot is a logic-test example, not an appropriate quality benchmark for client artwork.

The [evidence and review record](DESIGN-QUALITY-AUDIT-EVIDENCE-2026-09-16.md) identifies each finding's provenance, the two Ultra passes, the reproducible defect and the independent review dispositions.

## Fix the execution foundation first

### G01. A passed check can conceal an unresolved failed check

**Priority: before relying on automated completion. Confirmed defect.**

[The handoff validator](../plugins/visual-design-studio/library/design_system/validation.py) at lines 400 to 416 accepts any passed check for each criterion, while permitting another failed or pending check for that criterion. Both probes returned `valid: true`, no errors and no warnings for `completion: complete` and `readiness: ready`.

This is a record-consistency defect. It is separate from the validator's correctly stated inability to judge creative quality. [Delivery preflight](../plugins/visual-design-studio/library/DELIVERY-PREFLIGHT.md), line 14, already says failed required criteria prevent the affected delivery claim.

**Improve:** the existing handoff validator, templates and contract. Define one effective current result per criterion and candidate version. Keep superseded history explicitly separate. Do not invent human approval from a structural pass.

**Closure:** regression cases for passed plus failed and passed plus pending cover the reproduced defect. Candidate-version binding, stale evidence for a different candidate, and an explicitly superseded failure followed by a valid repair are proposed contract extensions, not additional reproduced defects. Unresolved current failures must prevent completion. Inspect other completion paths for the same conflict-handling problem before closing the fix.

**Interim mitigation for installed 0.1.0:** do not use a structural validator pass alone as completion evidence. Manually reconcile every current required criterion against the exact candidate. Any unresolved failed or pending required result keeps the affected work incomplete. Carry this warning into the next wrapper's readiness notes until the correction is verified.

### G02. Capability selection is specified but not validated

**Priority: before dependable project routing. Missing implementation.**

[Project launch](../plugins/visual-design-studio/PROJECT-LAUNCH.md), line 15, requires `SELECTED-CAPABILITIES.json`. [Usage](../plugins/visual-design-studio/library/USAGE.md), lines 62 to 76, defines IDs, entry hashes, exclusions, dependencies and repair provenance. The [CLI](../plugins/visual-design-studio/library/design_system/__main__.py), line 12, has no selection-record validator or matching template. The planner orders dependencies only.

**Improve:** add a small selection schema and deterministic validator to the existing CLI. Record prerequisite inputs as reused, required, provisionally authorized or not applicable. Preserve a lightweight instruction library; no new orchestration service is needed.

**Closure:** reject unknown IDs, hash mismatches and unresolved exclusion conflicts. A supplied approved logo must support a precise revision without restarting brand strategy. Test the existing rule in USAGE.md line 78 that `media-*` does not select provider IDs. This is a proposed regression test for that written rule, not an observed incorrect expansion.

### G03. Resume authority and copied template links can diverge

**Priority: before trustworthy interruption recovery. Instruction conflicts.**

[Project launch](../plugins/visual-design-studio/PROJECT-LAUNCH.md), line 16, and the [startup template](../project-starter/AGENTS.md.template) use `RESUME.md`. [Workflow continuity](../plugins/visual-design-studio/library/WORKFLOW.md), lines 24 to 28, requires `CURRENT.md`. Neither declares one to be a pointer to the other.

Copied [stage templates](../plugins/visual-design-studio/library/templates/stage-execution.md), lines 7, 22 and 31, also retain document-relative links such as `../HANDOFF-CONTRACT.md`. Those links no longer resolve correctly when the selected template moves into an independent project. An artifact-root declaration does not rewrite Markdown links.

**Improve:** establish one project state authority and explicitly map any older alias. Add a template adoption step that resolves instruction references against the pinned library while keeping project artifact references local.

**Closure:** create selected records in an independent project, verify all required instruction links, interrupt after a rejected revision, and recover the exact approved baseline and next action in a fresh session without prior chat context.

### G04. Installed readiness does not include the later repository correction

**Priority: before wider team distribution. Status integration gap.**

The [starting skill](../plugins/visual-design-studio/skills/design-project-start/SKILL.md), line 9, reads [current readiness](../plugins/visual-design-studio/READINESS.md), which still says installation and clean-project execution are pending. The newer repository README records bounded installation/startup proof outside the installed payload. Historical evidence should remain historical, but a fresh installed-only session needs one unambiguous current status.

**Improve:** release a corrected wrapper version with current scoped status, limitations and migration notes. Do not modify the installed cache or silently rewrite the pinned 0.1.0 payload.

**Closure:** a fresh installed-only session accurately distinguishes verified installation/startup, unresolved automatic discovery, and pending artwork/revision/host acceptance.

## Raise the creative standard

### G05. Add visual benchmarks that teach quality through examples

**Priority: first creative work batch. Written methods need stronger demonstrated evidence.**

The [website status](../plugins/visual-design-studio/library/WEBSITE-WORKFLOW.md), lines 84 to 86, labels acceptance scenarios as specifications. The [media exercises](../plugins/visual-design-studio/library/examples/media-quality-recipes/README.md) include technical and prepared examples. They are useful, but their existence does not establish distinctive output. The simple SVG campaign builder deliberately uses fixed layouts, system fonts and a schematic bottle. It is a test fixture, not a production art director.

**Improve existing owners:** `design-taste`, `design-media-quality-evaluation` and the example library. Separate engineering fixtures, rejected teaching examples and approved creative exemplars. Build a small original or authorized set with clearly different brand expressions. A good green-bottle photograph must not become the default aesthetic for every brand.

Use one shared example set, owned by media-quality evaluation, with other skills referencing its exact versions. The existing-brand fictional product case can reuse its authorized photographic master and declared identity. The contrasting new-brand website case needs its own original imagery through the available built-in image-generation route or authorized photography, with provenance and route availability recorded before execution. Do not spend on another provider without its scoped allowance. Product and environment imagery must retain the user's photographic requirement; logos, diagrams and editable type retain the existing exceptions. Never substitute the schematic bottle as a production photograph.

**Closure:** two contrasting fictional brand briefs produce actual compositions and one precise revision each. Compare each with a competent generic alternative using the same content. Retain initial output, critique, repair and reviewed result. Explain what makes the stronger version right for that brief.

### G06. Distinguish correctness from exceptional design

**Priority: alongside the benchmarks. Weak calibration.**

The [media rubric](../plugins/visual-design-studio/library/templates/media-quality-rubric.md), line 11, defines its highest score as meeting the brief with no observed defect. [Design craft](../plugins/visual-design-studio/library/DESIGN-CRAFT.md) already includes specificity and concept, but the [critique reference](../plugins/visual-design-studio/library/draft-skills/design-foundations/references/critique-calibration.md), line 15, points to worked artifacts outside the package.

**Improve existing owners:** taste, foundations and the rubric. Keep defect rejection separate from comparative creative judgment. Ask the reviewer to identify the strongest brief-specific idea, the intentional relationships between type, image, layout and copy, and what makes the work more effective than the generic alternative. Use annotated visual examples rather than another abstract quality score.

**Closure:** a comparative review distinguishes generic-but-correct, distinctive-and-effective, and attractive-but-factually-wrong candidates from the shared example set. The test author prepares the variants; the reviewing agent or human receives the brief and images without the generator/model labels or expected classifications until recording a judgment. This reduces one source of bias; it is not a blinded user study. The wrong product or claim must fail regardless of aesthetics. Observations must identify actual regions and choices. Human taste remains an explicit judgment, not a fabricated metric.

### G07. Make specialist craft selection explicit

**Priority: before normal website and campaign use. Routing reliability hypothesis, not absent skills.**

[The WEB starter route](../plugins/visual-design-studio/library/PROJECT-STARTER-PACKS.md), lines 100 to 105, mainly names generic UX, UI, prototype, production and delivery. [Website specialists](../plugins/visual-design-studio/library/WEBSITE-WORKFLOW.md), lines 38 to 50, separately cover art direction, full-page review and copy fit. UI already links craft review and website specialization. The proposed receiving-stage check should therefore be tested for usefulness, rather than justified by claiming those links are missing. No fresh agent omission was reproduced in this audit.

**Improve existing owners:** project start, starter packs and handoff. Add a compact decision at the receiving stage for art direction, composition, typography, real-copy fit, image treatment and motion. Record selected, reused or not applicable. Avoid automatically loading every capability.

**Closure:** an existing-brand landing page invokes or reuses appropriate art direction, copy fit, responsive composition and final critique. A heading-only change invokes relevant fit and preservation checks without reopening identity.

### G08. Execute the balanced-typography requirements

**Priority: before client-facing output. Strong rules, incomplete portable execution evidence.**

[Typography](../plugins/visual-design-studio/library/draft-skills/design-typography/SKILL.md), lines 53 to 59, already requires balanced endings across media, readable sizing and accessible reflow. [The craft lab](../plugins/visual-design-studio/library/CRAFT-LAB.md), lines 11 to 13 and 31 to 33, describes limited whitespace-based diagnostics and still marks actual responsive captures and diagnostic execution pending.

**Improve existing owners:** typography, web-copy-fit and craft lab. Test real font files, actual copy, narrow and intermediate widths, fallback loading, text enlargement and the final PDF/native export where selected. Use diagnostics to find candidates, then inspect visually. Do not shrink everything or force no-wrap to obtain a clean report.

**Closure:** detect a deliberate orphan and clipping example, avoid rejecting a legitimate short label, and repair the real composition without changing approved meaning or hiding text. Include authored-layout balance and user-adjusted readability as separate checks.

Current technical support: [MDN text-wrap-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style) documents browser and line-count limits; [W3C text-spacing guidance](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) requires supported spacing overrides to preserve content and function. These do not guarantee balanced typography and do not impose the override values as the authored design.

### G09. Connect reference knowledge to an actual design decision

**Priority: before claiming routine book-assisted startup. Integration and example gap.**

The [reference retrieval guide](../plugins/visual-design-studio/library/draft-skills/design-reference-direction/references/reference-retrieval.md), lines 9 and 17, describes an offline helper and `reference-techniques.json` absent from the inspected plugin inventory. Separately, the working [book workflow](../resources/REFERENCE-WORKFLOW.md) and [utility](../tools/reference_library.py) live outside the installed payload and need an explicit user instruction to adopt them. Ordinary installed startup does not discover those additions automatically.

**Improve existing owners:** reference-direction and project setup. Either package the permitted helper and annotations or clearly describe their absence with a supported manual route. Configure an optional local book-library root and a trusted retrieval-tool location. Books remain outside GitHub and the plugin. An absent optional library should not stop ordinary design work or lead to fabricated book claims.

**Closure:** a fresh project retrieves one relevant source, verifies its locator, inspects the original page when the lesson is visual, and records the resulting design change and its limits. Include an example where the advice should not be applied. No full-book synthesis claim follows from a search result.

### G10. Test revisions against attractive but incorrect work

**Priority: before expanding to many client assets. Procedure exists; end-to-end proof is incomplete.**

[Creative continuity](../plugins/visual-design-studio/library/CREATIVE-CONTINUITY.md) already covers feedback, invariants and stale assets. Its [exercise](../plugins/visual-design-studio/library/templates/creative-continuity-exercise.md), lines 15 to 25, already proposes revision, resume and deliberate-fault cases. Execute those cases rather than adding another consistency skill.

**Improve existing owners:** handoff, screen revisions and delivery. Compare rendered before/after work and file identity; declared JSON invariants cannot prove image geometry or label fidelity.

**Closure:** change one headline, preserve unrelated copy, logo and product details, and catch an attractive wrong-label image, a superseded asset and an unauthorized palette. Resume with the correct baseline. Bind every result to the actual candidate version.

### G11. Prove motion art direction, beyond moving an image

**Priority: before calling motion production-ready. Creative execution gap.**

[Motion effects](../plugins/visual-design-studio/library/draft-skills/design-motion-effects/SKILL.md) already covers purpose, choreography, style frames, animatics, holds and fallback. [Still-to-motion](../plugins/visual-design-studio/library/draft-skills/design-screen-still-motion/SKILL.md) covers layer preservation. The portable examples still distinguish prepared motion exercises from bounded playback logic.

**Improve existing owners:** those two skills and media evaluation. Produce one deliberately directed sequence from an accepted photographic still through storyboard/style frames, an animatic, editable motion and the final loop. Each movement should have a message or material/brand purpose. Generic zoom, parallax or transitions should not be assumed sufficient.

**Closure:** inspect the complete loop, text-reading time, transition points, seam, geometry, textures and label stability, plus static and reduced-motion alternatives where applicable. Real display/player acceptance remains a separate test. Preserve the user's photographic requirement for product/environment imagery and the existing vector/logo/diagram exceptions.

## Implementation order

| Batch | Work | Exit evidence |
| --- | --- | --- |
| 1. Reliable execution | G01 to G04: checks, selection, resume authority, portable templates and current wrapper status | Meaningful negative tests plus fresh-project startup and interrupted-session recovery |
| 2. Better decisions and craft | G06 rubric preparation; G07 to G09 selection checks, typography proof and reference integration | Draft comparison criteria, verified line-wrap cases and one reference-informed design decision |
| 3. Demonstrated output | G05 shared example set; G06 comparative review; G10 revisions; G11 one directed motion sequence derived from the selected example | One versioned collection of actual sources/exports, annotated comparisons, reviewed playback and retained first-attempt evidence |
| 4. Reviewed distribution | New package version, source-to-release mapping, host tests and upgrade/rollback documentation | Exact reviewed bytes, versioned archive/digest and separate Codex, Cursor and Claude Code acceptance results |

The two fictional briefs can be prepared without client assets. Human review is still needed to judge the resulting visual standard before presenting it as accepted quality. Existing-brand and new-brand client projects remain separate. PowerPoint and backup setup remain deferred. Provider generation still follows its recorded entitlement and budget.

## What this changes about the plan

No additional standalone skill is justified by this audit. The identified work belongs to existing owners. Keep one plugin with scoped project recipes and selectable capabilities. Avoid splitting plugins or adding a broad new framework until a real distribution or maintenance requirement justifies it.

The process should visibly carry a specific brief into an explicit concept, a carefully chosen visual language, real copy and imagery, an actual composition, comparative critique, a precise revision and a verified export. That progression has more value than adding more style names or asking a generator to make something premium.

## Limits and review status

This report does not complete the earlier reference-library release review, certify all providers, inspect all motion frames or verify target hardware. No production assets, source books or pinned plugin files were modified. The installed plugin retains its existing limitations until a reviewed new version is adopted.

Separate Claude milestone review returned successfully using `claude-fable-5-1`. Its scope was the audit text, without repository or image access. The parent resolved material findings about provenance, sequence, shared example ownership, photographic sourcing and the interim warning above. Details and considered disagreements are in the evidence record. This is a new audit review, not completion of the earlier reference-library review or approval of a plugin release.

Agent-Attribution: computer=Mac.lan; tool=Codex; version=codex-cli 0.154.0; timestamp=2026-09-16 17:27:10 AST
