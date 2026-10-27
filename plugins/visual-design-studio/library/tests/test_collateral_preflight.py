"""preflight_pdf.py: boxes, bleed, fonts, images and ppi, color spaces, output intents, exit codes.

Every PDF here is written by hand in the test (a few objects, an xref table, Flate where needed), so the suite has no
fixtures and no third-party PDF library.
"""
# Version-Timestamp: 2026-10-23 20:38:00 UTC
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
import zlib
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "skills" / "print-packaging-social" / "scripts" / "preflight_pdf.py"
_spec = importlib.util.spec_from_file_location("preflight_pdf", SCRIPT)
pf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pf)


def stream(dictionary, data, compress=False):
    """Return an object body for a stream; dictionary is the inside of << >> without Length/Filter."""
    if compress:
        data = zlib.compress(data)
        dictionary += b" /Filter /FlateDecode"
    return b"<< " + dictionary + b" /Length " + str(len(data)).encode() + b" >>\nstream\n" + data + b"\nendstream"


def build_pdf(objects, root=1, info=None, version=b"1.6", extra_trailer=b""):
    """objects: {num: body bytes}. Writes header, objects, xref and trailer."""
    out = bytearray(b"%PDF-" + version + b"\n%\xe2\xe3\xcf\xd3\n")
    offsets = {}
    for num in sorted(objects):
        offsets[num] = len(out)
        out += str(num).encode() + b" 0 obj\n" + objects[num] + b"\nendobj\n"
    size = max(objects) + 1
    xref = len(out)
    out += b"xref\n0 " + str(size).encode() + b"\n0000000000 65535 f \n"
    for num in range(1, size):
        out += (b"%010d 00000 n \n" % offsets[num]) if num in offsets else b"0000000000 65535 f \n"
    trailer = b"<< /Size " + str(size).encode() + b" /Root " + str(root).encode() + b" 0 R"
    if info:
        trailer += b" /Info " + str(info).encode() + b" 0 R"
    out += b"trailer\n" + trailer + extra_trailer + b" >>\nstartxref\n" + str(xref).encode() + b"\n%%EOF\n"
    return bytes(out)


def print_ready_pdf():
    """Business card: 252 x 144pt trim, 9pt bleed, embedded font, CMYK image at exactly 300 ppi, PDF/X-4 markers."""
    xmp = (b'<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
           b'<rdf:Description xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/">'
           b"<pdfxid:GTS_PDFXVersion>PDF/X-4</pdfxid:GTS_PDFXVersion></rdf:Description></rdf:RDF></x:xmpmeta>")
    content = b"q 252 0 0 144 9 9 cm /Im1 Do Q 0 0 0 1 k BT /F1 9 Tf 20 20 Td (Sample) Tj ET"
    return build_pdf({
        1: b"<< /Type /Catalog /Pages 2 0 R /Metadata 8 0 R /OutputIntents [<< /Type /OutputIntent /S /GTS_PDFX "
           b"/OutputConditionIdentifier (Test CMYK condition) /DestOutputProfile 7 0 R >>] >>",
        2: b"<< /Type /Pages /Kids [3 0 R] /Count 1 /MediaBox [0 0 270 162] >>",
        3: b"<< /Type /Page /Parent 2 0 R /TrimBox [9 9 261 153] /BleedBox [0 0 270 162] "
           b"/Resources << /Font << /F1 4 0 R >> /XObject << /Im1 5 0 R >> >> /Contents 6 0 R >>",
        4: b"<< /Type /Font /Subtype /TrueType /BaseFont /ABCDEF+SampleSans /FontDescriptor 9 0 R >>",
        5: stream(b"/Type /XObject /Subtype /Image /Width 1050 /Height 600 /ColorSpace /DeviceCMYK "
                  b"/BitsPerComponent 8 /Filter /DCTDecode", b"\xff\xd8 not a real jpeg \xff\xd9"),
        6: stream(b"", content, compress=True),
        7: stream(b"/N 4", b"not a real icc profile"),
        8: stream(b"/Type /Metadata /Subtype /XML", xmp),
        9: b"<< /Type /FontDescriptor /FontName /ABCDEF+SampleSans /FontFile2 10 0 R >>",
        10: stream(b"", b"\x00\x01\x00\x00 fake font"),
    })


