"""Modular and fluid type scale regression tests."""
# Version-Timestamp: 2026-10-20 02:04:10 UTC
import contextlib
import io
import json
import re
import unittest

from scripts import type_scale as ts


def run_cli(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ts.main(list(args))
    return code, out.getvalue(), err.getvalue()


class StaticScaleTests(unittest.TestCase):
    def test_major_third_from_16(self):
        items = {i["name"]: i for i in ts.scale(16, 1.25)}
        self.assertEqual(items["md"]["px"], 16)
        self.assertEqual(items["lg"]["px"], 20)
        self.assertEqual(items["xl"]["px"], 25)
        self.assertEqual(items["sm"]["px"], 12.8)
        self.assertEqual(items["xs"]["px"], 10.24)
        self.assertEqual(items["xl"]["rem"], 1.5625)
        self.assertEqual(list(items), ["xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"])

    def test_named_ratios(self):
        self.assertEqual(ts.resolve_ratio("minor-second"), 1.067)
        self.assertEqual(ts.resolve_ratio("major third"), 1.25)
        self.assertEqual(ts.resolve_ratio("perfect_fourth"), 1.333)
        self.assertEqual(ts.resolve_ratio("golden"), 1.618)
        self.assertEqual(ts.resolve_ratio("1.5"), 1.5)
        self.assertEqual(list(ts.RATIOS)[0], "minor-second")
        with self.assertRaises(ts.ScaleError):
            ts.resolve_ratio("enormous")
        with self.assertRaises(ts.ScaleError):
            ts.resolve_ratio(0.9)

    def test_step_names_extend_both_ways(self):
        names = [ts.step_name(s) for s in range(-4, 9)]
        self.assertEqual(names, ["3xs", "2xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"])

    def test_css_and_json_output(self):
        code, out, _ = run_cli("--base", "16", "--ratio", "golden", "--down", "1", "--up", "2", "--format", "css")
        self.assertEqual(code, 0)
        self.assertIn("--font-size-lg: 1.618rem; /* 25.89px, step 1 */", out)
        code, out, _ = run_cli("--ratio", "minor-third", "--format", "json")
        data = json.loads(out)
        self.assertEqual(data[3]["px"], 19.2)
        code, out, _ = run_cli("--list-ratios")
        self.assertIn("golden", out)


class FluidScaleTests(unittest.TestCase):
    ARGS = dict(min_vw=360, max_vw=1440, min_base=16, max_base=18, min_ratio=1.2, max_ratio=1.333)

    def test_interpolation_hits_both_endpoints(self):
        for item in ts.fluid_scale(**self.ARGS):
            at_min = item["intercept_px"] + item["slope"] * 360
            at_max = item["intercept_px"] + item["slope"] * 1440
            self.assertAlmostEqual(at_min, item["min_px"], delta=0.02)
            self.assertAlmostEqual(at_max, item["max_px"], delta=0.02)

    def test_base_step_clamp(self):
        md = {i["name"]: i for i in ts.fluid_scale(**self.ARGS)}["md"]
        self.assertEqual(md["clamp"], "clamp(1rem, 0.9583rem + 0.1852vw, 1.125rem)")

    def test_clamp_values_match_their_math(self):
        pattern = re.compile(r"clamp\(([\d.]+)rem, ([\d.-]+)rem ([+-]) ([\d.]+)vw, ([\d.]+)rem\)")
        for item in ts.fluid_scale(**self.ARGS):
            low, intercept, sign, slope_vw, high = pattern.match(item["clamp"]).groups()
            slope = float(slope_vw) / 100 * (-1 if sign == "-" else 1)
            self.assertAlmostEqual(slope, item["slope"], places=5)
            self.assertAlmostEqual(float(intercept) * 16, item["intercept_px"], delta=0.01)
            self.assertLessEqual(float(low), float(high))

    def test_shrinking_steps_use_a_negative_slope(self):
        xs = ts.fluid_scale(**self.ARGS)[0]
        self.assertEqual(xs["name"], "xs")
        self.assertLess(xs["slope"], 0)
        self.assertIn(" - ", xs["clamp"])

    def test_cli_documents_the_math(self):
        code, out, err = run_cli("--fluid", "--min-vw", "360", "--max-vw", "1440", "--min-base", "16", "--max-base",
                                 "18", "--min-ratio", "1.2", "--max-ratio", "1.333", "--format", "css")
        self.assertEqual(code, 0)
        self.assertIn("slope = (max - min) / (max_vw - min_vw)", out)
        self.assertIn("/* step 0: 16px @360 -> 18px @1440; slope = (18 - 16) / (1440 - 360) = 0.001852", out)
        self.assertIn("--font-size-md: clamp(1rem, 0.9583rem + 0.1852vw, 1.125rem);", out)
        self.assertEqual(err, "")

    def test_zoom_warning_for_extreme_growth(self):
        code, _, err = run_cli("--fluid", "--min-base", "12", "--max-base", "18", "--min-ratio", "1.1",
                               "--max-ratio", "1.618", "--up", "6")
        self.assertEqual(code, 0)
        self.assertIn("WCAG 1.4.4", err)

    def test_invalid_viewports(self):
        with self.assertRaises(ts.ScaleError):
            ts.fluid_scale(min_vw=1440, max_vw=360)
        code, _, err = run_cli("--fluid", "--min-vw", "800", "--max-vw", "400")
        self.assertEqual(code, 2)
        self.assertIn("max-vw", err)


if __name__ == "__main__":
    unittest.main()
