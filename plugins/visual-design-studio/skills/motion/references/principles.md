# Principles of motion

Version-Timestamp: 2026-10-20 01:59:37 UTC

Frank Thomas and Ollie Johnston set out 12 principles of animation in *The Illusion of Life: Disney Animation* (1981). They were written for character animation. Most of them carry over to interfaces and motion graphics if you read "character" as "element" and "emotion" as "meaning". Use them to diagnose why a motion feels wrong, not as a checklist to apply all at once.

## Purposes of motion

Every animation must serve one of these jobs. If you cannot name the job, remove the animation.

| Purpose | Job | Typical examples | Default budget |
| --- | --- | --- | --- |
| Feedback | Confirm the system received the input and what changed | Press states, toggles, validation, saved/sent confirmation, drag pickup | Starts within 100ms of input; 80-200ms total |
| Orientation and continuity | Show where something came from, where it went and how screens relate | Drawers sliding from their edge, shared-element transitions, list reorder, breadcrumbs collapsing | 200-500ms |
| Focus | Pull the eye to the one thing that changed or needs action | New-item highlight, error shake, badge increment, one hero reveal | One focal motion at a time; under 1s; loops over 5s need a pause control |
| Expression | Carry brand personality and reward | Logo ident, onboarding illustration, success celebration, branded loader | Only where it never delays a task; skippable; 0.6-3s |

Explanation (showing how a feature works, animating a data change) is orientation applied to content. Treat it with the same budget and make the final state readable without the animation.

## The 12 principles, translated

### 1. Squash and stretch

- **Original:** deformation shows mass and flexibility; volume stays constant (stretch 20% on one axis, squash about 17% on the other).
- **UI:** a press scale of 0.96-0.98 is the restrained form. Playful brands can stretch a switch thumb 20-30% along its travel at mid-move.
- **Motion graphics:** bouncing shapes, liquid blobs, characters landing.
- **Example:** a 20px switch thumb widens to 26px at the midpoint of a 200ms travel and returns to 20px on arrival. Never deform text, logos, product photography or chart marks.

### 2. Anticipation

- **Original:** a small opposite move prepares the audience for the main action.
- **UI:** skip it for user-initiated actions, because it adds latency. Use it for system-initiated or attention moments, such as a pull-to-refresh that stretches under tension or a card that dips 2% before it flips.
- **Motion graphics:** a logo pulls back 4-8 frames (at 24fps) before it resolves; a camera eases back before a push-in.
- **Example:** exit-only back-in curve `cubic-bezier(0.36, 0, 0.66, -0.56)` on a dismissed card, 240ms.

### 3. Staging

- **Original:** present one idea at a time with a clear silhouette and composition.
- **UI:** one focal motion per moment. When a dialog opens, the scrim fades and everything behind it stays still.
- **Motion graphics:** clear the frame before a key line lands; hold on the product before the end card.
- **Example:** dialog open: scrim opacity 0 to 0.5 over 200ms; panel scale 0.96 to 1 plus opacity over 320ms with `--ease-emphasized-decelerate`; nothing else moves.

### 4. Straight ahead and pose to pose

- **Original:** straight ahead draws frame by frame (fluid, less predictable); pose to pose sets key poses and fills the in-betweens (controlled).
- **UI:** almost everything is pose to pose: define start and end states and let interpolation fill. The straight-ahead equivalents are physics, particles, procedural noise and springs driven by gesture velocity.
- **Motion graphics:** block key poses first, refine timing, then polish. Simulate smoke, fire and confetti instead of keying them.
- **Example:** a toast spec is two states, `translateY(100%) opacity 0` to `translateY(0) opacity 1`. A confetti burst is a particle system with gravity and drag, capped at 1.5s.

### 5. Follow through and overlapping action

- **Original:** parts of a body stop at different times; loose parts keep moving after the body stops.
- **UI:** children trail their container by 20-60ms; a card's content settles slightly after the card; a spring with 2-5% overshoot gives natural follow-through.
- **Motion graphics:** offset related layers by 2-4 frames; drive a delay with `valueAtTime(time - delay)` (see [video and motion graphics](video-and-motion-graphics.md)).
- **Example:** a drawer slides in over 320ms; its list items begin 60ms later with a 30ms stagger.

### 6. Slow in and slow out

