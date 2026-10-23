"""The Claude Code skill mirror must match the canonical Codex skills.

Version-Timestamp: 2026-10-23 13:05:00 AST
"""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("sync_agent_skills", ROOT / "tools" / "sync_agent_skills.py")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class AgentSkillMirror(unittest.TestCase):
    def test_canonical_skills_exist(self):
        names = {p.name for p in (ROOT / ".agents" / "skills").iterdir() if p.is_dir()}
        self.assertIn("design-kit-authoring", names)
        self.assertIn("design-kit-eval-loop", names)

    def test_claude_mirror_matches_canonical(self):
        missing, extra, changed = sync.drift()
        self.assertEqual(
            (missing, extra, changed), ([], [], []),
            "Run: python3 tools/sync_agent_skills.py --apply",
        )

    def test_claude_md_imports_agents_md(self):
        first = (ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines()[0].strip()
        self.assertEqual(first, "@AGENTS.md")


if __name__ == "__main__":
    unittest.main()
