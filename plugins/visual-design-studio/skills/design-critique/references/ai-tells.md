# Generic-AI design tells

Version-Timestamp: 2026-10-20 02:29:27 UTC

Patterns that make work look machine-made or template-made. Each has an ID for review notes, what it looks like, why it happens and the specific fix. A pattern is a tell when it appears by default. When the brief asks for it and the execution earns it (a fintech for teenagers that really is neon, a luxury brand that really is symmetric), it is a decision; write the reason down.

The [AI-tells gallery](../../../library/examples/ai-tells/index.html) renders 18 of these side by side with a better version for a different industry and style each time. Gallery numbers are given as "Gallery 01".

## Fast detection

1. Run the **name-swap test**: cover the logo, read a competitor's name into it. If it still works, look for tells.
2. Run the **squint test**: blur the screenshot. A uniform gray field or three equal blobs means flat hierarchy (AT-16) or cards everywhere (AT-06).
3. Scan this list top to bottom against the screenshot. Note every hit by ID.
4. Two or three unrequested tells cap Distinctiveness at 3 in the [rubric](rubric.md); four or more cap it at 2.

## Color and surface

### AT-01 Default indigo-to-pink gradient (`default-gradient`)
- **Looks like:** a 135-degree wash from indigo (#6366F1) through purple (#A855F7) to pink (#EC4899) behind white centered text; the same gradient on buttons. Gallery 01.
- **Why:** these are stock Tailwind values and the house style of 2018-2023 SaaS, which dominate the examples models learned from. Indigo is the default primary in many UI kits.
- **Fix:** take color from the brand strategy or the domain (materials, place, product, heritage). Pick one accent with a role, check it at 4.5:1 for text use, and let neutrals carry most of the surface. If a gradient is right, build it from brand hues, interpolate in OKLCH to avoid gray midpoints, and give it a job (light, depth, progress).

### AT-07 Gratuitous glassmorphism (`gratuitous-glass`)
- **Looks like:** every panel frosted (`backdrop-filter: blur`) at 10-20% white over blurred color blobs, with white text that fades into light areas. Gallery 07.
- **Why:** it looks rich in a still Dribbble shot and echoes recent OS materials; models reach for it to signal "premium".
- **Fix:** use translucency only where real content sits behind it (a nav over photography, a sheet over a map) and tint it 60-75% so text clears 4.5:1 over the lightest thing behind. Put forms, prices and data on opaque surfaces. Provide an opaque fallback with `@supports not (backdrop-filter: blur(1px))`.

### AT-08 Gradient text headlines (`gradient-text`)
- **Looks like:** headline words filled with a cyan-to-violet-to-pink gradient via `background-clip: text`. Gallery 08.
- **Why:** a one-line "premium" effect, common on AI product sites.
- **Fix:** solid color at full strength, with emphasis from scale, weight, italic or a solid highlight block. If gradient type is a brand asset, keep it display-only (48px+), check contrast at the lightest stop, and make sure `forced-colors: active` falls back to a system color.

### AT-09 Glowing orbs and blobs (`glow-orbs`)
- **Looks like:** large blurred radial blobs (violet, cyan) behind hero text on near-black. Gallery 09.
- **Why:** shorthand for "AI", "energy" or "the future" that needs no subject knowledge.
- **Fix:** show the actual thing: product UI, data, material, place or process. If atmosphere is needed, derive it from the brand (a texture, a light quality in photography, a pattern from the logo).

### AT-17 Low-contrast gray body text (`gray-body-text`)
- **Looks like:** body copy in #999, #A3A3A3 or #9CA3AF at 14px light on white (2.5-2.8:1). Gallery 15.
- **Why:** gray reads as "minimal" in a thumbnail; gray-400 is a common default for secondary text.
- **Fix:** body text in the brand ink or #1F1F1F-#333333 (aim for 7:1, never under 4.5:1), 16-18px, regular weight. Keep muted colors for metadata and still clear 4.5:1.

### AT-20 Dark mode with neon glow (`neon-dark-mode`)
- **Looks like:** #05010F backgrounds, cyan or magenta borders with `box-shadow` glow, glowing text, gradient progress bars. Gallery 18.
- **Why:** "developer" and "AI" visual shorthand; glow hides weak hierarchy.
- **Fix:** dark surfaces around #0F1115-#1A1D23 with elevation from lighter surfaces, text around #E6E8EB, one accent and one status color per meaning, no glow. Avoid pure white on pure black for long reading (halation). Check muted text at 4.5:1 on the darkest surface it appears on.

## Typography and hierarchy

### AT-02 Inter or system sans for everything (`one-sans-everywhere`)
- **Looks like:** one sans family for display, body, labels and numbers; weight is the only lever. Gallery 02.
- **Why:** Inter and `system-ui` are safe, free and already in the starter template; models avoid committing to a typographic voice.
- **Fix:** choose type for the brand's character and the reading job: a display face with a point of view (serif, condensed, characterful grotesk), a text face for long reading, tabular or mono figures for data. Two families, three roles. Inter remains a good UI text face when the display face carries the voice.

### AT-16 Everything the same visual weight (`flat-hierarchy`)
- **Looks like:** headline, subhead, body and buttons within a few pixels of each other; bold everywhere or nowhere; the squint test shows a gray field.
- **Why:** components assembled independently, each with default sizes; no one decided the order.
- **Fix:** decide the first, second and third thing per view. On marketing pages make display type 2.5-4x the body size; on product screens use size, weight and position for the one number or action that matters. One primary action per view.

## Layout and composition

### AT-03 Centered hero plus three icon cards (`centered-hero-three-cards`)
- **Looks like:** pill badge, centered H1, centered subhead, two buttons, then three equal cards with an icon, a title and one line. Gallery 03.
- **Why:** the single most common landing template; symmetry feels safe.
- **Fix:** start from content priority, not the template. Use an asymmetric grid (7/5, 8/4), put the product or proof in the hero, and replace three interchangeable cards with a sequence, a comparison, an index or one strong proof.

### AT-06 Uniform rounded cards with soft shadows (`uniform-soft-cards`)
- **Looks like:** every block in a white card, 12-16px radius, `0 10px 30px rgba(0,0,0,.08)` shadow, all the same size. Gallery 06.
- **Why:** component libraries default to cards; a card is a safe container for anything.
- **Fix:** group with space and hairlines first. Reserve elevation for things that float (menus, dialogs, a dragged item) or for the one element that matters. Size by importance. Set radius from the brand (0-2px for Swiss or brutalist, 20px+ for playful), not the library default.

### AT-21 Symmetric everything (`symmetry-default`)
- **Looks like:** every section centered and mirrored; equal columns; text blocks centered for paragraphs longer than two lines.
- **Why:** centering is the easiest way to look "balanced" without a grid.
- **Fix:** flush-left text, a real column grid and deliberate asymmetry; align to 2-4 vertical axes. Keep symmetry for brands that need ceremony (luxury, Art Deco, civic and legal formality) and execute it precisely.

### AT-22 Identical section rhythm (`same-section-rhythm`)
- **Looks like:** every section is eyebrow, centered H2, subhead and a three-column grid, with the same padding, top to bottom.
- **Why:** sections generated one at a time from the same pattern.
- **Fix:** compose by content type: full-bleed image, list, table, quote, data, timeline. Alternate loud and quiet sections, vary density and height, and let at least one section break the grid.

### AT-18 Too many calls to action (`cta-pileup`)
- **Looks like:** three to five equal buttons in one view, plus a banner and "Learn more". Gallery 16.
- **Why:** every stakeholder's goal gets a button; models list every possible action.
- **Fix:** one primary action per view, one secondary as a text link; move the rest into context (pricing, contact, footer). Answer the questions that "Learn more" defers with content.

### AT-19 Badge and pill overload (`pill-overload`)
- **Looks like:** NEW, HOT, BESTSELLER, -30%, AI, Beta, ECO pills on one item; tag chips under every heading. Gallery 17.
- **Why:** pills are cheap emphasis; models add one per attribute.
- **Fix:** at most one status per item, and only when it changes the decision (back in stock, low stock, sale with a real reference price). Attributes go in plain text.

## Icons, imagery and illustration

### AT-04 Emoji as icons (`emoji-icons`)
- **Looks like:** 🚀 ⚡ 🔒 ✨ as feature icons, bullets or button decoration. Gallery 04.
- **Why:** typing an emoji is faster than choosing or drawing an icon.
- **Fix:** one icon family on a 24px grid with one stroke weight (draw them, or use a permissive set such as Lucide (ISC), Phosphor (MIT) or Material Symbols (Apache 2.0)), or no icons at all. Emoji belong in chat, user content or a deliberately playful voice.

### AT-05 Icons in pastel circles (`pastel-icon-circles`)
- **Looks like:** a line icon centered in a 48-64px lavender, mint, peach or sky circle, one per feature. Gallery 05.
- **Why:** a template trick to make stock icons feel designed.
- **Fix:** delete them when the text carries the meaning. If icons stay, set them inline at text size in the brand color, or make them real illustrations of the specific feature.

### AT-10 Fake dashboard screenshot hero (`fake-dashboard-hero`)
- **Looks like:** a tilted 3D mockup full of unreadable bars, donuts and placeholder numbers. Gallery 10.
- **Why:** it says "software" without designing a real screen.
- **Fix:** show one real, legible moment of the product at 1:1 or a close crop, with realistic data and an annotation. Let it bleed off an edge to imply the rest.

### AT-11 Sparkle icons for AI (`ai-sparkles`)
- **Looks like:** ✨ on every AI feature, "AI Magic" labels, purple gradients reserved for AI. Gallery 11.
- **Why:** an industry convention since 2023 and the fastest possible signifier.
- **Fix:** name the action and its inputs ("Draft reply from 3 help articles"), label generated output where users need to know, show sources, and offer edit, insert and discard. Give AI features a brand-native treatment, not a borrowed one.

### AT-12 Generic blob-people illustration (`blob-people`)
- **Looks like:** flat figures with tiny heads, long limbs and purple or no skin, high-fiving around a laptop. Gallery 12.
- **Why:** illustration packs made this the default "diverse, friendly" image.
- **Fix:** commission or define an illustration system with a point of view (line weight, palette, subjects, what is never drawn), draw the specific situation and objects, or use documentary photography of real people with consent.

### AT-13 Stock-photo smiles (`stock-smiles`)
- **Looks like:** a diverse team laughing at a laptop, a handshake, a headset agent smiling at the camera.
- **Why:** stock search and generic image prompts both return the median image.
- **Fix:** art-direct photography of real customers, staff, places and products, or show no people. For AI-generated images write a specific brief (subject, place, light, lens, moment), never depict real identifiable people without consent, and never present generated people as customers.

## Copy and proof

### AT-14 Meaningless metrics (`empty-metrics`)
- **Looks like:** "10x faster", "99.9% satisfaction", "500K+ users", "24/7 support" in large gradient numerals. Gallery 13.
- **Why:** the proof band is a template slot, and models fill slots with plausible numbers.
- **Fix:** use only numbers the client supplied, each with unit, population, period and source. Fewer and specific beats many and round. Never invent figures; with no data, use a qualitative proof such as a named, permissioned case study.

### AT-15 Vague promise copy (`vague-promise`)
- **Looks like:** "Unlock your potential", "Transform your workflow", "Take your brand to the next level", "All-in-one platform", "Effortless experience". Gallery 14.
- **Why:** abstract benefit phrases are the most frequent marketing language.
- **Fix:** concrete outcome, audience, mechanism and constraint: "Throw a set of four mugs in six Saturdays." Test each line: can a reader picture it, and could it be false?

### AT-23 Fake testimonials (`fake-testimonials`)
- **Looks like:** five stars, "This changed my life!", "Sarah J., CEO", an initials avatar, no company.
- **Why:** the testimonial grid is a template slot and models fill it.
- **Fix:** use only real, permissioned quotes with full name, role, company and a specific outcome. In drafts, label placeholders visibly ("Placeholder: replace with a real quote"). Fake reviews and testimonials are prohibited in many markets (for example the US FTC rule on consumer reviews and testimonials, 2024, and the UK Digital Markets, Competition and Consumers Act 2024); confirm with counsel.

### AT-24 Copy tells (`copy-tells`)
- **Looks like:** em-dash reveals ("Fast — really fast"), "It's not just X, it's Y", "Whether you're X or Y", triplets ("Fast. Simple. Secure."), rhetorical questions, "Say goodbye to X", "In a world where X". Gallery 14.
- **Why:** high-frequency rhetorical cadences in model output.
- **Fix:** plain declarative sentences with specific nouns and numbers. Cut the setup and keep the payoff. Use commas, colons or full stops; allow at most one em dash per page. Read it aloud.

### AT-26 Logo soup proof bar (`logo-soup`)
- **Looks like:** "Trusted by" with a row of grayscale generic or fictional wordmarks.
- **Why:** a template slot filled with placeholders.
- **Fix:** real customer logos with written permission, or one named case study, or nothing.

## Motion

### AT-25 Motion on everything (`motion-everything`)
- **Looks like:** every element fades up on scroll over 600-800ms with the same easing; cards lift on hover; parallax on decorative layers.
- **Why:** animation libraries make a default reveal one attribute away.
- **Fix:** give motion a job (feedback, continuity, attention to one thing). UI transitions 120-320ms, stagger 30-60ms, reveal once, and honor `prefers-reduced-motion` with opacity-only or no motion.

## Not tells on their own

Purple, gradients, glass, Inter, cards, centered layouts, dark mode and emoji are all legitimate when the brief calls for them and the execution is specific. Record the reason in the critique ("Gradient: brand asset since 2019; built from brand hues; display only") and score the execution with the [rubric](rubric.md).
