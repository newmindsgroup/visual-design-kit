"""Build or verify deterministic Visual Design Studio package metadata."""
# Version-Timestamp: 2026-09-27 14:43:14 AST
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile


OUTPUTS = {
    "PAYLOAD.sha256",
    "library/PACKAGE-MANIFEST.json",
    "library/CHECKSUMS.sha256",
}
REFERENCE_SOURCE = "tools/reference_library.py"
REFERENCE_TARGET = "library/scripts/reference_library.py"
CANONICAL_SOURCES = {
    REFERENCE_TARGET: REFERENCE_SOURCE,
    "library/scripts/import_reference_archive.py": "tools/import_reference_archive.py",
}
HISTORICAL_SOURCE = {
    "version": "0.1.0",
    "commit": "412e628",
    "payload_sha256": "dcca91274b676de49a0d4ee086aa7f4d6264c7ce8428cb259cdd0123c6683e4e",
    "statement": "Historical baseline only. These hashes do not verify current candidate bytes.",
}


class BuildError(ValueError):
    pass


def digest(content):
    return hashlib.sha256(content).hexdigest()


def ignored(relative):
    parts = relative.parts
    return (any(part in {".git", "private", "__pycache__", "tmp", "temp"} for part in parts)
            or relative.name.startswith(".build-plugin-") or relative.name == ".DS_Store" or relative.name.endswith((".pyc", ".tmp", "~")))


def secret_like(relative):
    name = relative.name.lower()
    return (name in {".env", "id_rsa", "id_ed25519", "credentials.json"}
            or name.startswith((".env.", "credentials", "secret"))
            or name.endswith((".pem", ".key", ".p12", ".pfx")))


def checked_root(value, label):
    raw = Path(value).expanduser().absolute()
    current = Path(raw.anchor)
    for part in raw.parts[1:]:
        current /= part
        if current.is_symlink():
            raise BuildError(f"unsafe {label} symlink: {current}")
    if not raw.is_dir():
        raise BuildError(f"{label} must be a regular directory")
    return raw.resolve()


def regular_files(root):
    root = checked_root(root, "plugin root")
    files = {}
    for current, directories, names in os.walk(root, followlinks=False):
        current_path = Path(current)
        retained = []
        for name in directories:
            candidate = current_path / name
            rel = candidate.relative_to(root)
            if ignored(rel):
                continue
            if candidate.is_symlink():
                raise BuildError(f"unsafe symlink: {rel.as_posix()}")
            retained.append(name)
        directories[:] = retained
        for name in names:
            candidate = current_path / name
            rel = candidate.relative_to(root)
            if ignored(rel):
                continue
            if candidate.is_symlink():
                raise BuildError(f"unsafe symlink: {rel.as_posix()}")
            if secret_like(rel):
                raise BuildError(f"secret-like file name: {rel.as_posix()}")
            if not candidate.is_file():
                raise BuildError(f"non-regular file: {rel.as_posix()}")
            files[rel.as_posix()] = candidate.read_bytes()
    return files


def output_path(plugin_root, relative):
    path = plugin_root / relative
    if path.is_symlink():
        raise BuildError(f"unsafe output symlink: {relative}")
    return path


def sha_lines(files):
    return "".join(f"{digest(files[path])}  {path}\n" for path in sorted(files))


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def expected_files(plugin_root, source_root, version, timestamp):
    plugin_root = checked_root(plugin_root, "plugin root")
    source_root = checked_root(source_root, "source root")
    if not isinstance(version, str) or not version.strip():
        raise BuildError("version must be nonempty")
    if not isinstance(timestamp, str) or not timestamp.strip():
        raise BuildError("timestamp must be nonempty")
    plugin_json = output_path(plugin_root, ".codex-plugin/plugin.json")
    try:
        metadata = json.loads(plugin_json.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise BuildError("unreadable plugin.json") from exc
    if metadata.get("version") != version:
        raise BuildError("--version must exactly match .codex-plugin/plugin.json")
    source_bytes = {}
    for target, relative in CANONICAL_SOURCES.items():
        source = source_root / relative
        if source.is_symlink() or not source.is_file():
            raise BuildError("canonical reference tool must be a regular file")
        source_bytes[target] = source.read_bytes()
    for relative in OUTPUTS | set(CANONICAL_SOURCES):
        output_path(plugin_root, relative)
    current = regular_files(plugin_root)
    for relative in OUTPUTS | set(CANONICAL_SOURCES):
        current.pop(relative, None)
    current.update(source_bytes)
    library = {path.removeprefix("library/"): content for path, content in current.items() if path.startswith("library/")}
    manifest_files = []
    for destination in sorted(path for path in library if path not in {"PACKAGE-MANIFEST.json", "CHECKSUMS.sha256"}):
        source_path = CANONICAL_SOURCES.get(f"library/{destination}", f"curated-plugin-source/{destination}")
        manifest_files.append({
            "destination": destination,
            "sha256": digest(library[destination]),
            "source": source_path,
            "status": "versioned-evaluation-input",
        })
    manifest = {
        "Version-Timestamp": timestamp,
        "canonical_source": {"path": "curated-plugin-source", "version": version, "meaning": "Logical identity of the current plugin library bytes; not a second filesystem directory. Reference helper and optional archive importer are copied from tools/."},
        "candidate": version,
        "distribution_scope": "public",
        "publication_review_required": True,
        "production_accepted": False,
        "files": manifest_files,
        "historical_source": HISTORICAL_SOURCE,
        "status": "public-supervised-evaluation",
    }
    current["library/PACKAGE-MANIFEST.json"] = json_bytes(manifest)
    library_with_manifest = {path.removeprefix("library/"): content for path, content in current.items() if path.startswith("library/") and path != "library/CHECKSUMS.sha256"}
    current["library/CHECKSUMS.sha256"] = sha_lines(library_with_manifest).encode("utf-8")
    payload = {path: content for path, content in current.items() if path != "PAYLOAD.sha256"}
    current["PAYLOAD.sha256"] = sha_lines(payload).encode("utf-8")
    return current


def compare(plugin_root, expected):
    actual = regular_files(plugin_root)
    errors = []
    for relative in sorted(OUTPUTS | set(CANONICAL_SOURCES)):
        if relative not in actual:
            errors.append(f"missing {relative}")
        elif actual[relative] != expected[relative]:
            errors.append(f"mismatch {relative}")
    return errors


def replace(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".build-plugin-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def build(plugin_root, source_root, version, timestamp, apply=False):
    expected = expected_files(plugin_root, source_root, version, timestamp)
    plugin_root = checked_root(plugin_root, "plugin root")
    if apply:
        for relative in [*sorted(CANONICAL_SOURCES), "library/PACKAGE-MANIFEST.json", "library/CHECKSUMS.sha256", "PAYLOAD.sha256"]:
            replace(output_path(plugin_root, relative), expected[relative])
    errors = compare(plugin_root, expected)
    return {"valid": not errors, "errors": errors, "applied": apply, "version": version}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", required=True, type=Path)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--timestamp", required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Compare expected bytes only. This is the default.")
    mode.add_argument("--apply", action="store_true", help="Write generated payload metadata. Default is check only.")
    args = parser.parse_args(argv)
    try:
        result = build(args.plugin_root, args.source_root, args.version, args.timestamp, args.apply)
    except BuildError as exc:
        result = {"valid": False, "errors": [str(exc)], "applied": False, "version": args.version}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
