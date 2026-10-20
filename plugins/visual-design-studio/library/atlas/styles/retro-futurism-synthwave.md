---
id: style.retro-futurism-synthwave
axis: style
name: Retro-Futurism / Synthwave
aliases: [synthwave, outrun, retrowave, vaporwave-adjacent, 80s neon, googie, space age, raygun gothic, tron style]
summary: The 1980s imagining the future - neon magenta and cyan on deep violet, sunset gradients, perspective grids, chrome-and-italic type and scanlines; nostalgic night-drive energy with a space-age lineage.
tags: [synthwave, retrowave, neon, 80s, grid, sunset, futuristic, nostalgia]
pairs_with: [industry.gaming-esports, industry.media-entertainment-streaming, industry.events-conferences, industry.automotive-mobility, industry.crypto-web3, archetype.explorer, archetype.outlaw, archetype.magician, channel.video-motion, channel.social-media]
avoid_with: [industry.healthcare-provider, industry.government-civic, industry.insurance, audience.older-adults, audience.neurodivergent, tier.luxury]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Retro-Futurism / Synthwave

## Essence

A memory of the future. Retro-futurism looks back at how past eras pictured tomorrow: 1950s-60s Space Age and Googie (LAX Theme Building, 1961; Space Needle, 1962; *The Jetsons*, 1962) and, in this entry, chiefly the 1980s: *Tron* (1982), *Blade Runner* (1982, with Syd Mead's concept art), *Miami Vice* (1984), Sega's *Out Run* (1986) and Roger Dean's album covers. The 2010s revival named Synthwave or Outrun grew from Kavinsky's "Nightcall" (2010), the film *Drive* (2011), *Hotline Miami* (2012) and *Stranger Things* (2016). Its mood is night driving, neon, speed and longing. Use it where nostalgia for the 1980s is a feature, not a costume.

## Visual signature

- Deep violet-black night skies with neon magenta, cyan and orange; a striped sunset sun above a perspective grid horizon.
- Glowing outlines, chrome-gradient italic type, and slanted, extended or monoline display faces; occasional neon script titling (as in the pink script of *Drive*'s titles).
- Scanlines, VHS noise, chromatic aberration and CRT curvature in moderation.
- Wireframe landscapes, palm trees, mountains, sports cars (Countach and DeLorean silhouettes), robots, pixel icons.
- Geometric framing: HUD brackets, triangles, lines at the horizon, laser grids.
- Older Space-Age strand: atomic starbursts, boomerang shapes and rocket motifs in pastel or chrome.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Monoton (OFL, logo moments only); Audiowide (OFL); Tilt Neon (OFL, variable); Bungee Inline (OFL); script accent Yellowtail (Google Fonts, Apache); commercial: ITC Benguiat (Ed Benguiat, 1977, the *Stranger Things* title face), Eurostile Bold Extended |
| Body font | Chakra Petch 400-500 (OFL) at 16-17px; commercial: DIN Next |
| Mono (labels, HUD) | Share Tech Mono or VT323 (OFL) |
| Type scale ratio | 1.333 (perfect fourth); display skewed -8 to -12 degrees only for short titles |
| Body size / line-height | 16-17px / 1.55; measure 50-65ch; body on solid dark panels |
| Display letter-spacing | +0.04em to +0.08em in caps; line-height 1.05 |
| Caps / labels | 11-13px, uppercase, +0.14em, weight 500 |
| Weights | 400 body, 500-700 UI, single weight display |
| Palette | Night #0B0221 (oklch 0.14 0.066 292); Dusk #2B0F54 (oklch 0.26 0.115 296); Magenta #FF2A9D (oklch 0.67 0.254 355); Cyan #12E8FF (oklch 0.85 0.145 208); Sun orange #FF8A3C (oklch 0.75 0.167 51); Sun yellow #FFD54A (oklch 0.89 0.157 92); Lavender #F3E9FF (oklch 0.95 0.031 306); Grid violet #8B5CF6 (oklch 0.61 0.219 293) |
| Verified pairs | Lavender on Night 17.14:1; Cyan on Night 13.41:1; Sun yellow on Night 14.23:1; Sun orange on Night 8.57:1; Magenta on Night 5.81:1; Night on Magenta 5.81:1; Lavender on Dusk 13.79:1; Cyan on Dusk 10.79:1; Magenta on Dusk 4.67:1; Grid violet on Night 4.75:1; Lavender on Magenta only 2.95:1 (never) |
| Accent proportion | Night and Dusk 70%+; Magenta and Cyan 10-15% as lines and glows; Sun orange and yellow only in the sun gradient and highlights |
| Radius | 0-4px; chamfered corners (clip-path) for HUD panels; circles for the sun |
| Borders | 1-2px neon (Cyan or Magenta) lines; corner brackets instead of full boxes |
| Shadow / elevation | Glow, not shadow: `0 0 8px rgba(255, 42, 157, 0.7), 0 0 24px rgba(255, 42, 157, 0.35)` on borders and display type only; never on body text |
| Spacing density | Medium: 8px base, 24-32px panel padding, 80-120px sections; strong center axis |
| Grid | Centered 12-column container with a full-bleed perspective floor (CSS `perspective: 600px; rotateX(60deg)`) and horizon at 55-62% of the hero height |
| Motion | Grid scroll linear 6-20s loop; sun sink 12s; glow pulse 3-4s ease-in-out; UI transitions 200-300ms cubic-bezier(0.2, 0, 0, 1) |

## Composition and layout

- Build the hero as a scene: gradient sky (Night to Dusk to Magenta at the horizon), striped sun, mountain silhouette, grid floor. Set the headline above or on the sun, aligned to the center axis.
- Keep content on solid or near-solid Night/Dusk panels with neon edges; text never sits directly on the glow or grid.
- Use a restrained component system: flat dark cards, neon 1-2px borders, HUD labels in mono, and buttons with a filled Magenta or Cyan face and Night text.
- Limit effects to the hero and key accents. Below the fold, switch to a calm dark theme so reading is comfortable.
- For music, events and game pages, use full-bleed video loops of night driving or abstract grid flythroughs (under 8MB, muted, with a static poster).
- Print and merch: dark inks with spot fluorescents, holographic foil, gradient risograph effects.

## Imagery and iconography

- 3D and illustration: sunsets, palm silhouettes, wireframe terrains, chrome logo extrusions, low-poly cars rendered in magenta and cyan rim light.
- Photography: night city, neon signs, wet asphalt, rain on glass, with color grading toward magenta/cyan split-toning.
- Icons: 1.5-2px monoline neon-style or pixel icons at 24px; avoid soft gradients.
- Textures: scanlines at 4-6% opacity, film grain, subtle bloom on highlights; avoid heavy CRT warp on text.

## Motion

Cruising, never frantic. The grid scrolls toward the viewer at a steady linear speed (6-20s per tile loop), the sun sinks slowly, glows breathe on 3-4s sine easing at 0.85-1.0 opacity, and UI elements change in 200-300ms. Avoid strobing, glitch bursts above 3 flashes per second (WCAG 2.3.1) and constant full-screen noise. With `prefers-reduced-motion`, freeze the grid, keep the static scene and remove glow pulsing.

## Fits and risks

- **Where it works today:** games, esports and indie studios (`industry.gaming-esports`), music, film and series marketing (`industry.media-entertainment-streaming`), festivals, bars and arcade events (`industry.events-conferences`), EV and car culture (`industry.automotive-mobility`), and tech communities (`industry.crypto-web3`), delivered through video and social formats (`channel.video-motion`, `channel.social-media`). `archetype.explorer`, `archetype.outlaw` and `archetype.magician` use it for escape and spectacle.
- **Accessibility risk:** neon glow text, low-luminance grounds and scanline overlays lower legibility; flicker, bloom and scrolling grids can trigger photosensitive, vestibular and migraine reactions. Contrast on glow elements is hard to verify.
- **Longevity risk:** the revival has run since about 2010 and the sunset-grid image is now stock and AI default; new entrants look derivative. Relying on it for a permanent identity ties the brand to 1980s nostalgia.
- **Wrong for:** `industry.healthcare-provider`, `industry.government-civic`, `industry.insurance`, `tier.luxury`, `audience.older-adults` and `audience.neurodivergent` (sensory load and low trust signals).

## Do and don't

- Do choose one hero scene and a small set of reusable motifs (sun, grid, brackets).
- Do restrict neon to 2 hues plus the sun, and keep large calm dark areas.
- Do render type as flat colored text with a subtle glow offset behind it, not glow in the glyph itself.
- Don't use pink-to-cyan gradient text for paragraphs or put light text over the sun gradient.
- Don't add every cliché: palm trees, DeLoreans, Greek busts, katakana and a Lamborghini in one layout.
- Don't leave the grid and glow animating when the tab is hidden or on battery-saving; pause them.

## Clichés and AI tells

- The lazy version: an AI-generated sunset-grid with palm trees, a chrome script "Retrowave" title, purple-pink gradient background, Orbitron body text and floating geometric shapes.
- Generated neon signs with gibberish lettering and inconsistent glow.
- Fix: base the world on a specific reference (a real 1986 arcade cabinet, a specific highway), draw the sun and grid as clean vectors or CSS, set UI in a legible sans on solid panels, and let the product's story pick the palette instead of defaulting to magenta and cyan.

## Accessibility notes

- Dark-ground neon passes comfortably: Lavender on Night 17.14:1, Cyan 13.41:1, Magenta 5.81:1; this is the style's main accessibility strength.
- Lavender on Magenta is 2.95:1 and fails; put Night text on Magenta buttons (5.81:1).
- Grid violet #8B5CF6 on Night is 4.75:1: acceptable for links at 16px+, but use Cyan for body-size interactive text.
- Never apply text-shadow glow with a spread large enough to blur glyph edges; test text at 200% zoom and against the brightest part of the background.
- No full-screen flashing, rapid scanline sweeps or looping VHS glitch; supply a "reduce effects" toggle in addition to `prefers-reduced-motion`.

## Reference anchors

- *Tron* (1982), *Blade Runner* (1982) and Syd Mead's concept art; *Miami Vice* (1984-1990)
- Sega, *Out Run* (1986) arcade cabinet and soundtrack
- Kavinsky, "Nightcall" (2010) and Nicolas Winding Refn's *Drive* (2011) title design
- *Hotline Miami* (2012) and *Stranger Things* (2016) title sequence in ITC Benguiat
- Roger Dean's covers for Yes and Googie architecture (LAX Theme Building, 1961) for the older retro-futurist line
- Syd Mead, *Sentinel* and *Oblagon* books for painterly future-industrial design
