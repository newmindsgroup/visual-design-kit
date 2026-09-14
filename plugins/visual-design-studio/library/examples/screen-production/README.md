# Screen production example

Version-Timestamp: 2026-09-11 20:20:00 AST

Parent: [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Checks: evidence (historical source evidence not included).

## Use

From the repository root:

```sh
python3 scripts/screen_campaign.py build examples/screen-production/campaign.json /tmp/screen-campaign-new-version
python3 scripts/screen_campaign.py verify /tmp/screen-campaign-new-version
python3 -m unittest tests.test_screen_campaign -q
node --test examples/screen-production/player.test.mjs
python3 -m http.server 17658 --bind 127.0.0.1 --directory examples/screen-production
```

Open the localhost server in a browser. Play cycles through three formats every eight seconds. Next pauses and changes format. Hidden tabs and reduced-motion preference pause playback. The preview does not test a real display player. Stop the local server when no longer needed.

## Editable source

[campaign.json](campaign.json) supplies explicit headline lines, colors and name. The [SVG export set](render-v1/manifest.json) contains original schematic product illustrations and separate wide, portrait and strip compositions. Text uses local Arial/Georgia fallbacks; exact font metrics vary by machine. Native-app import and production font substitution need separate validation.

Change the campaign record and build to a new empty destination. The builder refuses existing destinations. It accepts only this bounded example schema and layouts; it is not an arbitrary design engine. Length limits reject excessive text but do not prove visual fit. Manually inspect every new text variant.

## Evidence boundaries

Exact hashes detect accidental export changes, not authenticity or approval. The example carries candidate status and no real product claims. No client imagery, video, audio, CMS, external fonts, analytics, paid generation or external sensor is used. The HTML page is a local preview, not a tested kiosk or CMS adapter. The production skills describe broader methods whose native and hardware execution remain pending.

## Browser checks

Use a dedicated unsigned-in local debugging browser at port 17659, never a personal browser profile. With the local preview server running:

```sh
EVIDENCE_DIR=/tmp/screen-browser-evidence node examples/screen-production/browser-checks.mjs
```

The runner creates and closes its own tab, tests 1280 and 390 pixel viewports, captures formats, exercises keyboard start and a timed advance, emulates reduced motion and injects a missing-image URL. It does not contact a CMS or test physical hardware.

Version-Timestamp: 2026-09-11T23:27:03-04:00
