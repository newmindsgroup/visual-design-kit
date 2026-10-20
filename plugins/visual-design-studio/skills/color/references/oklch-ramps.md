# OKLCH ramps

Version-Timestamp: 2026-10-20 02:07:10 UTC

Build every ramp in OKLCH, then export sRGB hex (and optionally Display P3). OKLCH separates lightness (L, 0-1), chroma (C, 0 to about 0.37) and hue (H, 0-360 degrees) so you can change one without disturbing the others.

## Why OKLCH

- **Lightness means lightness.** In HSL, pure yellow `#FFFF00` and pure blue `#0000FF` are both "50% lightness", yet yellow is 1.07:1 against white and blue is 8.59:1. In OKLCH they are L 0.97 and L 0.45, which predicts that difference. Equal L steps look like equal steps across hues.
- **Hue stays put.** Lowering chroma or lightness in OKLCH keeps the hue stable; HSL and older CIELAB-based LCH drift (blues turn purple in CIELAB LCH).
- **Native CSS.** `oklch()` is supported in all major browsers since 2023, as are `color-mix(in oklch, ...)` and gradient interpolation `in oklch`. Relative color syntax (`oklch(from var(--x) calc(l + 0.08) c h)`) is widely supported since 2024.
- **Predictable contrast.** Because L tracks perceived lightness, a lightness target per ramp step gives similar contrast across hues. It is not identical to WCAG luminance, so always compute the final pairs.

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

- Yellows and greens only get vivid when light; you cannot have a dark, saturated yellow (it becomes olive or brown).
- Blues and violets get vivid when dark; light blues are pale by nature.
- Teal and cyan have low chroma everywhere in sRGB; P3 screens show noticeably more.
- **Gamut mapping:** when a requested color is out of gamut, reduce chroma at constant L and H until it fits (the CSS Color 4 approach, which searches chroma with a just-noticeable-difference tolerance). Do this before exporting hex; naive per-channel clipping shifts hue and lightness.

## Ramp algorithm

1. **Pick the hue** from the brand color (convert it: `color_tools.py convert '#hex'`). Pick a peak chroma: 0.10-0.16 for most UI accents, 0.18+ for vivid brands, 0.005-0.015 for neutrals.
2. **Set lightness targets** per step:

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L | 0.985 | 0.965 | 0.935 | 0.895 | 0.845 | 0.78 | 0.69 | 0.60 | 0.52 | 0.45 | 0.38 | 0.27 |

These targets give, for most hues: step 8 at 3:1+ on step 1 (borders, focus), step 9 at 4.5:1+ with white text (fills), step 11 at 4.5:1+ on steps 1-3 (text), step 12 at 12:1+.

3. **Shape chroma** as a fraction of the peak, low at the light end, peaking at steps 7-8:

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C fraction | 0.12 | 0.22 | 0.38 | 0.55 | 0.72 | 0.88 | 1.0 | 1.0 | 0.92 | 0.80 | 0.66 | 0.50 |

4. **Clamp each step to the gamut** (max in-gamut chroma at that L and H).
5. **Shift hue where it helps** (optional, 5-20 degrees across the ramp): yellows and oranges rotate toward red as they darken (to avoid olive); greens rotate toward teal; blues can rotate slightly toward cyan in the lightest steps.
6. **Pin the brand color.** Find the step whose L is nearest the brand's L and replace that step with the exact brand value. If the brand lands at step 7 or 8 (too light for white text), keep it as the brand fill for large areas and use step 9 for buttons.
7. **Verify anchors** with real contrast math (see [contrast](contrast.md)) and adjust L by 0.01-0.03 where a pair misses.
8. **Export** hex for sRGB, keep the `oklch()` source in the token `$description`, and optionally add a P3 value with more chroma for supporting screens.

Pseudocode:

```python
L = [0.985, 0.965, 0.935, 0.895, 0.845, 0.78, 0.69, 0.60, 0.52, 0.45, 0.38, 0.27]
F = [0.12, 0.22, 0.38, 0.55, 0.72, 0.88, 1.0, 1.0, 0.92, 0.80, 0.66, 0.50]
def ramp(hue, peak, shift=0.0):
    steps = []
    for i, (l, f) in enumerate(zip(L, F)):
        h = hue + shift * i / 11
        c = min(peak * f, max_in_gamut_chroma(l, h))   # binary search on chroma
        steps.append(oklch_to_hex(l, c, h))
    return steps
```

## Using the kit color tools

Run from the skill directory; check `--help` first for the exact flags.

```sh
python3 ../../../library/scripts/color_tools.py --help
python3 ../../../library/scripts/color_tools.py ramp --hue 195 --chroma 0.12 --name teal     # 12-step ramp
python3 ../../../library/scripts/color_tools.py convert '#047879'                               # hex <-> OKLCH
python3 ../../../library/scripts/color_tools.py contrast '#FFFFFF' '#047879'                   # WCAG 2.2 ratio
python3 ../../../library/scripts/color_tools.py apca '#626B6B' '#F9FAFA'                       # APCA Lc (advisory)
```

The teal and neutral ramps in [palette architecture](palette-architecture.md) are this algorithm's output for hue 195, peak chroma 0.12 and 0.012. When the script is unavailable, browser tools work: the OKLCH picker at oklch.com, Huetone (ramp building with contrast), and Adobe Leonardo (contrast-targeted ramps).

## CSS patterns

```css
:root {
  --color-accent-default: #047879;                                  /* oklch(0.52 0.088 195) */
  --color-accent-hover: #036262;                                    /* oklch(0.45 0.076 195) */
}
@media (color-gamut: p3) {
  :root { --color-accent-default: oklch(0.52 0.11 195); }           /* more chroma where the screen can show it */
}
.hero { background: linear-gradient(135deg in oklch, oklch(0.52 0.09 195), oklch(0.45 0.12 250)); }
.tint { background: color-mix(in oklch, var(--color-accent-default) 12%, var(--color-bg-canvas)); }
```

Keep generated tints and shades in the token file rather than computing them ad hoc in components, so contrast can be linted (`tokens.py lint` in the `design-system` skill).

## Neutral ramps

- Use the same lightness targets with peak chroma 0.005-0.015 and the accent's hue (cool brands) or a warm hue around 60-90 (paper, food, hospitality, luxury).
- Pure gray (chroma 0) suits photography-led and Swiss work; everything else looks better slightly tinted.
- Warm neutrals with a cool accent (or the reverse) add depth; keep the tint chroma under 0.02 so text stays neutral.

## Gradients

- Interpolate in OKLCH to avoid the gray dead zone between complementary hues: `linear-gradient(in oklch, ...)`.
- Two neighboring hues (30-90 degrees apart) read as light; complements read as loud. The generic purple-to-pink AI gradient is 290 to 350; use it only when the brief asks for that energy.
- Never place body text on an unbounded gradient; give it a solid backing or test the worst-case area.

## Ramp checklist

- Hue, peak chroma and any hue shift recorded in the token description.
- Brand color pinned to its nearest step and documented.
- Anchors pass: step 8 vs 1 at 3:1, white on 9 at 4.5:1 (or dark text if not), step 11 on 1-3 at 4.5:1.
- All values in sRGB gamut after mapping; P3 values optional.
- Visual review: steps look evenly spaced; no muddy midtones; light steps not neon.
