---
id: style.memphis-postmodern
axis: style
name: Memphis / Postmodern
aliases: [memphis, memphis milano, memphis group, 80s postmodern, postmodernism, squiggle and confetti, terrazzo pop]
summary: Playful 1980s postmodern geometry: squiggles, zigzags, confetti and terrazzo patterns, pastel-and-primary clashes, tilted shapes and wide geometric type; deliberate bad taste made joyful.
tags: [memphis, postmodern, playful, patterns, geometric, 80s, colorful, shapes]
pairs_with: [industry.kids-family, industry.education-edtech, industry.food-beverage-cpg, industry.events-conferences, industry.creative-agencies-studios, audience.teens-gen-z, archetype.jester, archetype.creator, channel.packaging, channel.social-media]
avoid_with: [industry.legal-professional-services, industry.healthcare-provider, tier.luxury, archetype.ruler, audience.neurodivergent, industry.insurance]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Memphis / Postmodern

## Essence

A joke with craft behind it. The Memphis Group formed in Milan around Ettore Sottsass in December 1980 and showed its first collection at the Milan furniture fair in September 1981; the name came from Bob Dylan's "Stuck Inside of Mobile with the Memphis Blues Again". Members included Michele De Lucchi, Matteo Thun, Nathalie du Pasquier, George Sowden, Martine Bedin and Andrea Branzi, with Peter Shire, Shiro Kuramata and Michael Graves among contributors. It rejected modernist good taste with plastic laminate, loud pattern, and furniture that looked like toys (Sottsass's Carlton bookcase, 1981). In graphics it spread through April Greiman's work, MTV-era broadcast design, *Pee-wee's Playhouse* (1986) and *Saved by the Bell* credits. Use it to make a brand feel youthful, optimistic and unafraid of looking silly.

## Visual signature