def screen_pdf():
    """Letter page: no trim or bleed, Helvetica not embedded, RGB image at 150 ppi, rg operator."""
    content = b"q 288 0 0 192 72 500 cm /Im1 Do Q 0.1 0.2 0.3 rg BT /F1 12 Tf 72 72 Td (Hi) Tj ET"
    return build_pdf({
        1: b"<< /Type /Catalog /Pages 2 0 R >>",
        2: b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        3: b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
           b"/Resources << /Font << /F1 4 0 R >> /XObject << /Im1 5 0 R >> >> /Contents 6 0 R >>",
        4: b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        5: stream(b"/Type /XObject /Subtype /Image /Width 600 /Height 400 /ColorSpace /DeviceRGB "
                  b"/BitsPerComponent 8", b"\x00" * 16),
        6: stream(b"", content),
    }, version=b"1.4")


def object_stream_pdf():
    """Page tree inside a compressed object stream; image placed through a scaled form XObject; spot color;
    inline image."""
    inner = {
        2: b"<< /Type /Pages /Kids [3 0 R] /Count 1 /MediaBox [0 0 400 400] >>",
        3: b"<< /Type /Page /Parent 2 0 R /TrimBox [0 0 400 400] /Resources << /XObject << /Fm1 5 0 R >> "
           b"/ColorSpace << /CS0 [/Separation /PANTONE#20186#20C /DeviceCMYK 9 0 R] >> >> /Contents 4 0 R >>",
    }
    header, body = b"", b""
    for num, obj in inner.items():
        header += str(num).encode() + b" " + str(len(body)).encode() + b" "
        body += obj + b" "
    objstm = stream(b"/Type /ObjStm /N 2 /First " + str(len(header)).encode(), header + body, compress=True)
    page_content = (b"/CS0 cs 1 scn 0 0 10 10 re f q 10 0 0 10 300 300 cm BI /W 10 /H 10 /CS /G /BPC 8 ID "
                    + bytes(range(100)) + b" EI Q q /Fm1 Do Q")
    form_content = b"q 100 0 0 50 0 0 cm /Im2 Do Q"
    return build_pdf({
        1: b"<< /Type /Catalog /Pages 2 0 R >>",
        4: stream(b"", page_content, compress=True),
        5: stream(b"/Type /XObject /Subtype /Form /BBox [0 0 200 200] /Matrix [2 0 0 2 0 0] "
                  b"/Resources << /XObject << /Im2 6 0 R >> >>", form_content, compress=True),
        6: stream(b"/Type /XObject /Subtype /Image /Width 200 /Height 100 /ColorSpace [/ICCBased 8 0 R] "
                  b"/BitsPerComponent 8", b"\x00" * 8),
        7: objstm,
        8: stream(b"/N 3", b"icc"),
        9: b"<< /FunctionType 2 /Domain [0 1] /C0 [0 0 0 0] /C1 [1 0.7 0 0] /N 1 >>",
    })


def run(pdf_bytes, *args):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test.pdf"
        path.write_bytes(pdf_bytes)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = pf.main([str(path), *args])
        return code, out.getvalue(), err.getvalue()


def report(pdf_bytes, *args):
    code, out, _ = run(pdf_bytes, "--json", *args)
    return code, json.loads(out)


class PrintReadyTests(unittest.TestCase):
    def test_clean_print_file_passes(self):
        code, r = report(print_ready_pdf())
        self.assertEqual(code, 0, r["findings"])
        self.assertEqual(r["page_count"], 1)
        self.assertEqual(r["pdf_version"], "1.6")

    def test_boxes_and_bleed_are_measured(self):
        _, r = report(print_ready_pdf())
        page = r["pages"][0]
        self.assertEqual(page["media_box"], [0, 0, 270, 162])  # inherited from the Pages node
        self.assertEqual(page["trim_box"], [9, 9, 261, 153])
        self.assertEqual(page["trim_size_mm"], [88.9, 50.8])
        self.assertAlmostEqual(page["min_bleed_mm"], 3.175, delta=0.006)

    def test_font_image_color_and_standard(self):
        _, r = report(print_ready_pdf())
        self.assertEqual(len(r["fonts"]), 1)
        self.assertTrue(r["fonts"][0]["embedded"])
        self.assertTrue(r["fonts"][0]["subset"])
        image = r["images"][0]
        self.assertEqual(image["pixels"], [1050, 600])
        self.assertEqual(image["color_space"], "DeviceCMYK")
        self.assertEqual(image["placements"][0]["ppi"], 300.0)
        self.assertEqual(image["placements"][0]["size_in"], [3.5, 2.0])
        self.assertEqual(sorted(r["color_spaces"]), ["DeviceCMYK"])
        self.assertEqual(r["pdfx_claimed"], "PDF/X-4")
        self.assertEqual(r["output_intents"][0]["subtype"], "GTS_PDFX")
        self.assertEqual(r["output_intents"][0]["profile_components"], 4)
        self.assertTrue(any("does not validate" in n for n in r["notes"]))

    def test_thresholds_are_flags(self):
        code, r = report(print_ready_pdf(), "--min-bleed", "5mm")
        self.assertEqual(code, 1)
        self.assertEqual([f["check"] for f in r["findings"]], ["bleed"])
        code, r = report(print_ready_pdf(), "--min-ppi", "400")
        self.assertEqual(code, 1)
        self.assertEqual([f["check"] for f in r["findings"]], ["resolution"])
        code, _ = report(print_ready_pdf(), "--min-bleed", "0.125in")
        self.assertEqual(code, 0)


