"""Deterministic package build checks for Visual Design Studio."""
# Version-Timestamp: 2026-09-27 14:43:14 AST
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CLI = Path(__file__).resolve().parents[1] / "tools" / "build_plugin.py"
STAMP = "2026-09-16T18:04:00-04:00"


class BuildPluginTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.source = root / "curated"
        self.plugin = root / "plugin"
        (self.source / "tools").mkdir(parents=True)
        (self.plugin / ".codex-plugin").mkdir(parents=True)
        (self.plugin / "library" / "examples" / "assets").mkdir(parents=True)
        (self.source / "tools" / "reference_library.py").write_bytes(b"canonical reference bytes\n")
        (self.source / "tools" / "import_reference_archive.py").write_bytes(b"canonical archive importer bytes\n")
        (self.plugin / ".codex-plugin" / "plugin.json").write_text(json.dumps({"name": "visual-design-studio", "version": "0.2.0"}), encoding="utf-8")
        (self.plugin / "library" / "README.md").write_text("library\n", encoding="utf-8")
        (self.plugin / "library" / "examples" / "assets" / "font.license").write_text("license\n", encoding="utf-8")
        (self.plugin / "library" / "examples" / "assets" / "image.png").write_bytes(b"asset-bytes")

    def invoke(self, *args, plugin_root=None, source_root=None):
        return subprocess.run([
            sys.executable, str(CLI), "--plugin-root", str(plugin_root or self.plugin), "--source-root", str(source_root or self.source),
            "--version", "0.2.0", "--timestamp", STAMP, *args,
        ], capture_output=True, text=True)

    def apply(self):
        result = self.invoke("--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def test_apply_then_check_is_deterministic_and_hashes_every_current_file(self):
        self.assertNotEqual(self.invoke().returncode, 0)
        self.apply()
        first = {path.relative_to(self.plugin).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                 for path in self.plugin.rglob("*") if path.is_file()}
        self.assertEqual(self.invoke("--check").returncode, 0)
        self.apply()
        second = {path.relative_to(self.plugin).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in self.plugin.rglob("*") if path.is_file()}
        self.assertEqual(first, second)
        payload_paths = {line.split("  ", 1)[1] for line in (self.plugin / "PAYLOAD.sha256").read_text().splitlines()}
        self.assertEqual(payload_paths, set(second) - {"PAYLOAD.sha256"})
        checksum_paths = {line.split("  ", 1)[1] for line in (self.plugin / "library" / "CHECKSUMS.sha256").read_text().splitlines()}
        self.assertEqual(checksum_paths, {path.removeprefix("library/") for path in second if path.startswith("library/")} - {"CHECKSUMS.sha256"})
        manifest = json.loads((self.plugin / "library" / "PACKAGE-MANIFEST.json").read_text())
        self.assertEqual(manifest["canonical_source"]["path"], "curated-plugin-source")
        self.assertEqual(manifest["historical_source"]["version"], "0.1.0")
        self.assertEqual((self.source / "tools" / "reference_library.py").read_bytes(), (self.plugin / "library" / "scripts" / "reference_library.py").read_bytes())
        self.assertEqual((self.source / "tools" / "import_reference_archive.py").read_bytes(), (self.plugin / "library" / "scripts" / "import_reference_archive.py").read_bytes())
        sources = {entry['destination']: entry['source'] for entry in manifest['files']}
        self.assertEqual(sources['scripts/import_reference_archive.py'], 'tools/import_reference_archive.py')

    def test_public_distribution_does_not_claim_production_acceptance(self):
        self.apply()
        manifest = json.loads((self.plugin / "library" / "PACKAGE-MANIFEST.json").read_text())
        self.assertNotIn("distribution_ready", manifest)
        self.assertEqual(manifest["distribution_scope"], "public")
        self.assertTrue(manifest["publication_review_required"])
        self.assertEqual(manifest["status"], "public-supervised-evaluation")
        self.assertFalse(manifest["production_accepted"])
        self.assertTrue(manifest["files"])
        self.assertTrue(all(item["status"] == "versioned-evaluation-input"
                            for item in manifest["files"]))

    def test_check_detects_payload_mutation_and_generated_copy_drift(self):
        self.apply()
        (self.plugin / "library" / "README.md").write_text("changed\n", encoding="utf-8")
        self.assertNotEqual(self.invoke().returncode, 0)
        self.apply()
        (self.plugin / "library" / "scripts" / "reference_library.py").write_text("drift\n", encoding="utf-8")
        result = self.invoke()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reference_library", result.stdout)
        self.apply()
        (self.plugin / "library" / "scripts" / "import_reference_archive.py").write_text("drift\n", encoding="utf-8")
        self.assertNotEqual(self.invoke().returncode, 0)

    def test_apply_refuses_unsafe_symlink_and_ignores_private_temp_and_bytecode(self):
        (self.plugin / "library" / "linked.md").symlink_to(self.plugin / "library" / "README.md")
        self.assertNotEqual(self.invoke("--apply").returncode, 0)
        (self.plugin / "library" / "linked.md").unlink()
        (self.plugin / "private").mkdir()
        (self.plugin / "private" / "secret.txt").write_text("not packaged", encoding="utf-8")
        (self.plugin / "library" / "__pycache__").mkdir()
        (self.plugin / "library" / "__pycache__" / "x.pyc").write_bytes(b"cache")
        (self.plugin / "library" / "scratch.tmp").write_text("temporary", encoding="utf-8")
        self.apply()
        payload = (self.plugin / "PAYLOAD.sha256").read_text()
        self.assertNotIn("private/", payload)
        self.assertNotIn("__pycache__", payload)
        self.assertNotIn("scratch.tmp", payload)

    def test_refuses_symlinked_plugin_or_source_root_including_a_symlinked_parent(self):
        direct = self.plugin.parent / "plugin-link"
        direct.symlink_to(self.plugin, target_is_directory=True)
        self.assertNotEqual(self.invoke("--apply", plugin_root=direct).returncode, 0)
        parent = self.plugin.parent / "parent-link"
        parent.symlink_to(self.plugin.parent, target_is_directory=True)
        self.assertNotEqual(self.invoke("--apply", plugin_root=parent / self.plugin.name).returncode, 0)
        source = self.source.parent / "source-link"
        source.symlink_to(self.source, target_is_directory=True)
        self.assertNotEqual(self.invoke("--apply", source_root=source).returncode, 0)

    def test_crashed_builder_temporary_file_is_not_shipped(self):
        (self.plugin / "library" / ".build-plugin-interrupted").write_text("unfinished metadata")
        self.apply()
        self.assertNotIn(".build-plugin-interrupted", (self.plugin / "PAYLOAD.sha256").read_text())

    def test_refuses_secret_like_names_instead_of_packaging_them(self):
        for name in [".env", "id_rsa", "release.pem", "credentials.json"]:
            with self.subTest(name=name):
                path = self.plugin / "library" / name
                path.write_text("placeholder", encoding="utf-8")
                result = self.invoke("--apply")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("secret-like", result.stdout)
                path.unlink()


if __name__ == "__main__":
    unittest.main()