- **Original:** objects accelerate from rest and decelerate into rest.
- **UI:** spatial movement is never linear. Elements entering use decelerate, elements leaving use accelerate, and elements moving within the screen use standard. Linear is correct only for opacity loops, rotation, progress and scroll-linked scrubbing.
- **Motion graphics:** use the graph editor; ease-out on arrivals is the default, and ease-in into a cut adds speed.
- **Example:** `--ease-decelerate` cubic-bezier(0, 0, 0, 1) on a menu entering, `--ease-accelerate` cubic-bezier(0.3, 0, 1, 1) on its exit. Values in [timing and easing](timing-and-easing.md).

### 7. Arcs

- **Original:** natural movement travels on arcs, not straight lines.
- **UI:** an element crossing a large diagonal distance looks mechanical on a straight path. Give x and y different easings, or use `offset-path`.
- **Motion graphics:** curve the motion-path handles and enable auto-orient for objects that should face their direction of travel.
- **Example:** a floating button expanding into a sheet: x uses `--ease-standard`, y uses `--ease-emphasized-decelerate`, and the path bows naturally.

### 8. Secondary action

- **Original:** a supporting action reinforces the main one without competing.
- **UI:** a checkmark draws after a button confirms; a cart badge bumps after "Add to cart"; a shadow grows as a card lifts.
- **Motion graphics:** background particles drift while the hero type lands, at 30-50% of the primary amplitude.
- **Example:** the button confirms over 200ms; 100ms later the cart badge scales 1 to 1.2 to 1 over 240ms.

### 9. Timing

- **Original:** the number of frames gives weight, mood and meaning.
- **UI:** small and frequent is fast, large and rare is slower. Use the duration tokens (120, 200, 320, 480ms), not arbitrary values.
- **Motion graphics:** at 24fps, 6 frames reads snappy, 12 normal and 24 weighty.
- **Example:** a toggle at 120ms and a full-screen sheet at 480ms in the same product feel coherent. The same 300ms on both feels wrong for each.

### 10. Exaggeration

- **Original:** push past realism so the idea reads clearly.
- **UI:** use sparingly and only at focus moments, such as an error shake or a success pulse. Calm brands exaggerate through contrast of timing, not through bounce.
- **Motion graphics:** overshoot a logo to 108-112% scale before it settles to 100%.
- **Example:** an invalid field shakes `translateX` 0, -8, 8, -6, 6, -3, 0px over 360ms, together with error text. The shake is never the only signal.

### 11. Solid drawing

- **Original:** forms have volume, weight and consistent perspective.
- **UI:** keep one light source and an elevation scale; a lift changes the shadow as well as the position; 3D flips share one perspective (800-1200px).
- **Motion graphics:** keep camera, depth of field and parallax ratios consistent across the piece.
- **Example:** card hover is `translateY(-2px)` plus a shadow change from `--shadow-sm` to `--shadow-md`. Never lift without a shadow change.

### 12. Appeal

- **Original:** characters need charisma and readable, pleasing design.
- **UI:** appeal comes from restraint, consistent curves and one or two signature moves used deliberately.
- **Motion graphics:** shape design, rhythm and cutting to music.
- **Example:** reserve a single 480ms `--ease-emphasized-decelerate` "unfold" for brand moments (first launch, plan upgraded) and reuse it everywhere those moments occur.

## When not to animate

- **High-frequency actions:** typing, keyboard shortcuts, command palettes, list scrolling and menus opened dozens of times a day. Use 0-100ms or nothing.
- **When it blocks the task:** input must work during a transition. Never make a user wait for an animation before they can act; every animation must be interruptible.
- **Exact values:** do not count a bank balance up from zero or tween a chart through values that never existed. Show the real value, then animate emphasis.
- **Text being read:** do not move or reflow text while someone reads it.
- **Stressful flows:** fraud alerts, medical results and payment failures get calm, minimal motion regardless of brand energy.
- **Reduced-motion users:** replace spatial movement with a short crossfade or an instant change (see [web implementation](web-implementation.md)).
- **Vestibular triggers:** large zooms, parallax with big speed differences, spinning and full-screen slides are the worst offenders. Cap them or offer an alternative.

## Motion AI tells

- Every section fades up 24-40px on scroll with the same 600ms ease. Fix: animate only content that benefits, once, and use the hierarchy in [choreography](choreography.md).
- Hover `scale(1.05)` plus shadow on every card. Fix: one hover language per component type, with the lift no more than 2-4px.
- Infinite gradient blobs or shimmer behind the hero. Fix: one ambient loop at most, slow (10-20s), paused offscreen and pausable.
- Typewriter headline on a marketing hero. Fix: show the headline immediately; save typing for terminal or narrative contexts.
- Bouncy springs on enterprise tables and forms. Fix: match personality to style and audience (see [motion system](motion-system.md)).
