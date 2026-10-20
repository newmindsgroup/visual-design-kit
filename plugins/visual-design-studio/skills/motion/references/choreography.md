# Choreography

Version-Timestamp: 2026-10-20 01:59:37 UTC

Choreography decides what moves, in what order, from where, and what stays still. Good choreography reads as one gesture; bad choreography reads as a dozen unrelated animations. Durations and curves come from [timing and easing](timing-and-easing.md).

## Stagger

| Context | Delay per item | Cap |
| --- | --- | --- |
| 2-5 related items (menu items, form fields) | 30-50ms | Last item starts within 200ms |
| 6-12 items (list, card row) | 20-40ms | Last item starts within 300ms |
| Grid | (row + column) × 20-30ms, so it moves as a diagonal wave | Last item starts within 300-400ms |
| Long or virtualized list | Stagger only the first 6-8 visible items; the rest arrive with the last staggered item | Same as above |
| Text by line | 60-120ms | 4-6 lines |
| Text by word | 30-80ms | About 12 words, otherwise switch to lines |
| Text by character | 10-30ms | Short display words only; whole word done within 600ms |

- Stagger follows reading order: top-left to bottom-right in left-to-right scripts, mirrored for right-to-left.
- Keep the whole group entrance (first start to last end) within 500-700ms for product UI. Editorial and brand moments may run to about 1.2s.
- Stagger entrances only. Exits leave together, faster.
- Do not re-stagger content the user has already seen (filtering, re-sorting, returning to a page).

Capped stagger in CSS, with the index set inline (`style="--i: 3"`):

```css
.item {
  transition: opacity var(--duration-slow) var(--ease-decelerate),
              transform var(--duration-slow) var(--ease-decelerate);
  transition-delay: calc(min(var(--i, 0), 8) * 30ms);
}
```

## Sequencing hierarchy

Bring elements in by role, in this order:

1. **Container or surface** establishes the space (sheet, dialog, card, page background).
2. **Primary content** carries the meaning (headline, key number, hero image).
3. **Secondary content** supports it (body text, list items, metadata).
4. **Actions** (buttons, links) arrive last but must be operable immediately.
5. **Decoration and ambient motion** come last, or never.

Each tier starts when the previous one is 30-50% complete. Starting after it finishes creates a slow waterfall; starting all at once loses the hierarchy.

Dialog open, as a worked timeline (total 360ms):

| Element | Start | End | Properties | Easing |
| --- | --- | --- | --- | --- |
| Scrim | 0ms | 200ms | opacity 0 to 0.5 | `--ease-linear` |
| Panel | 0ms | 320ms | opacity 0 to 1, scale 0.96 to 1 | `--ease-emphasized-decelerate` |
| Title | 80ms | 280ms | opacity, translateY 8px to 0 | `--ease-decelerate` |
| Body | 120ms | 320ms | opacity, translateY 8px to 0 | `--ease-decelerate` |
| Actions | 160ms | 360ms | opacity | `--ease-decelerate` |

Dialog close: everything together over 200ms with `--ease-emphasized-accelerate`; the scrim fades over the same 200ms. Focus moves into the dialog at 0ms, not when the animation ends.

## Transition patterns between views

| Pattern | When | How it moves |
| --- | --- | --- |
| Shared element | The same object persists (thumbnail to detail, avatar to profile) | The object moves and scales to its new box; surrounding content crossfades |
| Container transform | A container becomes the next surface (card to page, button to sheet) | The container morphs its bounds; old content fades out over the first third, new content fades in over the last two thirds |
| Shared axis | Spatial or sequential relationship (steps, tabs, forward and back) | Both views slide 24-48px along x, y or z (scale 0.92 to 1) while crossfading |
| Fade through | Unrelated destinations (bottom-navigation tabs) | Outgoing fades out quickly, then incoming fades in and scales 0.92 to 1 |
| Fade | Elements appearing in place (menus, snackbars) | Opacity, optionally with a 4-8px move |

These names follow Material Design's motion patterns, which are public, well documented and a sensible common vocabulary.

Shared-element rules:

- Use `--duration-slower` (400-500ms) with `--ease-emphasized-decelerate` or `--ease-standard`.
- When the aspect ratio changes, animate the container's size or clip and keep the image cropped with `object-fit: cover`. Never stretch the image.
- Crossfade text instead of scaling it between very different sizes; scaled text renders blurry and its line breaks jump.
- Keep the moving element above everything else for the whole transition.
- Back navigation reverses the same path. Focus lands on the destination's heading or the originating item.
- Implementations: View Transitions API with `view-transition-name` (web), FLIP, Motion `layoutId` (React), SwiftUI `matchedGeometryEffect` or the zoom navigation transition (iOS 18+), Compose `SharedTransitionLayout`. Code is in [web implementation](web-implementation.md).

## Transform origin

| Element | Origin | Starting scale or offset |
| --- | --- | --- |
| Menu, popover, select | The edge or corner attached to the trigger | Scale 0.95-0.98 plus opacity |
| Dialog | Center | Scale 0.95-0.98 (never from 0) |
| Tooltip | The side nearest the target | Translate 4-8px toward the target plus opacity |
| Sheet, drawer | The edge it is attached to | Translate 100% from that edge |
| Expanding card | The card's own position (measure it with FLIP) | Its real start bounds |
| Toggle, checkbox, radio | Center | n/a |
| Notification | The corner or edge where notifications live | Translate 16-24px plus opacity |

- Scaling from 0 looks like a slingshot zoom and makes text unreadable mid-flight. Start entrances at 0.9-0.98.
- Positioning libraries (Floating UI, Radix, Headless UI) expose the resolved placement; set `transform-origin` from it so a menu that flips above its trigger also flips its origin.
- In right-to-left layouts, mirror horizontal origins and slide directions.

## Follow-through and overlap

- Children trail their parent by 20-60ms.
- A medium-personality settle carries 2-5% overshoot in the last 10-20% of the move. Calm brands carry none.
- The next step of a sequence starts at 30-50% of the previous step.
- In code: Motion `transition={{ staggerChildren: 0.03, delayChildren: 0.05 }}`; GSAP timeline position parameters such as `"<0.08"` (80ms after the previous tween starts) or `"-=0.15"` (150ms before the timeline's current end).
- In After Effects: offset layers 2-4 frames, or link them with `valueAtTime(time - delay)` (see [video and motion graphics](video-and-motion-graphics.md)).

## Directional logic

- Pick one spatial model and keep it product-wide. Going forward in a flow, new content enters from the end edge (the right in left-to-right scripts) and old content exits toward the start edge; back reverses it; going deeper in a hierarchy moves along z (scale up and fade in).
- Sheets come from the bottom on phones and from the side on large screens; notifications come from where they are anchored.
- A direction carries meaning. Do not slide an item left on delete in one place and right in another.

## Avoiding motion overload

- One focal motion per moment. At most 2-3 elements in motion at once in product UI.
- At most one ambient loop per viewport. Pause it offscreen, and give it a pause control if it runs more than 5 seconds (WCAG 2.2 SC 2.2.2).
- Do not reveal every scroll section. Reveal only content whose arrival means something, and only once.
- Any animation a user sees 100 or more times a day is 150ms or less, or none.
- No auto-advancing carousels in product UI. In marketing, auto-advance at most every 5-7 seconds, pause on hover and focus, and provide a pause control.
- Overload test: screen-record 10 seconds of normal use. If more than three things move at any one instant, cut until they do not.