- Basic shapes in impossible combinations: triangle, semicircle, cylinder, squiggle, zigzag, arch, grid, tilted at odd angles.
- Patterns as image: confetti, terrazzo, bacteria-like dots (Sottsass's *Bacterio* laminate, 1978), stripes, checkers, pink-and-black hatch.
- Pastels beside primaries and black: pink, turquoise, lemon, lilac and cobalt on white, with bold black outlines.
- Wide geometric sans-serif display, tight and heavy, sometimes outlined or stacked; sentence-style slogans.
- Flat color with no photographic realism; objects float without perspective.
- Asymmetric, off-grid arrangements that still anchor to a single focal object or phrase.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Unbounded 700-900 (OFL, wide rounded geometric); Syne 800 (OFL, extra wide); Bowlby One (OFL, chunky); commercial: ITC Avant Garde Gothic (Herb Lubalin and Tom Carnase, 1970), Futura Extra Bold |
| Body font | Red Hat Text 400-500 (OFL) at 16-18px; commercial: ITC Avant Garde Gothic Book |
| Type scale ratio | 1.5 (perfect fifth) for large jumps; headlines 5-8x body size |
| Body size / line-height | 16-18px / 1.5; measure 45-60ch; body on solid paper panels |
| Display letter-spacing | -0.02em to 0 on wide faces; line-height 0.95-1.05 |
| Caps / labels | 12-14px, uppercase, +0.08em, weight 700 |
| Weights | 400 body, 700 UI, 800-900 display |
| Palette | Ink #121212 (oklch 0.18 0 0); Paper #FFFDF7 (oklch 0.99 0.008 91); Pink #FF6FAE (oklch 0.73 0.186 355); Teal #0FB5AE (oklch 0.70 0.119 190); Yellow #FFD23F (oklch 0.88 0.162 91); Cobalt #2D4EF5 (oklch 0.52 0.249 267); Lilac #B9A3F5 (oklch 0.77 0.117 296) |
| Verified pairs | Ink on Paper 18.42:1; Ink on Yellow 12.97:1; Ink on Lilac 8.58:1; Ink on Teal 7.35:1; Ink on Pink 7.26:1; Cobalt on Paper 5.87:1; white on Cobalt 5.97:1; Pink on Paper 2.54:1 and Teal on Paper 2.51:1 fail for text or thin borders |
| Accent proportion | 3-5 colors in play at once; no single color above 40%; Ink used as outlines and type |
| Radius | Mixed shape vocabulary: 0, 50% circles, semicircles, arches; UI controls use 0 or pill (999px), not a mid radius |
| Borders | 3px Ink outlines on shapes and cards; squiggle and zigzag dividers drawn as SVG strokes |
| Shadow / elevation | None on UI; decorative offset shapes and pattern-filled "shadows" (hatch or dot fills) as shapes, not blur |
| Spacing density | Medium: 8px base, 16-24px card padding, 56-96px sections; space organized around the focal object |
| Grid | 8-column loose grid; elements rotated 5-15 degrees; mobile stacks into a single column with shapes between sections |
| Motion | 250-450ms, cubic-bezier(0.68, -0.55, 0.27, 1.55) (back ease); pop, spin and wobble; loops capped at 3 cycles |

## Composition and layout

- Choose one hero object or phrase and give it the most space; then scatter 4-8 shapes around it with intentional collisions and one pattern field.
- Use pattern as a ground and keep text on solid Paper or Ink panels; pattern at full contrast under text breaks legibility.
- Tilt shapes, not text: rotate a headline at most 3-5 degrees and keep body copy level.
- Alternate bands: a pattern band, a color band, a text band; use zigzag or scalloped dividers instead of straight rules.
- Build components with the shape vocabulary: a semicircle badge, a triangle bullet, a squiggle underline for links.
- For social and packaging, create a kit of 12-20 shapes and 3-4 patterns, with rules for scale (large, medium, small) so applications feel designed, not random.

## Imagery and iconography

- Illustration: flat geometric shapes, bold outlines, collage-like arrangements; occasional hand-drawn squiggles.
- Photography: studio shots on solid color backgrounds with hard light; products and people cut out and mixed with shapes.
- Icons: filled, 3px outlined shapes at 24-32px with simple geometry; bold rather than delicate.
- Patterns: confetti, terrazzo and grid tiles authored as repeatable SVG at 80-160px so they remain light.

## Motion

Bouncy and playful. Shapes pop in with a back-ease overshoot over 250-450ms, spin 90 degrees on hover, and wobble 2-4 degrees. Use a short idle loop (3 cycles maximum) on one hero shape, then rest. Cap simultaneous moving shapes at 3. With `prefers-reduced-motion`, show final positions and replace pops with 120ms fades.

## Fits and risks

- **Fits:** children's and family products (`industry.kids-family`), learning tools (`industry.education-edtech`), snacks, drinks and packaging (`industry.food-beverage-cpg`, `channel.packaging`), festivals and events (`industry.events-conferences`), creative studios (`industry.creative-agencies-studios`) and social campaigns (`channel.social-media`). It talks to `audience.teens-gen-z` with `archetype.jester` humor, and `archetype.creator` brands use it to show a hand-made, experimental spirit.
- **Risks:** a 1980s revival cycle returns every few years, so identities built on shapes alone age quickly; the style is easy to execute badly (random shapes with no focal point). It conflicts with premium restraint and with serious tasks.
- **Wrong for:** `tier.luxury`, `archetype.ruler`, `industry.legal-professional-services`, `industry.healthcare-provider` and `industry.insurance` (credibility and calm), and `audience.neurodivergent` when pattern density or motion cannot be reduced.

## Do and don't

- Do commit to one focal object per layout and let shapes support it.
- Do repeat shapes and patterns systematically (three scales, four patterns, five colors).
- Do keep body text level, high contrast and on quiet surfaces.
- Don't use all patterns at once or fill every corner; calm areas make the loud ones read.
- Don't use Pink or Teal as text or thin lines on white; use them as fills with Ink text.
- Don't add 3D renders, gradients or glass; Memphis is flat and graphic.

## Clichés and AI tells

- The lazy version: a purple-teal-yellow squiggle wallpaper behind a SaaS landing page, with 90s confetti and Comic Sans-like fonts.
- Generated "Memphis" imagery with melted shapes, incoherent patterns and illegible lettering.
- Fix: define a limited shape kit drawn as clean vectors, assign each shape a role in the brand story, use real photography or product shots as the anchor, and choose a type face with personality (Unbounded or Syne) that still reads in paragraphs.

## Accessibility notes

- Ink text on any palette fill passes (lowest: Ink on Pink 7.26:1); Pink #FF6FAE on Paper is 2.54:1 and Teal on Paper 2.51:1, so they cannot be text, icons or hairlines on light grounds.
- Cobalt on Paper is 5.87:1 and white on Cobalt 5.97:1, a safe link and primary button pair.
- Patterns behind text reduce contrast unpredictably; keep a solid panel behind all copy and keep pattern contrast under 10% inside content areas.
- Bouncy overshoot, spinning shapes and busy backdrops can trigger vestibular and attention issues; provide a reduced-motion variant and pause loops after 5 seconds.
- Shapes carrying meaning (status, categories) need labels or icons in addition to color.

## Reference anchors

- Ettore Sottsass and the Memphis Group, Milan (1980-1988): Carlton bookcase (1981), Martine Bedin's Super lamp (1981), Nathalie du Pasquier's patterns
- Sottsass's *Bacterio* laminate for Abet Laminati (1978)
- April Greiman, *Hybrid Imagery* issue of *Design Quarterly* (1986)
- Michael Graves, Portland Building (1982) as architectural postmodernism
- *Pee-wee's Playhouse* set design (1986) and *Saved by the Bell* graphics as pop-cultural echoes
- https://en.wikipedia.org/wiki/Memphis_Group
