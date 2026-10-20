"""Spec radar extraction tests."""
# Version-Timestamp: 2026-10-20 05:10:00 UTC
import datetime as dt
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "spec_radar.py"
spec = importlib.util.spec_from_file_location("spec_radar", SCRIPT)
radar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radar)

ENTRY = """---
id: market.example
version_timestamp: "2026-07-01 00:00:00 UTC"
---

- Consumer privacy act in force since 2024 (verify enforcement date).
- Pix is the default payment rail (verify coverage).
- App Store screenshots at 1320x2868 px (verify current sizes).
- Verify that the build passes before shipping.
- Give users a way to verify a communication.
- A plain line with no marker.
"""


class SpecRadarTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "library" / "atlas" / "markets").mkdir(parents=True)
        (root / "library" / "atlas" / "markets" / "example.md").write_text(ENTRY, encoding="utf-8")
        self.items = radar.collect(root, dt.date(2026, 10, 20))

    def tearDown(self):
        self.tmp.cleanup()

    def test_collects_only_volatile_claims(self):
        self.assertEqual([i["line"] for i in self.items], [6, 7, 8])

    def test_topics(self):
        self.assertEqual([i["topic"] for i in self.items], ["regulation", "payments", "platform-specs"])

    def test_age_from_frontmatter_stamp(self):
        self.assertEqual({i["age_days"] for i in self.items}, {111})

    def test_markdown_summary(self):
        text = radar.render_markdown(self.items, dt.date(2026, 10, 20))
        self.assertIn("| total | 3 | 1 |", text)
        self.assertIn("`library/atlas/markets/example.md:6` (111 d)", text)

    def test_real_plugin_has_markers(self):
        self.assertGreater(len(radar.collect()), 50)


if __name__ == "__main__":
    unittest.main()
