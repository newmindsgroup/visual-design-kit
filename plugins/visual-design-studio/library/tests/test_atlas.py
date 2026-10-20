"""Design Space Atlas helper tests."""
# Version-Timestamp: 2026-10-20 02:05:00 UTC
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

LIBRARY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LIBRARY / "scripts"))
import atlas  # noqa: E402

STYLE_SECTIONS = atlas.SECTIONS["style"]


def entry(entry_id="style.alpha", pairs="industry.beta, archetype.gamma, tier.delta", avoid="", sections=STYLE_SECTIONS,
          summary="A deliberately long enough summary for the alpha test style entry.", body_lines=6):
    body = "\n\n".join(f"## {name}\n\n" + "\n".join(f"- line {i}" for i in range(body_lines)) for name in sections)
    return (f"---\nid: {entry_id}\naxis: {entry_id.split('.')[0]}\nname: Alpha\naliases: [alpha, first]\n"
            f"summary: {summary}\ntags: [one, two, three, four]\npairs_with: [{pairs}]\navoid_with: [{avoid}]\n"
            f"version_timestamp: 2026-10-20 02:05:00 UTC\n---\n\n# Alpha\n\n{body}\n")


class AtlasFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        registry = {"axes": {
            "style": {"directory": "styles", "entries": [{"id": "style.alpha", "name": "Alpha", "path": "styles/alpha.md"}]},
            "industry": {"directory": "industries", "entries": [{"id": "industry.beta", "name": "Beta", "path": "industries/beta.md"}]},
            "archetype": {"directory": "archetypes", "entries": [{"id": "archetype.gamma", "name": "Gamma", "path": "archetypes/gamma.md"}]},
            "tier": {"directory": "tiers", "entries": [{"id": "tier.delta", "name": "Delta", "path": "tiers/delta.md"}]},
        }}
        (self.root / "registry.json").write_text(json.dumps(registry))
        for directory in ("styles", "industries", "archetypes", "tiers"):
            (self.root / directory).mkdir()

    def write(self, text, path="styles/alpha.md"):
        (self.root / path).write_text(text, encoding="utf-8")

    def test_valid_entry_passes_and_index_builds(self):
        self.write(entry())
        errors, written, planned = atlas.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual((written, planned), (1, 4))
        index = atlas.build_index(self.root)
        self.assertEqual(index["total"], 1)
        self.assertEqual(index["entries"][0]["path"], "styles/alpha.md")

    def test_complete_reports_missing_entries(self):
        self.write(entry())
        errors, _, _ = atlas.validate(self.root, complete=True)
        self.assertTrue(any("industry.beta" in error for error in errors))

    def test_sections_must_match_schema_in_order(self):
        sections = list(STYLE_SECTIONS)
        sections[0], sections[1] = sections[1], sections[0]
        self.write(entry(sections=sections))
        errors, _, _ = atlas.validate(self.root)
        self.assertTrue(any("out of order" in error for error in errors), errors)
        self.write(entry(sections=STYLE_SECTIONS[:-1]))
        errors, _, _ = atlas.validate(self.root)
        self.assertTrue(any("missing Reference anchors" in error for error in errors), errors)

    def test_unknown_and_self_references_fail(self):
        self.write(entry(pairs="industry.beta, archetype.gamma, style.alpha", avoid="market.nowhere"))
        errors, _, _ = atlas.validate(self.root)
        self.assertTrue(any("references itself" in error for error in errors))
        self.assertTrue(any("unknown id market.nowhere" in error for error in errors))

    def test_unknown_ids_in_body_fail(self):
        self.write(entry().replace("- line 0", "- see `industry.beta` and industry.nope and style.css", 1))
        errors, _, _ = atlas.validate(self.root)
        self.assertEqual([e for e in errors if "body mentions" in e], ["styles/alpha.md: body mentions unknown atlas id industry.nope"])

    def test_thin_entries_and_bad_summaries_fail(self):
        self.write(entry(summary="too short", body_lines=1))
        errors, _, _ = atlas.validate(self.root)
        self.assertTrue(any("summary must be" in error for error in errors))
        self.assertTrue(any("too thin" in error for error in errors))

    def test_quotes_are_stripped_and_inner_colons_kept(self):
        meta, _ = atlas.parse_entry('---\nname: "Alpha: the first"\nsummary: Plain: with colon\n---\n')
        self.assertEqual(meta["name"], "Alpha: the first")
        self.assertEqual(meta["summary"], "Plain: with colon")

    def test_malformed_frontmatter_fails_cleanly(self):
        self.write("---\nid style.alpha\n---\n")
        errors, _, _ = atlas.validate(self.root)
        self.assertTrue(any("not key: value" in error for error in errors))

    def test_query_and_combine(self):
        self.write(entry())
        result = atlas.query("I want something alpha and first", self.root)
        self.assertEqual(result["style"][0]["id"], "style.alpha")
        combined = atlas.combine(["style.alpha"], self.root)
        self.assertIn("industry.beta", combined["also_consider"])
        with self.assertRaises(atlas.AtlasError):
            atlas.combine(["style.missing"], self.root)


class ShippedAtlas(unittest.TestCase):
    def test_shipped_atlas_is_complete_and_valid(self):
        errors, written, planned = atlas.validate(atlas.ATLAS, complete=True)
        self.assertEqual(errors, [], "\n".join(errors[:20]))
        self.assertEqual(written, planned)

    def test_shipped_index_is_current(self):
        stored = json.loads((atlas.ATLAS / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(stored, atlas.build_index(atlas.ATLAS), "run: python3 scripts/atlas.py build")

    def test_cli_query_runs(self):
        result = subprocess.run([sys.executable, str(LIBRARY / "scripts" / "atlas.py"), "query", "fintech for gen z"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("industry.fintech-banking", result.stdout)


if __name__ == "__main__":
    unittest.main()
