"""Schema 2.0 current handoff reconciliation regressions."""
# Version-Timestamp: 2026-09-16 18:39:54 AST
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from design_system.validation import validate


class CurrentHandoffTests(unittest.TestCase):
    def write(self, root, name, content):
        path = root / name
        path.write_text(content, encoding="utf-8")
        return {"path": name, "sha256": hashlib.sha256(content.encode()).hexdigest()}

    def record(self, root):
        candidate = self.write(root, "candidate.txt", "candidate-v1")
        evidence = self.write(root, "evidence.txt", "check-evidence")
        return {
            "schema_version": "2.0",
            "record_id": "handoff-current",
            "scope": "phase-only",
            "readiness": "ready",
            "requested_action": "review",
            "stage": "design",
            "owner": "synthetic-author",
            "next_action": "Review candidate",
            "completion": "complete",
            "inputs": [],
            "outputs": [copy.deepcopy(candidate)],
            "candidate": {"artifacts": [copy.deepcopy(candidate)], "approval": {"status": "none"}},
            "registry": {
                "personas": ["P-1"], "use_cases": ["U-1"], "requirements": ["R-1"],
                "decisions": ["D-1"], "criteria": ["C-1"]
            },
            "traceability": [{"persona": "P-1", "use_case": "U-1", "requirement": "R-1", "decision": "D-1", "criterion": "C-1"}],
            "current_checks": [{"criterion": "C-1", "status": "passed", "candidate_artifacts": [copy.deepcopy(candidate)], "evidence": copy.deepcopy(evidence)}],
            "historical_checks": [],
            "subject_type": "persona",
        }

    def result(self, data, root):
        return validate("handoff", data, root, as_of="2026-09-16")

    def codes(self, result):
        return {item["code"] for item in result["errors"]}

    def test_ready_complete_requires_one_passing_current_result_per_criterion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            self.assertTrue(self.result(data, root)["valid"])

    def test_failed_current_result_cannot_be_hidden_by_passing_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            failed = copy.deepcopy(data["current_checks"][0])
            failed["status"] = "failed"
            failed.pop("evidence")
            data["current_checks"].append(failed)
            self.assertIn("current_check_count", self.codes(self.result(data, root)))

    def test_pending_current_result_cannot_be_hidden_by_passing_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            pending = copy.deepcopy(data["current_checks"][0])
            pending["status"] = "pending"
            pending.pop("evidence")
            data["current_checks"].append(pending)
            self.assertIn("current_check_count", self.codes(self.result(data, root)))

    def test_stale_candidate_hash_rejects_current_completion_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            (root / "candidate.txt").write_text("candidate-v2", encoding="utf-8")
            self.assertIn("hash_mismatch", self.codes(self.result(data, root)))

    def test_missing_candidate_artifact_rejects_current_completion_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            (root / "candidate.txt").unlink()
            self.assertIn("missing_file", self.codes(self.result(data, root)))

    def test_current_result_must_bind_to_the_exact_declared_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["current_checks"][0]["candidate_artifacts"][0]["sha256"] = "0" * 64
            self.assertIn("candidate_binding", self.codes(self.result(data, root)))

    def test_historical_failure_is_separate_from_a_repaired_current_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["historical_checks"] = [{
                "criterion": "C-1", "status": "failed", "candidate_artifacts": [copy.deepcopy(data["candidate"]["artifacts"][0])],
                "superseded_by": "current_checks.C-1"
            }]
            self.assertTrue(self.result(data, root)["valid"])

    def test_legacy_partial_draft_handoff_remains_readable_with_migration_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["schema_version"] = "1.0-proposed"
            data["completion"] = "partial"
            data["readiness"] = "draft"
            data["checks"] = [{"criterion": "C-1", "status": "pending"}]
            data.pop("current_checks")
            data.pop("historical_checks")
            data["candidate"] = {"approval": {"status": "none"}}
            result = self.result(data, root)
            self.assertTrue(result["valid"])
            self.assertIn("handoff_schema_migration", {item["code"] for item in result["warnings"]})

    def test_legacy_handoff_cannot_claim_complete_or_ready(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["schema_version"] = "1.0-proposed"
            data["checks"] = [{"criterion": "C-1", "status": "passed", "evidence": copy.deepcopy(data["current_checks"][0]["evidence"])}]
            data.pop("current_checks")
            data.pop("historical_checks")
            data["candidate"] = {"approval": {"status": "none"}}
            self.assertIn("handoff_schema_migration", self.codes(self.result(data, root)))

    def test_empty_criteria_cannot_claim_complete_and_ready(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["registry"]["criteria"] = []
            data["current_checks"] = []
            self.assertIn("registry_ids", self.codes(self.result(data, root)))

    def test_traversal_candidate_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            for artifact in [data["candidate"]["artifacts"][0], data["current_checks"][0]["candidate_artifacts"][0]]:
                artifact["path"] = "../candidate.txt"
            self.assertIn("unsafe_path", self.codes(self.result(data, root)))

    def test_symlink_candidate_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            (root / "candidate-link.txt").symlink_to(root / "candidate.txt")
            for artifact in [data["candidate"]["artifacts"][0], data["current_checks"][0]["candidate_artifacts"][0]]:
                artifact["path"] = "candidate-link.txt"
            self.assertIn("unsafe_path", self.codes(self.result(data, root)))

    def test_nested_symlink_candidate_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            (root / "actual").mkdir()
            (root / "actual" / "candidate.txt").write_text("candidate-v1", encoding="utf-8")
            (root / "candidate-directory").symlink_to(root / "actual", target_is_directory=True)
            for artifact in [data["candidate"]["artifacts"][0], data["current_checks"][0]["candidate_artifacts"][0]]:
                artifact["path"] = "candidate-directory/candidate.txt"
            self.assertIn("unsafe_path", self.codes(self.result(data, root)))

    def test_ready_partial_handoff_rejects_failed_or_pending_current_result(self):
        for status in ("failed", "pending"):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                data = self.record(root)
                data["completion"] = "partial"
                data["current_checks"][0]["status"] = status
                data["current_checks"][0].pop("evidence")
                self.assertIn("completion_checks", self.codes(self.result(data, root)))

    def test_duplicate_candidate_path_and_hash_pair_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            duplicate = copy.deepcopy(data["candidate"]["artifacts"][0])
            data["candidate"]["artifacts"].append(duplicate)
            data["current_checks"][0]["candidate_artifacts"].append(copy.deepcopy(duplicate))
            self.assertIn("candidate_artifacts", self.codes(self.result(data, root)))

    def test_ready_handoff_rejects_not_applicable_current_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = self.record(root)
            data["current_checks"][0]["status"] = "not_applicable"
            data["current_checks"][0].pop("evidence")
            self.assertIn("completion_checks", self.codes(self.result(data, root)))
