# Visual design library team preview

Version-Timestamp: 2026-09-12T11:38:16-04:00

Candidate 11. This folder contains 130 selectable design capabilities. It is a review candidate, not an installed plugin or an automatic agent. Focused onboarding and motion reviews have returned. Whole-library release and full production acceptance remain pending. Use it with supervision.

## Start in Codex

Claude Code has bounded staged-write and read-only recovery evidence against candidate09. Its initial capability IDs needed explicit repair, so clean end-to-end acceptance remains open.

Extract the complete folder to a local location the agent can read. Keep the library unchanged and create a separate project directory for client assets, decisions and outputs. Open a task with access to both directories. A pasted repository URL does not load the files automatically. Do not copy all skills into the conversation or install every provider.

Give the agent this instruction, replacing the bracketed paths and task:

```text
Use the design library at [absolute library path]. Read its README.md and USAGE.md, then select only the relevant capabilities from capabilities.json.
Work in [absolute project path]. My task is [deliverable, audience, channel and purpose]. Existing assets and approved baseline are [paths or none]. Preserve accepted inputs and record missing facts honestly. Follow the selected workflow, inspect actual outputs and keep a handoff record in the project. Do not infer provider access, spending, publication or approval from this instruction.
```

Use [usage](USAGE.md) and [readiness](TEAM-READINESS.md). Python 3 is needed for the supplied CLI, Node for JavaScript examples, and a browser for previews. Other tools are conditional and must be discovered on the adopting computer. No credentials or subscriptions are included. These instructions are manually followed in either agent; automatic discovery and installation have not been certified. A bounded fresh Codex planning and recovery exercise passed against candidate 03. Clean end-to-end Claude Code and final team acceptance remain pending; see RELEASE-NOTES.md for version-specific evidence.

## Verify before use

Keep PACKAGE-MANIFEST.json and SHA256SUMS with the folder. Complete the download-verification procedure below before running library commands. Verify the payload hashes and use `python3 -m design_system plan ui` from the library root as a bounded startup check. This checks selection only. The [media exercises](examples/media-quality-recipes/README.md) distinguish prepared, logic-tested and visual fixtures.

## Updates and rollback

Install a newer candidate into a separate folder. Compare its manifest and release scope before changing a project's library path. Keep the prior folder and record which version/hash the project uses. Never silently replace accepted project assets during a library update. Report defects with the selected skill ID, version, sanitized brief, actual result and expected result; keep client data in the project.

Do not share this candidate externally until its final privacy, dependency and independent review gates are resolved. PowerPoint and backup setup remain deferred.


## Verify the download without running library code

Obtain the expected SHA-256 of the ZIP from the release owner through a separately trusted channel. A checksum delivered only inside the same download does not authenticate its source. On macOS, run the system command below against the downloaded archive and compare all 64 characters:

```sh
shasum -a 256 /absolute/path/candidate-11-review.zip
```

Only extract after that value matches. In the extracted folder, use the system utility to check the manifest-listed bytes:

```sh
shasum -a 256 -c SHA256SUMS
```

SHA256SUMS covers all payloads and PACKAGE-MANIFEST.json. It does not hash itself; the separately verified archive hash covers the checksum file too. The extracted tree must contain exactly the manifest destinations plus PACKAGE-MANIFEST.json and SHA256SUMS: 316 files total. Reject extras, missing files and symlinks. Hash matching establishes identical bytes, not safe code, licensing or release approval. This candidate remains internal review only until the release owner resolves its open gates.
