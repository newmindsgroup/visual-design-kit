# Persona workbench presentation contract

Version-Timestamp: 2026-10-22 08:25:00 AST

The owner's supplied reference defines the minimum content depth and interaction scope for this capability. Preserve the 118 canonical fields and all35 representation IDs. Source-specific brand colors, client persona wording, portraits and research claims are not reusable kit content. Generic renderer code and the original fictional fixture are reusable.

## Required presentation

- Detail header: actual approved portrait or explicit initials fallback, profile name/role, organization context, priority, research/approval status and a real permitted quote when available. Never invent a quote or portrait to fill the layout.
- All six detail tabs: Overview, Psychographics, Buying Journey, Content Preferences, Objections and Scenarios.
- Overview: job, goals, frustrations, behaviors, detailed pain/urgency/impact/current workaround/desired outcome. Preserve full list lengths.
- Psychographics: values, personality, lifestyle, attitudes, motivations, fears, complete day-in-life and emotional-journey stages. Unknown traits remain explicit, not guessed from sector.
- Buying Journey: awareness, consideration and decision with all triggers/questions/criteria/comparisons/objections/barriers/stakeholders/timing/content needs, influences and decision criteria.
- Content: formats, channels, tone, topics/avoid topics, reading level/length/frequency, persuasion/proof/key phrases/language/formality/avoid phrases and all four content stages.
- Objections: full objection/category/response/proof objects and alternatives/current solutions/switching barriers/competitor perceptions. Never truncate response text in comparison or export.
- Scenarios: name, description, trigger, outcome; win definition, personal/professional success and KPIs.
- Sidebar/context: all demographics and technology fields, content summary and other profiles. Long unverified context can be disclosed progressively but must remain accessible and included in the complete export.
- Comparison: choose two or three profiles, clear insufficient-selection and maximum states; all118 fields remain available side by side. Print uses the current selection; no silently shortened lists.
- Mapping: actual pages and paths; primary/secondary/tertiary assignments, raw weights, explicitly normalized display, journey stage, rationale, section strategies and coverage gaps. Weights are project planning decisions, not a measured audience share or universal60/30/10 rule. Reject unknown profile IDs and inconsistent joins.
- Localization: translated controls and labels, stable field/item IDs, supplied translated values and explicit source-language fallback. Partial translations must never display undefined or silently masquerade as reviewed translation.
- Delivery: editable JSON, self-contained private HTML, local print/PDF path and original source references. Printing Detail must include all six tabs and disclosed context; Comparison must not clip later columns. Viewport checks and actual PDF extraction are separate evidence.

## Improvements implemented in the original renderer

Visible evidence/status disclosure, keyboard-operated tabs, profile selector, valid2-to3 comparison guards, complete comparison text, honest translation fallback, explicit unknowns, object/list linkage, mapping validation and positive-sum normalization, isolated scrollable comparison tables on mobile, responsive hierarchy, approved local raster portraits only, no remote runtime dependencies and export encoding that prevents supplied content becoming executable markup.

These improve the owner reference without adopting its observed defects: missing enum translations, empty fields without explanation, mixed locale state, clipped/truncated comparison responses and misleading universal weight ranges. A zero-coverage persona is surfaced for review, not automatically reassigned.

## Build and use

From a verified library checkout:

```sh
python3 scripts/persona_workbench.py --demo --output /absolute/project/review/personas-v1.html
python3 scripts/persona_workbench.py --input /absolute/project/personas.json --project-root /absolute/project --output /absolute/project/review/personas-v2.html
```

Canonical input is a collection with records (each complete persona-record.json shape). Optional theme accepts accent, ink, ground, surface and border as six-digit hex values; supplied approved brand values win. It does not alter schema or grant visual approval. Review contrast after changing a theme. Default Inter uses an installed font with a system fallback; exact font packaging is a receiving-project task.

For authorized legacy nested data, preserve source files privately and use:

```sh
python3 scripts/persona_workbench.py --legacy-input /absolute/project/legacy-personas.json --source-locale es --targeting /absolute/project/legacy-targeting.json --portrait-root /absolute/project/approved-assets --output /absolute/project/review/personas-v3.html
```

The importer maps dictionary-shaped competitor perceptions into linked canonical items and preserves partial translations. It labels source content proposed and imported/unverified; it never asserts research validation. Declare --source-locale es or en for legacy imports; the importer does not guess the source language. A native canonical collection declares source_locale. Only a deliberately provided local portrait root is read; PNG/JPEG/WebP are embedded after path/magic/size checks. No URL fetch, HTML portrait or SVG execution. Output refuses overwrite; choose a new version path. There is no automatic upload, deployment, client send or browser installation.

## Acceptance and limits

Use the canonical persona validator for research-record structure and the workbench builder's additional renderer checks. The latter checks exact field/component sets, input shape, joins, weights and safe embedding. Neither validates facts, human preference, client rights or claimed outcomes. Do not report the fictional demo as a completed research persona.

Inspect desktop and narrow mobile, six tabs with keyboard/focus, both locales,2/3 comparison and insufficient/maximum states, mapping with/without weights, unknown/empty/error states, approved portrait/fallback, text enlargement, print all tabs and PDF text. Test altered values and a new project to prove future regeneration rather than a hand-built screenshot.

## Requested illustrative portraits and manual receiving

Version-Timestamp: 2026-10-22 13:32:00 AST

When the owner requests portraits for hypothetical personas, use original clearly labeled fictional composites, or permitted supplied images. Never represent them as participants, clients, testimonials or typical audience demographics. Preserve research unknowns. A receiving project's build may apply a documented presentation-only image overlay and portrait manifest; retain original record facts unchanged. Include portrait provenance, prompt, generator mode, source bytes/hash and disclosure. Verify every stable persona ID selects the correct image, circular cropping, all four profiles, mobile, full tabs and print. If a complete HTML/CSS brand manual is requested, integrate an actual rendered persona chapter and reciprocal navigation in the complete manual, not only a Markdown pointer. Preserve frozen prior editions and regenerate from canonical structured sources.
