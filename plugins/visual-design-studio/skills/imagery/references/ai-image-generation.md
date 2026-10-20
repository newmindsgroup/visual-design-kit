# AI image generation

Version-Timestamp: 2026-10-20 02:07:10 UTC

Generated images are a production medium like illustration or 3D. They are excellent for exploration, mood, backgrounds, stylized art and composites, and they are misleading when they stand in for proof. Write prompts like a photographer's brief, lock a style for consistency, clean up by hand, and keep an honest record.

## Appropriate vs misleading uses

| Appropriate (with disclosure where required) | Not acceptable |
| --- | --- |
| Moodboards, stylescapes and concept exploration | A "product photo" of a real product that was never photographed, or that shows features, finishes or contents it does not have |
| Backgrounds, textures, abstract and atmospheric imagery | Fake customers, fake testimonials, fake reviews with generated faces |
| Stylized illustration in a defined brand style | Fake before/after results (health, beauty, fitness, finance) |
| Storyboards, animatics and pre-visualization | Fake staff, team or founder photos |
| Labeled concept renders of products in development | Documentary-looking images of events, places or news that did not happen |
| Composites: real product photography placed in a generated environment, light-matched | Images of real, identifiable people without their written consent |
| Extending or cleaning up the brand's own photos (outpainting, object removal) | Fake UI screenshots, awards, certifications or press coverage |
| Placeholder images in comps, marked as placeholders | Anything implying an endorsement, location or capability that is not true |

When in doubt, ask: would a reasonable viewer believe this shows something real that the brand is claiming? If yes, use real photography or label the image clearly.

## Prompt anatomy

Write natural-language sentences in this order. Most current models follow descriptive prose better than keyword lists.

| Part | What to write | Example |
| --- | --- | --- |
| Subject and action | Who or what, doing what, with what expression | "A clinic receptionist in her fifties handing a printed receipt to an elderly patient, both smiling slightly" |
| Setting | Place, time, season, specific objects | "at a small wooden reception desk in a sunlit neighborhood clinic, potted fern, paper forms" |
| Framing | Shot size and angle | "medium shot at eye level, subject on the right third" |
| Lens and camera | Focal length, aperture, depth of field | "photographed on a 35mm lens at f/2.8, soft background" |
| Light | Quality, direction, time, color temperature | "soft morning window light from the left, warm daylight, gentle shadows" |
| Palette | Dominant colors in plain words | "muted teal, warm cream and natural wood tones" |
| Medium and style | Photograph, gouache, risograph print, vector flat, 3D render, film stock look | "natural editorial photograph, fine film grain" |
| Mood | One or two words | "calm, competent" |
| Composition and negative space | Where copy will go | "empty wall on the left 40% of the frame for a headline" |
| Constraints | What must not appear | "no text, no logos, no extra people, natural hands" |
| Output | Aspect ratio and size, if the tool takes it in the prompt | "16:9" |

Hex values are rarely followed exactly; describe colors in words and correct the grade afterward.

Example prompts:

1. **Lifestyle context (no product claim):** "Overhead photograph of a kitchen table on a Sunday morning: a half-eaten croissant, a ceramic coffee cup, an open paperback, scattered crumbs on a linen cloth. Soft diffused daylight from a north-facing window, 5500K, low contrast. Muted terracotta, oat and sage palette. Natural editorial photograph with fine grain. Leave the top third of the frame as plain linen for a headline. No text, no logos, no hands."
2. **Abstract hero background:** "Close macro photograph of light passing through rippled frosted glass, producing soft teal and amber gradients and fine caustic lines. Shallow depth of field, gentle vignette, calm and precise mood. No objects, no text. 16:9."
3. **Editorial illustration:** "Flat editorial illustration of a woman cycling across a bridge at dawn, built from simple geometric shapes, a limited palette of deep blue, coral and cream, subtle paper grain texture, generous empty sky above her for a title. Style: mid-century travel poster, screen-printed look. No text."

Keep a **style block**, a fixed paragraph of medium, light, palette, texture and constraints, and append it to every prompt in a campaign so the set stays consistent.

## Consistency across a set

- **Style references:** supply 2-5 images that show palette, medium and light; describe which attribute each one controls. A style reference must never override product truth or an approved logo.
- **Character references:** a reference sheet with front, three-quarter and side views, fixed outfit and palette. Repeat key identifying details in every prompt.
- **Seeds:** a fixed seed reproduces an image only with the same model version, prompt and settings. It helps iteration; it does not guarantee identity across different prompts.
- **Image-to-image and edits:** use the best approved image as the base; describe only the change, and ask the model to preserve everything else. Inspect the whole frame afterward, because edits often alter other areas.
- **Fine-tuning (LoRA or custom models):** for persistent characters or products. This is a separate data action: confirm rights to the training images and where the model is stored.
- **Contact-sheet review:** judge the set side by side, not image by image. Reject outliers in light direction, grade or proportion.
- Use only controls the current tool documents (aspect ratio, reference slots, seed, negative prompt, edit masks). Tools differ; never assume a parameter exists. Routing and tool-specific steps live in [ChatGPT Images](../../../library/draft-skills/design-chatgpt-images/SKILL.md), [OpenArt CLI](../../../library/draft-skills/design-openart-cli/SKILL.md) and [Higgsfield CLI](../../../library/draft-skills/design-higgsfield-cli/SKILL.md); compare tools with [route selection](../../../library/draft-skills/design-media-route-selection/SKILL.md).

## Text in images

