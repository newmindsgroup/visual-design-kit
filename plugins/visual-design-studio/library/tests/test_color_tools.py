"""OKLCH conversion, ramps, WCAG 2.x and APCA-W3 regression tests."""
# Version-Timestamp: 2026-10-20 02:04:10 UTC
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts import color_tools as ct


def run_cli(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ct.main(list(args))
    return code, out.getvalue(), err.getvalue()


class ConversionTests(unittest.TestCase):
    def test_srgb_red_matches_published_oklch(self):
        lightness, chroma, hue, alpha = ct.hex_to_oklch("#ff0000")
        self.assertAlmostEqual(lightness, 0.62796, places=4)
        self.assertAlmostEqual(chroma, 0.25768, places=4)
        self.assertAlmostEqual(hue, 29.234, places=2)
        self.assertEqual(alpha, 1.0)

    def test_white_and_black_are_achromatic_extremes(self):
        lightness, chroma, _, _ = ct.hex_to_oklch("#ffffff")
        self.assertAlmostEqual(lightness, 1.0, places=4)
        self.assertLess(chroma, 1e-4)
        self.assertAlmostEqual(ct.hex_to_oklch("#000000")[0], 0.0, places=6)

    def test_round_trip_is_exact_for_in_gamut_colors(self):
        for value in ("#0e7c86", "#a72800", "#f2f7fc", "#14191d", "#7f7f7f", "#123456"):
            lightness, chroma, hue, _ = ct.hex_to_oklch(value)
            self.assertEqual(ct.oklch_to_hex(lightness, chroma, hue), value)

    def test_short_and_alpha_hex_parse(self):
        self.assertEqual(ct.normalize_hex("#ABC"), "#aabbcc")
        self.assertAlmostEqual(ct.parse_hex("#00000080")[3], 128 / 255)
        with self.assertRaises(ct.ColorError):
            ct.parse_hex("#12345")

    def test_convert_accepts_css_oklch_syntax(self):
        result = ct.convert("oklch(62% 0.12 195deg)")
        self.assertEqual(result["l"], 0.62)
        self.assertTrue(result["hex"].startswith("#"))
        self.assertEqual(ct.convert(result["hex"])["hex"], result["hex"])

    def test_gamut_mapping_reduces_chroma_only(self):
        lightness, chroma, hue, mapped = ct.gamut_map(0.7, 0.4, 150)
        self.assertTrue(mapped)
        self.assertEqual((lightness, hue), (0.7, 150))
        self.assertLess(chroma, 0.4)
        self.assertTrue(ct.in_gamut(lightness, chroma, hue))
        self.assertFalse(ct.in_gamut(lightness, chroma + 0.01, hue))
        self.assertFalse(ct.gamut_map(0.7, 0.05, 150)[3])


class RampTests(unittest.TestCase):
    def setUp(self):
        self.ramp = ct.ramp(195, 0.12, name="teal")

    def test_default_steps_and_names(self):
        self.assertEqual([s["step"] for s in self.ramp], list(ct.DEFAULT_STEPS))
        self.assertEqual(self.ramp[0]["name"], "teal-50")

    def test_lightness_is_perceptually_even(self):
        by_step = {s["step"]: s["l"] for s in self.ramp}
        for step in range(100, 900, 100):
            self.assertAlmostEqual(by_step[step] - by_step[step + 100], 0.09, places=4)
        self.assertAlmostEqual(by_step[50] - by_step[100], 0.045, places=4)
        self.assertAlmostEqual(by_step[50], 0.975, places=4)
        self.assertAlmostEqual(by_step[950], 0.165, places=4)

    def test_chroma_tapers_at_both_extremes(self):
        target = {s["step"]: s["requested_c"] for s in self.ramp}
        self.assertEqual(target[500], 0.12)
        self.assertLess(target[50], target[200])
        self.assertLess(target[950], target[800])
        self.assertAlmostEqual(target[50], 0.12 * ct.CHROMA_FLOOR, places=4)

    def test_out_of_gamut_steps_are_mapped_into_srgb(self):
        mapped = [s for s in self.ramp if s["gamut_mapped"]]
        self.assertTrue(mapped, "teal at chroma 0.12 exceeds sRGB in the mid steps")
        for item in mapped:
            self.assertLess(item["c"], item["requested_c"])
            self.assertTrue(ct.in_gamut(item["l"], item["c"] - 0.0001, item["h"]))  # c is rounded to 4 places

    def test_custom_steps_hue_shift_and_determinism(self):
        custom = ct.ramp(72, 0.16, steps=[50, 500, 950], hue_shift=-24)
        self.assertEqual([s["step"] for s in custom], [50, 500, 950])
        self.assertAlmostEqual(custom[1]["h"], 72, places=1)
        self.assertGreater(custom[0]["h"], custom[2]["h"])
        self.assertEqual(ct.ramp(195, 0.12), ct.ramp(195, 0.12))

    def test_cli_formats(self):
        code, out, _ = run_cli("ramp", "--hue", "195", "--chroma", "0.12", "--name", "teal", "--format", "json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["name"], "teal")
        self.assertEqual(len(data["steps"]), 11)
        code, out, _ = run_cli("ramp", "--hue", "35", "--chroma", "0.19", "--name", "vermilion", "--format", "css")
        self.assertIn("--color-vermilion-600:", out)
        code, out, _ = run_cli("ramp", "--hue", "35", "--chroma", "0.19", "--steps", "100,500,900")
        self.assertIn("vs white", out)
        self.assertEqual(len(out.strip().splitlines()), 5)


class ContrastTests(unittest.TestCase):
    def test_wcag_reference_values(self):
        self.assertAlmostEqual(ct.contrast_ratio("#000000", "#ffffff"), 21.0, places=6)
        self.assertAlmostEqual(ct.contrast_ratio("#ffffff", "#ffffff"), 1.0, places=6)
        self.assertAlmostEqual(ct.contrast_ratio("#777777", "#ffffff"), 4.48, places=2)
        self.assertAlmostEqual(ct.contrast_ratio("#767676", "#ffffff"), 4.54, places=2)
        self.assertEqual(ct.contrast_ratio("#334155", "#f8fafc"), ct.contrast_ratio("#f8fafc", "#334155"))

    def test_verdicts(self):
        verdicts = {v["level"]: v["pass"] for v in ct.wcag_verdicts(4.6)}
        self.assertTrue(verdicts["AA normal text"])
        self.assertTrue(verdicts["AAA large text"])
        self.assertFalse(verdicts["AAA normal text"])
        code, out, _ = run_cli("contrast", "#777777", "#ffffff")
        self.assertEqual(code, 0)
        self.assertIn("4.48:1", out)
        self.assertIn("FAIL  AA normal text", out)
        self.assertIn("pass  AA large text", out)

    def test_translucent_colors_are_rejected(self):
        with self.assertRaises(ct.ColorError):
            ct.contrast_ratio("#00000080", "#ffffff")
        self.assertEqual(ct.composite("#00000080", "#ffffff"), "#7f7f7f")


class ApcaTests(unittest.TestCase):
    """Reference values published with APCA-W3 0.1.9 (github.com/Myndex/apca-w3)."""

    def test_black_white_extremes(self):
        self.assertAlmostEqual(ct.apca_contrast("#000000", "#ffffff"), 106.04, places=1)
        self.assertAlmostEqual(ct.apca_contrast("#ffffff", "#000000"), -107.88, places=1)

    def test_published_mid_gray_values(self):
        self.assertAlmostEqual(ct.apca_contrast("#888888", "#ffffff"), 63.056469930209424, places=6)
        self.assertAlmostEqual(ct.apca_contrast("#ffffff", "#888888"), -68.54146436644962, places=6)
        self.assertAlmostEqual(ct.apca_contrast("#000000", "#aaaaaa"), 58.146262578561334, places=6)
        self.assertAlmostEqual(ct.apca_contrast("#aaaaaa", "#000000"), -56.24113336839742, places=6)

    def test_low_contrast_clips_to_zero(self):
        self.assertEqual(ct.apca_contrast("#777777", "#777777"), 0.0)
        self.assertEqual(ct.apca_contrast("#787878", "#777777"), 0.0)

    def test_constants_are_the_published_set(self):
        self.assertEqual(ct.APCA["normBG"], 0.56)
        self.assertEqual(ct.APCA["normTXT"], 0.57)
        self.assertEqual(ct.APCA["revTXT"], 0.62)
        self.assertEqual(ct.APCA["revBG"], 0.65)
        self.assertEqual(ct.APCA["blkThrs"], 0.022)
        self.assertEqual(ct.APCA["blkClmp"], 1.414)
        self.assertEqual(ct.APCA["scaleBoW"], 1.14)
        self.assertEqual(ct.APCA["loBoWoffset"], 0.027)
        self.assertEqual(ct.APCA["deltaYmin"], 0.0005)
        self.assertEqual(ct.APCA["loClip"], 0.1)

    def test_cli(self):
        code, out, _ = run_cli("apca", "#000000", "#ffffff")
        self.assertEqual(code, 0)
        self.assertIn("Lc 106.0", out)
        code, out, _ = run_cli("apca", "#ffffff", "#000000", "--json")
        self.assertEqual(json.loads(out)["lc"], -107.9)


class PaletteTests(unittest.TestCase):
    def test_pairs_and_ramp_checks(self):
        report = ct.check_palette({
            "colors": {"ink": "#14191d", "paper": "#f2f7fc", "mist": "#aaaaaa",
                       "teal-100": "#c3f3f2", "teal-500": "#008989", "teal-900": "#001d1d"},
            "pairs": [{"fg": "ink", "bg": "paper", "min": 4.5}, {"fg": "mist", "bg": "paper", "min": 4.5}],
        })
        self.assertFalse(report["ok"])
        self.assertEqual([p["pass"] for p in report["pairs"]], [True, False])
        self.assertTrue(any("mist on paper" in e for e in report["errors"]))
        self.assertTrue(report["ramps"][0]["monotonic"])

    def test_non_monotonic_ramp_is_reported(self):
        report = ct.check_palette({"gray-100": "#eeeeee", "gray-200": "#111111", "gray-300": "#777777"})
        self.assertFalse(report["ok"])
        self.assertIn("not darker", report["errors"][0])

    def test_dtcg_tree_and_cli(self):
        tree = {"color": {"$type": "color", "fg": {"$value": "#111111"}, "bg": {"$value": "#ffffff"}},
                "pairs": [{"fg": "color-fg", "bg": "color-bg", "min": 7}]}
        self.assertTrue(ct.check_palette(tree)["ok"])
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "palette.json"
            path.write_text(json.dumps(tree), encoding="utf-8")
            code, out, _ = run_cli("check-palette", str(path))
            self.assertEqual(code, 0)
            self.assertIn("OK", out)
            path.write_text(json.dumps({"a": "#ffffff", "b": "#fefefe", "pairs": [{"fg": "a", "bg": "b"}]}),
                            encoding="utf-8")
            code, _, err = run_cli("check-palette", str(path))
            self.assertEqual(code, 1)
            self.assertIn("below 4.5:1", err)


if __name__ == "__main__":
    unittest.main()


class StepValidationTests(unittest.TestCase):
    def test_out_of_scale_steps_are_rejected(self):
        import subprocess, sys
        script = Path(__file__).resolve().parents[1] / "scripts" / "color_tools.py"
        bad = subprocess.run([sys.executable, str(script), "ramp", "--hue", "195", "--chroma", "0.1", "--steps", "1,2,3"],
                             capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("50-950", bad.stderr)
        good = subprocess.run([sys.executable, str(script), "ramp", "--hue", "195", "--chroma", "0.1", "--steps", "50,500,950"],
                              capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stderr)
