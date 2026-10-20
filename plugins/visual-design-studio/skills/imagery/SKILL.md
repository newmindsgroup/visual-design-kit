---
name: imagery
description: >-
  Directs and produces brand imagery: icon systems on a 24px grid, illustration style systems, photography art direction
  and shot lists, AI image generation prompting with consistency, rights and C2PA provenance, and 3D for stills and the
  web (glTF, compression budgets). Use when choosing or drawing icons, defining an illustration style, briefing a
  photoshoot or choosing stock, writing image-generation prompts, cleaning up or upscaling generated images, or adding
  3D renders or interactive 3D.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:07:10 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Imagery

Excellent imagery looks like it could only belong to this brand: one icon family drawn to one grid, one illustration language, photography with a describable light and grade, and generated or 3D images that are honest about what they are. The test is a contact sheet: every image side by side should read as one voice.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Medium | Real photography for real products, people and places; illustration for concepts, sensitive topics and things that do not exist yet; 3D for products in development, mechanisms and configurators; AI generation for concepts, backgrounds and stylized art | Brief explicitly approves another medium for a role, with disclosure where needed |
| Icon grid | 24x24 canvas, 2px padding (20x20 live area), keylines: circle 20, square 18, portrait 16x20, landscape 20x16 | Dense desktop tools: 20px grid with 1.5px padding |
| Icon stroke | 2px at 24px (1.5px for a lighter UI), round caps and joins for friendly, square caps and miter joins for technical | Never mix stroke weights or cap styles in one set |
| Icon sizes | 16, 20, 24, 32px with optical adjustments, not plain scaling | Marketing and feature icons: 48-96px, can be duotone |
| Icon set | One open-source family per product (Lucide, Phosphor, Heroicons, Tabler, Material Symbols) or one custom family | Apple-only apps may use SF Symbols within Apple's license |
| Illustration palette | 4-6 colors from the brand plus 2 neutrals, a separate skin-tone set of 8-10 tones | Kids and value tier: more saturation; luxury: 2-3 colors and texture |
| Photography light | Named direction, quality and color temperature in the brief (for example "soft window key from camera left, 5000-5600K, 2:1 ratio") | Never "nice lighting" |
| Lens language | 35mm equivalent for context, 50mm natural, 85-135mm portraits, 100mm macro for detail | Architecture: 24mm tilt-shift or corrected verticals |
| Export | Web: AVIF or WebP plus JPEG fallback at 1x and 2x of display size, sRGB; print: 300ppi at final size, converted to CMYK last | Hero images on slow networks: about 150-250KB at 1x |
| AI imagery | Allowed for concept, mood, backgrounds, abstract and stylized art, storyboards and labeled composites; never fake product photos, fake customers, fake testimonials or fake events | Client policy is stricter: follow it |
| Provenance | Keep a record (tool, model and version, date, prompt, references and rights, edits, approver); preserve C2PA Content Credentials through export | Platform or regulation requires a visible label: add it |
| Accessibility | Meaningful images get alt text describing purpose; decorative images get `alt=""`; meaningful icons 3:1 against their background; no flashing above 3 per second; no text baked into images except logos | Never relax |

## Workflow

1. **Decide each image's job** (explain, prove, attract, orient) and choose the medium per job using the defaults.
2. **Atlas and references.** Query the atlas for style, industry, market and audience; collect 12-20 references per medium and annotate what to take from each (light, crop, palette, line), never "make it like this".
3. **Define the system** before producing volume: icon rules ([iconography](references/iconography.md)), illustration style sheet ([illustration](references/illustration.md)), photography brief and shot list ([photography](references/photography.md)), prompt style block ([AI image generation](references/ai-image-generation.md)) or lookdev turntable ([3D](references/3d.md)).
4. **Pilot** 3-6 images that cover the hardest cases (a person, an object, an abstract concept, a small icon set).
5. **Render in context and inspect.** Place pilots in real layouts at real sizes: icons at 16-24px on light and dark, photos in the hero crop and the mobile crop, illustrations next to UI. Make a contact sheet. Fix and repeat.
6. **Produce volume** from the locked system; review every batch as a contact sheet.
7. **Record rights and provenance** (licenses, releases, AI records) and write alt text before handoff.

