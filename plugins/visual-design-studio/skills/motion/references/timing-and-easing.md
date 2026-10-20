# Timing and easing

Version-Timestamp: 2026-10-20 01:59:37 UTC

The values below map onto the kit's token contract (`--duration-*`, `--ease-*`). Use the tokens in code and move off them only when the brand's motion language says so (see [motion system](motion-system.md)). The [motion specimen](motion-specimen.html) shows every token side by side.

## Duration tokens

| Token | Value | Use for | Range when a brand overrides |
| --- | --- | --- | --- |
| `--duration-instant` | 0ms | Focus rings, high-frequency actions, reduced-motion fallbacks, state swaps that should not animate | 0ms |
| `--duration-fast` | 120ms | Micro feedback: hover, press, switch, checkbox, icon swap, tooltip exit | 80-150ms |
| `--duration-moderate` | 200ms | Small components: tooltip and menu enter, chips, tab indicator, snackbar exit | 150-250ms |
| `--duration-slow` | 320ms | Medium surfaces: dialogs, accordions, side sheets, toasts entering, card expand | 250-400ms |
| `--duration-slower` | 480ms | Large surfaces and page transitions: full-screen sheets, shared-element and container transforms | 400-600ms |

Above 600ms is for brand moments only (logo ident, onboarding illustration, celebration), and the user must be able to skip it. UI chrome above 500ms feels sluggish to most users.

Response-time anchors: about 0.1s feels instantaneous, about 1s keeps the flow of thought, and about 10s is the limit of attention (Jakob Nielsen, *Usability Engineering*, 1993). Feedback must begin within 100ms even when the full transition takes longer.

## Duration by interaction type

A common starting point for a phone-sized touch UI.

| Interaction | Enter | Exit | Tokens | Easing in / out |
| --- | --- | --- | --- | --- |
| Button press, hover color | 80-120ms | 80-120ms | fast | standard |
| Switch thumb, checkbox, radio | 120-200ms | 120-200ms | fast or moderate | standard |
| Tooltip (after a 300-600ms hover delay) | 150-200ms | 100-150ms | moderate / fast | decelerate / accelerate |
| Dropdown, menu, popover | 150-250ms | 100-150ms | moderate / fast | emphasized-decelerate / accelerate |
| Snackbar, toast | 200-320ms | 150-200ms | moderate or slow / moderate | decelerate / accelerate |
| Accordion, disclosure | 200-320ms | 200-250ms | moderate or slow | standard |
| Dialog, modal | 250-320ms | 150-200ms | slow / moderate | emphasized-decelerate / emphasized-accelerate |
| Bottom sheet, drawer | 300-400ms | 200-250ms | slow / moderate | emphasized-decelerate / accelerate |
| Route or page transition | 300-480ms | 200-300ms | slow or slower | standard or emphasized |
| Shared element, container transform | 400-500ms | 350-450ms | slower | emphasized-decelerate (or standard) |
| Skeleton shimmer | 1.2-2s per cycle | n/a | literal value | linear |
| Spinner rotation | 0.8-1.4s per turn | n/a | literal value | linear |

## Distance and size

Duration grows with travel distance, but much more slowly than the distance does. A common starting point:

| Travel or size | Duration |
| --- | --- |
| Up to 24px (press offsets, nudges) | 80-150ms |
| 24-120px (menus, tooltips, list reorder) | 150-250ms |
| 120-400px (dialogs, drawers, cards) | 250-400ms |
| 400px to a full viewport (sheets, page transitions) | 350-550ms |

An element that covers more than half the viewport takes `--duration-slow` or `--duration-slower` even when it travels a short way, because the area change is what the eye tracks.

## Enter and exit asymmetry

