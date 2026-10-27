"""Portable Lottie builder: conversions, subset validation and example round-trips."""
# Version-Timestamp: 2026-10-23 20:12:12 UTC
import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts import lottie_build as lb

LIBRARY = Path(__file__).resolve().parent.parent
EXAMPLE_LOTTIE = LIBRARY / "examples" / "motion-remotion" / "public" / "lottie"


def run_cli(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = lb.main(list(args))
    return code, out.getvalue(), err.getvalue()


def errors(doc):
    return [i for i in lb.validate(doc) if i["level"] == "error"]


def rules(doc):
    return {i["rule"] for i in errors(doc)}


class ConversionTests(unittest.TestCase):
    def test_hex_to_lottie_rgb_in_unit_range(self):
        self.assertEqual(lb.hex_to_lottie("#006c6c"), [0, 0.4235, 0.4235, 1])
        self.assertEqual(lb.hex_to_lottie("#ffffff"), [1, 1, 1, 1])
        self.assertEqual(lb.hex_to_lottie("#fff"), [1, 1, 1, 1])
        self.assertEqual(lb.hex_to_lottie("#00000080"), [0, 0, 0, 0.502])

    def test_hex_to_lottie_rejects_bad_input(self):
        for bad in ("006c6c", "#12345", "#gggggg", None):
            with self.assertRaises(ValueError):
                lb.hex_to_lottie(bad)

    def test_css_bezier_maps_to_out_and_in_tangents(self):
        out_t, in_t = lb.bezier_tangents([0.05, 0.7, 0.1, 1], dims=3)
        self.assertEqual(out_t, {"x": [0.05] * 3, "y": [0.7] * 3})
        self.assertEqual(in_t, {"x": [0.1] * 3, "y": [1.0] * 3})

    def test_bezier_allows_overshoot_y_but_not_x(self):
        lb.bezier_tangents([0.3, -0.5, 0.7, 1.5])
        with self.assertRaises(ValueError):
            lb.bezier_tangents([1.2, 0, 0, 1])
        with self.assertRaises(ValueError):
            lb.bezier_tangents([0, 0, 1])

    def test_token_easing_reaches_keyframes(self):
        tokens = lb.load_tokens()
        doc = lb.build(json.loads((lb.SPEC_DIR / "underline-sweep.json").read_text()), tokens)
        trim = doc["layers"][0]["shapes"][0]["it"][1]
        first = trim["e"]["k"][0]
        x1, y1, x2, y2 = tokens.get("ease.emphasized-decelerate")
        self.assertEqual((first["o"]["x"][0], first["o"]["y"][0]), (x1, y1))
        self.assertEqual((first["i"]["x"][0], first["i"]["y"][0]), (x2, y2))

    def test_duration_tokens_to_frames(self):
        self.assertEqual(lb.ms_to_frames(320, 30), 10)
        self.assertEqual(lb.ms_to_frames(480, 30), 14)
        self.assertEqual(lb.ms_to_frames(50, 30), 2)
        self.assertEqual(lb.parse_duration_ms("1.2s"), 1200)
        self.assertEqual(lb.load_tokens().duration_ms("duration.slow"), 320)
        with self.assertRaises(ValueError):
            lb.parse_duration_ms("fast")

    def test_brand_and_mode_change_colors(self):
        spec = json.loads((lb.SPEC_DIR / "logo-reveal.json").read_text())
        light = lb.build(spec, lb.load_tokens(brand="meridian", mode="light"))
        dark = lb.build(spec, lb.load_tokens(brand="ember", mode="dark"))
        self.assertNotEqual(json.dumps(light["assets"]), json.dumps(dark["assets"]))
        self.assertEqual(dark["meta"]["tokens"]["brand"], "ember")
        with self.assertRaises(ValueError):
            lb.load_tokens(brand="nope")


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.doc = lb.build(json.loads((lb.SPEC_DIR / "logo-reveal.json").read_text()))

    def test_generated_file_is_clean(self):
        self.assertEqual(lb.validate(self.doc), [])

    def test_expression_string_is_rejected_but_tangent_and_mask_x_are_not(self):
        doc = copy.deepcopy(self.doc)
        doc["layers"][0]["ks"]["o"]["x"] = "loopOut('cycle')"
        self.assertIn("no-expressions", rules(doc))
        self.assertNotIn("no-expressions", rules(self.doc))

    def test_forbidden_layers_effects_and_shapes(self):
        doc = copy.deepcopy(self.doc)
        layer = copy.deepcopy(doc["layers"][0])
        layer.update({"ty": 5, "ind": 9})
        doc["layers"].append(layer)
        self.assertIn("layer-type", rules(doc))
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"][0]["ef"] = [{"ty": 5}]
        self.assertIn("effects", rules(doc))
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"][0]["shapes"][0]["it"].insert(0, {"ty": "mm", "mm": 1})
        self.assertIn("shape-type", rules(doc))

    def test_required_keys_frame_rate_and_in_out_points(self):
        doc = copy.deepcopy(self.doc)
        del doc["w"]
        doc["fr"] = 0
        doc["op"] = doc["ip"]
        found = rules(doc)
        self.assertTrue({"required", "frame-rate", "in-out"} <= found)
        doc = copy.deepcopy(self.doc)
        doc["fr"] = 29.97
        self.assertEqual([i["rule"] for i in lb.validate(doc)], ["frame-rate"])
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"][0]["op"] = 0
        self.assertIn("in-out", rules(doc))
        doc = copy.deepcopy(self.doc)
        del doc["assets"][0]["layers"][0]["ks"]
        self.assertIn("required", rules(doc))

    def test_references_masks_mattes_and_rasters(self):
        doc = copy.deepcopy(self.doc)
        doc["layers"][0]["refId"] = "missing"
        self.assertIn("refId", rules(doc))
        doc = copy.deepcopy(self.doc)
        mask_layer = next(l for l in doc["assets"][0]["layers"] if l.get("hasMask"))
        mask_layer["masksProperties"][0]["mode"] = "i"
        self.assertIn("mask", rules(doc))
        del mask_layer["masksProperties"][0]["x"]
        self.assertIn("mask", rules(doc))
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"][0]["tt"] = 3
        self.assertIn("matte", rules(doc))
        doc = copy.deepcopy(self.doc)
        doc["assets"].append({"id": "img", "w": 10, "h": 10, "p": "data:image/png;base64,AA", "e": 1})
        self.assertIn("asset", rules(doc))
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"][0]["parent"] = 99
        self.assertIn("parent", rules(doc))

    def test_keyframe_order_and_tangents(self):
        doc = copy.deepcopy(self.doc)
        ring = next(l for l in doc["assets"][0]["layers"] if l["nm"].startswith("Ring"))
        keys = ring["shapes"][0]["it"][1]["e"]["k"]
        keys[1]["t"] = keys[0]["t"]
        self.assertIn("keyframes", rules(doc))
        doc = copy.deepcopy(self.doc)
        ring = next(l for l in doc["assets"][0]["layers"] if l["nm"].startswith("Ring"))
        del ring["shapes"][0]["it"][1]["e"]["k"][0]["i"]
        self.assertIn("keyframes", rules(doc))

    def test_colors_must_be_unit_range(self):
        doc = copy.deepcopy(self.doc)
        ring = next(l for l in doc["assets"][0]["layers"] if l["nm"].startswith("Ring"))
        ring["shapes"][0]["it"][2]["c"]["k"] = [0, 108, 108, 1]
        self.assertIn("color", rules(doc))

    def test_precomp_cycle_is_caught(self):
        doc = copy.deepcopy(self.doc)
        doc["assets"][0]["layers"].append(copy.deepcopy(doc["layers"][0]))
        doc["assets"][0]["layers"][-1]["ind"] = 50
        self.assertIn("refId", rules(doc))


class ExampleRoundTripTests(unittest.TestCase):
    def test_every_preset_has_a_spec(self):
        self.assertEqual(sorted(p.stem for p in lb.SPEC_DIR.glob("*.json")), sorted(lb.PRESETS))

    def test_examples_are_up_to_date_valid_and_small(self):
        for name, text in lb.example_outputs():
            target = EXAMPLE_LOTTIE / name
            self.assertTrue(target.exists(), "%s missing: run lottie_build.py examples" % target)
            self.assertEqual(target.read_text(encoding="utf-8"), text, "%s is stale" % name)
            doc = json.loads(text)
            self.assertEqual(lb.validate(doc), [], name)
            self.assertLess(len(text.encode("utf-8")), 30 * 1024, name)
            self.assertEqual(json.loads(lb.dumps(doc)), doc)

    def test_build_is_deterministic(self):
        spec = json.loads((lb.SPEC_DIR / "loader.json").read_text())
        self.assertEqual(lb.dumps(lb.build(spec)), lb.dumps(lb.build(spec)))

    def test_loader_loops_seamlessly(self):
        doc = lb.build(json.loads((lb.SPEC_DIR / "loader.json").read_text()))
        arc = doc["layers"][0]["shapes"][0]["it"]
        trim, transform = arc[1], arc[-1]
        self.assertEqual(trim["s"]["k"][0]["s"], [0])
        self.assertEqual(trim["e"]["k"][0]["s"], [0])
        self.assertEqual(trim["s"]["k"][-1]["s"], [100])
        self.assertEqual(transform["r"]["k"][-1], {"t": doc["op"], "s": [360]})

    def test_icon_morph_paths_keep_vertex_count(self):
        doc = lb.build(json.loads((lb.SPEC_DIR / "icon-morph.json").read_text()))
        for group in doc["layers"][0]["shapes"]:
            frames = group["it"][0]["ks"]["k"]
            counts = {len(k["s"][0]["v"]) for k in frames}
            self.assertEqual(len(counts), 1, group["nm"])

    def test_cli_build_validate_and_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "loader.json"
            code, stdout, _ = run_cli("build", str(lb.SPEC_DIR / "loader.json"), "-o", str(out), "--mode", "dark")
            self.assertEqual(code, 0)
            self.assertIn("frames", stdout)
            code, stdout, _ = run_cli("validate", str(out), "--json")
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(stdout)[str(out)], [])
            bad = json.loads(out.read_text())
            bad["layers"][0]["ty"] = 2
            out.write_text(json.dumps(bad))
            code, stdout, _ = run_cli("validate", str(out))
            self.assertEqual(code, 1)
            self.assertIn("FAIL", stdout)
            code, _, err = run_cli("examples", "--out", tmp, "--check")
            self.assertEqual(code, 1)
            self.assertIn("stale or missing", err)
        code, stdout, _ = run_cli("examples", "--check")
        self.assertEqual(code, 0, "public/lottie examples are stale")
        code, stdout, _ = run_cli("presets")
        self.assertEqual(code, 0)
        self.assertIn("logo-reveal", stdout)

    def test_unknown_preset_is_an_error(self):
        code, _, err = run_cli("build", str(lb.SPEC_DIR / "loader.json"), "--brand", "missing")
        self.assertEqual(code, 1)
        self.assertIn("unknown brand", err)
        with self.assertRaises(ValueError):
            lb.build({"preset": "confetti"})


if __name__ == "__main__":
    unittest.main()
