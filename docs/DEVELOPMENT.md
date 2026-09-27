# Development checks

Version-Timestamp: 2026-09-27 13:45:10 AST

Use a development checkout for these checks. Keep active project pins unchanged. The commands below use macOS or Linux shell syntax. Run them against trusted, verified package bytes and record the checkout commit, tool versions and results.

## Core checks

Python 3.9 or newer is required. The root and library Python suites use the standard library. From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Then from `plugins/visual-design-studio/library`:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
node --test examples/screen-production/player.test.mjs examples/media-quality-recipes/touch-session/session.test.mjs
```

Use a Node.js version that supports `node --test`. No npm packages are required for these two test files. Check `python3 --version` and `node --version` when recording results.

The [0.2.0 evidence](QUALITY-020-RELEASE.md) records 12 root Python tests, 51 library Python tests and 11 Node tests. These are historical counts, not a substitute for running the current checkout. Structural tests do not establish design quality, accessibility conformance or human acceptance.

## Preview the fictional examples

From `plugins/visual-design-studio/library`:

```sh
python3 -m http.server 17672 --bind 127.0.0.1
```

Open `http://127.0.0.1:17672/examples/quality-benchmark/`. Keep this terminal running while browser checks use the page. The server is bound to the local computer. Do not serve a client-data directory.

## Optional browser and export dependencies

The root `tools/` scripts require additional software:

| Script | Required software |
| --- | --- |
| `check_quality_examples.py` | Python Playwright package and its Chromium browser |
| `check_quality_video.py` | Python Playwright package and its Chromium browser |
| `export_quality_examples.py` | Python Playwright and Pillow packages, Chromium, and an FFmpeg executable for video export |

From the repository root, create an isolated environment under the ignored `private/` directory:

```sh
python3 -m venv private/qa-venv
private/qa-venv/bin/python -m pip install playwright Pillow
private/qa-venv/bin/python -m playwright install chromium
private/qa-venv/bin/python -m pip freeze
```

The last command records the versions selected in your environment. This repository does not supply a dependency lock for optional QA tools. Install FFmpeg separately if exporting video and pass its executable path explicitly. Python packages do not install FFmpeg for this workflow. Browser installation may also need operating-system packages; follow the installed Playwright tool's instructions for your host.

With the preview server running, execute browser checks from the repository root:

```sh
private/qa-venv/bin/python tools/check_quality_examples.py --base-url http://127.0.0.1:17672/examples/quality-benchmark/ --outdir private/qa-browser
```

The report and screenshots are written to `private/qa-browser`. Inspect the screenshots and any failed checks. A successful browser report covers the scripted cases only.

## Optional exports and video checks

Read each tool's arguments before use:

```sh
private/qa-venv/bin/python tools/export_quality_examples.py --help
private/qa-venv/bin/python tools/check_quality_video.py --help
```

The exporter requires `--base-url`, a new `--output` directory and `--ffmpeg` with the installed executable path. It refuses an existing output directory. Keep generated outputs outside a project's pinned package. The video checker expects the selected WebM to be served at `exports/tidal-motion.webm` beneath its `--base-url`, and verifies those served bytes against `--video-file`. Run it only with a matching served file and a new `--report` path.

Neither an export nor a browser playback check proves native application fidelity, physical screen compatibility or human visual approval. Record those separately when a project needs them.

## Package changes

Changes inside `plugins/visual-design-studio` invalidate the current payload digest. Rebuild the manifests using `tools/build_plugin.py` as part of a reviewed package revision, verify all listed files, and update `docs/VERIFIED-PIN.md` with the resulting digest. Never repair an installed cache or an active project pin in place. Existing projects adopt a new revision explicitly.
