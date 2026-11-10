# From chosen direction to production

Version-Timestamp: 2026-11-10 03:20:00 UTC

Once a direction is chosen, lock it into tokens and route each deliverable to the skill that owns it. Keep the decision traceable.

## 1. Record the decision

Write a short decision note in the project: chosen direction, runner-up, scores and weights, what the client said, open risks. For client projects that keep formal records (approvals, pins, resume), load the `design-project-start` skill and use its decision and resume records instead of inventing a new format.

## 2. Turn the direction into tokens

1. Copy `../../../library/tokens/src/` into the project (for example `design/tokens/`).
2. Create `brands/<brand>.tokens.json` with the direction's accent and neutral ramps (generate them with `python3 ../../../library/scripts/color_tools.py ramp --hue <H> --chroma <C> --name <name>`) and font families, the only brandable groups. Set radius and motion personality in the project copy of `primitives.tokens.json` (or `components.tokens.json`).
3. Build and lint with the project copy of `tokens.py` (`build`, then `lint`). Lint enforces the contrast guarantees in every mode; fix failures by adjusting ramp steps, never by suppressing the check.
4. Use `dist/tokens.css` (or `dist/tailwind.css`) in code and `dist/figma-variables.json` for Figma variables.

See the `design-system` skill for token architecture, theming and Figma.

## 3. Route deliverables

| Deliverable | Skill | First output |
| --- | --- | --- |
| Logo, identity, guidelines | `brand-identity` | Logo territories refined into a mark with construction and variants; brand book per [brand book production](../../brand-identity/references/brand-book-production.md); file set per [identity deliverables](../../brand-identity/references/identity-deliverables.md) |
| Type system | `typography` | Scale, pairings, specimens in the target media |
| Color system | `color` | Ramps, semantic roles, dark mode, contrast table |
| Grids and composition | `layout` | Grid specs per breakpoint or format |
| UI icon family or app icon | `icon-design` | Semantic registry, optical variants, editable source and appearance contact sheet |
| Illustration, photo, AI imagery | `imagery` | Shot list or illustration rules |
| Motion language and video | `motion` | Motion tokens and 3-5 signature moments; finished video and Lottie per the [production pipeline](../../motion/references/production-pipeline.md) |
| Research, IA, flows | `ux-design` | Flows and IA validated with users when possible |
| Screens and components | `ui-design` | State-complete components and key screens |
| Website | `web-design` | Page architecture, responsive layouts, performance budget |
| Cinematic landing page or hero (media-led launch, campaign or showpiece) | `web-design` | A [landing spec](../../web-design/references/landing-spec-template.md) with one signature idea and real values, built and looked at per the [cinematic landing workflow](../../web-design/references/cinematic-landing.md); scored with the [cinematic addendum](../../design-critique/references/cinematic-addendum.md) |
| macOS/iOS/Android app | `native-app-design` | Platform-correct screens and handoff |
| Reference app or site reconstruction | `reference-reconstruction` | Observed screens, states, measurements and matched-condition comparisons |
| Design system | `design-system` | Token build, component API, documentation |
| Charts and infographics | `data-visualization` | Chart choices and data palette |
| Print, packaging, social, decks, email, sales and marketing collateral | `print-packaging-social` | Finished files: print master PDF plus a Canva editable twin ([pipeline](../../print-packaging-social/references/print-production-pipeline.md), [Canva handoff](../../print-packaging-social/references/canva-handoff.md)); decks from the [PPTX example](../../../library/examples/deck-pptx/README.md) |
| Any third-party icon, font, music or sound | (all) | A provenance record per [asset licenses](../../../library/knowledge/ASSETS-LICENSES.md) |
| Review | `design-critique` | Rubric scores and prioritized fixes |

## 4. Prompts for generators and build tools

When a deliverable is produced by another AI tool (image generators, video generators, v0, Lovable, Figma Make, another agent), write its prompt from the chosen recipe, never from scratch:

1. **Source of truth:** the recipe and tokens. Name the typefaces, hex palette with proportions, layout logic, imagery style, motion personality, voice and the clichés to avoid. Add the channel's specs (aspect ratio, safe areas, sizes).
   For a build agent (Claude Code, Codex, Cursor or a site builder), also brief:
   - **References, not adjectives:** the [reference-first](reference-first.md) table (product, pattern, why it works for this user). Delete "modern", "clean" and "premium" unless a reference shows what they mean.
   - **The job and the user before the screen:** who opens it, when, and what must be obvious ("the first screen a warehouse lead sees at 6 a.m. to spot late orders"), not just "a dashboard".
   - **The system constraints up front:** one accent and its single job, the type scale, the 4px spacing unit, light, dark or both.
   - **The component libraries by name**, from `ui-design`'s [component libraries](../../ui-design/references/component-libraries.md) ("shadcn/ui on Radix for base components, Sonner for toasts; do not hand-build them"), and which one section may carry a showpiece.
   - **An avoid list:** the clichés above plus the AI tells that apply (default shadcn look, decorative gradients, low-contrast gray text, oversized headings, color used for emphasis instead of size).
   - **Persist repeated rules:** when the project will be built over many sessions, write the constraints, library picks and avoid list into the project's `AGENTS.md` instead of repeating them in every prompt.
   - **Iterate in small passes:** after the first build, one specific fix per message ("the primary button is the only accent element", "H1 to 32px"); a broad rewrite changes what was already right.
2. **Prompt craft:** if the `prompt-engineering-expert` plugin is installed (listed in this kit's marketplace), hand it the recipe and the target tool and ask for the prompt. It runs a gap scan, applies its blueprint and scores the result. Without it, use the prompt anatomy in `imagery`'s [AI image generation](../../imagery/references/ai-image-generation.md) reference. For website builders (Lovable, Bolt, v0, Cursor, Manus, Google AI Studio, Kimi), start from `web-design`'s [builder prompts](../../web-design/references/builder-prompts.md): the landing spec is the prompt body, with per-tool stack lines marked verify.
3. **Check the output, not the prompt:** run what comes back through `design-critique` against the same recipe, and fix the prompt (not the image by hand) when a tell repeats.
   To have another agent iterate until it beats a named real bar, generate the prompt from `prompt-engineering-expert`'s gauntlet-loop template (1.4.0 and later) and follow `design-critique`'s [gauntlet loop](../../design-critique/references/gauntlet-loop.md) for the bar capture, hard gates, blind critic and cost ceiling.
4. **Record** tool, model, version, prompt and approver, as the `imagery` provenance default requires.

## 5. Keep the idea intact

Every downstream deliverable should pass a quick check against the chosen recipe: same type roles, same palette proportions, same layout logic, same motion personality, same voice. When a deliverable needs to deviate (a dense dashboard inside an expressive brand), document the rule ("product UI uses the neutral ramp and accent at 5% coverage") rather than drifting.
