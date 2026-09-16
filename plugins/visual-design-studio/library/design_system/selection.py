"""Validate read-only capability selection records against a trusted catalog."""
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
import fnmatch
import hashlib
import json
from pathlib import Path

from .validation import MAX_BYTES, catalog_plan, load_json

VERSION = "1.0"


def _sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _inside(root, value):
    """Return a real, regular, exact-case descendant of root, or None."""
    if not isinstance(value, str) or not value:
        return None
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        return None
    candidate = root / relative
    current = root
    try:
        for part in relative.parts:
            if current.is_symlink():
                return None
            names = {child.name for child in current.iterdir()}
            if part not in names:
                return None
            current = current / part
        resolved = candidate.resolve(strict=True)
        if candidate.is_symlink() or not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
            return None
    except (OSError, RuntimeError):
        return None
    return resolved


class _Report:
    def __init__(self):
        self.errors = []

    def error(self, code, path, message):
        self.errors.append({"code": code, "path": path, "message": message})

    def result(self, expanded_patterns):
        return {
            "valid": not self.errors,
            "errors": self.errors,
            "warnings": [],
            "expanded_patterns": expanded_patterns,
            "executes": False,
            "assurance": "Selection structure and current local bytes only; no capability execution or approval.",
        }


def _records(report, value, path, required=True):
    if not isinstance(value, list):
        report.error("type", path, "Expected an array")
        return []
    if required and not value:
        report.error("required", path, "At least one selection is required")
    return value


def _expand(report, entries, by_id, path, library_root):
    output = []
    seen = set()
    for index, entry in enumerate(entries):
        item_path = f"{path}.{index}"
        if not isinstance(entry, dict) or set(entry) != {"pattern", "entries"}:
            report.error("type", item_path, "Pattern requires only pattern and entries")
            continue
        pattern, supplied = entry.get("pattern"), entry.get("entries")
        if not isinstance(pattern, str) or not pattern or not isinstance(supplied, list):
            report.error("type", item_path, "Pattern text and expanded entry array required")
            continue
        matches = sorted(key for key in by_id if fnmatch.fnmatchcase(key, pattern))
        if not matches:
            report.error("unknown_pattern", item_path + ".pattern", "Pattern matches no current catalog IDs")
        supplied_ids = [item.get("id") for item in supplied if isinstance(item, dict)]
        if len(supplied_ids) != len(supplied) or any(not isinstance(x, str) for x in supplied_ids) or len(set(supplied_ids)) != len(supplied_ids) or sorted(supplied_ids) != matches:
            report.error("pattern_expansion", item_path + ".entries", "Entries must exactly list the current pattern expansion")
        for item in supplied:
            _selected_entry(report, item, by_id, item_path + ".entries", library_root)
        if pattern in seen:
            report.error("duplicate_pattern", item_path + ".pattern", "Each pattern may appear once")
        seen.add(pattern)
        output.extend(matches)
    return output


def _selected_entry(report, item, by_id, path, library_root):
    if not isinstance(item, dict) or set(item) != {"id", "entry", "sha256"}:
        report.error("type", path, "Capability requires only id, entry and sha256")
        return None
    capability_id, entry, expected = item.get("id"), item.get("entry"), item.get("sha256")
    if not isinstance(capability_id, str) or capability_id not in by_id:
        report.error("unknown_id", path + ".id", "Capability ID is not in the current catalog")
        return None
    catalog_entry = by_id[capability_id].get("entry")
    if entry != catalog_entry:
        report.error("catalog_entry", path + ".entry", "Entry must exactly match the catalog entry")
    if not isinstance(expected, str) or len(expected) != 64 or any(char not in "0123456789abcdef" for char in expected):
        report.error("hash_format", path + ".sha256", "SHA-256 must be 64 lowercase hexadecimal characters")
    elif library_root is not None:
        target = _inside(library_root, entry)
        if target is None:
            report.error("unsafe_path", path + ".entry", "Entry must be an exact-case regular file inside library root")
        elif _sha256(target) != expected:
            report.error("hash_mismatch", path + ".sha256", "Entry bytes differ from recorded SHA-256")
    return capability_id


