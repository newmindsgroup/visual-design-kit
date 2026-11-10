# Prompts for AI site builders

Version-Timestamp: 2026-11-10 03:00:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

When a client wants a prompt to paste into Lovable, Bolt, v0, Cursor, Manus, Google AI Studio or Kimi, the [landing spec](landing-spec-template.md) is the deliverable. Write it from the approved direction and tokens, never from scratch: imperative, exact, ordered. Then adapt the opening and the delivery for the tool. This is the website case of `design-director`'s [prompt handoff](../../design-director/references/handoff.md#4-prompts-for-generators-and-build-tools); when the `prompt-engineering-expert` plugin is installed, hand it the spec and the target tool for the gap scan and scoring.

## Per-tool adaptation

Builders change their default stacks and conventions often. Every row is "verify": check the tool's current documentation or a fresh project before relying on it (as of November 2026).

| Tool | Stack line to open with | Notes (verify) |
| --- | --- | --- |
| Lovable | "React + Vite + TypeScript + Tailwind CSS + shadcn/ui; `motion` (motion/react) for animation; lucide-react for icons." | Put the tokens as HSL CSS variables in `index.css`, which is the convention its starter uses. Ask for the hero in one message; for long pages, "build the hero and the next two sections now", then continue. |
| Bolt | "Vite + React + TypeScript + Tailwind CSS + motion, single page, no backend." | Follows numbered structure closely: keep sections numbered and the tokens in one block. Ask for one component per file. |
| v0 | "Next.js App Router + Tailwind CSS + shadcn/ui; motion for animation." | Conservative with motion unless asked: spell out every animation with trigger, duration, easing and reduced-motion state. |
| Cursor or Claude Code | The project's existing stack, or "a single index.html, no build step". | Can follow very long specs; include the file structure and the token file path. Prefer running the kit's own [cinematic workflow](cinematic-landing.md) when the agent has this plugin. |
| Manus, Kimi, Google AI Studio | "Build a single standalone index.html (inline CSS and JS, no build step)." | Agentic builders do best with one self-contained file and every asset path spelled out. |

## Rules for any builder

1. **Exact media paths.** Give every asset's real URL or file name, what it is for, how it is positioned and its poster. Builders invent stock media when you are vague. Never paste a URL you have not checked, and never one you lack rights to.
2. **Exact copy.** Spell out every headline, nav label, CTA and proof line. Left alone, builders write "Unlock your potential".
3. **Numbers, not adjectives:** sizes per breakpoint as `clamp()`, tracking, durations, easing curves, opacities, radii, from the tokens.
4. **Tokens first, in one block.** Paste the brand's semantic tokens (from `dist/tokens.css` or `dist/tailwind.css`) with their names, so the builder uses `--color-accent-default`, not a guessed hex.
5. **Accessibility as requirements, not wishes:** one `h1`; landmarks; visible focus with the focus-ring token; 44 px touch targets; alt text; `prefers-reduced-motion` alternatives for every animation; a pause control for anything moving longer than 5 seconds; no text under 4.5:1.
6. **Pin library versions** you name (`motion@14.4.0`, `gsap@3.15.0`, `three@0.170.0`), and say "do not add other animation libraries".
7. **Constraints last:** finish with "Do not" lines, for example "No extra sections, no decorative blobs, no purple gradients, no placeholder images, no emoji icons, no invented statistics or testimonials." Builders weigh what comes last.
8. **Length:** 3,000-15,000 characters is normal for a gallery-grade hero. Do not trim precision to save space.
9. **When the result drifts:** send one focused fix per message ("make the H1 clamp(3.5rem, 2rem + 6vw, 7.5rem) with -0.04em tracking"), not a long list.
10. **Name the component libraries** the builder should install ("shadcn/ui for base components, Sonner for toasts, NumberFlow for the price") and say "do not hand-build toasts, drawers or command menus"; then restyle per `ui-design`'s [component libraries](../../ui-design/references/component-libraries.md). Reference screens and the job of the page come from `design-director`'s [prompt handoff](../../design-director/references/handoff.md#4-prompts-for-generators-and-build-tools).
11. **Check the output, not the prompt.** Render what comes back with `design-critique` (`render_review.mjs --early 350` on the preview URL) and score it against the same direction. When a defect repeats, fix the prompt.

## Prompt skeleton

```text
ROLE AND STACK
<stack line for the tool>. Build exactly what follows; add nothing that is not listed.

BRIEF
<brand>, <what it is, for whom>. Direction "<name>": <mood in three words>. Signature: <the one idea>.

TOKENS (use these names)
<paste the semantic tokens and the font link>

COMPONENTS
<libraries by name, e.g. shadcn/ui, Sonner; which one section may carry a showpiece>

LAYOUT AND CONTENT
1. Navigation: ...
2. Hero: ... (H1 copy, sizes, tracking, color token, motion with reduced-motion state)
3. <Section>: ...

MEDIA
<slot>: <url or file>, <element and attributes>, <object-position>, <poster>, <behavior>

MOTION
<table rows: element, trigger, delay, duration, easing, from-to, reduced motion>; pause control bottom right for loops.

ACCESSIBILITY AND PERFORMANCE
<the rule 5 list>; LCP element is <poster | h1>; no layout shift; works at 390 px with no horizontal scroll.

DO NOT
<the constraint list>
```

## Record the handoff

Store the final prompt, the tool and its version or date, the model if shown, the approved direction it came from and who approved the result, as the `imagery` provenance default and `design-director`'s handoff step 4 require.