- Exits run 20-35% shorter than entrances. Legacy Material Design guidance used 225ms in and 195ms out for mobile ([Material Design, duration and easing](https://m1.material.io/motion/duration-easing.html)). The user already knows what is leaving.
- Entrances decelerate: they arrive fast and settle. Exits accelerate: they start gently and leave fast. A plain fade is an acceptable exit.
- Exits can be simpler than entrances: fade plus an 8-16px move instead of the full reverse path.
- When content swaps, the outgoing content leaves first or overlaps the incoming by at most half its duration.
- If a user interrupts an entrance, reverse from the current value; scale the exit duration by the progress already made.

## Device and screen size

| Context | Adjustment from the table above | Why |
| --- | --- | --- |
| Phone | Baseline | Short travel, touch input |
| Tablet | +20-30% for large-surface transitions | Longer travel; legacy Material suggested about 30% longer |
| Desktop with a pointer | -20-30% for UI chrome; legacy Material suggested 150-200ms for desktop transitions | Pointer users act quickly and expect immediacy |
| Watch | About -30% | Tiny travel; glanceable sessions |
| TV and 10-foot UI | Phone values, up to +20% for full-screen moves; focus movement 150-250ms | Large pixel distances but small visual angle; fast full-screen moves smear |
| Signage and OOH | Message holds dominate (see [kinetic typography](kinetic-typography.md)) | No interaction; reading time is the constraint |
| Low-end devices | Drop secondary motion before shortening primary motion | Keep the orientation cue; lose the flourish |

## Easing curves

| Token | Value | Character | Use for |
| --- | --- | --- | --- |
| `--ease-standard` | cubic-bezier(0.2, 0, 0, 1) | Quick start, long soft settle | On-screen movement, resizing, state changes |
| `--ease-decelerate` | cubic-bezier(0, 0, 0, 1) | Arrives at full speed, settles | Elements entering: menus, tooltips, toasts |
| `--ease-accelerate` | cubic-bezier(0.3, 0, 1, 1) | Gentle start, leaves fast | Elements leaving for good |
| `--ease-emphasized-decelerate` | cubic-bezier(0.05, 0.7, 0.1, 1) | Dramatic arrival, very long settle | Hero entrances: dialogs, sheets, shared elements |
| `--ease-emphasized-accelerate` | cubic-bezier(0.3, 0, 0.8, 0.15) | Holds, then exits fast | Hero exits |
| `--ease-linear` | linear | Constant rate | Opacity loops, rotation, progress, scroll-scrubbed timelines |

These follow Material 3's easing set. Material 3's full "emphasized" easing is a two-segment path that one cubic-bezier cannot express; on the web, `--ease-standard` is the usual stand-in for it.

Reference curves outside the contract: the CSS keywords as defined in CSS Easing Functions, plus the common cubic-bezier approximations of Robert Penner's easing equations (as published on easings.net):

| Name | Value | Note |
| --- | --- | --- |
| CSS `ease` | cubic-bezier(0.25, 0.1, 0.25, 1) | Browser default; do not rely on it |
| CSS `ease-in-out` | cubic-bezier(0.42, 0, 0.58, 1) | Symmetric; reads slow on UI |
| easeOutCubic (GSAP `power2.out`) | cubic-bezier(0.33, 1, 0.68, 1) | Softer alternative to decelerate |
| easeOutQuart (GSAP `power3.out`) | cubic-bezier(0.25, 1, 0.5, 1) | Editorial reveals |
| easeOutExpo (GSAP `expo.out`) | cubic-bezier(0.16, 1, 0.3, 1) | Luxury and cinematic reveals |
| easeInOutCubic (GSAP `power2.inOut`) | cubic-bezier(0.65, 0, 0.35, 1) | Camera moves, loops |
| easeOutBack | cubic-bezier(0.34, 1.56, 0.64, 1) | About 10% overshoot; playful brands only |
| easeInBack | cubic-bezier(0.36, 0, 0.66, -0.56) | Anticipation on exits |

Avoid: `ease-in` on entrances (feels sluggish), linear on spatial movement (feels robotic), and the same curve on everything.

## Springs

A spring has stiffness k (higher is faster), damping c (higher bounces less) and mass m (higher is heavier and slower). The damping ratio is ζ = c / (2√(k·m)): ζ = 1 settles without overshoot, ζ < 1 bounces, ζ > 1 creeps. Designers think in perceptual terms instead: a duration (period) T and a bounce. Convert with k = m·(2π/T)² and c = 4π·ζ·m / T. For bounce from 0 to 1, ζ ≈ 1 - bounce.

| Feel | ζ / bounce | SwiftUI | Motion (React or JS) | Physics, m = 1 | Overshoot |
| --- | --- | --- | --- | --- | --- |
| Precise | 1.0 / 0 | `.smooth` or `.spring(duration: 0.5, bounce: 0)` | `{ type: "spring", visualDuration: 0.5, bounce: 0 }` | k 158, c 25 | 0% |
| Snappy | 0.85 / 0.15 | `.snappy` (small bounce) | `{ type: "spring", visualDuration: 0.3, bounce: 0.15 }` | k 439, c 36 (T 0.3s) | under 1% |
| Gentle bounce | 0.7 / 0.3 | `.bouncy` (higher bounce) | `{ type: "spring", visualDuration: 0.5, bounce: 0.3 }` | k 158, c 18 | about 5% |
| Playful | 0.55 / 0.45 | `.spring(duration: 0.6, bounce: 0.45)` | `{ type: "spring", visualDuration: 0.6, bounce: 0.45 }` | k 110, c 12 (T 0.6s) | about 13% |

- Apple documents `.smooth`, `.snappy` and `.bouncy` qualitatively (no bounce, small bounce, higher bounce); the commonly cited values are about 0, 0.15 and 0.3. Check the exact preset in Xcode before matching another platform to it.
- Motion's documented `spring` defaults are stiffness 100, damping 10, mass 1 (ζ = 0.5, about 16% overshoot), with `bounce` 0.25 when you use duration-based options. Setting stiffness, damping or mass overrides `bounce` and `duration`. Defaults vary by property and version, so always set the transition explicitly.
- Jetpack Compose names its constants: `Spring.DampingRatioNoBouncy` 1.0, `LowBouncy` 0.75, `MediumBouncy` 0.5, `HighBouncy` 0.2; `Spring.StiffnessLow` 200, `MediumLow` 400, `Medium` 1500, `High` 10000.
- CSS has no spring primitive, but `linear()` approximates one. Gentle bounce (ζ 0.7, T 0.5s), run over 600ms:

```css
--ease-spring-gentle: linear(0, 0.089 6%, 0.282 12%, 0.496 19%, 0.688 25%, 0.837 31%, 0.94 38%, 1.003 44%, 1.035 50%, 1.046 56%, 1.044 62%, 1.036 69%, 1.026 75%, 1.017 81%, 1.009 88%, 1.004 94%, 1);
```

`--ease-spring-gentle` is a project extension, not part of the base token contract (see [motion system](motion-system.md)).

Use springs for gesture-driven, interruptible movement that should inherit velocity: drag release, swipe-to-dismiss, sheets and physical metaphors. Use bezier tokens for system-driven changes that must be coordinated on a timeline, because a spring's real settle time comes out of its physics rather than from a number you set. When you need springs inside choreography, set `visualDuration` so the spring lines up with the tokens.

## Frame rates and timing in frames

| Frame rate | One frame | Where it is used |
| --- | --- | --- |
| 23.976 / 24 | 41.7ms | Cinema and the film look; character animation "on twos" (12 drawings per second) |
| 25 | 40ms | PAL-heritage broadcast: Europe, much of Africa, Asia and Oceania |
| 29.97 / 30 | 33.3ms | NTSC-heritage broadcast (Americas, Japan, Korea); the common web and social default |
| 50 / 59.94 / 60 | 20 / 16.7ms | Sports, gaming, screen recordings of UI, high-motion social |

frames = ms × fps / 1000, rounded to whole frames:

| Token | 24fps | 25fps | 30fps | 60fps |
| --- | --- | --- | --- | --- |
| fast 120ms | 3 | 3 | 4 | 7 |
| moderate 200ms | 5 | 5 | 6 | 12 |
| slow 320ms | 8 | 8 | 10 | 19 |
| slower 480ms | 12 | 12 | 14 | 29 |

Motion-graphics starting points at 24-25fps: text in 8-15 frames, transitions 8-20 frames, whip or smash cuts 4-8 frames, logo resolve 24-48 frames, end-card hold at least 48 frames. Set the composition to the delivery frame rate from the start. Render UI demos at 60fps, because fast eases judder at 24-30fps.

## Common timing failures

- Everything at 300ms with one curve: no hierarchy. Fix: small things fast, big things slower, using the four token steps.
- Exits as long as entrances. Fix: one token step shorter on exit.
- 600ms+ dropdowns and dialogs. Fix: cap UI chrome at `--duration-slower`.
- Linear slides. Fix: decelerate in, accelerate out.
- Stagger totals over 500ms. Fix: cap them (see [choreography](choreography.md)).
