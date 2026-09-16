"""Refresh only existing local hash references in the benchmark records."""
# Version-Timestamp: 2026-09-16 18:42:00 AST
import argparse
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
LIBRARY = HERE.parents[2]
RECORDS = ("evidence.json", "handoff.json", "selection.json")


class RecordError(ValueError):
    pass


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RecordError(f"unreadable record: {path.name}") from exc


def local_file(relative):
    if not isinstance(relative, str) or not relative:
        raise RecordError("reference path must be nonempty text")
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise RecordError(f"unsafe reference: {relative}")
    candidate = LIBRARY
    for part in rel.parts:
        candidate /= part
        if candidate.is_symlink():
            raise RecordError(f"symlinked reference: {relative}")
    candidate = candidate.resolve()
    if not candidate.is_relative_to(LIBRARY) or not candidate.is_file():
        raise RecordError(f"missing local reference: {relative}")
    return candidate


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def refresh_references(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and "sha256" in value:
            value["sha256"] = sha256(local_file(value["path"]))
        for item in value.values():
            refresh_references(item)
    elif isinstance(value, list):
        for item in value:
            refresh_references(item)


def refresh_selection(record):
    catalog_ref = record.get("catalog")
    if not isinstance(catalog_ref, dict) or catalog_ref.get("path") != "capabilities.json":
        raise RecordError("selection catalog must remain capabilities.json")
    catalog_bytes = local_file("capabilities.json").read_bytes()
    catalog_ref["sha256"] = hashlib.sha256(catalog_bytes).hexdigest()
    try:
        by_id = {item["id"]: item for item in json.loads(catalog_bytes)["capabilities"]}
    except (TypeError, KeyError, json.JSONDecodeError) as exc:
        raise RecordError("current capabilities catalog is malformed") from exc
    entries = list(record.get("selected", []))
    for pattern in record.get("patterns", []):
        if isinstance(pattern, dict):
            entries.extend(pattern.get("entries", []))
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("id") not in by_id:
            raise RecordError("selection contains an unknown capability")
        entry["entry"] = by_id[entry["id"]]["entry"]
        entry["sha256"] = sha256(local_file(entry["entry"]))
    provenance = record.get("provenance")
    if isinstance(provenance, dict):
        provenance["catalog_sha256"] = catalog_ref["sha256"]


def replace_declared_hash(value, path, digest):
    if isinstance(value, dict):
        if value.get("path") == path and "sha256" in value:
            value["sha256"] = digest
        for item in value.values():
            replace_declared_hash(item, path, digest)
    elif isinstance(value, list):
        for item in value:
            replace_declared_hash(item, path, digest)


def canonical(value):
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def expected_records():
    records = {name: load(HERE / name) for name in RECORDS}
    refresh_references(records["evidence.json"])
    evidence_bytes = canonical(records["evidence.json"]).encode("utf-8")
    refresh_references(records["handoff.json"])
    replace_declared_hash(records["handoff.json"], "examples/quality-benchmark/contract-examples/evidence.json", hashlib.sha256(evidence_bytes).hexdigest())
    refresh_selection(records["selection.json"])
    return {name: canonical(value) for name, value in records.items()}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Compare current records only. This is the default.")
    mode.add_argument("--apply", action="store_true", help="Write refreshed declared hashes.")
    args = parser.parse_args(argv)
    try:
        expected = expected_records()
        drift = [name for name, content in expected.items() if (HERE / name).read_text(encoding="utf-8") != content]
        if args.apply:
            for name in drift:
                (HERE / name).write_text(expected[name], encoding="utf-8")
            drift = []
        result = {"valid": not drift, "changed": drift, "applied": args.apply}
    except RecordError as exc:
        result = {"valid": False, "changed": [], "applied": False, "error": str(exc)}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
