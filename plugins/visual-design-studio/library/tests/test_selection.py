"""Selection record contract regression tests."""
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
import copy
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from design_system.selection import validate_selection


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.library = Path(__file__).resolve().parents[1]
        self.catalog = self.library / "capabilities.json"

    def record(self, project, selected=None, exclusions=None, dispositions=None):
        selected = ["identity"] if selected is None else selected
        catalog = json.loads(self.catalog.read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in catalog["capabilities"]}
        selections = []
        for capability_id in selected:
            item = by_id[capability_id]
            entry = self.library / item["entry"]
            selections.append({"id": capability_id, "entry": item["entry"], "sha256": digest(entry)})
        return {
            "schema_version": "1.0",
            "catalog": {"path": "capabilities.json", "schema_version": catalog["schema_version"], "sha256": digest(self.catalog)},
            "selected": selections,
            "patterns": [],
            "excluded": exclusions or [],
            "prerequisites": dispositions or [
                {"id": "research", "disposition": "reuse", "reason": "Accepted research covers this bounded refinement.", "evidence": "records/research.json"},
                {"id": "persona", "disposition": "not_applicable", "reason": "This logo revision keeps the accepted audience scope.", "evidence": ""},
                {"id": "brand-strategy", "disposition": "reuse", "reason": "Accepted positioning remains authoritative.", "evidence": "records/strategy.json"},
            ],
            "provenance": {"original_input": "identity", "resolution_basis": "exact catalog ID", "repair_actor": "agent", "catalog_sha256": digest(self.catalog)},
        }

    def closure(self, selected):
        catalog = json.loads(self.catalog.read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in catalog["capabilities"]}
        resolved = set()
        def visit(capability_id):
            for dependency in by_id[capability_id]["depends_on"]:
                resolved.add(dependency)
                visit(dependency)
        for capability_id in selected:
            visit(capability_id)
        return resolved

    def entries(self, capability_ids):
        catalog = json.loads(self.catalog.read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in catalog["capabilities"]}
        return [{"id": capability_id, "entry": by_id[capability_id]["entry"],
                 "sha256": digest(self.library / by_id[capability_id]["entry"])}
                for capability_id in sorted(capability_ids)]

    def dispositions(self, selected):
        return [{"id": capability_id, "disposition": "reuse",
                 "reason": "Accepted bounded input remains applicable.",
                 "evidence": "records/accepted-input.json"}
                for capability_id in sorted(self.closure(selected) - set(selected))]

    def test_accepts_bounded_reuse_for_identity_revision(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            result = validate_selection(self.record(project), project, self.library)
        self.assertTrue(result["valid"], result["errors"])
        self.assertFalse(result["executes"])

    def test_rejects_changed_selected_entry_hash(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["selected"][0]["sha256"] = "0" * 64
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("hash_mismatch", {item["code"] for item in result["errors"]})

    def test_rejects_missing_transitive_dependency_disposition(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["prerequisites"] = record["prerequisites"][:-1]
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("missing_prerequisite", {item["code"] for item in result["errors"]})

    def test_rejects_conflicting_expanded_exclusion(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            result = validate_selection(self.record(project, exclusions=[{"id": "brand-strategy"}]), project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("exclusion_conflict", {item["code"] for item in result["errors"]})

    def test_media_pattern_stays_bounded_to_media_prefix(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            media_ids = [item["id"] for item in json.loads(self.catalog.read_text())["capabilities"] if item["id"].startswith("media-")]
            record = self.record(project, selected=[], dispositions=self.dispositions(media_ids))
            record["patterns"] = [{"pattern": "media-*", "entries": self.entries(media_ids)}]
            result = validate_selection(record, project, self.library)
        self.assertTrue(result["valid"], result["errors"])
        self.assertNotIn("chatgpt-images", result["expanded_patterns"]["media-*"])
        self.assertNotIn("openart-cli", result["expanded_patterns"]["media-*"])
        self.assertNotIn("higgsfield-cli", result["expanded_patterns"]["media-*"])

    def test_rejects_unknown_pattern_and_malformed_types(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["patterns"] = [{"pattern": "missing-*", "entries": []}]
            record["excluded"] = "identity"
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        codes = {item["code"] for item in result["errors"]}
        self.assertIn("unknown_pattern", codes)
        self.assertIn("type", codes)

    def test_rejects_paths_outside_trusted_roots(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["catalog"]["path"] = "../capabilities.json"
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("unsafe_path", {item["code"] for item in result["errors"]})

    def test_rejects_symlinked_catalog_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            link = self.library / "catalog-link.json"
            try:
                link.symlink_to(self.catalog)
                record["catalog"]["path"] = "catalog-link.json"
                result = validate_selection(record, project, self.library)
            finally:
                link.unlink(missing_ok=True)
        self.assertFalse(result["valid"])
        self.assertIn("unsafe_path", {item["code"] for item in result["errors"]})

    def test_rejects_unsupported_schema_version(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["schema_version"] = "2.0"
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("schema_version", {item["code"] for item in result["errors"]})

    def test_cli_validates_selection_without_execution(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record_path = project / "SELECTED-CAPABILITIES.json"
            record_path.write_text(json.dumps(self.record(project)), encoding="utf-8")
            completed = subprocess.run(
                ["python3", "-m", "design_system", "validate", "selection", str(record_path),
                 "--root", str(project), "--library-root", str(self.library)],
                cwd=self.library, text=True, capture_output=True, check=False,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
        self.assertFalse(json.loads(completed.stdout)["executes"])

    def test_rejects_stale_pattern_entry_hash(self):
        with tempfile.TemporaryDirectory() as temporary:
            record = self.record(Path(temporary), selected=[])
            record["patterns"] = [{"pattern": "identity", "entries": self.entries(["identity"])}]
            record["patterns"][0]["entries"][0]["sha256"] = "0" * 64
            result = validate_selection(record, temporary, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("hash_mismatch", {item["code"] for item in result["errors"]})

    def test_malformed_pattern_id_fails_without_exception(self):
        with tempfile.TemporaryDirectory() as temporary:
            record = self.record(Path(temporary))
            record["patterns"] = [{"pattern": "identity", "entries": [{"id": [], "entry": "x", "sha256": "0" * 64}]}]
            result = validate_selection(record, temporary, self.library)
        self.assertFalse(result["valid"])

    def test_top_level_list_is_invalid_through_direct_validator_and_cli(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            result = validate_selection([], project, self.library)
            record_path = project / "SELECTED-CAPABILITIES.json"
            record_path.write_text("[]", encoding="utf-8")
            completed = subprocess.run(
                ["python3", "-m", "design_system", "validate", "selection", str(record_path),
                 "--root", str(project), "--library-root", str(self.library)],
                cwd=self.library, text=True, capture_output=True, check=False,
            )
        self.assertFalse(result["valid"])
        self.assertIn("record_type", {item["code"] for item in result["errors"]})
        self.assertEqual(completed.returncode, 1, completed.stderr + completed.stdout)
        self.assertFalse(json.loads(completed.stdout)["valid"])

    def test_malformed_catalog_shapes_are_invalid_without_exception(self):
        for content in ("[]", '{"schema_version":"1.0-proposed","capabilities":[{"id":[],"entry":"x","depends_on":[]}]}'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temporary:
                project = Path(temporary) / "project"
                library = Path(temporary) / "library"
                project.mkdir()
                library.mkdir()
                catalog = library / "capabilities.json"
                catalog.write_text(content, encoding="utf-8")
                record = self.record(project)
                record["catalog"] = {"path": "capabilities.json", "schema_version": "1.0-proposed", "sha256": digest(catalog)}
                result = validate_selection(record, project, library)
                self.assertFalse(result["valid"])
                self.assertIn("catalog", {item["code"] for item in result["errors"]})

    def test_list_disposition_is_invalid_without_exception(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["prerequisites"][0]["disposition"] = []
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("disposition", {item["code"] for item in result["errors"]})

    def test_rejects_prerequisite_disposition_for_directly_selected_capability(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            record = self.record(project)
            record["prerequisites"].append({
                "id": "identity", "disposition": "reuse",
                "reason": "This must be selected directly, not treated as a dependency.",
                "evidence": "records/identity.json",
            })
            result = validate_selection(record, project, self.library)
        self.assertFalse(result["valid"])
        self.assertIn("prerequisite_id", {item["code"] for item in result["errors"]})
