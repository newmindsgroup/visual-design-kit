# Category scan

Version-Timestamp: 2026-10-20 02:05:00 UTC

A category scan shows what the audience already sees, so directions can either meet expectations on purpose or stand apart on purpose. It takes 20-40 minutes of agent time and replaces guesswork about "what competitors do".

## Steps

1. **List 6-12 players.** Direct competitors, the category leader, one challenger, one adjacent-category brand the audience also uses, and any brand the client admires. Use WebSearch when available; otherwise ask the client or use the atlas industry entry's reference anchors.
2. **Capture.** For each, look at the homepage (or app store page, packaging, social profile) at 1440 and 390 widths. `node ../../design-critique/scripts/render_review.mjs <url> --widths 390,1440 --out <dir>` produces screenshots and a font/contrast report. Keep screenshots in the project's working folder for internal analysis only; never republish or ship them.
3. **Code each one** on the six axes:

| Axis | Record |
| --- | --- |
| Type | Classification (geometric sans, grotesque, humanist, serif, slab, display), case, weight, scale contrast |
| Color | Dominant hue, temperature, saturation, light or dark, accent usage |
| Layout | Grid logic, density, symmetry, hero pattern, whitespace |
| Imagery | Photography, illustration, 3D, product renders, UI screenshots, abstract; who is shown |
| Motion | None, subtle, scroll-driven, playful, cinematic |
| Voice | Formal-casual, serious-playful, respectful-irreverent, matter-of-fact-enthusiastic |

4. **Map.** Plot the set on two axes that matter to the brief (common pairs: warm-cool by restrained-expressive; traditional-progressive by mass-premium). Use a simple table or an SVG scatter. Mark clusters.
5. **Find the white space.** Name the crowded corner (for example "navy, geometric sans, phone mockups, 'simple' headlines") and 1-2 open positions that are relevant to the audience. An empty quadrant is only an opportunity if the audience would value it.
6. **List category clichés** you observed, merged with the atlas industry entry's *Category clichés*. Every direction must avoid them unless it uses one deliberately and says why.

## Output (keep it short)

```markdown
**Scanned:** 9 brands (list)
**Crowded:** ...
**Open:** ...
**Clichés to avoid:** ...
**Implication:** Direction A meets expectations on purpose; B and C occupy the open space at ...
```

## Ethics and limits

- Analyze public pages only; respect robots and terms; do not log in or scrape at volume.
- Never copy a competitor's distinctive assets, layouts or copy into a direction.
- If web access is unavailable, say the scan is based on the atlas and prior knowledge, which may be out of date.
