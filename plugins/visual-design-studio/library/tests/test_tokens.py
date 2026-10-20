"""Design token build, lint and staleness regression tests."""
# Version-Timestamp: 2026-10-20 02:04:10 UTC
import contextlib
import io
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import color_tools as ct
from scripts import tokens as tk

LIBRARY = Path(__file__).resolve().parents[1]
SRC = LIBRARY / "tokens" / "src"
DIST = LIBRARY / "tokens" / "dist"
BROKEN = LIBRARY / "tests" / "fixtures" / "tokens-broken"


def run_cli(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = tk.main(list(args))
    return code, out.getvalue(), err.getvalue()


def root_block(css):
    match = re.search(r"^:root \{\n(.*?)^\}", css, re.S | re.M)
    return match.group(1)


class SourceCopy:
    """Temporary copy of tokens/src that a test can mutate."""

    def __enter__(self):
        self._dir = tempfile.TemporaryDirectory()
        self.path = Path(self._dir.name) / "src"
        shutil.copytree(SRC, self.path)
        return self

    def __exit__(self, *exc):
        self._dir.cleanup()

    def edit(self, name, change):
        path = self.path / name
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def lint(self):
        return tk.lint(tk.load_source(self.path))["errors"]


class ShippedTokensTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = tk.load_source(SRC)
        cls.report = tk.lint(cls.source)
        cls.outputs = tk.build_outputs(cls.source)

    def test_lint_passes(self):
        self.assertEqual(self.report["errors"], [])
        self.assertEqual(self.report["stats"]["brands"], ["meridian", "ember"])
        self.assertEqual(self.report["stats"]["modes"], ["light", "dark", "high-contrast"])
        self.assertGreater(self.report["stats"]["contrast_pairs_checked"], 200)

    def test_every_contract_variable_is_in_root(self):
        declared = set(re.findall(r"^\s+(--[a-z0-9-]+):", root_block(self.outputs["tokens.css"]), re.M))
        light = re.search(r'^:root,\n\[data-theme="light"\] \{\n(.*?)^\}', self.outputs["tokens.css"], re.S | re.M)
        declared |= set(re.findall(r"^\s+(--[a-z0-9-]+):", light.group(1), re.M))
        missing = [name for name in tk.CONTRACT if name not in declared]
        self.assertEqual(missing, [])
        self.assertEqual(len(tk.CONTRACT), 111)

    def test_contract_values(self):
        css = self.outputs["tokens.css"]
        for line in ("--font-size-md: 1rem;", "--font-size-5xl: 3.75rem;", "--space-0: 0;", "--space-24: 6rem;",
                     "--radius-full: 9999px;", "--letter-spacing-normal: 0;", "--duration-slower: 480ms;",
                     "--ease-emphasized-accelerate: cubic-bezier(0.3, 0, 0.8, 0.15);", "--ease-linear: linear;",
                     "--z-toast: 1400;", "--container-xl: 1280px;", "--gutter: clamp(1rem, 4vw, 2rem);",
                     "--size-target-min: 24px;", "--measure-body: 66ch;", "--line-height-relaxed: 1.65;"):
            self.assertIn(line, css)
        self.assertNotIn("--breakpoint-", css)

    def test_css_structure(self):
        css = self.outputs["tokens.css"]
        order = [css.index(marker) for marker in (
            ":root {", ':root,\n[data-theme="light"] {', '[data-theme="dark"] {', '[data-theme="high-contrast"] {',
            "@media (prefers-color-scheme: dark) {", "@media (prefers-contrast: more) {", '[data-brand="ember"] {',
            ":root,\n[data-theme],\n[data-brand] {", "@media (prefers-reduced-motion: reduce) {")]
        self.assertEqual(order, sorted(order))
        motion = css[css.index("@media (prefers-reduced-motion: reduce)"):]
        for name in ("fast", "moderate", "slow", "slower"):
            self.assertIn(f"--duration-{name}: 0.01ms;", motion)
        self.assertNotIn("--duration-instant", motion)
        brand = css[css.index('[data-brand="ember"] {'):css.index("/* Components")]
        self.assertIn("--color-accent-600: var(--color-vermilion-600);", brand)
        self.assertIn("--font-family-display: var(--font-stack-fraunces);", brand)
        self.assertNotIn("--color-bg-", brand, "brands override primitives only")

    def test_dark_mode_is_designed_not_inverted(self):
        values = json.loads(self.outputs["tokens.resolved.json"])["values"]
        for brand in ("meridian", "ember"):
            dark = values[brand]["dark"]
            light = values[brand]["light"]
            canvas, surface, raised = (ct.hex_to_oklch(dark[f"color.bg.{n}"])[0]
                                       for n in ("canvas", "surface", "surface-raised"))
            self.assertLess(canvas, surface)
            self.assertLess(surface, raised, "elevated surfaces get lighter in dark mode")
            self.assertNotEqual(dark["color.bg.canvas"], "#000000")
            self.assertGreater(canvas, 0.1)
            self.assertNotEqual(dark["color.fg.default"], "#ffffff")
            accent_dark, accent_light = ct.hex_to_oklch(dark["color.accent.default"]), \
                ct.hex_to_oklch(light["color.accent.default"])
            self.assertLess(accent_dark[1] / accent_dark[0], accent_light[1] / accent_light[0],
                            "dark accents are less saturated (C/L) than light ones")

    def test_brands_differ_where_they_should(self):
        values = json.loads(self.outputs["tokens.resolved.json"])["values"]
        meridian, ember = values["meridian"]["light"], values["ember"]["light"]
        self.assertNotEqual(meridian["color.accent.default"], ember["color.accent.default"])
        self.assertNotEqual(meridian["color.bg.canvas"], ember["color.bg.canvas"])
        self.assertEqual(meridian["space.4"], ember["space.4"])
        self.assertEqual(meridian["font.family.display"][0], "Schibsted Grotesk")
        self.assertEqual(ember["font.family.display"][0], "Fraunces")
        self.assertNotEqual(meridian["font.family.display"], meridian["font.family.body"])
        hue = ct.hex_to_oklch(meridian["color.accent.400"])[2]
        self.assertAlmostEqual(hue, 195, delta=3)
        self.assertAlmostEqual(ct.hex_to_oklch(ember["color.accent.400"])[2], 35, delta=3)

    def test_components_alias_semantic_tokens_only(self):
        view = tk.merged(self.source)
        for token in self.source.components.tokens.values():
            for target in tk._alias_targets(token.value):
                ref = view[target]
                self.assertTrue(ref.tier == "semantic" or ref.css_name in tk.CONTRACT, token.dotted)

    def test_tailwind_mapping(self):
        tailwind = self.outputs["tailwind.css"]
        self.assertIn("@theme inline reference {", tailwind)
        for line in ("--background-color-canvas: var(--color-bg-canvas);",
                     "--background-color-surface: var(--color-bg-surface);",
                     "--text-color-default: var(--color-fg-default);", "--text-color-muted: var(--color-fg-muted);",
                     "--border-color-default: var(--color-border-default);",
                     "--background-color-accent: var(--color-accent-default);",
                     "--text-color-on-accent: var(--color-fg-on-accent);", "--spacing: var(--space-1);",
                     "--radius-md: var(--radius-md);", "--font-display: var(--font-family-display);",
                     "--ease-standard: var(--ease-standard);", "--transition-duration-fast: var(--duration-fast);",
                     "--breakpoint-md: 48rem;", "--container-md: 768px;"):
            self.assertIn(line, tailwind)
        css_names = set(re.findall(r"^\s+(--[a-z0-9-]+):", self.outputs["tokens.css"], re.M))
        for target in re.findall(r"var\((--[a-z0-9-]+)\)", tailwind):
            self.assertIn(target, css_names)

    def test_figma_variables_shape(self):
        data = json.loads(self.outputs["figma-variables.json"])
        collections = {c["name"]: c for c in data["collections"]}
        self.assertEqual(list(collections), ["Primitives", "Semantic"])
        self.assertEqual(collections["Semantic"]["modes"], ["Light", "Dark", "High contrast"])
        self.assertEqual(collections["Primitives"]["modes"], ["Meridian", "Ember"])
        names = {(c["name"], v["name"]): v for c in data["collections"] for v in c["variables"]}
        semantic = collections["Semantic"]["variables"]
        self.assertEqual(len(semantic), len(tk.SEMANTIC_COLOR_PATHS))
        for collection in data["collections"]:
            for variable in collection["variables"]:
                self.assertEqual(set(variable["valuesByMode"]), set(collection["modes"]), variable["name"])
                for value in variable["valuesByMode"].values():
                    if isinstance(value, dict) and "alias" in value:
                        target = names[(value["alias"]["collection"], value["alias"]["name"])]
                        self.assertEqual(target["type"], variable["type"])
        canvas = names[("Semantic", "color/bg/canvas")]
        self.assertEqual(canvas["scopes"], ["FRAME_FILL", "SHAPE_FILL"])
        self.assertEqual(canvas["codeSyntax"]["WEB"], "var(--color-bg-canvas)")
        self.assertEqual(names[("Primitives", "space/4")]["valuesByMode"]["Meridian"], 16)
        self.assertEqual(names[("Primitives", "color/teal/600")]["scopes"], [])

    def test_build_is_deterministic(self):
        again = tk.build_outputs(tk.load_source(SRC))
        self.assertEqual(again, self.outputs)
        with tempfile.TemporaryDirectory() as one, tempfile.TemporaryDirectory() as two:
            self.assertEqual(run_cli("build", "--out", one)[0], 0)
            self.assertEqual(run_cli("build", "--out", two)[0], 0)
            for name in tk.OUTPUTS:
                self.assertEqual((Path(one) / name).read_bytes(), (Path(two) / name).read_bytes(), name)
                self.assertNotRegex((Path(one) / name).read_text(encoding="utf-8"), r"20\d\d-\d\d-\d\d")

    def test_shipped_dist_is_current(self):
        code, out, _ = run_cli("check")
        self.assertEqual(code, 0, out)

    def test_ramps_match_recipes(self):
        self.assertEqual(tk.check_ramps(self.source), [])


class StalenessTests(unittest.TestCase):
    def test_check_detects_stale_and_missing_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertEqual(run_cli("build", "--out", temporary)[0], 0)
            self.assertEqual(run_cli("check", "--out", temporary)[0], 0)
            css = Path(temporary) / "tokens.css"
            css.write_text(css.read_text(encoding="utf-8").replace("#ffffff", "#fffffe", 1), encoding="utf-8")
            code, out, _ = run_cli("check", "--out", temporary)
            self.assertEqual(code, 1)
            self.assertIn("stale", out)
            (Path(temporary) / "figma-variables.json").unlink()
            code, out, _ = run_cli("check", "--out", temporary)
            self.assertIn("missing", out)

    def test_source_change_makes_dist_stale(self):
        with SourceCopy() as copy, tempfile.TemporaryDirectory() as out:
            self.assertEqual(run_cli("build", "--src", str(copy.path), "--out", out)[0], 0)
            copy.edit("primitives.tokens.json", lambda d: d["radius"]["md"].update({"$value": "6px"}))
            self.assertEqual(run_cli("check", "--src", str(copy.path), "--out", out)[0], 1)


class BrokenFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.errors = tk.lint(tk.load_source(BROKEN))["errors"]

    def assertReported(self, *fragments):
        for fragment in fragments:
            self.assertTrue(any(fragment in error for error in self.errors), f"{fragment!r} not in lint output")

    def test_structure_errors(self):
        self.assertReported("[structure] primitives.tokens.json: color.bad-hex: color must be #rrggbb",
                            "[structure] primitives.tokens.json: Radius: names must be lowercase")

    def test_alias_errors(self):
        self.assertReported("[alias] primitives.tokens.json: color.loop-a: circular alias: color.loop-a -> color.loop-b",
                            "[alias] semantic.light.tokens.json: color.fg.subtle: unresolved alias {color.gray.missing}")

    def test_contract_errors(self):
        self.assertReported("[contract] missing contract variable --color-bg-sunken",
                            "[contract] missing contract variable --space-1",
                            "[contract] semantic.light.tokens.json: missing semantic token color.accent.default",
                            "[contract] missing breakpoint.md (768px)")

    def test_tier_and_brand_errors(self):
        self.assertReported(
            "[tier] components.tokens.json: button.bg aliases primitive color.gray.900",
            "[tier] components.tokens.json: button.padding is a literal",
            "[tier] semantic.light.tokens.json: color.bg.surface-raised is a literal",
            "[brand] brands/bad.tokens.json: color.gray.100 is not brandable")

    def test_contrast_errors_name_the_pair_and_ratio(self):
        self.assertReported(
            "[contrast] fixture/light: color.fg.muted #aaaaaa on color.bg.canvas #ffffff is 2.32:1, needs 4.5:1",
            "[contrast] bad/light: color.fg.muted #aaaaaa on color.bg.surface-raised #ffffff is 2.32:1")

    def test_build_and_lint_cli_fail(self):
        code, out, _ = run_cli("lint", "--src", str(BROKEN))
        self.assertEqual(code, 1)
        self.assertIn("FAILED", out)
        with tempfile.TemporaryDirectory() as temporary:
            code, _, err = run_cli("build", "--src", str(BROKEN), "--out", temporary)
            self.assertEqual(code, 1)
            self.assertIn("build aborted", err)
            self.assertEqual(list(Path(temporary).iterdir()), [])


class MutationTests(unittest.TestCase):
    def test_renamed_contract_name_is_flagged_with_a_hint(self):
        def rename(data):
            fg = data["color"]["fg"]
            fg["secondary"] = fg.pop("muted")
        with SourceCopy() as copy:
            for mode in ("light", "dark", "high-contrast"):
                copy.edit(f"semantic.{mode}.tokens.json", rename)
            errors = copy.lint()
        self.assertTrue(any("missing contract variable --color-fg-muted (renamed? found --color-fg-secondary" in e
                            for e in errors), errors)

    def test_low_contrast_dark_mode_fails_in_every_brand(self):
        with SourceCopy() as copy:
            copy.edit("semantic.dark.tokens.json",
                      lambda d: d["color"]["fg"]["muted"].update({"$value": "{color.neutral.600}"}))
            errors = copy.lint()
        for brand in ("meridian", "ember"):
            self.assertTrue(any(e.startswith(f"[contrast] {brand}/dark: color.fg.muted") and "needs 4.5:1" in e
                                for e in errors), errors)

    def test_high_contrast_requires_seven_to_one(self):
        with SourceCopy() as copy:
            copy.edit("semantic.high-contrast.tokens.json",
                      lambda d: d["color"]["fg"]["muted"].update({"$value": "{color.neutral.600}"}))
            errors = copy.lint()
        self.assertTrue(any("high-contrast: color.fg.muted" in e and "needs 7:1" in e for e in errors), errors)

    def test_component_aliasing_a_primitive_fails(self):
        with SourceCopy() as copy:
            copy.edit("components.tokens.json",
                      lambda d: d["button"]["primary"]["bg"].update({"$value": "{color.teal.600}"}))
            errors = copy.lint()
        self.assertIn("[tier] components.tokens.json: button.primary.bg aliases primitive color.teal.600; components "
                      "may alias semantic tokens and public scale tokens only", errors)

    def test_hand_edited_ramp_is_flagged(self):
        with SourceCopy() as copy:
            copy.edit("primitives.tokens.json", lambda d: d["color"]["teal"]["600"].update({"$value": "#006d6d"}))
            errors = copy.lint()
        self.assertTrue(any(e.startswith("[ramp] primitives.tokens.json: color.teal.600 is #006d6d") for e in errors))

    def test_contract_value_drift_is_flagged(self):
        with SourceCopy() as copy:
            copy.edit("primitives.tokens.json", lambda d: d["space"]["4"].update({"$value": "1.1rem"}))
            errors = copy.lint()
        self.assertIn("[contract] --space-4 is 1.1rem, contract says 1rem", errors)

    def test_new_brand_is_built_and_linted(self):
        with SourceCopy() as copy:
            brand = {"color": {"$type": "color", "accent": {str(s): {"$value": "{color.blue.%d}" % s}
                                                            for s in ct.DEFAULT_STEPS}}}
            (copy.path / "brands" / "harbor.tokens.json").write_text(json.dumps(brand), encoding="utf-8")
            source = tk.load_source(copy.path)
            self.assertEqual(tk.lint(source)["errors"], [])
            css = tk.build_css(source)
        self.assertIn('[data-brand="harbor"] {', css)
        self.assertIn("--color-accent-600: var(--color-blue-600);", css)


if __name__ == "__main__":
    unittest.main()
