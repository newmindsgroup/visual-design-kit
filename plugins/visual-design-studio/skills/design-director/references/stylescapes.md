# Stylescapes: rendering directions

Version-Timestamp: 2026-10-20 02:05:00 UTC

A stylescape is a single page that shows a direction as if it already existed: hero composition, palette, type, components, an application, imagery, motion and voice. It is the cheapest artifact that lets a client react to the real thing instead of adjectives.

## How to make one

1. Copy `../../../library/examples/stylescapes/_template/stylescape.html` into the project's working folder as `directions/<letter>-<name>/index.html`. Never write inside the installed kit.
2. Set the direction's tokens in the template's `:root` block using the token contract names (`--color-bg-canvas`, `--color-accent-default`, `--font-family-display`, `--radius-md`, `--duration-moderate`, `--ease-standard`, ...). Values come from the direction recipe.
3. Self-host fonts (OFL families from Google Fonts or Fontsource) next to the page with their license files; record commercial alternatives in the rationale. Never hotlink fonts in client deliverables (privacy and reliability).
4. Fill all ten sections: direction header, hero, palette with computed contrast, type specimens with real copy, components with focus and error states, 1-2 applications for the main channel, imagery and icon samples, motion note and demo, voice lines, rationale.
5. Make the hero the showpiece. Use real-sounding copy from the brief, not lorem ipsum. Draw imagery with CSS and inline SVG or use client-approved assets; for photographic directions, describe the shot list and show a composed placeholder rather than stock photos.
6. Render and inspect: `node ../../design-critique/scripts/render_review.mjs directions/<letter>-<name>/index.html --widths 390,1440 --full-page`, then look at the screenshots and fix overflow, orphans, contrast and generic-AI tells.

## Presenting several directions

- Build a `directions/index.html` comparison page with one row per direction: hero thumbnail (screenshot), name, position (expected / adjacent / breaking), three palette chips, type names and the weighted score.
- Show the directions at the same size and fidelity. Uneven polish biases the choice.
- When the host supports it (claude.ai Artifacts, Claude Code artifacts), publish the comparison page privately and share the link; otherwise send the screenshots.

## Fidelity guide

| Stage | Fidelity | Time per direction |
| --- | --- | --- |
| Early exploration (5 directions) | Hero, palette, type, voice only | Short |
| Standard (3-4 directions) | All ten sections | Medium |
| Final two | Add a second application and a real interaction prototype | Longer |

## Examples

The calibration set in `../../../library/examples/stylescapes/` shows twelve finished stylescapes across very different briefs: a Gen Z neobank in Brazil, pediatric telehealth, a Kyoto inn, an industrial IoT dashboard, streetwear, Puerto Rican coffee packaging, a law firm, a climate nonprofit, an esports team, a pharmacy app for older adults, an Arabic-first fashion store and a developer CLI. Look at two or three relevant ones before making your own to calibrate the quality bar and the range.
