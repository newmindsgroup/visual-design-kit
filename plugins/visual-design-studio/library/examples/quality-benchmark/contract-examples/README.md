# Worked record bundle

Version-Timestamp: 2026-09-16 18:27:39 AST

These records cover the FORM and TIDAL fictional quality-benchmark collection. They bind the exact current source, asset and export bytes in the library. They are technical exercise records only. They do not assert client approval, human preference, brand truth, accessibility certification, target-device acceptance, or permission to publish.

`selection.json` selects `web-copy-fit` for the documented headline-only revision. `evidence.json` records fictional-source and export identity. `handoff.json` leaves human review pending while retaining the supplied technical observation: the browser-release run reported 20 combinations passing, and the v4 exported video completed twelve-second playback with 287 decoded callbacks and at least 2539 sampled brand pixels. Raw proof remains in the repository-private quality packet and is not distributed in this library.

Regenerate hashes only after changing the bound source, assets, exports, capability entries, or this record bundle. Validate from the library root:

```sh
python3 -m design_system validate evidence examples/quality-benchmark/contract-examples/evidence.json --root .
python3 -m design_system validate handoff examples/quality-benchmark/contract-examples/handoff.json --root .
python3 -m design_system validate selection examples/quality-benchmark/contract-examples/selection.json --root . --library-root .
```

Use `python3 examples/quality-benchmark/contract-examples/generate_examples.py --check` to detect declared-reference drift. After final local source bytes are stable, `--apply` refreshes hashes only for paths already present in these records. It does not discover files, import private proof, change statuses, or create approval evidence.
