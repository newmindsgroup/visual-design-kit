"""Packaging validator tests."""
# Version-Timestamp: 2026-10-20 02:05:00 UTC
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate_plugin  # noqa: E402

GOOD_SKILL = """---
name: sample-skill
description: Use when testing the validator with a well formed skill.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:05:00 UTC"
---

# Sample

See [ref](references/ref.md).

Catalog IDs covered: typography
"""


class ValidatorFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        plugin = self.repo / "plugins" / "visual-design-studio"
        self.plugin = plugin
        for path, data in {
            plugin / ".claude-plugin" / "plugin.json": {"name": "visual-design-studio", "version": "1.0.0"},
            plugin / ".codex-plugin" / "plugin.json": {"name": "visual-design-studio", "version": "1.0.0"},
            self.repo / ".claude-plugin" / "marketplace.json": {"name": "m", "owner": {"name": "o"}, "metadata": {"version": "1.0.0"},
                                                                 "plugins": [{"name": "visual-design-studio", "source": "./plugins/visual-design-studio", "version": "1.0.0"}]},
            self.repo / ".agents" / "plugins" / "marketplace.json": {"plugins": [{"name": "visual-design-studio"}]},
            plugin / "library" / "capabilities.json": {"capabilities": [{"id": "typography"}]},
        }.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data), encoding="utf-8")
        skill = plugin / "skills" / "sample-skill"
        (skill / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_text(GOOD_SKILL, encoding="utf-8")
        (skill / "references" / "ref.md").write_text("# Ref\n", encoding="utf-8")

    def errors(self):
        return validate_plugin.validate(self.repo)[0]

    def test_good_fixture_passes(self):
        self.assertEqual(self.errors(), [])

    def test_version_mismatch(self):
        (self.plugin / ".codex-plugin" / "plugin.json").write_text(json.dumps({"name": "visual-design-studio", "version": "0.9.0"}))
        self.assertTrue(any("version mismatch" in e for e in self.errors()))

    def test_bad_name_and_extra_keys(self):
        text = GOOD_SKILL.replace("name: sample-skill", "name: Claude_Skill").replace("license: MIT", "license: MIT\nwhen_to_use: x")
        (self.plugin / "skills" / "sample-skill" / "SKILL.md").write_text(text)
        errors = self.errors()
        self.assertTrue(any("must equal folder" in e for e in errors))
        self.assertTrue(any("not accepted by claude.ai" in e for e in errors))
        self.assertTrue(any("'claude' or 'anthropic'" in e or "lowercase" in e for e in errors))

    def test_broken_link_and_unknown_catalog_id(self):
        text = GOOD_SKILL.replace("references/ref.md", "references/missing.md").replace("covered: typography", "covered: typography, nope")
        (self.plugin / "skills" / "sample-skill" / "SKILL.md").write_text(text)
        errors = self.errors()
        self.assertTrue(any("broken link references/missing.md" in e for e in errors))
        self.assertTrue(any("unknown catalog IDs ['nope']" in e for e in errors))

    def test_links_in_code_are_ignored(self):
        text = GOOD_SKILL.replace("See [ref](references/ref.md).", "See [ref](references/ref.md) and `[x](nowhere.md)`.\n\n```\n[y](nowhere.md)\n```")
        (self.plugin / "skills" / "sample-skill" / "SKILL.md").write_text(text)
        self.assertEqual(self.errors(), [])

    def test_bin_directory_is_rejected(self):
        (self.plugin / "bin").mkdir()
        self.assertTrue(any("bin/" in e for e in self.errors()))

    def test_long_description_is_rejected(self):
        text = GOOD_SKILL.replace("description: Use when testing the validator with a well formed skill.", "description: " + "x" * 1100)
        (self.plugin / "skills" / "sample-skill" / "SKILL.md").write_text(text)
        self.assertTrue(any("limit 1024" in e for e in self.errors()))


class ShippedPackage(unittest.TestCase):
    def test_repository_packaging_is_valid(self):
        errors, _, info = validate_plugin.validate(ROOT)
        self.assertEqual(errors, [], "\n".join(errors))
        self.assertGreaterEqual(len(info["skills"]), 16)


if __name__ == "__main__":
    unittest.main()
