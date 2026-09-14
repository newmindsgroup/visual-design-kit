# Selecting references and visual direction

Version-Timestamp: 2026-09-10 20:14:15 AST

Original method for a bounded reference decision. Use with [research](draft-skills/design-evidence-research/SKILL.md) and [reference direction](draft-skills/design-reference-direction/SKILL.md). This is not a style catalog or a list of mandatory aesthetic defaults.

## Start from the decision

Name the task, audience, medium, content density, device/input conditions and success measure. Establish approved identity, existing system, exact requested change and protected baseline. Altering opacity, luminance or a derived color is still a visual change; do not describe it as preserving an exact approved token. If the request conflicts with an invariant, propose a separate variant or keep that change pending. For an exploratory brief without a kit, distinguish observed cues from proposed rules. Ask only for information that would change the recommendation.

Search the existing project and installed references first. Use a gallery to discover examples, a platform's official documentation to establish behavior, and the original site's current rendered interface to check a derived description. Keep the initial comparison small, often two or three meaningfully different directions. Stop when evidence distinguishes a viable direction or names a finite missing prerequisite. More thumbnails are not automatically more research.

For each source record URL/path, publisher, date/version or commit, video timecode/section if applicable, inspected content/state, access gaps, and rights/cost status. Classify it as official specification, provider documentation, observed product, third-party interpretation, or creator opinion. Do not promote a generated DESIGN.md to official brand authority.

## Describe the visual grammar

Use concrete axes rather than relying on a label such as premium or minimalist:

| Axis | Compare | Acceptance question |
| --- | --- | --- |
| Hierarchy and density | Sparse narrative, balanced task UI, dense operational view | Can the intended user find the next action and important exception? |
| Typography | Proportions, scale, weight, line length, numeral/label treatment | Does real long or translated content remain readable in the target medium? |
| Color and surface | Semantic roles, accent share, light/dark, borders, elevation | Are meaning and interaction clear without depending on color alone? |
| Layout and shape | Rhythm, alignment, grid, radii, grouping | Does structure explain content rather than decorate it? |
| Imagery | Documentary, illustration, diagram, texture, cinematic media | Is it truthful, licensed and useful to this task? |
| Motion | Feedback, orientation, narrative, decoration | What does movement communicate, and what works when it is absent? |

Evaluate fit, brand continuity, comprehension, accessibility, implementation/maintenance effort and rights/cost. Use evidence-backed qualitative judgments unless weights and measures are genuinely defined. Do not manufacture a precise score from impressions.

Record each borrowed principle as observation, proposed adaptation, task rationale and rejection boundary. Preserve recognizable relationships while creating original expression. Do not transplant another brand's marks, character designs, copy, proprietary fonts or entire visual identity. Site access and an open-source wrapper do not confer rights to the referenced assets.

## Choose motion by purpose and representation

| Need | Candidate representation | Evidence before acceptance |
| --- | --- | --- |
| Confirm an action or show progress | Native component feedback, short transition | Keyboard/touch equivalence, interruption, completion and error behavior |
| Explain spatial or sequential change | Transition or diagram animation | Users retain orientation; no required information disappears |
| Tell a visual story | Video, image sequence, scroll narrative | Playback controls/fallback, loading budget, crops, reduced motion and content access |
| Let users inspect geometry | Actual interactive model or scene | Geometry truth, navigation, fallback, device performance and accessible alternatives |
| Add atmosphere only | Optional static artwork or restrained effect | Does not obstruct content; removal preserves the complete task |

Video of a moving camera is not an interactive 3D model. AI-created imagery is not factual evidence of a physical product or property. Prefer truthful supplied assets where representation matters. Record resolution, duration, aspect ratio, loop boundaries, poster/fallback and generation provenance when media is selected. A proposed video needs an available authorized production path; native playback does not make asset generation or hosting free. When only stills and existing local tools are available, begin with a static or simple still-image treatment within that capacity.

State a performance budget appropriate to the project and measure on representative hardware. Choose the simplest technique that meets the behavior. CSS/native transitions may suffice; an animation library is justified by sequencing or lifecycle needs. Prefer transforms/opacity where appropriate, clean up offscreen work, and verify rather than promise frame rate. Do not require preloaders, custom cursors, parallax or scroll pinning just to signal visual quality.

Treat reduced-motion support as a design requirement when appropriate to the product; distinguish it from a claim of full WCAG conformance. The specific interaction-animation criterion is Level AAA. Automatically moving content has a separate Level A pause/stop/hide criterion with defined conditions. Verify the current official criterion and its applicability when implementing. Test the actual experience and all applicable requirements.

## Close the selection

Recommend one direction with a bounded alternative and explicit rejected choices. Identify which criteria are observed, inferred or still untested. Pass original rules and permitted references to identity/UI, with token roles, image/font rights and the proposed motion contract. Keep raw source excerpts and private research in their approved archive. Implementation approval, legal clearance, user validation and deployment remain separate decisions.

Use the [structured companion](REFERENCE-CONTRACT.md) to catch recorded baseline changes, unsupported operation-cost claims and missing verification. It cannot judge the originality or relevance of a direction. Use current authoritative identity and physical-display references for those specific gaps without replacing this process.

## Measured website comparisons

For a task that needs a comparison of two live interfaces, record each URL, capture date, viewport, theme, relevant interaction state and measurement scope. Compare matching states and comparable content density. Confirm that the expected content and fonts have loaded; deliberately inspect relevant lazy-loaded regions through normal browser actions. An empty or unexpectedly sparse measurement is an unresolved capture problem until checked, not evidence that the site has no typography or borders.

For each material difference, keep the subject observation, reference observation, locator or capture, proposed change and task-specific rationale together. Separate routine implementation from decisions requiring a new identity or content choice. Rank changes by the actual task's expected benefit and estimated effort, labeling estimates as estimates. A numerical difference alone does not establish which design is better.

Computed CSS is a measurement of a particular rendered state, not automatic recovery of a canonical token system. Distinguish authored UI from embeds, cookie banners and other incidental content. Check representative values against their rendered elements, especially fonts, composite colors and multi-sided borders. A failed check narrows or invalidates affected findings; do not silently repair a table with guessed values. Frequency counts can help discover candidates, but nested elements and inherited styles can inflate them. Declare pseudo-elements, shadow roots, embedded frames, canvas and other unmeasured regions as coverage limits when the selected method does not inspect them.

Use the existing reference decision and approved identity for the adaptation. A subject does not inherit the reference's colors, asset rights or dark theme because they were measured. Select an interactive comparison only when manipulating a variable would clarify a real decision; otherwise a compact evidence-linked table is sufficient. The original derivation is recorded in the source version pinned in the package manifest. No downloaded tool or installed state is included by this method.


## Specialized selection

The [design craft framework](DESIGN-CRAFT.md) connects foundations, typography, color and motion. Use its relevant skill for a project-specific choice, then record the direction here through the existing decision contract. Avoid duplicate research and preserve an already approved visual baseline.
