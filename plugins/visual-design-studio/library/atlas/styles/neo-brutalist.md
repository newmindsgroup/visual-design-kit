---
id: style.neo-brutalist
axis: style
name: Neo-Brutalism
aliases: [neubrutalism, neobrutalism, neo brutalist ui, hard shadow ui, gumroad style, chunky outline ui]
summary: Friendly, loud interfaces: thick black outlines, hard offset shadows, flat pastel and saturated fills, chunky grotesque type and snappy press states; playful structure, still highly legible.
tags: [neo-brutalist, thick-borders, hard-shadow, flat, playful, bold, ui, pastel]
pairs_with: [industry.saas-b2b, industry.developer-tools, industry.fintech-banking, industry.ecommerce-dtc, industry.creative-agencies-studios, audience.teens-gen-z, archetype.everyperson, archetype.jester, channel.marketing-website, tier.mid-market]
avoid_with: [tier.luxury, tier.ultra-luxury, industry.healthcare-provider, industry.insurance, audience.older-adults, industry.legal-professional-services]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Neo-Brutalism

## Essence

A softened, commercial descendant of web brutalism (see `style.web-brutalist`) that took shape around 2019-2021 as design-tool and creator-economy products looked for an alternative to glassy gradients and rounded SaaS. Gumroad's rebrand (around 2021-2023) is its best-known mainstream example, and community neobrutalism component kits for shadcn/ui and Tailwind spread it. The recipe: black outlines 2-4px thick, hard offset shadows with no blur, flat saturated or pastel fills, heavy grotesque type, and clear, tactile press states. It looks rebellious but behaves like a very legible, conventional UI.

## Visual signature

- 2-4px solid near-black borders on cards, buttons, inputs and images.
- Hard shadows: the same shape offset 4-8px down and right in black, no blur.
- Flat fills in bright pastels and saturated primaries (yellow, pink, blue, lime, coral) on a cream or white canvas.
- Heavy grotesque headlines in sentence or title case, large and tight; a clean sans for body; optional monospace for labels and numbers.
- Buttons that physically press: they translate toward their shadow on `:active`.
- Hand-made touches: sticker-like badges, rotated labels, doodled arrows, squiggles, emoji-free icons.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Bricolage Grotesque 700-800 (OFL, optical-size and width axes); Archivo 800-900 at width 110-125 (OFL); Darker Grotesque 800-900 (OFL); commercial: GT America Extended (Grilli Type), Druk Wide (Commercial Type) |
| Body font | Public Sans 400-500 (OFL); commercial: GT America Standard |
| Mono (labels, numerals) | DM Mono (OFL) |
| Type scale ratio | 1.25 (major third) UI; display up to 1.5 on heroes |
| Body size / line-height | 16-18px / 1.5; measure 55-70ch |
| Display letter-spacing | -0.02em to -0.03em at 40px+; line-height 1.0-1.1 |
| Caps / labels | 12-13px, uppercase, +0.04em, weight 700, often in mono |
| Weights | 400 body, 600-700 UI labels, 800 display |
| Palette | Ink #111111 (oklch 0.18 0 0); Cream #FFF4E0 (oklch 0.97 0.029 83); Yellow #FFDC58 (oklch 0.90 0.152 94); Pink #FF90E8 (oklch 0.80 0.170 335); Blue #7AA2F7 (oklch 0.72 0.132 264); Lime #B8F34A (oklch 0.89 0.201 127); Coral #FF6B57 (oklch 0.71 0.185 30); focus Cobalt #2D4EF5 (oklch 0.52 0.249 267) |
| Verified pairs | Ink on Cream 17.33:1; Ink on Yellow 14.05:1; Ink on Lime 14.35:1; Ink on Pink 9.36:1; Ink on Blue 7.50:1; Ink on Coral 6.74:1; Cobalt on Cream 5.47:1; white on Coral only 2.80:1 and Pink on Cream 1.85:1 (fills, never text) |
| Accent proportion | Fills are the identity: 2-3 saturated fills share 30-50% of the surface; text is always Ink |
| Radius | One value across the system: 0 (strict) or 8px (friendly); never mix |
| Borders | 2px Ink on controls, 3px on cards and images; 4px on hero panels |
| Shadow / elevation | Hard offset: `4px 4px 0 0 #111111` default, `6px 6px 0` on hover, `0 0 0` pressed; no blur or spread |
| Spacing density | Medium to tight: 4px base, 16-24px card padding, 48-80px sections; generous gaps so shadows breathe |
| Grid | 12 columns, 24-32px gutters (to fit the 6-8px shadows); cards snap to grid with identical heights |
| Motion | 80-140ms, ease-out (cubic-bezier(0.2, 0, 0, 1)); press translate 4px; no easing flourishes |

## Composition and layout

