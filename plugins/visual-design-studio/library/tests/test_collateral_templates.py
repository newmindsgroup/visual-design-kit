"""Collateral templates: token wiring, page setup, fonts, sample marking and the color values printed on the page."""
# Version-Timestamp: 2026-10-23 20:38:00 UTC
import json
import math
import re
import shutil
import subprocess
import unittest
from pathlib import Path

LIBRARY = Path(__file__).resolve().parents[1]
COLLATERAL = LIBRARY / "examples" / "collateral"
TOKENS_DIST = LIBRARY / "tokens" / "dist"
SCRIPTS = LIBRARY.parent / "skills" / "print-packaging-social" / "scripts"

# file: (@page size, number of .page elements)
TEMPLATES = {
    "brand-guidelines.html": ("11in 8.5in", 9),
    "one-pager.html": ("8.5in 11in", 1),
    "case-study.html": ("8.5in 11in", 2),
    "proposal-cover.html": ("8.5in 11in", 1),
    "business-card.html": ("3.5in 2in", 2),
    "social-carousel.html": ("1080px 1350px", 5),
    "capabilities-deck.html": ("1920px 1080px", 4),
}
LOCAL_PROPERTIES = {"--page-w", "--page-h"}


def read(name):
    return (COLLATERAL / name).read_text(encoding="utf-8")


def style_text(html):
    blocks = re.findall(r"<style>(.*?)</style>", html, re.S)
    attrs = re.findall(r'style="([^"]*)"', html)
    return "\n".join(blocks + attrs)


