# OKLCH ramps

Version-Timestamp: 2026-10-20 02:07:10 UTC

Build every ramp in OKLCH, then export sRGB hex (and optionally Display P3). OKLCH separates lightness (L, 0-1), chroma (C, 0 to about 0.37) and hue (H, 0-360 degrees) so you can change one without disturbing the others.

## Why OKLCH

- **Lightness means lightness.** In HSL, pure yellow `#FFFF00` and pure blue `#0000FF` are both "50% lightness", yet yellow is 1.07:1 against white and blue is 8.59:1. In OKLCH they are L 0.97 and L 0.45, which predicts that difference. Equal L steps look like equal steps across hues.
- **Hue stays put.** Lowering chroma or lightness in OKLCH keeps the hue stable; HSL and older CIELAB-based LCH drift (blues turn purple in CIELAB LCH).
- **Native CSS.** `oklch()` is supported in all major browsers since 2023, as are `color-mix(in oklch, ...)` and gradient interpolation `in oklch`. Relative color syntax (`oklch(from var(--color-accent-default) calc(l + 0.08) c h)`) is widely supported since 2024.
- **Predictable contrast.** Because L tracks perceived lightness, the same step gives similar contrast across hues. It is not identical to WCAG luminance, so always compute the final pairs.

## The gamut problem

sRGB can only show limited chroma at each lightness, and the limit depends on hue. Maximum in-gamut chroma in sRGB (computed):

| L | Red 25 | Orange 60 | Yellow 95 | Green 145 | Teal 195 | Blue 250 | Violet 300 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.30 | 0.121 | 0.070 | 0.061 | 0.094 | 0.051 | 0.084 | 0.160 |
| 0.40 | 0.162 | 0.093 | 0.082 | 0.125 | 0.068 | 0.113 | 0.213 |
| 0.50 | 0.202 | 0.117 | 0.102 | 0.157 | 0.085 | 0.141 | 0.266 |
| 0.60 | 0.243 | 0.140 | 0.123 | 0.188 | 0.102 | 0.169 | 0.258 |
| 0.70 | 0.190 | 0.164 | 0.143 | 0.220 | 0.119 | 0.163 | 0.185 |
| 0.80 | 0.114 | 0.140 | 0.164 | 0.251 | 0.136 | 0.104 | 0.118 |
| 0.90 | 0.051 | 0.064 | 0.158 | 0.195 | 0.153 | 0.050 | 0.056 |
| 0.95 | 0.024 | 0.031 | 0.079 | 0.088 | 0.075 | 0.024 | 0.027 |

What this means:

- Yellows and greens only get vivid when light; a dark, saturated yellow is impossible (it becomes olive or brown).
- Blues and violets get vivid when dark; light blues are pale by nature.
- Teal and cyan have low chroma everywhere in sRGB; P3 screens show noticeably more.
- **Gamut mapping:** when a requested color is out of gamut, reduce chroma at constant L and H until it fits (the CSS Color 4 approach). Do this before exporting hex; naive per-channel clipping shifts hue and lightness.

## The kit's ramp algorithm

`library/scripts/color_tools.py ramp` generated the kit's primitives (`slate`, `sand`, `teal`, `vermilion`, `green`, `amber`, `red`, `blue`). It works like this:

1. **Steps** 50, 100, 200 ... 900, 950 (11 steps). Neutral ramps add 850 and 975 for dark-mode surfaces.
2. **Lightness is linear in the step:** `L = 0.975 - (step - 50) / 900 * 0.81`, so 50 is L 0.975, 500 is L 0.57 and 950 is L 0.165. Every 100 steps is the same perceived lightness difference (0.09).
3. **Chroma tapers from the middle:** `C = peak * (0.12 + 0.88 * sin(pi * t) ^ 0.65)` with `t = (step - 50) / 900`. Chroma peaks at step 500 and falls to 12% of the peak at 50 and 950, so light tints and dark shades stay calm.
4. **Optional hue shift** rotates hue linearly across the ramp (half subtracted at 50, half added at 950). Use 10-20 degrees for yellows and oranges so dark steps go toward red-brown instead of olive.
5. **Gamut mapping** reduces chroma at constant L and H wherever the request exceeds sRGB.

