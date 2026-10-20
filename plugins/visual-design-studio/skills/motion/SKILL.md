---
name: motion
description: >-
  Designs and specifies motion for interfaces, websites, brands, video and displays: purpose, the 12 animation principles, duration and easing tokens, springs, choreography, brand motion language, kinetic type, CSS, View Transitions, GSAP, Motion, Lottie, Rive, After Effects, Remotion, export specs, captions, loudness and UI sound, with reduced-motion and flash safety. Use when animating UI, choosing durations or easing, building a motion system, making an ident, social or explainer video, kinetic type, Lottie or Rive assets, or sound.
license: MIT
metadata:
  version-timestamp: "2026-10-20 01:59:37 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 01:59:37 UTC"
---

# Motion

Excellent motion is felt more than seen: every movement has a job (feedback, orientation, focus or expression), uses the brand's small set of durations and curves, never blocks the user, and degrades gracefully to stillness. Spectacle is reserved for the few moments that earn it.

## Defaults

| Decision | Default | Move off it when |
| --- | --- | --- |
| Purpose | Every animation names its job: feedback, orientation, focus or expression | No job: cut it |
| Durations | `--duration-fast` 120ms (micro), `--duration-moderate` 200ms (small), `--duration-slow` 320ms (medium), `--duration-slower` 480ms (large surfaces, pages) | Calm brands 20-25% shorter; luxury and expressive brands up to 25% longer |
| UI ceiling | Chrome at 480ms or less; brand moments up to 3s and skippable | Never for repeated actions |
| Easing | Enter `--ease-decelerate` or `--ease-emphasized-decelerate`; exit `--ease-accelerate`; move `--ease-standard`; `--ease-linear` only for opacity loops, progress and scroll scrubbing | Brand language adds overshoot or springs |
| Enter and exit | Exit 20-35% shorter than enter (one token step) | Exit and re-enter loops that must match |
| Latency | Feedback starts within 100ms of input; input is never blocked by animation | None |
| Properties | `transform` and `opacity`; never `transition: all` | Color and filter for small elements, after measuring |
| Stagger | 20-50ms per item; the last item starts within 300ms; entrances only | Editorial moments up to about 1.2s total |
| Springs | For gestures and interruptible movement; bounce 0 (calm) to 0.3 (playful), set explicitly | Coordinated timelines use bezier tokens |
| Reduced motion | Tokens drop to 0.01ms automatically; replace spatial movement with an opacity fade of 200ms or less, or an instant change | Essential motion (a video the user started) |
| Loops and flashes | Anything auto-moving for more than 5s gets pause, stop or hide (WCAG 2.2.2); no more than 3 flashes per second (2.3.1) | None |
| On-screen text | Hold for 1s + words ÷ 3 seconds, at least 1.5-2s, once fully legible | Add 50% for numbers, legal text and second-language audiences |
| Video delivery | Source frame rate; ProRes 422 HQ master; H.264 1080p at 8-12 Mbps; streaming and social loudness about -14 LUFS, EBU R128 -23 LUFS, ATSC A/85 -24 LKFS | The platform or broadcaster spec sheet |
| Sound | Off by default on the web; never the only carrier of information; UI sounds 50-300ms | Games, music products and kiosks with an agreed brief |

## Workflow

1. **Read the brief for motion variables:** medium (product UI, website, video, display), audience, style, archetype, industry, channel and platform. Run the atlas query below and read the Motion section of each selected style.
2. **Set the personality:** place the brand on the calm-to-energetic spectrum and fix the token values ([motion system](references/motion-system.md)).
3. **List the moments:** every state change, transition and brand moment, with its purpose ([principles](references/principles.md)). Cut anything without a purpose, and anything a user sees 100+ times a day that is not 150ms or less.
4. **Specify each moment:** trigger, properties, duration token, easing token, choreography, interruption behavior and reduced-motion alternative ([timing and easing](references/timing-and-easing.md), [choreography](references/choreography.md)). Use the [motion specification template](../../library/templates/motion-spec.md) for client work.
5. **Choose the medium and engine:** CSS, WAAPI, View Transitions, GSAP or Motion ([web implementation](references/web-implementation.md)); Lottie or Rive ([Lottie and Rive](references/lottie-and-rive.md)); After Effects or Remotion ([video and motion graphics](references/video-and-motion-graphics.md)).
6. **Build the riskiest moment first:** the page transition, the hero ident or the most-used interaction, wired to tokens.
7. **Render and inspect:** play at 1x and at 0.25x, and screen-record at 60fps to step through frames. Check reduced motion, a phone, keyboard use and interruption (click twice quickly). For video, watch full playback on the target player, check loop seams three times, run a flash check, meter loudness and check caption timing and safe areas.
8. **Measure:** frame timing in DevTools at 4x CPU throttle, INP and CLS, transferred bytes for Lottie, Rive and video.
9. **Document and hand off:** the pattern table and token mapping ([motion system](references/motion-system.md)), the Lottie and Rive handoff checklists, and export specs. Compare against the [motion specimen](references/motion-specimen.html).

## Decisions that change the answer

Motion personality depends on style and archetype first, then audience, industry and channel:

