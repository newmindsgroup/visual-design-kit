# Motion system and brand motion language

Version-Timestamp: 2026-10-20 01:59:37 UTC

A motion language is a small set of tokens and rules that makes every animation in a brand feel related, the way a type scale does for text. Build it from the brand's style and archetype, cap it by audience and industry, and write it down so product, marketing and video teams produce the same feel.

## Personality spectrum

Place the brand on one axis first. Most brands sit in the middle two columns.

| Parameter | Calm / precise | Balanced | Expressive | Energetic / bouncy |
| --- | --- | --- | --- | --- |
| Medium-component duration | 160-240ms | 200-320ms | 280-400ms | 240-360ms (springs feel quick, settle long) |
| Large transition | 300-400ms | 400-480ms | 480-600ms | 400-550ms |
| Default easing | `--ease-standard`, `--ease-decelerate` | Standard plus `--ease-emphasized-decelerate` for heroes | Emphasized plus easeOutExpo cubic-bezier(0.16, 1, 0.3, 1) | Springs; easeOutBack cubic-bezier(0.34, 1.56, 0.64, 1) |
| Spring bounce | 0 (ζ 1.0) | 0-0.1 | 0.1-0.2 | 0.25-0.45 |
| Overshoot | None | None | Up to 3% | 5-13% |
| Entrance travel | 4-12px | 8-24px | 16-48px | 24-64px plus scale |
| Entrance scale | 0.98 to 1 | 0.96 to 1 | 0.92 to 1 | 0.8 to 1, overshoot to 1.05-1.1 |
| Stagger per item | 20-30ms | 30-40ms | 40-60ms | 50-80ms |
| Rotation | None | None | Up to 3 degrees | 5-15 degrees |
| Squash and stretch | Never | Never | Illustrations only | Icons, characters and shapes (never text or logos) |
| Ambient loops | None | Rare | Hero only, slow | Allowed, with pause control |
| Signature moments | None | 1 | 2-3 | Many small delights, each skippable |

## Style families

Use with `python3 ../../../library/scripts/atlas.py show <id>` to read each style's own Motion section. Where this table and an atlas entry disagree, the entry wins for that style.

| Atlas style | Personality | Medium duration | Easing and technique |
| --- | --- | --- | --- |
| `style.swiss-international` | Precise | 160-240ms | `--ease-standard`; position and opacity only; text reveals line by line; 30-40ms stagger; no bounce, parallax or blur |
| `style.data-dense-utilitarian` | Precise, minimal | 100-160ms | Feedback only; re-sorts and filters at 200ms or less, or instant |
| `style.civic-plain` | Minimal | Up to 200ms | Function only; no decorative motion |
| `style.clinical-calm` | Calm | 200-300ms | `--ease-decelerate`; low amplitude; nothing flashes or pulses |
| `style.corporate-modern` | Calm to balanced | 200-280ms | Standard plus emphasized-decelerate for dialogs and sheets |
| `style.flat-material` | Balanced | 200-320ms | The contract tokens as they stand (they follow Material 3) |
| `style.quiet-minimal` | Calm, slow | 300-450ms | Opacity-led; travel 8px or less; long decelerate |
| `style.scandinavian-nordic` | Calm | 240-360ms | Standard; soft fades; natural, unhurried |
| `style.classic-luxury-serif` | Slow, graceful | 400-700ms reveals | easeOutExpo or emphasized-decelerate; long crossfades; slow image push 1.0 to 1.05 over 6-10s; no bounce |
| `style.fashion-editorial-didone` | Slow with hard cuts | 600-900ms masks | Mask and clip reveals against hard cuts on the beat |
| `style.editorial-magazine` | Balanced | 300-500ms | Line-by-line mask reveals; 80-120ms line stagger |
| `style.dark-tech-developer` | Crisp, fast | 120-200ms | Standard; terminal-style typing only where it fits; cursor blink about 1Hz |
| `style.glass-spatial` | Smooth, deep | 300-450ms | Springs with bounce 0-0.15; depth parallax; budget blur carefully |
| `style.vibrant-gradient-saas` | Expressive | 300-500ms | Emphasized; slow gradient drift (10-20s loops), paused offscreen |
| `style.playful-bubbly` | Springy | 250-400ms | Springs with bounce 0.3-0.45; squash and stretch on icons; overshoot 8-12% |
| `style.memphis-postmodern` | Energetic, jumpy | 150-300ms | Snappy steps, rotation, `steps()` easing for jumps |
| `style.y2k-cyber` | Energetic, glitchy | 80-200ms | Stepped jitter, chromatic offsets; check flash limits |
| `style.neo-brutalist` | Abrupt | 0-120ms | Hard 4px press offsets, `steps(2)` or instant swaps; no soft fades |
| `style.web-brutalist` | Raw | Instant or browser default | Little or no motion is the statement |
| `style.bold-geometric-sport` | Fast, aggressive | 150-250ms | easeOutExpo; whip pans, diagonal wipes, smash cuts |
| `style.kinetic-experimental-type` | Type-led | 400-1200ms | Variable-font axis animation, split text (see [kinetic typography](kinetic-typography.md)) |
| `style.illustrative-narrative` | Character-led | Varies | All 12 principles; Lottie or Rive (see [Lottie and Rive](lottie-and-rive.md)) |
| `style.handcrafted-organic` | Soft, imperfect | 300-500ms | "Boiling" lines at 8-12fps on twos or threes; soft eases |
| `style.art-deco` | Ceremonial | 500-800ms | Symmetrical reveals, line draws, emphasized-decelerate |
| `style.skeuomorphic-tactile` | Physical | 200-350ms | Real-world springs, press depth, material inertia |

