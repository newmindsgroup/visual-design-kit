---
id: style.web-brutalist
axis: style
name: Raw Web Brutalism
aliases: [brutalist web design, brutalist websites, raw html, anti-design, default web aesthetic, unstyled web, raw brutalism]
summary: Deliberately raw websites: system fonts, browser-blue links, hard black-and-white blocks and visible structure; honesty and speed over polish. Niche and risky; needs usability scaffolding.
tags: [brutalist, raw, anti-design, html, monospace, default, stark, web]
pairs_with: [industry.creative-agencies-studios, industry.media-entertainment-streaming, industry.nonprofit-ngo, industry.developer-tools, archetype.outlaw, archetype.creator, channel.marketing-website, audience.expert-power-users, audience.low-bandwidth-entry-devices]
avoid_with: [industry.healthcare-provider, industry.fintech-banking, tier.luxury, audience.older-adults, audience.children-under-13, archetype.caregiver]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Raw Web Brutalism

## Essence

The website shows its own bones. Named after architectural brutalism (from *béton brut*, raw concrete: Le Corbusier's Unité d'Habitation in Marseille, 1952; Reyner Banham's essay "The New Brutalism", 1955), web brutalism rejects templates, gradients and polish for default fonts, plain links, hard rectangles and content-first structure. Pascal Deville's Brutalist Websites collection (started 2014) gave the style its name; Craigslist (1995) and Hacker News (2007) are the accidental ancestors. It is a stance as much as a style: honest, fast and slightly confrontational.

## Visual signature

- System fonts at default sizes: Times New Roman, Arial or Courier New; no webfont, or one monospace used with intent.
- Browser-default link colors (blue, purple visited), underlines, `<hr>` rules and `<table>` layouts rendered visibly.
- Stark black-and-white, with a single hot flat color (pure red, yellow, green) at most; no gradients, no shadows, no rounding.
- Raw structure shown on purpose: borders on every block, visible grids, oversized headings, text in giant uppercase, raw filenames.
- Layouts that ignore conventional hierarchy: overlapping text blocks, off-grid placement, huge empty fields, a single column pushed against an edge.
- Unprocessed imagery (original-size JPEGs, screenshots, low-res scans) and animated GIFs.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | System serif or sans at heavy size: Times New Roman, Arial Bold; Courier New for code-like heads; OFL stand-ins Tinos, Arimo, Cousine; Space Mono Bold (OFL); commercial: Helvetica Neue, Times |
| Body font | The browser default: Times New Roman 16-20px; or Courier Prime (OFL) / IBM Plex Mono (OFL) at 16px for a typewriter register |
| Type scale ratio | Browser default heading scale (2em, 1.5em, 1.17em) or an extreme jump: headings at 8-14vw, body at 16-20px |
| Body size / line-height | 16-20px / 1.4-1.6 (default 1.2 is too tight for reading); measure up to 80ch if a column constraint is not set, preferably capped at 70ch |
| Display letter-spacing | 0; tight (-0.04em) for giant uppercase headings |
| Caps / labels | Uppercase 14-16px, 0 to +0.04em; or all-lowercase monospace |
| Weights | Regular 400 and Bold 700 only |
| Palette | Black #000000 (oklch 0 0 0); White #FFFFFF (oklch 1 0 0); Link #0000EE (oklch 0.43 0.297 264); Visited #551A8B (oklch 0.38 0.172 302); Active #EE0000 (oklch 0.60 0.245 29); Button face #EFEFEF (oklch 0.95 0 0); Mark #FFFF00 (oklch 0.97 0.211 110) |
| Verified pairs | Black on White 21.00:1; Link on White 9.40:1; Visited on White 11.01:1; Black on Mark 19.56:1; Link on Mark 8.75:1; Link on Button face 8.17:1; Active #EE0000 on White 4.53:1 (the Chromium default #FF0000 is only 4.00:1); Link on Black 2.23:1 fails |
| Accent proportion | 0-10%; one pure color used flatly, or none |
| Radius | 0; never round |
| Borders | 1-3px solid black on blocks, tables and inputs; `<hr>` and default `<fieldset>` borders |
| Shadow / elevation | None |
| Spacing density | Browser defaults (8px body margin, 1em paragraph spacing) or deliberate extremes: no padding, or huge empty fields |
| Grid | None or a rough single column; optionally a visible CSS grid with 1px borders; tables for tabular data only |
| Motion | None; instant state changes (0ms); native behaviors only (anchors, `<details>`, scroll) |

## Composition and layout

- Start from semantic HTML (headings, lists, `<nav>`, `<main>`, `<table>`) and add only the CSS that expresses a point of view: one oversized heading, one border rule, one measure.
- Let the content define the layout; use a single column, left-aligned, or a dense table of contents on the home page as the main navigation.
- Make navigation text visible and literal ("Work", "About", "Contact"); no hamburger menus or hidden gestures.
- Use scale and contrast, not decoration, to show hierarchy: heading at 12vw next to 16px body.
- If you break the grid, break it once and on purpose (a block pinned to the right edge, a heading running off the page), and verify mobile reflow.
- Keep pages small: under 100KB of HTML and CSS, no JavaScript frameworks, fonts from the system, images sized and compressed.

## Imagery and iconography

- Photography and screenshots shown straight, with unedited borders or captions in monospace; flat black-and-white dither is acceptable.
- Icons: none, or plain text glyphs (arrows "->", "x", "+", asterisks) that are real characters, not icon fonts.
- Illustration: ASCII art, hand scans, primitive vector shapes, GIFs; never glossy 3D.
- Video: native `<video controls>` without custom skins.

## Motion

Absent by design. State changes are immediate, links change color, and nothing slides. If motion is needed (a marquee, a blinking cursor), keep it to one element and stop it under `prefers-reduced-motion`. Respect the 3-flashes-per-second limit of WCAG 2.3.1; the GIF-era habit of blinking text is an accessibility hazard.

## Fits and risks

- **Where it works today:** art, architecture and design studio portfolios (`industry.creative-agencies-studios`), record labels, galleries and independent publishers (`industry.media-entertainment-streaming`), campaigns and collectives (`industry.nonprofit-ngo`), developer tool docs and personal sites (`industry.developer-tools`, `audience.expert-power-users`), and fast static marketing pages (`channel.marketing-website`). The honest, lightweight HTML also suits `audience.low-bandwidth-entry-devices`. `archetype.outlaw` and `archetype.creator` use the rawness as a stance.
- **Accessibility risk:** the plain-HTML core is robust (semantic, zoomable, high contrast), but the performative variant often fails WCAG: overlapping text at 200% zoom (1.4.4, 1.4.10), missing visible focus (2.4.7), tiny link targets (2.5.8), and unlabeled controls. Test with keyboard, a screen reader and 400% zoom.
- **Longevity and brand risk:** it is a statement tied to a design-culture moment; it can look broken or negligent to ordinary customers, hurts trust in regulated or care contexts, and becomes a pastiche when copied. Plan a restrained evolution rather than a permanent identity for mass brands.
- **Wrong for:** `industry.healthcare-provider` and `industry.fintech-banking` (trust and error recovery matter more than attitude), `tier.luxury`, `audience.older-adults` and `audience.children-under-13` (need guidance and friendly affordances), and `archetype.caregiver`.

## Do and don't

- Do keep real semantics, visible focus and underlined links; the rawness should reduce effort, not add it.
- Do choose one deliberate break (scale, color or layout) and let everything else stay plain.
- Do set `max-width` and a viewport meta tag; "no design" still needs a readable measure.
- Don't hide navigation, rely on color alone for links or use text smaller than 14px.
- Don't confuse chaos with brutalism: overlapping, illegible text is a bug, not a signal.
- Don't add the usual polish later (soft shadows, glass, rounded buttons) and still call it brutalist.

## Clichés and AI tells

- The lazy version: Courier New in all caps, black-on-white, a `box-shadow` offset on every button, a pink hero and the headline "WE BREAK THE RULES". That is neo-brutalism or a template, not raw web brutalism.
- Generated pages that fake rawness with deliberate misalignment, hand-written CSS "glitches" and broken links.
- Fix: write the actual content first, use real default HTML elements, keep the tooling off the page, and make one specific design decision that expresses the brand's position (a single huge word, a tabular index, a monospaced voice).

## Accessibility notes

- Default link blue #0000EE on White is 9.40:1 and visited purple #551A8B is 11.01:1; keep the underline so color is not the only cue.
- Chromium's default active-link red #FF0000 is 4.00:1 on White (Firefox's #EE0000 is 4.53:1); if you restyle, set `a:active` to #C00000 (6.48:1 on White) or darker.
- Pure yellow #FFFF00 backgrounds with Black text (19.56:1) are safe, but yellow text on white fails; test every pair.
- Hit area: default inline links are often under 24px high; add padding to nav and footer links to meet WCAG 2.2 target size.
- Do not remove focus outlines. If you restyle, use a 3px solid outline in Black or Link blue with a 2px offset.

## Reference anchors

- Pascal Deville, Brutalist Websites (started 2014)
- David Copeland, *Brutalist Web Design* (brutalist-web.design), a manifesto for content-first, honest sites
- Reyner Banham, "The New Brutalism" (1955); Le Corbusier, Unité d'Habitation (1952); Alison and Peter Smithson
- Craigslist and Hacker News as unpolished, durable interfaces
- Bloomberg Businessweek print covers (2010s) as a graphic parallel
- W3C WCAG 2.2 (https://www.w3.org/TR/WCAG22/) for the checks this style must still pass