## Decisions that change the answer

- **Style and archetype.** Swiss and Sage briefs want objective, cropped photography and monoline icons; Jester and Creator want illustration with character and irregular shapes; Lover wants close crops, warm light and texture. Read the style entry's "Imagery and iconography" section.
- **Tier.** Value: product-forward, bright, high-key, many images. Premium and luxury: fewer, larger images, still life and material detail, slower edits, more negative space.
- **Industry.** Healthcare and finance: real people with consent, no fear imagery, no coins or shields. Food: appetite appeal, steam and texture are real. B2B: real product UI over abstract 3D blobs.
- **Market and audience.** Cast and locate locally; check gestures and symbols per market; children's products favor illustration; older adults need high-contrast, uncluttered images.
- **Channel.** Social needs vertical 9:16 and 4:5 crops planned at the shoot; print needs 300ppi CMYK; web needs responsive crops and performance budgets; signage needs bold silhouettes.

## Common failures

- Mixed icon families, stroke weights or fill styles in one interface → one family, one stroke, filled only for selected state.
- Emoji used as icons → a drawn icon with an accessible label.
- Stock clichés (handshake, team high-five, person pointing at a glowing screen, robot hand touching a human hand) → specific, unposed situations from the brand's real world.
- Corporate Memphis by default (flat figures with tiny heads, oversized limbs, purple skin) → a style derived from the brand's shape language and an inclusive skin-tone set.
- AI tells (waxy skin, extra fingers, garbled text, identical faces, teal-orange grade, everything glowing) → ordinary light, real materials, imperfection, manual cleanup.
- Text baked into generated images → generate clean copy space and set live type in layout.
- 3D model that downloads 20MB before anything appears → poster image first, compressed GLB under budget, lazy load.

## References

- [Iconography](references/iconography.md): grid and keylines, stroke and corners, optical sizes, filled vs outline, metaphors, SVG hygiene, open-source sets and licenses.
- [Illustration](references/illustration.md): style system, characters, inclusive representation, spot/hero/scene types, commissioning brief.
- [Photography](references/photography.md): art direction brief, shot lists, stock selection, retouching, releases.
- [AI image generation](references/ai-image-generation.md): prompt anatomy, consistency, text limits, appropriate use, provenance, rights, cleanup and upscaling.
- [3D](references/3d.md): when 3D helps, tools, materials and lighting, web 3D budgets, accessibility.
- Atlas, when style, industry, market or audience matters:
  - `python3 ../../library/scripts/atlas.py query "editorial food photography warm"`
  - `python3 ../../library/scripts/atlas.py show style.illustrative-narrative`
  - `python3 ../../library/scripts/atlas.py show audience.children-under-13`
- Deep process for client media production: [media art direction](../../library/draft-skills/design-media-art-direction/SKILL.md), [route selection](../../library/draft-skills/design-media-route-selection/SKILL.md), [reference control](../../library/draft-skills/design-media-reference-control/SKILL.md), [image repair](../../library/draft-skills/design-media-image-repair/SKILL.md), [quality evaluation](../../library/draft-skills/design-media-quality-evaluation/SKILL.md), [production recipes](../../library/draft-skills/design-media-production-recipes/SKILL.md), [ChatGPT Images](../../library/draft-skills/design-chatgpt-images/SKILL.md), [OpenArt CLI](../../library/draft-skills/design-openart-cli/SKILL.md), [Higgsfield CLI](../../library/draft-skills/design-higgsfield-cli/SKILL.md), [original supporting assets](../../library/draft-skills/design-screen-original-assets/SKILL.md), [dimensional product visualization](../../library/draft-skills/design-screen-dimensional/SKILL.md) and the [media generation contract](../../library/MEDIA-GENERATION.md).

Catalog IDs covered: media-art-direction, media-route-selection, media-reference-control, media-image-repair, media-quality-evaluation, media-production-recipes, chatgpt-images, openart-cli, higgsfield-cli, screen-original-assets, screen-dimensional