def validate_selection(data, root, library_root):
    """Validate a selection v1.0 record. This function never executes capabilities."""
    report = _Report()
    expanded_patterns = {}
    try:
        raw_project_root = Path(root)
        raw_library_root = Path(library_root)
        if raw_project_root.is_symlink() or raw_library_root.is_symlink():
            raise OSError("Trusted roots cannot be symlinks")
        project_root = raw_project_root.resolve(strict=True)
        trusted_library = raw_library_root.resolve(strict=True)
    except (OSError, RuntimeError, TypeError):
        report.error("unsafe_path", "root", "Project and library roots must exist")
        return report.result(expanded_patterns)
    if not project_root.is_dir() or not trusted_library.is_dir() or project_root.is_symlink() or trusted_library.is_symlink():
        report.error("unsafe_path", "root", "Roots must be regular directories")
        return report.result(expanded_patterns)
    if not isinstance(data, dict):
        report.error("record_type", "", "Top-level record must be an object")
        return report.result(expanded_patterns)
    if data.get("schema_version") != VERSION:
        report.error("schema_version", "schema_version", "Unsupported selection schema version")
        return report.result(expanded_patterns)
    allowed = {"Version-Timestamp", "schema_version", "catalog", "selected", "patterns", "excluded", "prerequisites", "provenance"}
    unknown = set(data) - allowed
    if unknown:
        report.error("unknown_field", "", "Unsupported selection record field")
    catalog_ref = data.get("catalog")
    catalog = None
    if not isinstance(catalog_ref, dict) or set(catalog_ref) != {"path", "schema_version", "sha256"}:
        report.error("type", "catalog", "Catalog requires only path, schema_version and sha256")
    else:
        catalog_path = _inside(trusted_library, catalog_ref.get("path"))
        if catalog_path is None:
            report.error("unsafe_path", "catalog.path", "Catalog must be an exact-case regular file inside library root")
        elif catalog_ref.get("path") != "capabilities.json":
            report.error("catalog_identity", "catalog.path", "Selection uses the library capabilities.json identity")
        elif not isinstance(catalog_ref.get("sha256"), str) or len(catalog_ref["sha256"]) != 64 or any(char not in "0123456789abcdef" for char in catalog_ref["sha256"]):
            report.error("hash_format", "catalog.sha256", "SHA-256 must be 64 lowercase hexadecimal characters")
        elif _sha256(catalog_path) != catalog_ref["sha256"]:
            report.error("hash_mismatch", "catalog.sha256", "Catalog bytes differ from recorded SHA-256")
        else:
            try:
                loaded_catalog = load_json(catalog_path)
                if not isinstance(loaded_catalog, dict):
                    raise ValueError("Catalog must be an object")
                if loaded_catalog.get("schema_version") != catalog_ref.get("schema_version"):
                    report.error("catalog_version", "catalog.schema_version", "Catalog version differs from current bytes")
                catalog_plan(loaded_catalog, [loaded_catalog["capabilities"][0]["id"]])
                if any(not isinstance(item, dict) or not isinstance(item.get("entry"), str) or not item["entry"] for item in loaded_catalog["capabilities"]):
                    raise ValueError("Catalog entries require paths")
                catalog = loaded_catalog
            except (AttributeError, ValueError, TypeError, KeyError, IndexError, OSError):
                catalog = None
                report.error("catalog", "catalog", "Catalog is malformed or cannot be planned")
    if catalog is None:
        return report.result(expanded_patterns)
    by_id = {entry["id"]: entry for entry in catalog["capabilities"]}
    selected = _records(report, data.get("selected"), "selected", required=False)
    selected_ids = [_selected_entry(report, item, by_id, f"selected.{index}", trusted_library) for index, item in enumerate(selected)]
    patterns = _records(report, data.get("patterns"), "patterns", required=False)
    pattern_ids = _expand(report, patterns, by_id, "patterns", trusted_library)
    for item in patterns:
        if isinstance(item, dict) and isinstance(item.get("pattern"), str):
            expanded_patterns[item["pattern"]] = sorted(key for key in by_id if fnmatch.fnmatchcase(key, item["pattern"]))
    chosen = [key for key in selected_ids + pattern_ids if key is not None]
    if not chosen:
        report.error("required", "selected", "Select an exact capability or a nonempty pattern")
    if len(chosen) != len(set(chosen)):
        report.error("duplicate_selection", "selected", "A capability may be selected once across IDs and patterns")
    try:
        closure = set(catalog_plan(catalog, chosen)) if chosen else set()
    except ValueError:
        report.error("dependency", "selected", "Selected capability dependencies are unresolved or cyclic")
        closure = set()
    excluded = _records(report, data.get("excluded"), "excluded", required=False)
    excluded_ids = set()
    for index, item in enumerate(excluded):
        path = f"excluded.{index}"
        if not isinstance(item, dict) or (set(item) != {"id"} and set(item) != {"pattern"}):
            report.error("type", path, "Exclusion requires exactly id or pattern")
            continue
        if "id" in item:
            if not isinstance(item["id"], str) or item["id"] not in by_id:
                report.error("unknown_id", path + ".id", "Excluded ID is not in the current catalog")
            else:
                excluded_ids.add(item["id"])
        else:
            pattern = item["pattern"]
            matches = {key for key in by_id if isinstance(pattern, str) and fnmatch.fnmatchcase(key, pattern)}
            if not isinstance(pattern, str) or not pattern or not matches:
                report.error("unknown_pattern", path + ".pattern", "Exclusion pattern matches no current catalog IDs")
            excluded_ids.update(matches)
    conflicts = closure & excluded_ids
    if conflicts:
        report.error("exclusion_conflict", "excluded", "Exclusion intersects selected or transitive dependency: " + ", ".join(sorted(conflicts)))
    prerequisites = _records(report, data.get("prerequisites"), "prerequisites", required=False)
    dispositions = {}
    for index, item in enumerate(prerequisites):
        path = f"prerequisites.{index}"
        if not isinstance(item, dict) or set(item) != {"id", "disposition", "reason", "evidence"}:
            report.error("type", path, "Prerequisite requires id, disposition, reason and evidence")
            continue
        capability_id = item.get("id")
        if not isinstance(capability_id, str) or capability_id not in closure or capability_id in chosen:
            report.error("prerequisite_id", path + ".id", "Prerequisite must be a transitive dependency, not a directly selected capability")
            continue
        if capability_id in dispositions:
            report.error("duplicate_prerequisite", path + ".id", "Each prerequisite has one disposition")
        dispositions[capability_id] = item
        disposition = item.get("disposition")
        if not isinstance(disposition, str) or disposition not in {"reuse", "create", "provisional", "not_applicable"}:
            report.error("disposition", path + ".disposition", "Use reuse, create, provisional or not_applicable")
        if not isinstance(item.get("reason"), str) or not item["reason"].strip():
            report.error("required", path + ".reason", "A scope-specific reason is required")
        evidence = item.get("evidence")
        if not isinstance(evidence, str):
            report.error("type", path + ".evidence", "Evidence must be text")
        elif disposition != "not_applicable" and not evidence.strip():
            report.error("required", path + ".evidence", "Reuse, create and provisional dispositions require evidence")
    for capability_id in closure - set(chosen):
        if capability_id not in dispositions:
            report.error("missing_prerequisite", "prerequisites", "Missing disposition for dependency " + capability_id)
    provenance = data.get("provenance")
    if not isinstance(provenance, dict) or set(provenance) != {"original_input", "resolution_basis", "repair_actor", "catalog_sha256"}:
        report.error("type", "provenance", "Provenance requires original_input, resolution_basis, repair_actor and catalog_sha256")
    else:
        for key in ("original_input", "resolution_basis", "repair_actor"):
            if not isinstance(provenance.get(key), str) or not provenance[key].strip():
                report.error("required", "provenance." + key, "Nonempty provenance text required")
        if provenance.get("catalog_sha256") != catalog_ref.get("sha256"):
            report.error("provenance", "provenance.catalog_sha256", "Provenance must bind the current catalog hash")
    return report.result(expanded_patterns)