def luminance(hex_value):
    channels = [int(hex_value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    channels = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(a, b):
    hi, lo = sorted([luminance(a), luminance(b)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


class TemplateTests(unittest.TestCase):
    def test_every_template_is_wired_to_the_shared_layers(self):
        for name in TEMPLATES:
            html = read(name)
            with self.subTest(template=name):
                self.assertIn("Version-Timestamp:", html)
                self.assertRegex(html, r'<html lang="en" data-brand="meridian" data-theme="light">')
                self.assertRegex(html, r"<title>[^<]+\(sample\)</title>")
                order = [html.index(f'href="styles/{f}"') for f in ("tokens.css", "fonts.css", "collateral.css")]
                self.assertEqual(order, sorted(order), "tokens.css, fonts.css, collateral.css in that order")
                self.assertIn('src="assets/brand.js"', html)

    def test_page_size_and_page_count(self):
        for name, (size, pages) in TEMPLATES.items():
            html = read(name)
            with self.subTest(template=name):
                self.assertRegex(html, r"@page \{\s*size: " + re.escape(size) + ";")
                self.assertEqual(len(re.findall(r'<section class="page[ "]', html)), pages)

    def test_business_card_has_bleed_and_marks(self):
        html = read("business-card.html")
        page_rule = re.search(r"@page \{(.*?)\}", html, re.S).group(1)
        self.assertIn("bleed: 0.125in;", page_rule)
        self.assertIn("marks: crop;", page_rule)
        self.assertEqual(html.count('data-bleed="0.125in"'), 2)
        self.assertIn("inset: calc(-1 * var(--bleed));", html)

    def test_sample_content_is_marked_on_every_page(self):
        for name in TEMPLATES:
            html = read(name)
            sections = re.split(r'<section class="page', html)[1:]
            for index, section in enumerate(sections, start=1):
                with self.subTest(template=name, page=index):
                    self.assertIn("SAMPLE", section)

    def test_no_literal_colors_in_styles(self):
        sources = {"styles/collateral.css": read("styles/collateral.css")}
        sources.update({name: style_text(read(name)) for name in TEMPLATES})
        for name, css in sources.items():
            with self.subTest(source=name):
                self.assertIsNone(re.search(r"#[0-9a-fA-F]{3,8}\b", css), "use tokens, not hex")
                self.assertIsNone(re.search(r"\b(rgb|rgba|hsl|hsla|oklch)\(", css), "use tokens, not color functions")

    def test_every_custom_property_resolves(self):
        defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", read("styles/tokens.css")))
        defined |= set(re.findall(r"(--[a-z0-9-]+)\s*:", read("styles/collateral.css")))
        used_collateral = set(re.findall(r"var\((--[a-z0-9-]+)", read("styles/collateral.css")))
        self.assertEqual(used_collateral - defined - LOCAL_PROPERTIES, set())
        for name in TEMPLATES:
            html = read(name)
            local = set(re.findall(r"(--[a-z0-9-]+)\s*:", style_text(html)))
            used = set(re.findall(r"var\((--[a-z0-9-]+)", html))
            with self.subTest(template=name):
                self.assertEqual(used - defined - local, set())

    def test_field_names_are_snake_case(self):
        for name in TEMPLATES:
            for field in re.findall(r'data-field="([^"]+)"', read(name)):
                with self.subTest(template=name, field=field):
                    self.assertRegex(field, r"^[a-z][a-z0-9_]*$")

    def test_brand_text_comes_in_pairs(self):
        for name in TEMPLATES:
            html = read(name)
            with self.subTest(template=name):
                self.assertEqual(html.count('class="only-meridian"'), html.count('class="only-ember"'))


class TokenAndFontTests(unittest.TestCase):
    def test_tokens_copy_is_fresh(self):
        self.assertEqual((COLLATERAL / "styles" / "tokens.css").read_bytes(), (TOKENS_DIST / "tokens.css").read_bytes(),
                         "copy library/tokens/dist/tokens.css to examples/collateral/styles/tokens.css")

    def test_fonts_resolve_and_carry_licenses(self):
        css = read("styles/fonts.css")
        urls = re.findall(r'url\("([^"]+)"\)', css)
        self.assertGreaterEqual(len(urls), 7)
        for url in urls:
            path = (COLLATERAL / "styles" / url).resolve()
            with self.subTest(url=url):
                self.assertTrue(path.is_file())
                license_text = (path.parent / "OFL.txt").read_text(encoding="utf-8")
                self.assertIn("SIL Open Font License", license_text)
        families = {p.name for p in (COLLATERAL / "fonts").iterdir() if p.is_dir()}
        used = {Path(u).parent.name for u in urls}
        self.assertEqual(families, used, "every bundled family is used and every used family is bundled")

    def test_guideline_color_values_match_resolved_tokens(self):
        resolved = json.loads((TOKENS_DIST / "tokens.resolved.json").read_text(encoding="utf-8"))["values"]
        html = read("brand-guidelines.html")
        swatches = re.findall(r'<span class="only-(meridian|ember)" data-token="([^"]+)" data-format="(hex|rgb)">([^<]+)</span>', html)
        self.assertEqual(len(swatches), 20)  # 5 swatches x 2 brands x HEX and RGB
        for brand, token, fmt, shown in swatches:
            value = resolved[brand]["light"][token]
            expected = value if fmt == "hex" else " ".join(str(int(value[i:i + 2], 16)) for i in (1, 3, 5))
            with self.subTest(brand=brand, token=token, format=fmt):
                self.assertEqual(shown, expected)

    def test_guideline_contrast_claims_are_not_rounded_up(self):
        resolved = json.loads((TOKENS_DIST / "tokens.resolved.json").read_text(encoding="utf-8"))["values"]
        html = read("brand-guidelines.html")
        claims = re.findall(r'<span class="only-(meridian|ember)" data-contrast="([^ ]+) on ([^"]+)">([\d.]+):1</span>', html)
        self.assertEqual(len(claims), 8)
        for brand, fg, bg, shown in claims:
            values = resolved[brand]["light"]
            actual = contrast(values[fg], values[bg])
            with self.subTest(brand=brand, pair=f"{fg} on {bg}"):
                self.assertLessEqual(float(shown), actual)
                self.assertLess(actual - float(shown), 0.1)
                self.assertGreaterEqual(actual, 4.5, "every listed text pair passes WCAG AA")
                self.assertEqual(float(shown), math.floor(actual * 10) / 10)


class ScriptTests(unittest.TestCase):
    def test_render_script_is_versioned_and_parses(self):
        script = SCRIPTS / "render_collateral.mjs"
        text = script.read_text(encoding="utf-8")
        self.assertIn("Version-Timestamp:", text)
        self.assertIn("tagged: true", text)
        self.assertIn("outline: true", text)
        self.assertIn("preferCSSPageSize: true", text)
        node = shutil.which("node")
        if not node:
            self.skipTest("node not installed")
        result = subprocess.run([node, "--check", str(script)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_render_script_help_runs_without_playwright(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node not installed")
        result = subprocess.run([node, str(SCRIPTS / "render_collateral.mjs"), "--help"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--brand", result.stdout)


if __name__ == "__main__":
    unittest.main()
