"""Optional toolkit integrity and two-host contract regressions.

Version-Timestamp: 2026-10-27 07:48:54 AST
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/build_toolkits.py'

class ToolkitIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name).resolve()
        self.plugin = self.repo / 'extras/fixture'
        for host in ('.codex-plugin', '.claude-plugin'):
            p = self.plugin / host / 'plugin.json'
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'name': 'fixture', 'version': '1.0.0', 'skills': './skills/'}))
        p = self.plugin / 'skills/example/SKILL.md'
        p.parent.mkdir(parents=True)
        p.write_text('---\nname: example\ndescription: Example\n---\n\n# Example\n')
        (self.plugin / 'LICENSE').write_text('MIT License\nCopyright Example\n')

    def run_builder(self, apply=False):
        return subprocess.run([sys.executable, str(SCRIPT), '--repo', str(self.repo), '--plugin', 'fixture', '--apply' if apply else '--check'], capture_output=True, text=True)

    def test_build_check_and_tamper(self):
        built = self.run_builder(True)
        self.assertEqual(built.returncode, 0, built.stderr + built.stdout)
        self.assertEqual(self.run_builder().returncode, 0)
        (self.plugin / 'skills/example/SKILL.md').write_text('changed')
        self.assertEqual(self.run_builder().returncode, 1)

    def test_check_never_creates_a_manifest(self):
        self.assertEqual(self.run_builder().returncode, 1)
        self.assertFalse((self.plugin / 'PAYLOAD.sha256').exists())

    def test_rejects_version_drift_without_write(self):
        p = self.plugin / '.codex-plugin/plugin.json'
        data = json.loads(p.read_text()); data['version'] = '2.0.0'; p.write_text(json.dumps(data))
        result = self.run_builder(True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('version', result.stdout)
        self.assertFalse((self.plugin / 'PAYLOAD.sha256').exists())

    def test_rejects_skill_name_drift(self):
        (self.plugin / 'skills/example/SKILL.md').write_text('---\nname: other\ndescription: Example\n---\n')
        self.assertEqual(self.run_builder(True).returncode, 1)

    def test_rejects_symlink_and_secret(self):
        (self.plugin / 'linked').symlink_to(self.repo / 'outside')
        self.assertEqual(self.run_builder(True).returncode, 1)
        (self.plugin / 'linked').unlink()
        (self.plugin / 'credentials.json').write_text('{}')
        self.assertEqual(self.run_builder(True).returncode, 1)

    def test_added_file_invalidates_payload(self):
        self.assertEqual(self.run_builder(True).returncode, 0)
        (self.plugin / 'extra.txt').write_text('unlisted')
        self.assertEqual(self.run_builder().returncode, 1)

    def test_invalid_manifest_has_controlled_error(self):
        (self.plugin / '.codex-plugin/plugin.json').write_text('[]')
        result = self.run_builder(True)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('manifest', result.stdout)

    def test_plugin_name_cannot_traverse(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--repo', str(self.repo), '--plugin', '../outside', '--apply'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)

if __name__ == '__main__':
    unittest.main()
