# Google Vids reference
Version-Timestamp: 2026-10-01 21:48:22 UTC
Official documentation checked 2026-10-01. Documentation is distinct from live account evidence.

| Area | Documented workflow | Verification boundary |
| --- | --- | --- |
| Native editor | Blank Vid, templates, uploads, scenes and objects | Current Chrome/Firefox on Mac; verify actual account |
| Styles | Default background, typography, shape and line colors | New objects inherit defaults; inspect existing objects |
| Motion/timing | Scene transitions, enter/exit/loop, text animation, photo effects, object tracks | Inspect crops, overlaps and final runtime |
| Audio | Trim/split, volume, fades, balance and ducking | Included/cleared assets, final listening check |
| Captions | English automatic captions, manual/uploaded tracks, styled captions | Verify export; Spanish speech may need manual captions |
| Sizes/limits | Landscape, portrait, square; dedicated limits page says 30 minutes | Older general/recording/import pages conflict; live UI decisive |
| Slides | Each imported slide becomes an editable scene; AI extras can be disabled | Non-AI scene defaults 5 seconds; verify import fidelity |
| Delivery | Saved editable Vid; MP4 to Drive/device | Private permission and independent native/export checks |
| Automation | application/vnd.google-apps.vid; files.download operation for MP4 | files.export/exportLinks unsupported; public scene API not found |

## AI and rights gate
Basic editing and generative AI availability differ by edition, administrator settings, region and rollout. Business plans can use per-feature monthly allowances; personal/Individual plans can use credits. Do not hardcode free/unlimited or a model name. Visible controls do not prove an included quota. Unknown action cost selects manual photo/logo/text work. Do not upgrade or buy credits without scoped approval.

Optional AI clips have newer documented 3 to 10 second, 720p/1080p and up to seven ingredient-image controls, alongside older residual text. Use observed controls. Do not route around regional restrictions. Optional voiceover, music and avatars need entitlement and rights checks. Avoid real-person cloning and artist/brand references in generated music prompts. Stock can be used commercially subject to Google's terms but cannot be redistributed standalone, in third-party templates, or as a logo. Web images need separate clearance. Brand-owned assets are the safest reusable template sources.

## Sources
- [Account availability and quotas](https://support.google.com/docs/answer/15609411?hl=en)
- [Getting started and export](https://support.google.com/docs/answer/15082958?hl=en)
- [Brand styles](https://support.google.com/docs/answer/16105028?hl=en)
- [Slides import](https://support.google.com/docs/answer/15577408)
- [Motion/photo effects](https://support.google.com/docs/answer/14999375?hl=en)
- [Object timing](https://support.google.com/docs/answer/14960797)
- [Transitions](https://support.google.com/docs/answer/14916386)
- [Audio](https://support.google.com/docs/answer/14999865?hl=en)
- [Voiceovers](https://support.google.com/docs/answer/15070345)
- [Captions](https://support.google.com/docs/answer/14953386?hl=en)
- [Video size](https://support.google.com/docs/answer/16545758?hl=en)
- [Dedicated limits](https://support.google.com/docs/answer/16286470?hl=en)
- [Generated clips](https://support.google.com/docs/answer/16143507)
- [Generated music](https://support.google.com/docs/answer/16855124)
- [Stock/web rights](https://support.google.com/docs/answer/15001094)
- [Drive MIME types](https://developers.google.com/workspace/drive/api/guides/mime-types)
- [Drive downloads with long-running operations](https://developers.google.com/workspace/drive/api/guides/long-running-operations)
- [Unsupported export formats](https://developers.google.com/workspace/drive/api/guides/ref-export-formats)

A creator tutorial is reference evidence only. Its example ingredient count, included/free claims, model names and successful generated brand labels are not universal limits, entitlements or fidelity guarantees.

## Native workflow observations (2026-10-01; recheck live)
- Set Video size → Portrait 9:16 before inserting portrait source material. Changing the canvas does not thoughtfully recompose a landscape design; rebuild safe-margin layout at the target ratio.
- File → Slides to video inserts selected scenes after the selected existing scene; it does not replace the whole timeline. Disable the AI extras switch, verify scene/object editability, remove only superseded project scenes, and check the resulting total runtime.
- Scene animation → Simple Fade → Enter → Apply to all scenes gave legible titles in the inspected short-scene export. The Soft preset left text incompletely revealed at mid-scene; preset names are not evidence of readability. Inspect rendered frames.
- Select a photograph's object track → Animation → Object → Photo effect offers Slide, Zoom in/out and Breathe with loop-duration/reverse controls. Use gentle photographic movement when an unseen 3D angle would require fabricated geometry.
- Included stock music insertion can automatically extend to the project timeline. Sound controls expose percent volume and second-based fades. Measure exported signal and listen; UI percent alone does not establish loudness.
- An observed AI prompt panel offered model, resolution, portrait and duration selectors and enabled Generate, but did not disclose action quota/credit balance. An accepted prompt is a UI test, not successful generation or verified no-charge access.
