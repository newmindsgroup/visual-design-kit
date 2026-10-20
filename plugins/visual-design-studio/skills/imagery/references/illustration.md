# Illustration systems

Version-Timestamp: 2026-10-20 02:07:10 UTC

An illustration style is a set of rules, not a set of pictures. Define shape, line, color, texture, perspective and character construction precisely enough that two different illustrators produce work that looks like one hand, then build the library from spot to hero to scene.

## When illustration beats photography

- Abstract ideas (security, growth, data flow, "how it works").
- Products or places that do not exist yet.
- Sensitive subjects where photographs of real people would intrude or stigmatize (illness, debt, grief, abuse).
- Children's products and education.
- Inclusive representation across many audiences without casting dozens of shoots.
- Brand ownership: a distinctive style is harder to copy than stock photography.

Use photography instead when proof matters (real product, real place, real team, real results).

## Style system dimensions

Write each dimension down with numbers. This becomes the style sheet that commissioning briefs and AI style blocks point to.

| Dimension | Decide | Example values |
| --- | --- | --- |
| Shape language | Geometric or organic; primitive set; corner treatment | Built from circles and rounded rectangles, corner radius 25% of the shape's short side, no sharp points |
| Line | None, monoline or variable; weight relative to artboard; color | Monoline 3px at a 400px spot illustration (0.75% of width), line color #1F2430 rather than pure black |
| Color | Palette size, roles, proportions, where brand accent appears | 4 brand colors plus 2 neutrals; accent on at most one focal object per scene; background tints at 8-15% |
| Skin tones | Separate set, never brand colors | 8-10 tones from light to deep, varied in undertone (warm, neutral, cool), not one hue at different lightness |
| Shading | Flat, cel or gradient | One cel shadow at 12-18% darker in the same hue, light from top-left |
| Texture | None, grain, halftone, paper, brush | Monochrome grain at 4-6% opacity on fills only |
| Perspective | Flat front, isometric, dimetric, 1- or 2-point | Flat for UI spots; 2:1 pixel dimetric (lines at about 26.57 degrees) for "isometric" tech scenes |
| Proportion | Head-to-body ratio for people | 1:3 to 1:4 stylized friendly; 1:6 to 1:7 naturalistic |
| Detail by size | What survives at each size | Spot: no facial features below 120px; hero: faces and hands |
| Composition | Crops, negative space, framing | Subjects cropped by one edge at most; 30-40% negative space for copy in hero art |
| Motion readiness | Layer naming and pivots | Separate limbs and props on named layers for Lottie or Rive rigging |

Pilot the system by drawing the same three test subjects in each candidate style: a person doing something, an object, and an abstract concept. Choose the style that handles all three.

## Character construction

- Build characters from the style's primitives. Draw a construction sheet: head, torso, limbs as shapes with proportions written on it.
- Produce a turnaround (front, three-quarter, side, back) and an expression sheet with 6-8 core emotions (neutral, happy, focused, surprised, worried, frustrated, relieved, proud).
- Simplify hands consistently (four fingers is acceptable in stylized work if applied everywhere) and draw a hand pose library: open, pointing, holding, typing, waving.
- Silhouette test: fill each pose solid black. If the action is unreadable, change the pose, not the detail.
- Use a line of action for every pose so figures do not look stiff.
- Mascots: define the do-not list (never angry, never sexualized, never mocking users) and the poses for app states (empty, error, success, loading).

## Inclusive representation

- **Skin:** a set of 8-10 tones that includes genuinely deep tones with warm and cool undertones. Draw facial features and shadows with a darker shade of each skin tone, not one fixed line color, so features stay visible on deep tones.
- **Avoid the non-human-color dodge.** Blue, purple or green skin (the Corporate Memphis convention) avoids representation rather than achieving it.
- **Hair:** straight, wavy, curly and coily textures, protective styles, gray hair, baldness, head coverings (hijab, turban, kippah, headwrap).
- **Bodies and ages:** a range of sizes, heights, ages from children to older adults.
- **Disability:** wheelchair users, prosthetic limbs, white canes, hearing aids, guide dogs, and non-visible disability cues where relevant. Show disabled people as experts and protagonists, not only as recipients of help.
- **Roles:** rotate who is the expert, the leader, the customer and the helper across the library; audit a scene set by counting who holds power in each image.
- **Casting matrix:** for a library of scenes, plan representation in a table (scene, characters, skin tone, age, gender expression, disability, role) before drawing, so diversity is designed rather than retrofitted.
- **Review:** have people from the represented groups review the library, especially for stereotypes in dress, setting and behavior.

