# Build fidelity: compare the approved design with what shipped

Version-Timestamp: 2026-10-20 10:34:29 UTC

A build is faithful when a reviewer cannot tell the approved render and the built page apart at every agreed width, except where real content or a recorded decision says otherwise. Prove it with a pixel diff, a computed-style diff and a person looking at both. [compare_build.mjs](../scripts/compare_build.mjs) does the first two in one run.

## When to run it

| Moment | Approved side | Built side | Threshold |
| --- | --- | --- | --- |
| A stylescape or HTML comp was approved and then built | The approved HTML file (frozen copy) | Local build or preview URL | 2% |
| Figma frame approved, page built from it | Frame exported as PNG at 1x, wrapped in HTML (below) | Preview URL | 5-10%, read the regions |
| Regression check on a released page | The released URL or a saved copy of it | Preview URL of the change | 0.5% outside the changed section |
| Token release (color, type, space) | Pre-release build | Post-release build | No threshold: every region must trace to an intended token change |
| Component library change | Specimen page before (`library/examples/react-system/` specimen or Storybook story) | Specimen after | 0% outside the changed component |

Run it before asking for client sign-off on a build, on every pull request that touches a template or the token files, and before release. It is evidence for step 11 of the critique workflow, not a replacement for looking.

## Defaults

| Setting | Default | Move off it when |
| --- | --- | --- |
| Widths | 390 and 1440, full page | Add 768 when the tablet layout differs; add the brief's named devices |
| Changed-pixel threshold | 2% per width | 0.5% for regressions of a released page; 5-10% when one side is a Figma PNG |
| Color tolerance | 0.05 (YIQ distance) | 0.1 only for cross-renderer pairs; at 0.1 a #FF5B3A to #E0452A swap passes unseen |
| Anti-aliased edge pixels | Ignored (counted separately) | `--include-aa` when you need sub-pixel text rendering parity |
| Motion | Reduced motion, animations finished | `--motion` only to compare an animation's end state that reduced motion hides |
| Masks | Anything that changes between loads | See "Masking dynamic content" |
| Style matching | Elements with the same `id` or `data-testid` | Add `data-testid` to the 10-20 elements that carry the design: headings, primary actions, cards, nav, form fields |
| Fail on style drift | Off | `--strict-styles` in CI once the build has passed one human review |

## Run it

```sh
# From the skill folder; Playwright from the working project or PLAYWRIGHT_MODULE / PLAYWRIGHT_CHROMIUM
node scripts/compare_build.mjs approved/index.html http://127.0.0.1:4321/ --widths 390,1440 --out review/fidelity-round-1
node scripts/compare_build.mjs approved.html built.html --mask "#live-rates,[data-dynamic]" --threshold 2%
node scripts/compare_build.mjs approved.html built.html --element "#pricing"    # one section, no cascade
node scripts/compare_build.mjs approved/index.html built/index.html --serve --root .   # pages that fetch() or load ../ assets
```

Output per width: `<w>-approved.png`, `<w>-built.png`, `<w>-diff.png` (changed pixels red, ignored edge pixels amber, the largest regions outlined blue on a faded copy of the approved render) and one `report.json`. The console prints PASS or FAIL per width, the changed share, the five largest regions with the smallest matched element that contains each one, and the style drift. Exit code 0 means within threshold, 1 means above threshold (or drift with `--strict-styles`), 2 means a usage or runtime error.

## Comparing against a Figma frame

The script compares two web pages. For a Figma frame, export it as PNG at 1x at the same width as the viewport, then wrap it:

```html
<!doctype html><meta charset="utf-8"><title>Approved frame</title>
<style>html,body{margin:0;background:#fff}img{display:block;width:1440px}</style>
<img src="home-1440.png" alt="">
```

Run one width per export (`--widths 1440` against the 1440 frame). Figma and Chromium rasterize text differently, so a correct build still shows changed pixels along every text edge. Calibrate first: compare one frame you know matches, note its share, and set the threshold just above it (start at 5-10% if you cannot calibrate). Read the regions instead of the total: a region that covers a whole card or section is real drift; thin outlines around every text line are rasterizer noise. Style drift is empty for this pair (the image has no elements), so check type and color values against Dev Mode variables by hand or through `get_design_context` in the [figma-workflow](../../figma-workflow/SKILL.md) skill.

## Reading the result

