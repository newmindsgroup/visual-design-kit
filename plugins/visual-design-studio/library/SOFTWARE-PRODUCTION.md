# Choose and verify the production tool

Version-Timestamp: 2026-09-10 19:58:10 AST

Use this with the existing production skill, [medium contracts](TOOLCHAINS.md) and work record. Choose by required result, editable handoff and recipient workflow. Software names are candidates, not a quality ranking: a mature native app is preferred when it satisfies requirements better, while code or current chat tools are suitable when they meet the same acceptance needs. Do not build a replacement editor just because an existing app lacks an immediately available connector.

## Selection and execution

1. Record required native master, final formats, editability, dimensions/units, content/brand inputs, target medium, intended reviewer and downstream use. Include color/profile/bleed, font/link handling, motion/audio or interaction requirements only when relevant. Unknowns hold the dependent output claim.
2. Compare the existing workspace and suitable installed/service tools for fidelity, editability, repeatability, revision control, integration coverage, privacy, entitlement/cost and recipient compatibility. Record the chosen route and reason in the existing work record. A hybrid route may generate initial content in code, refine it in an app and return verified exports; designate one canonical editable source and document conversion losses.
3. Discover actual tools and read the relevant installed skill. Prefer a supported purpose-built connector or documented local scripting/API path that preserves the required semantics. Browser/native UI automation is a valid route when needed and observable. MCP is not inherently better than scripting; an API is not automatically included in a desktop subscription. Confirm action-specific access and no additional charge before using it. Respect an explicit current authorization rather than asking again.
4. Use an isolated candidate or copy, preserve baseline and recoverability, and operate within the specified workspace/design. Check current app/document state before resuming; do not blindly replay a mutation. Client or confidential content may leave the host only under recorded authorization for that destination, content scope and applicable data-handling requirements. Use original synthetic fixtures for initial access tests. Do not install unvetted bridges, change global app settings or spend credits merely to unblock a route.
5. Inspect the actual editable structure and rendered result, then save/export using the selected specification. Reopen the source in its intended app and exports in the intended viewer. Record tool/version, actual paths or stable cloud IDs/version, content/format checks, losses and remaining gaps. A screenshot, PDF or flattened import is not a layered/native master. A file hash proves byte identity, not native editability or visual quality.
6. Use the existing stage handoff and manifest. Cloud-native work needs the real design ID, version and approved access boundary plus local exported bytes where required; a URL alone does not satisfy local file-manifest checks. No sharing/permissions/publication follows from preparing a handoff. Mark unavailable operations as blocked or limited output, never silently substitute a weaker deliverable.

Before execution, copy [destination readiness](SOFTWARE-READINESS.md) into the project workspace and fill it from current evidence. Authored methods support planning; actual tool control and output acceptance require destination checks. Load only the applicable mode: [Illustrator](draft-skills/design-production-interface/references/illustrator.md), [Photoshop](draft-skills/design-production-interface/references/photoshop.md), [Figma](draft-skills/design-production-interface/references/figma.md), [Canva](draft-skills/design-production-interface/references/canva.md). These instructions do not install executors or inherit tested status.

## Figma versus Adobe: choose by the editable result

These are task-selection recommendations informed by the official sources below, not a claim that every route has been tested. When desktop Figma is required by the brief, browser evidence alone does not meet that requirement. Using a desktop app does not make its account files local-only or establish offline storage, account permissions or an included MCP entitlement.

| Required result | Candidate starting tool (verify readiness first) | Why and what remains authoritative |
| --- | --- | --- |
| Website/app screens, reusable UI components, variants, auto layout, interactive prototype and collaborative design handoff | Figma Design, when desktop access and required features are verified | Native UI relationships matter. Preserve components, instances, layout rules and prototype connections. A screenshot or SVG export cannot replace this source |
| Logo, custom icon family, vector illustration or scalable identity artwork | Illustrator | Precise vector artwork and an editable AI master. Import approved SVG copies into Figma when needed for UI; Illustrator remains the artwork source |
| Photo retouching, product compositing, cutouts, masks and layered raster artwork | Photoshop | Keep layered PSD source and nondestructive structure. Export reviewed image copies for UI or campaign layouts; Figma does not replace the PSD master |
| Screen UI using a custom logo and edited product photography | Illustrator plus Photoshop plus Figma | Illustrator owns logo artwork, Photoshop owns photo masters, Figma owns UI composition/components. One authoritative master per asset or system, with named versions linking them |
| Simple UI icon or geometric shape that only belongs to one interface | Figma can suffice | Do not add a vector-app round trip without an artwork or delivery requirement. Choose Illustrator when illustration complexity or an AI handoff justifies it |
| Retail touchscreen experience | Figma for flows, screen system and prototype; Adobe for required assets; code/runtime for implementation | Prototype transitions are design evidence only. Verify actual touch targets, reach, idle/reset/privacy states, offline behavior and accessibility on intended hardware separately |
| Static retail display campaign | Illustrator for vector-led composition or Photoshop for photo-led composition, according to editable delivery requirements | Figma may supply shared screen templates if the team requires them. Verify exact canvas, profile, export, readability and actual player behavior; no universal preferred app |
| Working website or app | Code and target runtime, with Figma when design-system or review needs justify it | Figma is optional for a small direct-to-code change. Tested implementation remains authoritative for runtime behavior; map approved tokens and document differences |

