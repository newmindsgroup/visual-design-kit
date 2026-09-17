# Audit evidence and review dispositions

Version-Timestamp: 2026-09-16 17:27:10 AST

Parent: [quality audit and implementation order](DESIGN-QUALITY-AUDIT-2026-09-16.md). Baseline: `39cc800`. This record summarizes returned worker findings and parent verification; it is not a verbatim transcript or evidence of implemented repairs.

## Audit passes

- `/root/ultra_design_audit`, requested `gpt-6-astra`, effort `ultra`: read-only craft assessment. Returned seven findings: comparative benchmarks, specialist selection, typography execution, critique calibration, reference usability, revision continuity and motion craft. It found substantial existing coverage and recommended no new standalone skill. It did not inspect private books, call providers or change files.
- `/root/ultra_package_audit`, requested `gpt-6-astra`, effort `ultra`: read-only routing, package and acceptance assessment. Returned seven findings: contradictory completion checks, absent selection validation, split resume authority, nonportable copied links, optional-reference startup gap, stale installed status and incomplete end-to-end proof. It supplied an in-memory reproduction of the first finding. It did not call providers or change files.
- Parent: inspected repository and installed bytes, read governing contracts, ran actual tests, independently reproduced contradictory handoff results, inspected two historical visual assets, checked relevant primary-source typography guidance and consolidated the plan.

## Per-finding provenance

| Finding | Origin | Parent verification and scope |
| --- | --- | --- |
| G01 | Package pass | Reproduced passed+failed and passed+pending returning valid; inspected validation.py:398-416 and DELIVERY-PREFLIGHT.md:14 |
| G02 | Package pass | Read PROJECT-LAUNCH, USAGE and CLI kinds; inspected template inventory. Missing selection validation is confirmed; suggested tests are future work |
| G03 | Package pass | Read WORKFLOW.md:24-28, startup/launch and stage template. File-name conflict and document-relative relocation problem confirmed by source inspection, not a fresh recovery trial |
| G04 | Package pass | Read installed-entry/readiness contract and root status; configuration enabled and 322 installed hashes verified. Automatic startup was not retested |
| G05 | Craft pass | Read example/status limits and fixed SVG builder; viewed one existing photograph and one schematic fallback screenshot. Broader creative quality remains untested |
| G06 | Craft pass | Read rubric and critique reference; positive-quality calibration is a reasoned recommendation, not an experimentally measured deficiency |
| G07 | Craft pass | Read WEB route, website specialist table and UI's craft/specialization links. Reliability risk only; no missed selection by a fresh agent reproduced |
| G08 | Craft pass | Read typography rule, diagnostic code and CRAFT-LAB pending execution statement. No new viewport or export typography test ran in this audit |
| G09 | Both passes | Inventory search found no described reference-techniques.json/helper in plugin; read actual out-of-payload reference workflow and entry. Retrieval tool was not re-reviewed or books reopened |
| G10 | Craft and package passes | Read creative-continuity method/exercise and current backlog limits. No new rendered revision/resume case executed |
| G11 | Craft pass | Read motion-effects, motion specification, still-to-motion and exercise limits. No full video playback reviewed in this audit |

Source links in the parent report resolve against this checkout. Recommendations distinguish source inspection, reproduced behavior, historical evidence and future tests.

## Reproduce the confirmed defect

Run from `plugins/visual-design-studio/library`. This reads existing fixture files and constructs records in memory; it does not alter the plugin.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import hashlib, json
from design_system.validation import validate
root = Path.cwd()
data = json.loads((root / 'templates/handoff-actor-record.json').read_text())
data.update(record_id='AUDIT-CASE', owner='Audit', next_action='Review candidate',
            completion='complete', readiness='ready')
data['registry']['actors'][0].update(
    role='Reviewer', goal='Inspect a sample', context='Fictional audit case')
source = root / 'examples/screen-production/campaign.json'
reference = {'path': str(source.relative_to(root)),
             'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
data['outputs'] = [reference]
for state in ['failed', 'pending']:
    data['checks'] = [
        {'criterion': 'C-1', 'status': 'passed', 'evidence': reference},
        {'criterion': 'C-1', 'status': state}]
    print(state, json.dumps(validate('handoff', data, str(root))))
PY
```

Observed for both states: `valid: true`, `errors: []`, `warnings: []`, with the normal structural-only assurance disclaimer. Expected behavior for a completed record with unresolved current conflicting results: reject completion or explicitly report the conflict. The test uses an existing hashed fixture as its declared output and evidence; it makes no claim of creative validation.

Exact probe inputs and results are retained locally in ignored `private/design-quality-audit-20260916/negative-probes.json`. Parent search found the explicit any-passed completion logic in `validation.py`; a similar-pattern scan is an implementation follow-up, not a claim that every possible acceptance defect has been ruled out.

## Existing test results

| Working directory | Command | Result |
| --- | --- | --- |
| Repository root | `python3 -m unittest discover -s tests -v` | 6 passed |
| Plugin library | `python3 -m unittest discover -s tests -v` | 9 passed |
| Plugin library | `node --test examples/screen-production/player.test.mjs examples/media-quality-recipes/touch-session/session.test.mjs` | 11 passed |

The initial library discovery command run from the repository root failed to import `scripts`. The documentation already specifies the library working directory, where it passed. A convenient root-level test command is a useful later improvement; this invocation mistake is not equated with broken copied-template links.

## Independent Claude review

Stable audit task ID: `vd-quality-audit-20260916`, phase `milestone`, one attempt. Preflight reported subscription authentication and included-model policy ready. The actual call returned `review_returned` with `actual_models: [claude-fable-5-1]`, exit 0. This success concerns this audit only; it does not repair, rerun or close the older exhausted reference-library review.

The reviewer received the audit text only and had no repository, image or tool access. Its file references and reported test results were therefore not independently tool-verified. Raw result and exit status remain in ignored `private/design-quality-audit-20260916/`.

| Reviewer observation | Disposition |
| --- | --- |
| Add per-finding provenance and avoid implying Ultra guarantees quality | Added this record and removed the unsupported comparative effort claim |
| Benchmark creation must precede annotated comparison; avoid overlapping collections | Split rubric preparation from executed comparison and assigned one shared example set |
| Specify photographic sourcing for both fictional briefs | Added authorized-master versus original imagery routes, scoped provider allowance and vector/logo/diagram exceptions |
| Provide interim mitigation for installed validator defect | Added manual reconciliation warning in G01 and required wrapper propagation |
| Do not reopen an exhausted reference-library release review | Retained startup integration recommendation within the present scope. No old review retry or utility release claim is made; the user did not cancel reference integration |
| Separate reproduced defect from proposed version-binding extensions | Labeled proposed additional cases; cited the existing media-pattern rule as a future regression target |
| Treat root-level test discovery as portability work | Kept as optional command convenience because current documented invocation works; not classified as a product defect |
| Label photographic judgment and define comparison blinding | Marked as one parent visual judgment; defined withheld labels and explicitly excluded user-study claims |

No second review is claimed. The parent reconciled the returned observations and checked the revised document; implementation and release reviews remain future work.

Agent-Attribution: computer=Mac.lan; tool=Codex; version=codex-cli 0.154.0; timestamp=2026-09-16 17:27:10 AST