## Illustration types

| Type | Typical size | Content | Use |
| --- | --- | --- | --- |
| Spot | 64-240px | One object or a tiny vignette, 1-3 colors | Empty states, feature lists, onboarding steps, error pages |
| Hero | 1200-2400px wide | A narrative moment, characters, room for copy | Landing page heroes, campaign key visuals, covers |
| Scene | Full artboard | An environment with several characters and story | Editorial, explainers, annual reports, packaging panels |
| Product illustration | Varies | Simplified UI or device drawings in the style | Marketing pages, docs, app store screenshots |
| Pattern | Tileable 512-1024px | Repeating motifs from the style | Packaging, backgrounds, merchandise |
| Animated | Spot or hero | Rigged layers | Lottie or Rive for UI states, social loops |

Production specs:

- Master in vector (Illustrator, Figma, Affinity) with named layers; raster painterly styles at 2x final size in layered PSD or Procreate files.
- Export spots as optimized SVG (often under 10-20KB each); export complex or textured art as AVIF or WebP with PNG fallback, at 1x and 2x.
- Keep a source library organized by type and theme, with tags for search.

## Commissioning brief

Send this to an illustrator or studio:

1. **Objective:** what the illustrations must help people understand or feel.
2. **Audience and markets.**
3. **Piece list:** each piece with type, size, placement, the content it must show, and copy that will sit beside it.
4. **Style:** the style sheet (above) or 6-10 references, each annotated with what to take from it (palette, line, texture, composition). Reference movements and techniques, not a living artist to imitate.
5. **Brand constraints:** palette, type, logo rules, things to avoid.
6. **Representation requirements:** the casting matrix.
7. **Deliverables:** formats, layer naming, source files, color profile, animation-ready layers if needed.
8. **Usage rights:** media, territory, duration, exclusivity, modification rights, and whether it is a license or an assignment of copyright. In the US, a commissioned work from an independent contractor is "work made for hire" only in specific statutory categories with a signed agreement; otherwise use a written assignment. Moral rights (attribution, integrity) apply in many countries, including the UK and EU states. Confirm terms with counsel.
9. **Process:** sketch round, color round, final; two revision rounds per stage is a common starting point.
10. **Schedule and budget.**

## Generic tells and fixes

- **Corporate Memphis** (tiny heads, oversized limbs, flat purple people, floating plants) → derive shapes from the brand's own geometry and use real skin tones.
- **Default library color** (for example the purple accent many free illustration libraries ship with) → recolor to the brand palette and adjust values, not just hue.
- **Isometric everything on floating platforms** → use isometric only when spatial relationships are the point.
- **Glossy 3D clay characters by default** → choose 3D only when the brand's material language supports it.
- **Inconsistent hands, eyes and line weights across a library** → construction sheet and a reviewer comparing every piece on one contact sheet.

## Accessibility

- Alt text describes the meaning ("A clinic receptionist handing a patient a printed receipt"), not the style.
- Purely decorative illustrations get `alt=""`.
- Never put essential information only in an illustration; repeat it in text.
- Shapes that carry meaning (diagram parts, map areas) need 3:1 contrast against neighbors.
- Animated illustrations respect `prefers-reduced-motion` and do not loop endlessly next to reading content.

## AI and illustration

Generators can draft style explorations and backgrounds fast, but drift on hands, faces and line weight across a set. Lock a style reference set, generate in small batches, redraw or vectorize finals, and record provenance. See [AI image generation](ai-image-generation.md).
