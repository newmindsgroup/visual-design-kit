# Effect recipes by communication purpose

Version-Timestamp: 2026-09-08 20:15:10 AST

Every row has status: authored-unverified. These are recipe definitions, not snippets or tested implementations. Each selected row inherits the full [motion specification](../../../templates/motion-spec.md), including timing, interruption, keyboard/touch, reduced/static/no-JS fallback and measured budget fields. Mark nonapplicable fields with a reason. No row can be promoted to tested without its actual implementation/version and evidence.

| ID / recipe | Use and structure | Critical variable/check | Complete fallback | Status |
| --- | --- | --- | --- | --- |
| M01 Threshold reveal | Introduce a section on entry | Trigger boundary, initial state and once/replay; content must survive failed initialization | Content already visible | authored-unverified |
| M02 Staggered group | Explain order within related items | Total group delay, stable reading order; focused item immediately available | All items visible together | authored-unverified |
| M03 Reading progress | Show position in an article | Correct container/range after resize and font load; not fake task completion | Article and headings remain sufficient | authored-unverified |
| M04 Sticky narrative | Keep explanation beside changing scenes | Entry/exit, pin height, focus and small-screen layout | Sequential unpinned content | authored-unverified |
| M05 Parallax depth | Support a spatial narrative | Limited travel, crop boundaries, vestibular impact; reject when purely distracting | Fixed composition | authored-unverified |
| M06 Scroll-scrubbed sequence | Explain measured stages or object change | Scroll-to-frame mapping, reverse, loading and factual continuity | Ordered stills and captions | authored-unverified |
| M07 Section snap | Deliberate full-section navigation when justified | Escape, native input, zoom and variable-height content; never trap reading | Normal scrolling | authored-unverified |
| M08 Shared-element transition | Preserve identity across views | Stable correspondence, cancellation, history and focus destination | Immediate route/state change | authored-unverified |
| M09 Expand/collapse | Show a relationship and reveal detail | Size/content changes, ARIA state, focus and interrupted toggles | Immediate accessible expansion | authored-unverified |
| M10 State feedback | Confirm pending/success/error | Accurate state timing and nonvisual equivalent; never animate false progress | Text/icon/state change | authored-unverified |
| M11 Text or mask reveal | Introduce a short title with intention | Reading order, selectable text and clip bounds | Complete readable title | authored-unverified |
| M12 SVG path draw | Explain construction, route or connection | Meaningful direction and consistent stroke speed; accessible description | Finished labeled path | authored-unverified |
| M13 Shape morph | Explain relation between two forms | Compatible geometry, intermediate meaning and brand invariants | Two labeled states | authored-unverified |
| M14 Kinetic typography | Emphasize scripted speech or words | Phrase-level timing, legibility, no false emphasis | Full text/captions plus static frame | authored-unverified |
| M15 Logo ident | Establish brand at a chosen moment | Clear space, undistorted final mark and hold time | Approved static logo | authored-unverified |
| M16 Lower third/callout | Identify speaker, object or fact | Safe areas, duration, source truth, captions collision | Persistent readable label | authored-unverified |
| M17 Data transition | Explain change in a dataset | Stable scale, exact endpoints and truthful interpolation | Final values plus comparison/table | authored-unverified |
| M18 Looping scene | Atmospheric or explanatory repeat | Seam, dwell/reading time, pause controls where required | Poster with complete information | authored-unverified |
| M19 Hover/focus response | Clarify an actionable element | Equivalent focus/touch meaning, no layout jump | Visible affordance and focus ring | authored-unverified |
| M20 Cursor/tilt response | Optional spatial play where appropriate | Fine-pointer gating; no essential hover-only content or replaced cursor | Normal pointer and stable surface | authored-unverified |

Do not stack several recipes on the same element without defining which owns each property and how the timelines combine. Plan relationship and hierarchy before choreography. Use already-vetted libraries if needed; inspecting documentation does not authorize installation or prove license suitability.

Implementation research: [MDN scroll animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations), [W3C scroll animation draft](https://www.w3.org/TR/scroll-animations-1/) and [GSAP media-query lifecycle](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/). The W3C draft is not a browser support guarantee; verify the exact target. GSAP is an optional provider, not a dependency of these authored recipes.

For any automatically starting variant that lasts more than five seconds and runs alongside other content, apply the pause/stop/hide requirement unless an applicable exception is established. Scroll-driven response is not automatically the same as auto-starting playback. Inspect the actual trigger for M05/M06; M14/M18 autoplay variants need the explicit check. Record tested status, implementation version, evidence and coverage in the selected project motion specification. This generic catalog remains authored-unverified unless a linked reusable implementation and receipt are added.
