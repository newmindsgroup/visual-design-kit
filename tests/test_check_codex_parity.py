"""Codex parity checker: manifest, versions, skills, agent fallback, skill mirror.

Version-Timestamp: 2026-10-23 18:00:00 UTC
"""

import contextlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("check_codex_parity", ROOT / "tools" / "check_codex_parity.py")
parity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(parity)

SKILL = "---\nname: {name}\ndescription: >-\n  Does {name} work.\nmetadata:\n  version-timestamp: \"2026-10-23\"\n---\n\n# {name}\n\n{body}\n"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, data):
    write(path, json.dumps(data, indent=2))


class Fixture:
    """A minimal kit layout that passes every check."""

    def __init__(self, base, version="1.2.3"):
        self.repo = Path(base)
        self.plugin = self.repo / "plugins" / "visual-design-studio"
        write_json(self.plugin / ".codex-plugin" / "plugin.json",
                   {"name": "visual-design-studio", "version": version, "skills": "./skills/"})
        write_json(self.plugin / ".claude-plugin" / "plugin.json", {"name": "visual-design-studio", "version": version})
        write_json(self.repo / ".claude-plugin" / "marketplace.json", {
            "metadata": {"version": version},
            "plugins": [{"name": "visual-design-studio", "source": "./plugins/visual-design-studio", "version": version}],
        })
        write_json(self.repo / ".agents" / "plugins" / "marketplace.json", {
            "plugins": [{"name": "visual-design-studio",
                         "source": {"source": "local", "path": "./plugins/visual-design-studio"}}],
        })
        write(self.plugin / "agents" / "scout-agent.md", "---\nname: scout-agent\n---\n")
        write(self.plugin / "skills" / "alpha" / "SKILL.md", SKILL.format(name="alpha", body="Plain skill."))
        write(self.plugin / "skills" / "beta" / "SKILL.md", SKILL.format(
            name="beta", body="Dispatch `scout-agent` per lane ([lanes](references/lanes.md))."))
        write(self.plugin / "skills" / "beta" / "references" / "lanes.md",
              "# Lanes\n\nUse scout-agent.\n\n## Single-context fallback (hosts without plugin agents)\n\nDo it inline.\n")
        for side in (".agents", ".claude"):
            write(self.repo / side / "skills" / "kit-maint" / "SKILL.md", "same\n")

    def run(self):
        return parity.run(self.repo)


class CodexParity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.kit = Fixture(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def failing(self, result):
        return {name for name, state in result["checks"].items() if state == "fail"}

    def test_fixture_passes(self):
        result = self.kit.run()
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["version"], "1.2.3")
        self.assertEqual(result["skills"], 2)
        self.assertEqual(result["agents"], ["scout-agent"])

    def test_this_repository_passes(self):
        result = parity.run(ROOT)
        self.assertTrue(result["valid"], result["errors"])

    def test_missing_codex_manifest(self):
        (self.kit.plugin / ".codex-plugin" / "plugin.json").unlink()
        result = self.kit.run()
        self.assertIn("manifest", self.failing(result))
        self.assertIn("skills", self.failing(result))

    def test_skills_key_required_and_must_resolve(self):
        path = self.kit.plugin / ".codex-plugin" / "plugin.json"
        write_json(path, {"name": "visual-design-studio", "version": "1.2.3"})
        self.assertIn("manifest", self.failing(self.kit.run()))
        write_json(path, {"name": "visual-design-studio", "version": "1.2.3", "skills": "./nowhere/"})
        self.assertIn("manifest", self.failing(self.kit.run()))
        write_json(path, {"name": "visual-design-studio", "version": "1.2.3", "skills": "../../"})
        self.assertIn("manifest", self.failing(self.kit.run()))

    def test_version_mismatch(self):
        write_json(self.kit.plugin / ".codex-plugin" / "plugin.json",
                   {"name": "visual-design-studio", "version": "9.9.9", "skills": "./skills/"})
        result = self.kit.run()
        self.assertEqual(self.failing(result), {"versions"})
        self.assertTrue(any("9.9.9" in e for e in result["errors"]))

    def test_marketplace_entry_version_mismatch(self):
        write_json(self.kit.repo / ".claude-plugin" / "marketplace.json", {
            "metadata": {"version": "1.2.3"},
            "plugins": [{"name": "visual-design-studio", "version": "1.2.2"}],
        })
        self.assertEqual(self.failing(self.kit.run()), {"versions"})

    def test_codex_marketplace_must_list_plugin(self):
        write_json(self.kit.repo / ".agents" / "plugins" / "marketplace.json", {"plugins": []})
        self.assertEqual(self.failing(self.kit.run()), {"versions"})

    def test_skill_needs_name_and_description(self):
        write(self.kit.plugin / "skills" / "alpha" / "SKILL.md", "---\nname: wrong\n---\n\nBody\n")
        result = self.kit.run()
        self.assertEqual(self.failing(result), {"skills"})
        self.assertEqual(len([e for e in result["errors"] if "alpha" in e]), 2)

    def test_skill_folder_without_skill_md(self):
        (self.kit.plugin / "skills" / "gamma").mkdir()
        self.assertEqual(self.failing(self.kit.run()), {"skills"})

    def test_agent_mention_without_fallback_fails(self):
        write(self.kit.plugin / "skills" / "alpha" / "references" / "panel.md", "Ask scout-agent to review.\n")
        result = self.kit.run()
        self.assertEqual(self.failing(result), {"fallback"})
        self.assertTrue(any("panel.md" in e and "scout-agent" in e for e in result["errors"]))

    def test_without_subagents_line_is_a_marker(self):
        write(self.kit.plugin / "skills" / "alpha" / "references" / "panel.md",
              "Ask scout-agent to review.\n\n- **Without subagents:** review in one context.\n")
        self.assertTrue(self.kit.run()["valid"])

    def test_link_to_fallback_file_counts(self):
        write(self.kit.plugin / "skills" / "alpha" / "references" / "panel.md",
              "Ask scout-agent ([fallback](../../beta/references/lanes.md#single-context-fallback)).\n")
        self.assertTrue(self.kit.run()["valid"])

    def test_agent_name_inside_longer_word_ignored(self):
        write(self.kit.plugin / "skills" / "alpha" / "references" / "notes.md", "A super-scout-agents list.\n")
        self.assertTrue(self.kit.run()["valid"])

    def test_mirror_drift(self):
        write(self.kit.repo / ".claude" / "skills" / "kit-maint" / "SKILL.md", "edited\n")
        write(self.kit.repo / ".claude" / "skills" / "extra" / "SKILL.md", "stray\n")
        result = self.kit.run()
        self.assertEqual(self.failing(result), {"mirror"})
        self.assertEqual(len(result["errors"]), 2)

    def test_root_plugin_json_warns_only(self):
        write_json(self.kit.plugin / "plugin.json", {"name": "visual-design-studio"})
        result = self.kit.run()
        self.assertTrue(result["valid"])
        self.assertTrue(result["warnings"])

    def test_exit_codes_and_json(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(parity.main(["--repo", self.tmp, "--json"]), 0)
        self.assertTrue(json.loads(out.getvalue())["valid"])
        write_json(self.kit.plugin / ".claude-plugin" / "plugin.json", {"name": "visual-design-studio", "version": "0"})
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(parity.main(["--repo", self.tmp]), 1)
        empty = tempfile.mkdtemp()
        try:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(parity.main(["--repo", empty, "--json"]), 2)
            self.assertFalse(json.loads(out.getvalue())["valid"])
        finally:
            shutil.rmtree(empty)


if __name__ == "__main__":
    unittest.main()