Anchor results for any hue with these defaults (computed for hues 25 to 300 at typical peak chroma): white text on step 600 at 6.2-7.2:1, step 700 text on step 100 at 7.6-8.3:1, step 500 on step 50 at 3.9-4.5:1 (borders and focus), step 950 text on step 300 at 8.1-9.1:1 (dark-mode on-accent). That is why the semantic tokens map accent default to 600 in light mode and 300 in dark mode.

The 11-step lightness grid is fixed; the brand color is matched by choosing the step nearest its L and checking that the hue and chroma land close. If an exact brand value must appear in the ramp, put it in the brand file as its own primitive and point the relevant semantic token at it after checking contrast.

## Using the kit color tools

Run from the skill directory (paths are relative to `skills/color/references/`; from `SKILL.md` drop one `../`):

```sh
python3 ../../../library/scripts/color_tools.py ramp --hue 195 --chroma 0.12 --name teal --format table
python3 ../../../library/scripts/color_tools.py ramp --hue 85 --chroma 0.14 --hue-shift -15 --name ochre --format css
python3 ../../../library/scripts/color_tools.py convert '#006C6C' 'oklch(0.62 0.12 195)'
python3 ../../../library/scripts/color_tools.py contrast '#FFFFFF' '#006C6C'
python3 ../../../library/scripts/color_tools.py apca '#565F67' '#F2F7FC'
python3 ../../../library/scripts/color_tools.py check-palette palette.json
```

- `ramp` options: `--steps` (step names on the 50-950 scale), `--l-max` and `--l-min` (lightness at 50 and 950), `--floor` (share of chroma kept at the ends), `--taper` (0 keeps chroma constant), `--hue-shift`, `--format json|css|table`.
- `contrast` prints the WCAG 2.2 ratio with AA and AAA verdicts and an APCA Lc for reference; `apca` prints Lc (APCA-W3 0.1.9) with the level it meets.
- Example outputs: white on `#006C6C` is 6.25:1 (Lc -85.8); `#565F67` muted text on `#F2F7FC` canvas is Lc 77.1.

When the script is unavailable, browser tools work: the OKLCH picker at oklch.com, Huetone (ramp building with contrast), and Adobe Leonardo (contrast-targeted ramps).

## CSS patterns

```css
:root {
  --color-accent-default: #006c6c;                                   /* teal 600, oklch(0.481 0.082 195) */
  --color-accent-hover: #005050;                                     /* teal 700 */
}
@media (color-gamut: p3) {
  :root { --color-accent-default: oklch(0.481 0.1 195); }           /* more chroma where the screen can show it */
}
.hero { background: linear-gradient(135deg in oklch, oklch(0.48 0.08 195), oklch(0.39 0.12 255)); }
.tint { background: color-mix(in oklch, var(--color-accent-default) 12%, var(--color-bg-canvas)); }
```

Keep generated tints and shades in the token files rather than computing them ad hoc in components, so contrast can be linted (`tokens.py lint`, see the `design-system` skill).

## Neutral ramps

- Use the same lightness grid with peak chroma 0.01-0.02 and either the accent's hue (cool brands; Meridian's slate sits at hue about 245) or a warm hue around 60-90 (paper, food, hospitality, luxury; Ember's sand ramp is warm).
- Pure gray (chroma 0) suits photography-led and Swiss work; most other styles look better slightly tinted.
- A warm neutral with a cool accent (or the reverse) adds depth; keep neutral chroma under 0.02 so text stays neutral.

## Gradients

- Interpolate in OKLCH to avoid the gray dead zone between distant hues: `linear-gradient(in oklch, ...)`.
- Neighboring hues (30-90 degrees apart) read as light; complements read as loud. The generic purple-to-pink AI gradient runs from about hue 290 to 350; use it only when the brief asks for that energy.
- Never place body text on an unbounded gradient; give it a solid backing or test the worst-case area.

## Ramp checklist

- Hue, peak chroma, hue shift and any custom lightness range recorded in the token `$description`.
- Brand color matched to its nearest step, or added as its own primitive with checked pairs.
- Anchors pass: white on 600 at 4.5:1, 700 on 100 at 4.5:1, 500 on 50 at 3:1, 950 on 300 at 4.5:1.
- All values in sRGB gamut after mapping; P3 values optional.
- Visual review: steps look evenly spaced; no muddy midtones; light steps not neon.