- Build with stacked, bordered blocks: a hero card in Yellow, a feature grid in mixed pastels, a Cream ground between. Alignment is strict; the attitude comes from color, borders and type.
- Keep reading surfaces plain: long text sits on Cream or White, not on saturated fills.
- Use rotated sticker badges (-3 to 3 degrees) and doodle arrows as accents, no more than 2-3 per viewport.
- Make states unmistakable: hover raises the shadow, `:active` collapses it, selected uses a fill and a thicker border, disabled uses dashed borders and a flat fill.
- In product UI, apply the language to shells and controls (buttons, cards, tabs) but use simpler tables and charts for dense data; maintain 40-48px row heights and clear zebra or rule patterns.
- Marketing pages: oversize one headline, one hard-shadow CTA and a real product screenshot inside a 3px-bordered frame.

## Imagery and iconography

- Product screenshots in bordered frames with a hard shadow; photography cut out or placed in rectangles with the same border.
- Illustration: flat vector, simple shapes, thick outlines, limited to the palette; stickers and hand-drawn doodles.
- Icons: 2px monoline, square or rounded caps to match the radius, drawn at 24px; fill selected states with a palette color.
- Charts: thick bars with Ink outlines, direct labels, categorical fills from the palette plus patterns for color-blind safety.

## Motion

Snappy and physical. On hover a button lifts 2px (shadow grows from 4px to 6px) in 100ms; on press it translates by the shadow offset and the shadow disappears in 80ms. Modals pop with a 140ms scale from 0.96 and a hard backdrop. Marquees and sticker wiggles are optional and slow (8-12s loops). With `prefers-reduced-motion`, keep the press translation (it communicates state) but remove loops and wiggles.

## Fits and risks

- **Where it works today:** product-led SaaS and developer tools (`industry.saas-b2b`, `industry.developer-tools`), creator and community platforms, DTC and merch (`industry.ecommerce-dtc`), studios and event microsites (`industry.creative-agencies-studios`), and campaigns aimed at `audience.teens-gen-z`. Consumer fintech uses it as the category-breaking direction (`industry.fintech-banking`) with `archetype.everyperson` or `archetype.jester` voices. It fits `channel.marketing-website` and `tier.mid-market` best.
- **Longevity risk:** it peaked in 2021-2024 and is now strongly associated with startup templates and AI-generated "quirky" UIs. Expect it to date; build it on tokens (border width, shadow offset, radius, fills) so it can relax into a calmer system.
- **Accessibility risk:** generally strong (Ink on pastel passes), but low-vision users may struggle with visual clutter; the shadow can be mistaken for a focus state, and rotated stickers hurt reading.
- **Brand risk:** the playful frame can undercut gravity for large balances, medical or legal content. For fintech keep transaction and confirmation screens calm and conventional.
- **Wrong for:** `tier.luxury` and `tier.ultra-luxury`, `industry.healthcare-provider`, `industry.insurance`, `industry.legal-professional-services`, and `audience.older-adults` where trust and calm outweigh energy.

## Do and don't

- Do define the system with four tokens: border width, shadow offset, one radius and a fill palette.
- Do give every interactive element a pressed, hover, focus and disabled state that differ from the resting state.
- Do keep body copy on neutral surfaces and set all text in Ink.
- Don't use soft blurry shadows or gradients in the same layout; they dissolve the language.
- Don't put white text on pastel fills or Pink and Yellow text on Cream; use Ink.
- Don't give every element a shadow; reserve it for interactive and elevated objects.

## Clichés and AI tells

- The lazy version: Space Grotesk headline, yellow hero with `4px 4px 0` shadow on every card, rotated pink sticker saying "NEW", and a three-card feature row with emoji.
- Component libraries that apply the shadow and border to every element, including text paragraphs and table rows.
- Fix: swap the default grotesque for a font with character (Bricolage Grotesque or Archivo Expanded), restrict shadows to buttons and raised cards, derive the fills from the brand rather than pastel defaults, add custom illustration, and prove the system works on a dense screen as well as a landing page.

## Accessibility notes

- Ink text on every palette fill passes AA (lowest: Ink on Coral 6.74:1); white on Coral is 2.80:1 and fails, so never invert text on fills.
- A 2-3px Ink border gives every control a 3:1 or better boundary against Cream (Ink on Cream 17.33:1), which satisfies non-text contrast for inputs.
- Do not use the shadow as the focus or selected indicator. Use a separate focus ring: 3px Cobalt #2D4EF5, offset 3px onto the Cream ground (5.47:1). Cobalt on Pink is only 2.96:1, so offset the ring onto the page ground.
- Rotated stickers and labels must stay under 5 words and be duplicated as normal text for screen readers.
- Touch targets: keep 44px minimum height; shadows do not count toward the hit area, so pad accordingly.

## Reference anchors

- Gumroad's rebrand (around 2021-2023) as the best-known mainstream example
- Community neobrutalism component kits for shadcn/ui and Tailwind; Figma Community neubrutalism UI kits
- Bloomberg Businessweek print covers and raw web brutalism as lineage (`style.web-brutalist`)
- Memphis Group posters and 1990s Gen-Z zines as visual parents
- W3C WCAG 2.2 success criteria 1.4.11 (non-text contrast) and 2.4.13 (focus appearance, AAA) for focus design