class ScreenPdfTests(unittest.TestCase):
    def test_print_intent_lists_every_production_problem(self):
        code, r = report(screen_pdf())
        self.assertEqual(code, 1)
        checks = sorted({f["check"] for f in r["findings"]})
        self.assertEqual(checks, ["bleed", "color", "font-embedding", "output-intent", "resolution", "trim"])
        self.assertEqual(r["images"][0]["placements"][0]["ppi"], 150.0)
        font = r["fonts"][0]
        self.assertFalse(font["embedded"])
        self.assertTrue(font["standard14"])

    def test_screen_intent_only_flags_missing_fonts(self):
        code, r = report(screen_pdf(), "--intent", "screen")
        self.assertEqual(code, 1)
        self.assertEqual([f["check"] for f in r["findings"]], ["font-embedding"])
        self.assertTrue(any("150.0 ppi" in n for n in r["notes"]))

    def test_allow_rgb_drops_the_color_finding(self):
        _, r = report(screen_pdf(), "--allow-rgb")
        self.assertNotIn("color", {f["check"] for f in r["findings"]})

    def test_text_report(self):
        code, out, _ = run(screen_pdf())
        self.assertEqual(code, 1)
        self.assertIn("NOT EMBEDDED", out)
        self.assertIn("FINDINGS (6)", out)
        self.assertIn("result: 6 finding(s)", out)


class StructureTests(unittest.TestCase):
    def test_object_streams_forms_spot_colors_and_inline_images(self):
        code, r = report(object_stream_pdf(), "--allow-rgb", "--min-bleed", "0mm", "--min-ppi", "72")
        self.assertEqual(r["page_count"], 1)
        self.assertEqual(r["pages"][0]["trim_box"], [0, 0, 400, 400])
        by_name = {i["name"]: i for i in r["images"]}
        form_image = by_name["Im2"]
        self.assertEqual(form_image["color_space"], "ICCBased RGB (N=3)")
        self.assertEqual(form_image["placements"][0]["size_in"], [2.778, 1.389])  # 100x50pt scaled 2x by the form
        self.assertEqual(form_image["placements"][0]["ppi"], 72.0)
        inline = by_name["inline image"]
        self.assertEqual(inline["pixels"], [10, 10])
        self.assertEqual(inline["color_space"], "DeviceGray")
        self.assertEqual(inline["placements"][0]["ppi"], 72.0)
        self.assertIn("Separation: PANTONE 186 C", r["color_spaces"])
        self.assertTrue(any("PANTONE 186 C" in n for n in r["notes"]))
        self.assertEqual([f["check"] for f in r["findings"]], ["output-intent"])
        self.assertEqual(code, 1)

    def test_require_pdfx(self):
        _, r = report(screen_pdf(), "--require-pdfx")
        self.assertIn("pdfx", {f["check"] for f in r["findings"]})


class ErrorTests(unittest.TestCase):
    def test_not_a_pdf_exits_2(self):
        code, _, err = run(b"hello, not a pdf")
        self.assertEqual(code, 2)
        self.assertIn("not a PDF", err)

    def test_encrypted_exits_2(self):
        data = build_pdf({1: b"<< /Type /Catalog /Pages 2 0 R >>", 2: b"<< /Type /Pages /Kids [] /Count 0 >>",
                          3: b"<< /Filter /Standard /V 1 /R 2 >>"}, extra_trailer=b" /Encrypt 3 0 R")
        code, _, err = run(data)
        self.assertEqual(code, 2)
        self.assertIn("encrypted", err)

    def test_missing_file_exits_2(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = pf.main(["/nonexistent/file.pdf"])
        self.assertEqual(code, 2)

    def test_parse_length_units(self):
        self.assertAlmostEqual(pf.parse_length("3mm"), 8.5039, places=3)
        self.assertAlmostEqual(pf.parse_length("0.125in"), 9.0)
        self.assertAlmostEqual(pf.parse_length("9pt"), 9.0)
        self.assertAlmostEqual(pf.parse_length("3"), pf.parse_length("3mm"))
        with self.assertRaises(Exception):
            pf.parse_length("three")


if __name__ == "__main__":
    unittest.main()
