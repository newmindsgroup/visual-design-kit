# Install for an independent project

Version-Timestamp: 2026-09-27T14:05:22-04:00

Keep one trusted kit checkout separate from each brand project. The kit supplies instructions and local helpers. Your AI host, design apps, accounts and provider permissions are separate.

## Requirements

- Git to obtain and pin the repository.
- Codex, Cursor or Claude Code, installed and authenticated through that product, with access to the kit and project folders.
- Python 3.9 or newer for the bundled command-line helpers. Core validators and reference search use only the standard library.
- A system SHA-256 utility, such as `shasum` on macOS or `sha256sum` on Linux.

Node.js is needed for the JavaScript tests. Playwright, Chromium, Pillow and FFmpeg are optional development/export tools; see [Development checks](docs/DEVELOPMENT.md). They are not required to read the instructions or select capabilities.

The shell examples use macOS or Linux syntax. Authoring-machine evidence is from macOS. Other operating systems and host versions need their own execution checks.

## Get and pin the kit

```sh
git clone https://github.com/newmindsgroup/visual-design-kit.git
cd visual-design-kit
git checkout --detach v0.2.1
git rev-parse HEAD
```

Record that full commit ID in the project. Use a dedicated checkout that stays unchanged during project work. If selecting an older reviewed commit, check out that exact commit in a separate directory and use its matching pin record. Do not combine one edition's files with another edition's digest.

## Verify the package

Read [the current package pin](docs/VERIFIED-PIN.md) from your trusted repository source. From the repository root on macOS:

```sh
shasum -a 256 plugins/visual-design-studio/PAYLOAD.sha256
```

Compare all 64 characters with the pin record. Then verify the listed file bytes from the package directory:

```sh
cd plugins/visual-design-studio
shasum -a 256 -c PAYLOAD.sha256
```

On Linux, use `sha256sum` for the first command and `sha256sum -c PAYLOAD.sha256` for the second. Stop if the expected digest is unavailable, any file check fails, or the checkout contains unexplained modifications. `git status --short` helps identify changed or extra files in a Git checkout. The manifest checks listed files; it does not itself reject extra files or authenticate an unknown publisher.

`PAYLOAD.sha256` covers all packaged files, including `library/PACKAGE-MANIFEST.json` and `library/CHECKSUMS.sha256`; it excludes itself. Its own expected digest lives in the pin record outside the package. Repository-level docs, tooling and starter files are pinned by the Git commit.

Use the verified SHA-256 of `PAYLOAD.sha256` for the starter's trusted-digest field. Use the absolute path to `plugins/visual-design-studio` for its package-root field. Run no bundled scripts until verification succeeds.

## Configure the project entry

Create a separate directory or repository for each brand. Open your AI task there. Merge [AGENTS.md.template](project-starter/AGENTS.md.template) into the relevant project instruction file, following [the starter guide](project-starter/README.md):

| Host | Project instruction file | Current evidence |
| --- | --- | --- |
| Codex | `AGENTS.md` | Earlier editions have authoring-Mac install and explicit startup evidence |
| Cursor | `AGENTS.md` | Documented route; native-session acceptance remains unverified |
| Claude Code | `CLAUDE.md` | Documented route; native-session acceptance remains unverified |

Replace both placeholders, preserve existing instructions, and use exactly one marked entry block per instruction file. Keep machine-specific paths in local configuration instead of shared client commits. The project path is authoritative; an optional plugin cache must not silently replace it.

Start a fresh task. Confirm that the agent reads the intended entry, reports the expected edition and digest, and keeps its outputs inside the project. Give it the [initial brief](plugins/visual-design-studio/PROJECT-LAUNCH.md#initial-request). Review its first artifact before continuing. [Host compatibility and acceptance](docs/IDE-COMPATIBILITY.md) describes the remaining checks.

## Optional Codex plugin installation

From the repository root:

```sh
codex plugin marketplace add .
codex plugin add visual-design-studio@visual-design-team --json
codex plugin list --marketplace visual-design-team --json
```

These command forms are available in Codex CLI 0.154.0. Earlier package editions were installed and enabled on the authoring Mac. Verify the actual edition and state reported on your host. The marketplace adds one instruction plugin with no bundled connector, hook, credential or provider subscription.

Open a fresh task after installation. Automatic discovery failed in an earlier authoring session because the host's skills context budget omitted the entry. Use the configured project entry when discovery is unavailable. Do not assume that the task which installed a plugin has reloaded its skills.

This is Codex packaging. Native Cursor and Claude Code plugin installers are not provided; use their project entries above.

## Updates, rollback and removal

Review a new edition in a separate checkout. Verify its pin, compare changed instructions and checks, then deliberately update only the project's marked entry and version record. Keep the previous checkout and project pin until the new version is accepted.

An observed upgrade to 0.2.0 removed the previous Codex cache directory. A cache is therefore unsuitable as the only copy of a project pin. For rollback, restore the project's entry to its preserved, verified checkout. Reinstalling an older native plugin additionally depends on the host's supported commands and has not been qualified here.

Use the host's supported removal controls for an installed plugin. Removing a plugin does not authorize deleting project outputs or a pinned checkout used by another project. Removal behavior still requires host-specific verification.

## Scope of the evidence

The [0.2.0 record](docs/QUALITY-020-RELEASE.md) describes its installation, payload checks, automated tests and bounded fictional examples. Version 0.2.1 corrects the public onboarding. Earlier host checks do not automatically qualify this edition on another machine.

The package remains for supervised evaluation. Human aesthetic acceptance, real client outcomes, accessibility, physical display behavior and provider operations must be checked for the selected project. Optional books require your own authorized compatible local collection; no public book download is included.
