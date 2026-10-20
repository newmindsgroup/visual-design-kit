"""Weighted direction scoring tests."""
# Version-Timestamp: 2026-10-20 02:05:00 UTC
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "plugins" / "visual-design-studio" / "skills" / "design-director" / "scripts" / "score_directions.py"
spec = importlib.util.spec_from_file_location("score_directions", SCRIPT)
score = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score)

EXAMPLE = {"preset": "regulated", "directions": {
    "A": {"objective": 3, "audience": 4, "differentiation": 2, "brand": 3, "accessibility": 5, "feasibility": 5, "scalability": 4, "longevity": 4, "risk": 5},
    "B": {"objective": 4, "audience": 5, "differentiation": 4, "brand": 4, "accessibility": 4, "feasibility": 4, "scalability": 4, "longevity": 4, "risk": 4},
    "C": {"objective": 4, "audience": 3, "differentiation": 5, "brand": 3, "accessibility": 3, "feasibility": 4, "scalability": 3, "longevity": 2, "risk": 3},
}}


class ScoreDirectionsTests(unittest.TestCase):
    def test_presets_sum_to_100(self):
        for name, weights in score.PRESETS.items():
            self.assertEqual(sum(weights), 100, name)
            self.assertEqual(len(weights), len(score.CRITERIA), name)

    def test_worked_example_matches_documented_scores(self):
        result = score.report(EXAMPLE)
        self.assertEqual(result["scores"], {"A": 3.95, "B": 4.15, "C": 3.4})
        self.assertEqual(result["winner"], "B")
        flips = result["sensitivity"]
        self.assertEqual(len(flips), 1)
        self.assertEqual((flips[0]["criterion"], flips[0]["delta"], flips[0]["winner"]), ("differentiation", -10, "tie"))

    def test_custom_weights_are_renormalized(self):
        custom = dict(EXAMPLE, weights={"objective": 1, "audience": 1})
        custom.pop("preset")
        result = score.report(custom)
        self.assertAlmostEqual(sum(result["weights"].values()), 100, places=6)
        self.assertEqual(result["scores"]["B"], 4.5)

    def test_invalid_input_is_rejected(self):
        bad = json.loads(json.dumps(EXAMPLE))
        bad["directions"]["A"]["risk"] = 7
        with self.assertRaises(score.ScoreError):
            score.report(bad)
        with self.assertRaises(score.ScoreError):
            score.report({"preset": "nope", "directions": EXAMPLE["directions"]})
        with self.assertRaises(score.ScoreError):
            score.report({"directions": {"A": EXAMPLE["directions"]["A"]}})

    def test_cli_markdown(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "-"], input=json.dumps(EXAMPLE), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| **Weighted** |", result.stdout)
        self.assertIn("Winner: **B**", result.stdout)


if __name__ == "__main__":
    unittest.main()