```sh
python3 ../../library/scripts/atlas.py query "luxury skincare calm sensual"
python3 ../../library/scripts/atlas.py show style.classic-luxury-serif
python3 ../../library/scripts/atlas.py combine style.playful-bubbly archetype.jester audience.older-adults
```

- **Style:** `style.swiss-international` is precise (160-240ms, standard easing, no bounce); `style.playful-bubbly` is springy (bounce 0.3-0.45, squash and stretch on icons); `style.classic-luxury-serif` is slow (400-700ms reveals, expo-out, long crossfades); `style.neo-brutalist` is abrupt (instant swaps, hard offsets). The full table is in [motion system](references/motion-system.md).
- **Archetype:** sets tempo and energy (`archetype.ruler` controlled, `archetype.hero` fast and forceful, `archetype.jester` bouncy, `archetype.caregiver` gentle).
- **Audience:** caps amplitude. `audience.older-adults`, `audience.neurodivergent` and `audience.disability-accessibility-first` get lower amplitude, fewer loops and an in-app motion setting. `audience.children-under-13` can be bouncier but must never flash.
- **Industry and flow:** money, health and security flows stay calm whatever the brand energy.
- **Channel:** `channel.web-app` and `channel.native-app` are dominated by feedback and orientation; `channel.marketing-website` adds expression; `channel.video-motion` and `channel.social-media` add kinetic type, holds, safe areas, captions and loudness; `channel.ooh-signage` runs on hold times and silent comprehension.
- **Platform:** desktop runs 20-30% faster than phone and tablet slower; iOS favors springs; Android follows Material 3 tokens.
- **Market:** mirror direction for right-to-left scripts; 25fps in PAL-heritage regions and 30fps in NTSC-heritage regions; broadcast loudness follows EBU R128 or ATSC A/85.
- **Tier:** luxury slows down and removes bounce; value tiers favor fast, functional motion.

## Common failures

- Same 300ms ease on everything, so nothing has hierarchy. Use the four duration steps and pick the curve by enter, exit or move.
- Every section fades up on scroll. Reveal only meaningful content, once, in hierarchy order.
- Animations that block input or cannot be interrupted. Accept input immediately and reverse from the current value.
- Reduced motion handled by deleting all feedback. Replace movement with a short fade or an instant state change.
- Bounce on enterprise tables and payment flows. Match personality to style and flow criticality.
- Animating `width`, `top` or `box-shadow` and dropping frames. Use transforms, opacity and FLIP.
- Kinetic text that never holds still. Hold the complete line for at least 1s + words ÷ 3.
- Lottie files with embedded rasters and unsupported effects. Check the support matrix and the size budget before animating.
- Video mastered loud and clipped, or captions colliding with platform UI. Meter to the destination target and design inside the safe zone.
- Sound used as the only signal. Pair every sound with a visual and, where possible, a haptic.

## References

- [Principles](references/principles.md): purposes of motion, the 12 principles in UI and motion graphics, when not to animate.
- [Timing and easing](references/timing-and-easing.md): duration tables, easing curves, springs, frame rates and frame counts.
- [Choreography](references/choreography.md): stagger, sequencing, shared elements, transform origin, overload rules.
- [Motion system](references/motion-system.md): personality spectrum, atlas style and archetype mapping, tokens, documentation template.
- [Kinetic typography](references/kinetic-typography.md): hold times, techniques, legibility, captions, WCAG 2.2.2, 2.3.1 and 2.3.3.
- [Web implementation](references/web-implementation.md): CSS, WAAPI, View Transitions, scroll-driven animation, GSAP (license verified 2026), Motion, performance, reduced motion.
- [Lottie and Rive](references/lottie-and-rive.md): export, feature support, dotLottie, players, state machines, data binding, choosing a medium, handoff checklists.
- [Video and motion graphics](references/video-and-motion-graphics.md): After Effects rigs and expressions, MOGRT, Remotion, export specs, safe areas, loudness.
- [Sound](references/sound.md): UI sound, sonic branding, levels, accessibility.
- [Motion specimen](references/motion-specimen.html): live comparison of every duration and easing token.
- Working code: [website motion library](../../library/MOTION-LIBRARY.md), [motion and media recipes](../../library/MOTION-RECIPES.md), [Astro motion playground](../../library/examples/astro-motion/README.md), [screen content and motion method card](../../library/knowledge/screen-content-and-motion.md).
- Deep process for client projects: [motion effects](../../library/draft-skills/design-motion-effects/SKILL.md), [web motion library](../../library/draft-skills/design-web-motion-library/SKILL.md), [screen animation](../../library/draft-skills/design-screen-animation/SKILL.md), [kinetic type](../../library/draft-skills/design-screen-kinetic-type/SKILL.md), [screen video](../../library/draft-skills/design-screen-video/SKILL.md), [loops](../../library/draft-skills/design-screen-loops/SKILL.md), [audio and captions](../../library/draft-skills/design-screen-audio-captions/SKILL.md), [storyboards](../../library/draft-skills/design-screen-storyboard/SKILL.md), [still to motion](../../library/draft-skills/design-screen-still-motion/SKILL.md), [screen effects](../../library/draft-skills/design-screen-effects/SKILL.md).

Catalog IDs covered: motion, web-motion-library, screen-animation, screen-kinetic-type, screen-video, screen-loops, screen-audio-captions, screen-storyboard, screen-still-motion, screen-effects