Selection order: required handoff and native editability, output fidelity, reusable structure, recipient workflow, verified access/data boundary, then iteration cost. Familiarity or connector convenience alone must not decide the tool. If the preferred route is unavailable, record the hold or agree on a weaker deliverable explicitly. Do not quietly replace native UI components with flattened artwork.

Before moving assets between apps, record source file/version, export path/settings, intended use, font and link dependencies, and allowed conversions. Verify imported dimensions, color, text, vector geometry, transparency and component/variable relationships relevant to that asset. Import/export is not assumed lossless. For web/app work, verify contrast, focus order, keyboard and screen-reader behavior, text scaling and applicable localization/RTL in the actual implementation; Figma prototype inspection does not prove these behaviors. Changes return to the owning master, followed by refreshed exports and downstream checks.

Official basis, checked 2026-09-08: [Figma native design files, components and prototypes](https://help.figma.com/hc/en-us/articles/15297425105303-Explore-design-files), [auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties), [desktop app](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app), [offline limitations](https://help.figma.com/hc/en-us/articles/360040328553-What-can-I-do-offline-in-Figma), and [Adobe's product comparison, a vendor explanation rather than a benchmark, Illustrator versus Photoshop](https://www.adobe.com/creativecloud/design/illustrator-vs-photoshop.html). Broader motion and publishing routes below remain candidates with their own verification requirements.

## Other deliverable routes

| Need | Candidate tools and required verification |
| --- | --- |
| Multi-page brand guide, report or print layout | InDesign if available; suitable existing layout/deck tool otherwise. Verify master structure, page styles, links/fonts, overset text, page boxes, color and target PDF requirements |
| Presentation or editable sales deck | Canva, Keynote or PowerPoint based on recipient workflow. Verify slides, notes, fonts, media, editable elements and target presentation/export behavior |
| Motion, compositing or video | After Effects, Premiere, available Adobe operations or another suitable installed editor. Verify editable timeline, source assets, frame rate, duration, audio, codec and real playback/loop behavior |
| Website/application | Existing code tools or Open Design where appropriate; native design apps for accepted assets/UI systems. A design export is not a tested application; run actual target build/browser/device checks |
| Digital OOH/shared touch | Use appropriate design/media tools for assets plus actual player/device contracts for delivery. Neither Adobe export nor browser preview proves field readability, reach, session privacy or playback reliability |

A future app-specific skill is justified when verified operations and repeated deliverables warrant an independently reusable mode. Until then, these references extend the existing production capability without creating speculative plugins or duplicate libraries.

## Optional presentation software

PowerPoint is deferred unless the user or recipient explicitly requires it. Do not spend setup or validation time on it by default. Any selected presentation tool needs its own native editability, notes/media, playback and export checks. No prior fixture result is inherited.

## Infographics and generated media

Use [infographics](draft-skills/design-infographics/SKILL.md) for evidence, layout/style selection and editable visual explanations. Use [media routing](MEDIA-GENERATION.md) to select Higgsfield or OpenArt as a conditional asset-production step. Shared masters, export checks and delivery remain under this production contract.


Version-Timestamp: 2026-09-11T23:21:42-04:00

## Website owner editing

When owner maintenance is part of a website handoff, identify the permitted text, image, link and page-metadata fields and their authoritative source. Use the site's existing CMS, editor or structured content where it fits; a custom CMS is optional. Preserve the original asset while reviewing replacements, preview long copy and changed imagery at relevant widths, then save and reopen to verify persistence and affected outputs. Check replacement-image alternative text, edited heading structure and link purpose, and relevant contrast. Check field validation and edit/publish access if an editor is included. Retain a recoverable prior version and explain the owner's supported edits. A browser preview alone does not establish permissions, persistence or a working publish path.md).

Use this with the existing production skill, [medium contracts](TOOLCHAINS.md) and work record. Choose by required result, editable handoff and recipient workflow. Software names are candidates, not a quality ranking: a mature native app is preferred when it satisfies requirements better, while code or current chat tools are suitable when they meet the same acceptance needs. Do not build a replacement editor just because an existing app lacks an immediately available connector.