1. **Size mismatch first.** When the page heights differ, everything below the first difference shifts and the total explodes. Find the topmost region, fix it, re-run. Use `--element` to compare one section at a time when a shift upstream hides what happens below.
2. **Style drift second.** It names the cause: `fontFamily "Bricolage Grotesque" -> "DejaVu Serif"` (font failed to load or wrong token), `padding 12px 20px -> 10px 20px` (off-scale spacing), `backgroundColor #2b44ff -> #3355ff` (hard-coded color instead of a token). Fix causes, not pixels.
3. **Regions third.** Open the diff PNG and both screenshots at the region's coordinates. Confirm each region by eye before calling it a defect.
4. **Below threshold is not a pass on its own.** A 0.4% diff can be a wrong button color across every call to action. Read the style drift even when the pixel check passes; the pixel tolerance lets small color shifts through (#2B44FF to #3355FF passes at 0.05) so that rendering noise does not fail builds.

## What counts as acceptable drift

| Acceptable (record it, do not fix) | Not acceptable (fix before review) |
| --- | --- |
| Anti-aliasing and sub-pixel text differences between machines | Any token value change: color, font family, weight, size, radius, shadow |
| Real copy replacing approved placeholder copy, when it still fits the layout (then re-approve that text) | Spacing that is not on the space scale, or differs from the comp by more than 2px |
| Image recompression (AVIF/WebP) with no visible change at 100% zoom | Element size off by more than 2px or 2%, whichever is larger |
| Line breaks that move one word at a width between the approved breakpoints, without runts or overflow | Different line breaks at the approved widths in headings and hero copy |
| Live data inside masked regions | Missing or reordered sections, swapped icons, missing states (hover, focus, error, empty) |
| Browser-native controls (scrollbars, date pickers) differing by platform | Fallback font rendering because a web font failed to load |
| Changes the client approved after the comp, logged in the decision record | "Improvements" nobody approved, however small |

Position tolerance is 2px, size tolerance 2px or 2%, color and font values are exact token matches, and line height is within 0.5px. These are kit starting points; a client contract or design-system policy overrides them.

## Masking dynamic content

Masked elements are painted solid magenta in both screenshots and skipped in style drift.

- **Mask:** clocks and relative times, live prices and rates, carousels and rotating testimonials, video and canvas, maps, ads and third-party embeds, randomized avatars, A/B test slots, personalization.
- **Freeze instead of mask when you can:** load fixture data, pass a fixed seed or date (`?seed=1`, a mocked `Date`), set the consent cookie so the banner does not render, pause carousels on the first slide. Frozen content is still compared; masked content is not.
- **Keep masks under about 10% of the page.** A page that needs more masks than that needs fixtures.
- **Masks move with layout.** A mask over an element that shifted paints in a different place in each screenshot and adds changed pixels. Fix layout drift above it first.
- **Name masks by selector in the report** so reviewers know what was not compared.

## States and interactions

The script captures the resting state only. Compare states through pages that render them statically: the react-system specimen sets `data-preview-state` to draw hover, focus and pressed without interaction, so a specimen-to-specimen comparison covers every state in one run. For a single interactive state, script it in Playwright and compare screenshots, or capture both states by hand and review them side by side.

## Pair fidelity with performance

A pixel-perfect build that loads its hero in 4 seconds fails the brief. Run both gates on the same preview URL and report them together. Thresholds and budgets live in [performance and Core Web Vitals](../../web-design/references/performance.md).

| Gate | Tool | Pass |
| --- | --- | --- |
| Visual fidelity | `compare_build.mjs` | Under threshold at every width, no unexplained style drift |
| Lab performance | Lighthouse (mobile) or Lighthouse CI | LCP 2.5 s or less (design target 2.0 s), CLS 0.1 or less (target 0.05), TBT as the INP proxy |
| Weight budgets | Lighthouse or bundle analysis | Within the budget table in the performance reference |
| Field performance | RUM with `web-vitals`, then CrUX | LCP, INP and CLS at p75 within "good" after launch |

Where the two gates interact:

- **Fonts:** fidelity needs the brand font; performance needs it fast. Preload the one or two WOFF2 files used above the fold and use metric-matched fallbacks; do not "fix" a slow font by dropping it, which turns into style drift on every heading.
- **Hero media:** match the approved crop with a responsive `img` (`srcset`, `sizes`, `fetchpriority="high"`), not a CSS background, so fidelity and LCP both pass.
- **Layout shift:** when the built page is taller or shorter than the approved one at load, check CLS too; late-loading content that pushes the layout down fails both gates.
- **Motion:** the fidelity run uses reduced motion. Check the full-motion version separately for INP and long animation frames.

A Lighthouse CI assertion block for the same URL (verify keys against the Lighthouse CI documentation for your version):

```json
{
  "ci": {
    "assert": {
      "assertions": {
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["warn", { "maxNumericValue": 200 }]
      }
    }
  }
}
```

## Record the result

Save the output folder next to the critique round (`review/fidelity-round-N/`). In the review record, write: approved artifact and version, built URL and commit, widths, threshold, masks, changed share per width, accepted drift with reasons, fixed drift, and the Lighthouse numbers from the same commit. Only a named person approves the build; the script's PASS means "ready for review".

## Limits

- Chromium only. Safari and Firefox rendering still needs a manual pass on real browsers ([browser QA](../../../library/draft-skills/design-web-browser-qa/SKILL.md)).
- Full pages are clipped at 16,000px (`--max-height`); compare long pages by section with `--element`.
- Elements without `id` or `data-testid` are not style-checked; the pixel diff still covers them.
- Pixel parity proves sameness, not quality. A faithful build of a weak design still needs the rubric.
