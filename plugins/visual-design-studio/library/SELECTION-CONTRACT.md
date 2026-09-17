# Capability selection contract

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

`SELECTED-CAPABILITIES.json` is a read-only record of the instruction capabilities selected for a scoped project. It does not execute a capability, create a prerequisite, grant provider access or establish approval.

Use schema version `1.0` only. Record the exact current `capabilities.json` path, catalog schema version and lowercase SHA-256. The library root is trusted only when passed explicitly to the CLI. Entry paths must match catalog entries exactly, resolve as regular files under that root and use their host's exact filename casing. Every selected ID stores the exact entry and SHA-256 of its current bytes.

Use exact catalog IDs in `selected`. A broad choice uses `patterns`, with `pattern` plus an `entries` array that exactly records its full current expansion. Patterns are expanded against complete current catalog IDs during validation. `media-*` expands only IDs that begin `media-`; it never implies `chatgpt-images`, `openart-cli` or `higgsfield-cli`.

Keep `excluded` separate. An exact ID or pattern exclusion that intersects a selected ID or its transitive `depends_on` closure is a visible validation failure. The validator never removes a capability to resolve that conflict.

For each transitive dependency that is not selected directly, record one `prerequisites` disposition: `reuse`, `create`, `provisional`, or `not_applicable`. Each has a scope-specific reason. `reuse`, `create`, and `provisional` also require evidence text. This captures bounded use: an accepted logo can be reused for a revision, accepted positioning can remain authoritative, and a dependency can be not applicable without restarting brand strategy.

`provenance` keeps the original input, exact resolution basis, repair actor, and the same catalog hash. It makes assisted repairs visible instead of presenting them as first-pass resolution.

Run from the library root:

```sh
python3 -m design_system validate selection /absolute/project/SELECTED-CAPABILITIES.json \
  --root /absolute/project --library-root /absolute/library
```

Exit 0 means only that this structure, catalog identity, dependency closure, exclusions and present local bytes passed. It is not a quality, factual, rights, approval, provider, execution, client or device acceptance result.