## Archetypes

The archetype sets tempo and energy; the style sets the surface vocabulary (curve shape, technique).

| Archetype | Motion tendency |
| --- | --- |
| `archetype.sage` | Measured and precise; standard easing; motion explains |
| `archetype.ruler` | Slow, controlled, symmetrical; no bounce |
| `archetype.caregiver` | Gentle; long decelerate; 300-450ms |
| `archetype.innocent` | Light and soft; small-bounce springs |
| `archetype.everyperson` | Unpretentious; the contract defaults |
| `archetype.jester` | Bouncy springs, exaggeration, surprise |
| `archetype.creator` | Varied and crafted; kinetic type; signature moments |
| `archetype.explorer` | Spatial; camera moves and directional travel |
| `archetype.hero` | Fast and powerful; easeOutExpo; strong anticipation |
| `archetype.outlaw` | Abrupt cuts, glitch, steps; rule-breaking timing |
| `archetype.magician` | Transformations, morphs, reveals, particles |
| `archetype.lover` | Slow and sensual; long crossfades; ease-in-out |

Resolving conflicts:

1. Audience caps everything. Older adults, neurodivergent users and vestibular-sensitive users get lower amplitude and fewer loops whatever the brand. Children's products can be bouncier but must never flash.
2. Industry overrides brand inside critical flows. Payments, health results and security prompts stay calm in a jester brand too.
3. Channel sets the medium: a 30-second social ad can be far more energetic than the same brand's app.

## Motion tokens

Keep the contract names and change values only within the override ranges in [timing and easing](timing-and-easing.md). Never rename a contract token.

| Brand position | `--duration-fast` | `--duration-moderate` | `--duration-slow` | `--duration-slower` | Hero easing |
| --- | --- | --- | --- | --- | --- |
| Calm / precise | 100ms | 160ms | 240ms | 360ms | `--ease-standard` |
| Balanced (contract default) | 120ms | 200ms | 320ms | 480ms | `--ease-emphasized-decelerate` |
| Expressive or luxury | 150ms | 240ms | 400ms | 600ms | cubic-bezier(0.16, 1, 0.3, 1) |
| Energetic | 120ms | 200ms | 320ms | 480ms, with springs for gestures | easeOutBack or a `linear()` spring |

Brands often need values the base contract does not name. Add them as project extensions in the component tier and raise them with the design-system owner; do not ship them as if they were part of the contract:

- `--ease-overshoot`: cubic-bezier(0.34, 1.56, 0.64, 1)
- `--ease-spring-gentle`: the `linear()` spring in [timing and easing](timing-and-easing.md)
- `--motion-stagger`: 30ms
- `--motion-distance-sm`, `--motion-distance-md`: 8px, 24px
- `--motion-scale-enter`: 0.96

DTCG source, following the format used in `library/tokens/src/` (as of the 2025.10 DTCG format, durations are objects and cubic-bezier is a four-number array):

```json
{
  "duration": {
    "slow": { "$type": "duration", "$value": { "value": 320, "unit": "ms" } }
  },
  "easing": {
    "emphasized-decelerate": { "$type": "cubicBezier", "$value": [0.05, 0.7, 0.1, 1] }
  },
  "motion": {
    "dialog-enter": {
      "$type": "transition",
      "$value": { "duration": "{duration.slow}", "delay": { "value": 0, "unit": "ms" }, "timingFunction": "{easing.emphasized-decelerate}" }
    }
  }
}
```

Map every token to the platforms that consume it: CSS custom properties, SwiftUI `Animation` values, Compose `tween()` or `spring()`, After Effects graph-editor influence values, and Lottie or Rive source files.

## Documentation template

A motion language document has these sections, each with a recorded example clip or a specimen link:

1. **Personality:** three adjectives and one "never" ("precise, calm, confident; never bouncy").
2. **Principles:** three to five rules with a do and a don't each.
3. **Tokens:** durations, easings, springs, distances, scales, stagger, with platform mappings.
4. **Patterns:** a table, one row per pattern.
5. **Signature moments:** logo ident, first launch, success, empty state, each with its timing sheet.
6. **Choreography rules:** order, overlap, stagger caps and direction model (see [choreography](choreography.md)).
7. **Accessibility:** reduced-motion behavior per pattern, flash limits and pause controls.
8. **Specimens:** link the live specimen (start from [motion-specimen.html](motion-specimen.html)) and reference renders.
9. **Governance:** who approves a new pattern and how it gets into the tokens.

Pattern table to fill in:

| Pattern | Trigger | Properties | Duration | Easing | Reduced-motion alternative |
| --- | --- | --- | --- | --- | --- |
| Dialog enter | Open action | opacity, scale 0.96 to 1 | `--duration-slow` | `--ease-emphasized-decelerate` | 150ms opacity only |
| Dialog exit | Close, Escape, scrim click | opacity, scale to 0.98 | `--duration-moderate` | `--ease-emphasized-accelerate` | Instant |
| Toast enter | System event | translateY 16px to 0, opacity | `--duration-slow` | `--ease-decelerate` | Opacity only |
| Success | Task complete | Check draw plus icon scale 1 to 1.1 to 1 | `--duration-slower` | `--ease-standard` | Static check icon and text |
