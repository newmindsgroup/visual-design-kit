# Canva handoff

Version-Timestamp: 2026-10-23 20:38:00 UTC

Canva holds the editable twin: the version a client's marketing team changes without a designer. The kit's HTML and its WeasyPrint PDF stay the master of record and the print master ([print production pipeline](print-production-pipeline.md)). Plan and API facts below come from Canva's Connect OpenAPI spec, release "[2026-10-21] Release" (https://raw.githubusercontent.com/canva-sdks/canva-connect-api-starter-kit/main/openapi/spec.yml), and from Canva help pages read through search summaries on 2026-10-23. Canva changes plans and limits often: verify against the account before promising a client anything.

## Pick the route

| Situation | Route | Editability | Effort |
| --- | --- | --- | --- |
| Recurring piece (cards, sell sheets, social series, case studies) | Rebuild once as a Canva **brand template** with named data fields, then autofill per use | Best: native Canva text and frames | One rebuild per layout |
| One-off piece the client wants to tweak | **Import** the PDF or a simple PPTX, then check every page | Partial: depends on the import | Low up front, check time after |
| Final print run after edits in Canva | Manual **PDF Print** export from the editor, then `preflight_pdf.py` | n/a | Manual |
| Print run with no edits | Send the kit's WeasyPrint master; Canva is not involved | n/a | None |

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Field names | Same as the template's `data-field` names (`headline`, `stat_1`, `email`) | The client's Canva already has a naming scheme |
| Plan for autofill and brand templates | Canva Pro, Teams or Enterprise (spec 2026-10-21) | Account shows otherwise: follow the account |
| Fonts | Upload the brand's OFL fonts to the client's Canva brand kit | Client fonts: their license must allow upload to Canva |
| Images | Upload final images as assets; reference asset IDs in autofill | |
| Print from Canva | Editor download, PDF Print, crop marks and bleed on, CMYK if the plan offers it | Never use an API PDF export for press |
| Where designs live | The client's Canva team or the agency's vetted team, in a named folder per project | |

## Plans, limits and conflicts

- The spec says: "Autofill for designs and brand templates is available when your app acts on behalf of a user on Canva Pro (including Canva Education and Canva for Nonprofits), Canva Teams, or Canva Enterprise. Usage limits will be introduced in the future." Plan for limits you cannot see yet: batch autofills, log each job, and keep the kit's PDF as the fallback.
- Brand template endpoints need "a Canva plan with access to brand templates (such as Canva Pro, Canva Teams, or Canva Enterprise)". Publishing a brand template also needs an admin or designer role.
- Conflict: older canva.dev autofill guide pages still say Enterprise only, and Canva's AI Connector help says autofill "may only be available on Enterprise" [search summary]. The spec is newer, but test autofill on the actual account before quoting it.
- Data field types for brand templates: text, images (image or video assets) and charts.
- Design analytics are Enterprise only; `/v1/resizes` needs a premium plan such as Pro.

## Brand template route (recurring collateral)

1. Render the kit template to PNG and PDF for reference (`render_collateral.mjs`).
2. In Canva, rebuild the layout at the same size with the brand kit's colors and fonts. Match the type scale from the kit's `collateral.css` and the tokens.
3. Mark each replaceable element as a data field named exactly like the HTML `data-field`. Publish it as a brand template.
4. Read the template's dataset (connector `get-brand-template-dataset`, or `GET /v1/brand-templates/{id}/dataset`) and check every field name and type against the HTML.
5. Autofill a new design per use: text from the brief, images as uploaded asset IDs. Review it, then export for the channel.

## Import route (one-off pieces)

- Supported import types include PDF, PPTX and PPT, AI, PSD, Affinity, Keynote and DOCX [search summary]. Canva help gives PDF import limits of up to 500 pages, 300MB and about 1,400 elements; PPTX up to 300MB and 300 slides, with charts, SmartArt, 3D and WordArt ignored.
- Help pages disagree on whether imported PDF text stays editable. Treat an import as a starting point: check each text box, font substitution, image crop and color on every page before the client edits.
- For a deck, a simple PPTX (text boxes and images, charts as images) imports more cleanly than the PDF.

## Exports

- API exports cover pdf, jpg, png, pptx, gif, mp4, html bundles and csv. PDF export options are only `export_quality`, `size` (a4, a3, letter, legal; Docs only) and `pages`. **There is no CMYK, bleed or crop-mark option in the API**, so an API PDF is a screen PDF, never a print master. A print-quality export exists only for Print Partners (`/v1/print-partner/exports`, preview).
- For press from Canva: in the editor choose PDF Print, turn on crop marks and bleed, choose CMYK where the plan offers it (reported to need Pro; the official plan matrix is unverified), download, then run `python3 scripts/preflight_pdf.py <file>.pdf` and send it to the printer's preflight and proof.

## Connector gate

The Canva connector (Canva AI Connector, MCP) is optional. Before calling its tools:

| Before calling | Do first | Why |
| --- | --- | --- |
| Any Canva tool, each session | Load the host's Canva skill if one is listed; otherwise call the connector's `help` tool and read the result | The skill or help carries the call rules the tools assume |
| Anything that uploads client material | Confirm the client allows their assets in Canva and which team they belong in | Client data goes only to services the client or agency has vetted |
| `autofill-design`, `create-design-from-brand-template` | `search-brand-templates`, then `get-brand-template-dataset` | Field names and types must match before filling |
| `upload-asset-from-url`, `import-design-from-url` | Make sure the URL is reachable without creating a public link to confidential files | A public link leaks the file |
| `export-design` | `get-export-formats` for the design | Formats differ by design type |
| `generate-design`, `generate-image` | Client approval for AI generation with their brand | AI output may not match the brand or license terms |

Tools seen in a Claude session on 2026-10-23: `list-brand-kits`, `search-brand-templates`, `get-brand-template-dataset`, `create-design-from-brand-template`, `autofill-design`, `upload-asset-from-url`, `import-design-from-url`, `export-design`, `get-export-formats`, `resize-design`, `merge-designs`, `generate-design`, `generate-image`, plus comment tools. A `help` call failed with a missing-scope error, so plan gating per tool is unverified. If a call fails on plan or scope, stop and tell the user which plan or permission the account needs; do not retry in a loop.

## Without the connector

Hand the user the kit's PDF and PNGs, a field table (`data-field` name, current text, character limit) and these steps: upload fonts and images to the brand kit, rebuild or import, name the fields, publish the brand template. Everything else in this file still applies; Codex and other single-context hosts follow the same steps.

## Common failures

- Using a Canva API PDF as the print file → no CMYK, bleed or marks; export PDF Print by hand or send the kit's master.
- Autofill promised to a client on a plan that turns out not to allow it → test on the account first; keep the HTML route as the fallback.
- Field names that differ between HTML and Canva → autofill leaves fields empty; check the dataset against `data-field` names.
- Fonts substituted after import → upload the brand fonts to the brand kit before importing.
- Confidential drafts uploaded to a personal Canva account → use the client's or agency's team space only.
- Brand template edited after publishing → field names drift; read the dataset again before each autofill batch.
