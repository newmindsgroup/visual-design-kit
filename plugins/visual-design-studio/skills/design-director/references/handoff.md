# From chosen direction to production

Version-Timestamp: 2026-10-27 07:43:23 AST

Once a direction is chosen, lock it into tokens and route each deliverable to the skill that owns it. Keep the decision traceable.

## 1. Record the decision

Write a short decision note in the project: chosen direction, runner-up, scores and weights, what the client said, open risks. For client projects that keep formal records (approvals, pins, resume), load the `design-project-start` skill and use its decision and resume records instead of inventing a new format.

## 2. Turn the direction into tokens

1. Copy `../../../library/tokens/src/` into the project (for example `design/tokens/`).
2. Create `brands/<brand>.tokens.json` with the direction's accent and neutral ramps (generate them with `python3 ../../../library/scripts/color_tools.py ramp --hue <H> --chroma <C> --name <name>`), font families, radius and motion personality.
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
2. **Prompt craft:** if the `prompt-engineering-expert` plugin is installed (listed in this kit's marketplace), hand it the recipe and the target tool and ask for the prompt. It runs a gap scan, applies its blueprint and scores the result. Without it, use the prompt anatomy in `imagery`'s [AI image generation](../../imagery/references/ai-image-generation.md) reference.
3. **Check the output, not the prompt:** run what comes back through `design-critique` against the same recipe, and fix the prompt (not the image by hand) when a tell repeats.
4. **Record** tool, model, version, prompt and approver, as the `imagery` provenance default requires.

## 5. Keep the idea intact

Every downstream deliverable should pass a quick check against the chosen recipe: same type roles, same palette proportions, same layout logic, same motion personality, same voice. When a deliverable needs to deviate (a dense dashboard inside an expressive brand), document the rule ("product UI uses the neutral ramp and accent at 5% coverage") rather than drifting.
