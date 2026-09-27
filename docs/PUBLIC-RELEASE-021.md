# Public edition preparation

Version-Timestamp: 2026-09-27T13:51:02-04:00

The owner authorized public GitHub distribution and selected MIT for original work on September 27, 2026. This 0.2.1 patch adds scoped license notices, fixes installation and reference-library guidance, and separates public distribution from production acceptance. It does not introduce new design output or new provider access.

## Audit scope and results

- Enumerated remote refs before publication: main, one earlier review branch and PR 1 head. All pointed into the audited 16-commit history; no remote tags, notes or additional pull refs were advertised.
- Scanned 450 reachable blobs and all 16 commit objects for known token/key signatures, credential URLs, JWTs, private Google sharing links, local user paths and suspicious credential assignments. No matches were found. This is a bounded pattern scan plus manual review, not a guarantee that every possible secret can be detected.
- No LFS pointers, submodules or private registry/dependency URLs were found in that history. Commit identities use GitHub noreply addresses. The current tree contains no full reference books, extraction bundles, client source material or credentials identified by the audit.
- Reviewed the only existing PR body and its empty comment/review threads. GitHub reported no Actions runs or artifacts, releases, Pages deployment or Discussions. No wiki repository was accessible. Public description will describe the reusable kit.
- Reviewed the three bundled fonts and their individual complete SIL OFL notices. Asset provenance hashes match. Fictional PNGs have no EXIF fields; PDF properties identify fictional titles and Chromium/Skia, not client or author data. No example media bytes were changed for this patch.
- Replaced the stale 0.1.0 startup pin and nonexistent archive verification instructions. Optional books are clearly user-supplied, separately permitted references; the kit has no universal downloadable book collection.
- Added MIT, third-party notices, contribution guidance and a private security reporting route. Original generated examples are labeled and do not promise exclusivity or clearance for a particular commercial use.

## Verification

13 root Python tests, 51 library Python tests and 11 Node tests pass. The public-distribution metadata regression failed on the old manifest and passes on the new contract: intended public audience, publication review still required, production acceptance false. After final edits, all 366 payload checksums and 357 library checksums verify, the deterministic build check passes, and plugin/entry-skill validation passes. Changed documentation links and Python syntax compilation pass. A bounded UI plan and packaged reference-helper startup also execute successfully. The exact package pin is in [VERIFIED-PIN](VERIFIED-PIN.md).

No UI or media design changed in this patch. Existing rendering evidence remains scoped to the [0.2.0 examples](QUALITY-020-RELEASE.md); it is not a new browser, host or hardware acceptance claim. Public setup and package checks do not prove native Cursor/Claude Code execution or client aesthetic approval.

## Review and publication sequence

Claude Fable 5.1 reviewed the sanitized approach. Its useful additions were remote-ref coverage, contributor identity and binary metadata checks, and anonymous post-publication access verification. The history scan found no credential requiring rotation or sensitive object requiring a history rewrite. Private GitHub secret scanning was unavailable on this repository; enable and verify the free public protections after visibility changes, without purchasing a plan.

Final independent review and final package validation precede publication. Read GitHub's actual visibility and anonymous access before claiming the repository is public. Internal scan/review logs remain outside version control in the ignored local audit directory.

## Recovery and ongoing limits

Keep prior project pins unchanged until deliberately upgraded. Public copies cannot be recalled by making the repository private again. If sensitive content is discovered later, address the underlying access or credential exposure and request appropriate history/cache remediation. Do not treat removal from the current branch as erasure of history.

The next functional acceptance belongs in separate real projects: native host startup, actual output/revision/resume, provider access when needed, and relevant human/device review. These are reported limitations, not reasons to include private client data in this kit.
