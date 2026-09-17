# Validator cross-review 020

Version-Timestamp: 2026-09-16 18:26:45 AST

This independent local review inspected the G01 handoff reconciliation changes and the template adopter. It did not change production source, package manifests, installation state, or publication state. It is not the final independent Claude review.

## Checks that passed

`python3 -m unittest tests.test_handoff_current` passed 9 tests. The later repaired `python3 -m unittest tests.test_adopt_template` passed 8 tests. Final verification also ran the selection worker's 15 focused tests and the full 41-test library suite successfully.

The handoff probes confirmed that a legacy `1.0-proposed` record claiming both complete and ready fails with `handoff_schema_migration`, and that a current check bound to a candidate-artifact superset fails with `candidate_binding`.

The practical CLI minimum was clear and safe: `adopt_template.py stage-execution.md --project-root /tmp --destination quality-020-cli-probe.md` returned a JSON dry-run plan and created no file. Its help text documents that `--apply` is required for a write.

## Historical findings and resolutions

CR-01 historical finding: `library/scripts/adopt_template.py:_template_path` accepted an in-root symlink as a template source. An isolated `alias.md` symlink to `templates/real.md` was adopted successfully. The old implementation resolved first and then checked `is_file()`, which followed the symlink.

CR-01 resolution: `_template_path` now rejects `.` and `..` components and checks every requested component for a symlink before resolution. `test_rejects_source_symlink_and_destination_directory_symlink` proves that `alias.md` is rejected. This is covered by the final eight-test adopter suite.

CR-02 historical finding: `library/scripts/adopt_template.py:adopt` had a parent-directory race. After `mkdir` and the post-mkdir containment check, replacement of the destination parent with a directory symlink could occur before `output.open("x")`. A controlled isolated probe wrote `adopted.md` under an external directory. Exclusive file creation prevented overwrite, but did not retain the write beneath the project root.

CR-02 resolution: the adopter now opens the project root and each parent directory by descriptor, uses no-follow flags for every descent, and creates the output with descriptor-relative exclusive creation plus `O_NOFOLLOW`. The opened directory chain remains the write authority even if a pathname is replaced later. The final regression rejects a destination-directory symlink. It is a deterministic containment check, not a stress test against hostile filesystem or kernel behavior.

The detailed machine-readable record is `private/quality-020/cross-review.json` in the authoring workspace (not distributed).