- Models still garble small text, long strings, non-Latin scripts, brand names and numbers, even when headlines look right.
- Never bake final copy, prices, legal text, dates or logos into a generated image. Generate clean copy space and set live type in the layout, where it can be edited, translated, read by screen readers and indexed.
- If in-scene text is essential (a shop sign, a label in a mockup), keep it to 1-3 short words, check every glyph at 100%, and replace it with real type in compositing when it matters.
- Logos: composite the real vector logo afterward; never let a generator draw it.

## Product truth and compositing

- Photograph the real product (or use approved CAD renders), then generate or shoot the environment.
- Match perspective (camera height and focal length), light direction and softness, color temperature, and add a contact shadow and reflections.
- When using a product photo as an image-to-image reference, compare label text, proportions, colors, materials and part counts against the original at matched size. Any drift is a defect, not a style.
- Label composites and concept renders wherever a viewer could take them for photography of a real scene, and follow the client's disclosure policy.

## Rights, likeness and artists

- **Living artists:** do not prompt with living artists' names or "in the style of [living artist]". Describe the attributes instead: medium, era, movement, palette, line quality, composition. Historical movements (Bauhaus, ukiyo-e, Art Deco poster) are fine.
- **Trademarks and characters:** do not generate other brands' logos, products, packaging or copyrighted characters.
- **Likeness:** do not generate identifiable real people without written consent. Right-of-publicity laws protect likeness in many places, and some now cover AI imitations specifically (for example Tennessee's ELVIS Act of 2024 for voice and likeness).
- **Ownership:** the US Copyright Office (*Copyright and Artificial Intelligence, Part 2: Copyrightability*, January 2025) holds that purely AI-generated material is not protected by copyright; human selection, arrangement and substantial modification can be. Tell clients that raw outputs may not be exclusively ownable, and do not use generated art as a logo or key brand asset without human authorship.
- **Tool terms:** read the current terms for commercial use, training on your inputs, and any IP indemnity (some vendors offer indemnity on enterprise plans).
- Confirm rights questions with counsel for the specific use and jurisdiction.

## Provenance and labeling

- **Content Credentials (C2PA):** a signed manifest embedded in the file that records the tool, edits and, optionally, the author. Several generators attach C2PA manifests or invisible watermarks (for example Google's SynthID). Preserve them: many export, optimization and CMS pipelines strip metadata. Check files with the Content Credentials Verify tool at contentcredentials.org.
- **Platform labels:** Meta, TikTok and YouTube label or require disclosure of realistic AI-generated or altered content; TikTok reads C2PA data to label automatically; YouTube requires creators to disclose realistic altered or synthetic content. Follow each platform's current rules.
- **Regulation:** the EU AI Act's Article 50 transparency obligations apply from 2 August 2026: deployers must disclose deepfakes (realistic content depicting real people, places or events), with lighter "appropriate disclosure" for evidently artistic, satirical or fictional works; providers must make outputs machine-detectable. Advertising law (for example US FTC rules on deceptive advertising, UK CAP Code) applies to AI images like any other. Confirm requirements with counsel for the specific product and jurisdiction.
- **Internal record per image:** tool, model and version, date, prompt and style block, reference images with their rights, seed and settings if any, edits and repairs, human contributions, approver, disclosure decision. Store it next to the asset.

## Cleanup and upscaling

Inspect at 100% and at final size:

- Hands and fingers (count), teeth, eyes (matching catchlights and gaze), ears, earrings and glasses symmetry.
- Text and glyphs, logos, numbers on objects.
- Physics: shadow directions agree, reflections match, objects touch surfaces, liquids and fabric behave.
- Background faces and crowds (often melted), repeating textures, impossible architecture.
- Edges: halos, cut-outs, fringing around hair.
- Product geometry and label facts against the source.

Fix with targeted inpainting for contextual areas and manual retouching for anything exact. Return to the best approved source when detail degrades; do not keep regenerating a degraded derivative. See [image repair](../../../library/draft-skills/design-media-image-repair/SKILL.md).

Upscaling:

- Many generators output around 1-2 megapixels. An A4 page at 300ppi needs 2480x3508px; a 1920px web hero at 2x needs 3840px. Plan 2-4x upscaling for print and large screens.
- AI upscalers invent detail. They are fine for textures and atmosphere; never use them to "recover" faces of real people, label text or product details that must be factual.
- After upscaling: remove artifacts, add a consistent fine grain (about 1-3% monochrome) to unify composites, grade to the brand palette, then convert to CMYK last for print.

## Generic AI look and how to avoid it

| Tell | Fix in the prompt or in post |
| --- | --- |
| Waxy, poreless skin | "visible skin texture, natural imperfections", retouch at standard level only |
| Everything dramatic: rim light, haze, teal-orange | Ordinary light from a named source, neutral grade |
| Perfect symmetry and centered subjects | Specify the third, the crop, the tilt |
| Bokeh everywhere | Specify aperture and what is in focus |
| Floating objects | "resting on", plus a contact shadow in post |
| The same face in every image | Describe age, features and casting differences; use real people where identity matters |
| Over-saturated fantasy color | Name a restrained palette; grade down |

## Budget and process

- Agree a candidate count and spend limit before generating; 4-8 candidates per direction is a common starting point.
- Generate one hero still per direction and inspect it before deriving formats or motion.
- Score candidates with the [media quality evaluation](../../../library/draft-skills/design-media-quality-evaluation/SKILL.md) rubric, and keep art direction in the [media art direction](../../../library/draft-skills/design-media-art-direction/SKILL.md) packet; for multi-shot campaigns use [reference control](../../../library/draft-skills/design-media-reference-control/SKILL.md).
