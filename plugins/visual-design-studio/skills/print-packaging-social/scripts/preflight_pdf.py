#!/usr/bin/env python3
# Version-Timestamp: 2026-10-23 20:38:00 UTC
# Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.309; timestamp=2026-10-23 20:38:00 UTC
"""Preflight report for a PDF before it goes to a printer or a client.

Standard library only, Python 3.9+. Reads the PDF directly (zlib for Flate streams) and reports:

- page count; MediaBox, CropBox, BleedBox, TrimBox per page and the bleed on each side;
- fonts and whether each is embedded (Type 3 and subset fonts flagged);
- image XObjects and inline images: pixel size, color space, filter, and effective ppi at the placed size when the
  content stream shows it (otherwise "unknown");
- color spaces in use: DeviceRGB, DeviceCMYK, DeviceGray, ICCBased (with component count), Separation and DeviceN
  names (spot colors), Lab, Indexed;
- OutputIntents, PDF/X and PDF/A markers (Info dictionary and XMP), tagging and outline.

This is a preflight report, not a PDF/X validator. Markers are what the file claims; a printer's preflight (or
Acrobat Preflight) and a hard proof remain the acceptance test.

Exit codes: 0 no findings, 1 findings, 2 error (not a PDF, encrypted, unreadable).

    python3 preflight_pdf.py file.pdf [--intent print|screen] [--min-bleed 3mm] [--min-ppi 300] [--json]
"""

import argparse
import base64
import json
import math
import re
import sys
import zlib

VERSION = "0.8.0"
WHITESPACE = b" \t\r\n\x0c\x00"
DELIMITERS = b"()<>[]{}/%"
STANDARD_14 = {
    "Courier", "Courier-Bold", "Courier-Oblique", "Courier-BoldOblique", "Helvetica", "Helvetica-Bold",
    "Helvetica-Oblique", "Helvetica-BoldOblique", "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic",
    "Symbol", "ZapfDingbats",
}
MAX_FORM_DEPTH = 12


class PdfError(Exception):
    """The file cannot be read as a PDF."""


class Name(str):
    """A PDF name object (/Foo), kept distinct from strings."""


class Ref(tuple):
    """An indirect reference (num, gen)."""

    @property
    def num(self):
        return self[0]


class Stream:
    def __init__(self, dictionary, raw):
        self.dict = dictionary
        self.raw = raw


class Keyword(bytes):
    """A bare keyword or content-stream operator."""


# ---------- lexer and parser ----------

class Lexer:
    def __init__(self, data, pos=0):
        self.data = data
        self.pos = pos
        self.peeked = []

    def _skip(self):
        data, n = self.data, len(self.data)
        while self.pos < n:
            c = data[self.pos]
            if c in WHITESPACE:
                self.pos += 1
            elif c == 0x25:  # % comment
                while self.pos < n and data[self.pos] not in b"\r\n":
                    self.pos += 1
            else:
                break

    def _read(self):
        self._skip()
        data, n = self.data, len(self.data)
        if self.pos >= n:
            return None
        c = data[self.pos:self.pos + 1]
        if c == b"/":
            start = self.pos + 1
            self.pos = start
            while self.pos < n and data[self.pos] not in WHITESPACE and data[self.pos] not in DELIMITERS:
                self.pos += 1
            raw = data[start:self.pos]
            raw = re.sub(rb"#([0-9A-Fa-f]{2})", lambda m: bytes([int(m.group(1), 16)]), raw)
            return Name(raw.decode("latin-1"))
        if c == b"(":
            return self._literal_string()
        if c == b"<":
            if data[self.pos + 1:self.pos + 2] == b"<":
                self.pos += 2
                return Keyword(b"<<")
            end = data.find(b">", self.pos)
            if end < 0:
                raise PdfError("unterminated hex string")
            hexpart = re.sub(rb"\s", b"", data[self.pos + 1:end])
            self.pos = end + 1
            if len(hexpart) % 2:
                hexpart += b"0"
            try:
                return bytes.fromhex(hexpart.decode("ascii"))
            except ValueError:
                return b""
        if c == b">":
            if data[self.pos + 1:self.pos + 2] == b">":
                self.pos += 2
                return Keyword(b">>")
            self.pos += 1
            return Keyword(b">")
        if c in (b"[", b"]", b"{", b"}"):
            self.pos += 1
            return Keyword(c)
        start = self.pos
        while self.pos < n and data[self.pos] not in WHITESPACE and data[self.pos] not in DELIMITERS:
            self.pos += 1
        if self.pos == start:  # stray delimiter such as ')'
            self.pos += 1
            return Keyword(data[start:self.pos])
        word = data[start:self.pos]
        if re.fullmatch(rb"[+-]?(\d+\.?\d*|\.\d+)", word):
            text = word.decode("ascii")
            if "." in text:
                return float(text)
            return int(text)
        return Keyword(word)

    def _literal_string(self):
        data, n = self.data, len(self.data)
        self.pos += 1
        depth, out = 1, bytearray()
        escapes = {ord("n"): b"\n", ord("r"): b"\r", ord("t"): b"\t", ord("b"): b"\b", ord("f"): b"\f",
                   ord("("): b"(", ord(")"): b")", ord("\\"): b"\\"}
        while self.pos < n:
            c = data[self.pos]
            if c == 0x5C:  # backslash
                self.pos += 1
                if self.pos >= n:
                    break
                e = data[self.pos]
                if e in escapes:
                    out += escapes[e]
                    self.pos += 1
                elif 0x30 <= e <= 0x37:
                    octal = re.match(rb"[0-7]{1,3}", data[self.pos:self.pos + 3]).group(0)
                    out.append(int(octal, 8) & 0xFF)
                    self.pos += len(octal)
                elif e in b"\r\n":
                    self.pos += 2 if data[self.pos:self.pos + 2] == b"\r\n" else 1
                else:
                    self.pos += 1
                continue
            if c == 0x28:
                depth += 1
            elif c == 0x29:
                depth -= 1
                if depth == 0:
                    self.pos += 1
                    return bytes(out)
            out.append(c)
            self.pos += 1
        raise PdfError("unterminated string")

    def next(self):
        if self.peeked:
            return self.peeked.pop(0)
        return self._read()

    def peek(self, k=0):
        while len(self.peeked) <= k:
            self.peeked.append(self._read())
        return self.peeked[k]


def parse_value(lex, refs=True):
    token = lex.next()
    if token is None:
        raise PdfError("unexpected end of data")
    if isinstance(token, Keyword):
        if token == b"<<":
            result = {}
            while True:
                key = lex.next()
                if key == b">>" or key is None:
                    return result
                if not isinstance(key, Name):
                    continue
                result[str(key)] = parse_value(lex, refs)
        if token == b"[":
            items = []
            while True:
                if lex.peek() == b"]":
                    lex.next()
                    return items
                if lex.peek() is None:
                    return items
                items.append(parse_value(lex, refs))
        if token == b"true":
            return True
        if token == b"false":
            return False
        if token == b"null":
            return None
        return token
    if refs and isinstance(token, int) and isinstance(lex.peek(0), int) and lex.peek(1) == b"R":
        gen = lex.next()
        lex.next()
        return Ref((token, gen))
    return token


def decode_stream(stream, pdf=None):
    """Return decoded bytes, or None when a filter is not supported."""
    d = stream.dict
    filters = d.get("Filter")
    params = d.get("DecodeParms")
    if pdf:
        filters, params = pdf.resolve(filters), pdf.resolve(params)
    if filters is None:
        filters = []
    elif not isinstance(filters, list):
        filters = [filters]
    if not isinstance(params, list):
        params = [params] * len(filters)
    data = stream.raw
    for name, parm in zip(filters, params):
        if name in ("FlateDecode", "Fl"):
            try:
                data = zlib.decompress(data)
            except zlib.error:
                try:
                    data = zlib.decompressobj().decompress(data)
                except zlib.error:
                    return None
            if isinstance(parm, dict) and int(parm.get("Predictor", 1) or 1) >= 10:
                data = _png_unpredict(data, int(parm.get("Columns", 1) or 1) * int(parm.get("Colors", 1) or 1)
                                      * max(1, int(parm.get("BitsPerComponent", 8) or 8) // 8))
        elif name in ("ASCIIHexDecode", "AHx"):
            hexpart = re.sub(rb"\s", b"", data).split(b">")[0]
            if len(hexpart) % 2:
                hexpart += b"0"
            data = bytes.fromhex(hexpart.decode("ascii"))
        elif name in ("ASCII85Decode", "A85"):
            body = re.sub(rb"\s", b"", data)
            if body.startswith(b"<~"):
                body = body[2:]
            body = body.split(b"~>")[0]
            data = base64.a85decode(body)
        else:
            return None
    return data


def _png_unpredict(data, row_bytes):
    out, prev, i = bytearray(), bytearray(row_bytes), 0
    while i + 1 + row_bytes <= len(data):
        kind, row = data[i], bytearray(data[i + 1:i + 1 + row_bytes])
        for x in range(row_bytes):
            left = row[x - 1] if x else 0
            up = prev[x]
            ul = prev[x - 1] if x else 0
            if kind == 1:
                row[x] = (row[x] + left) & 0xFF
            elif kind == 2:
                row[x] = (row[x] + up) & 0xFF
            elif kind == 3:
                row[x] = (row[x] + (left + up) // 2) & 0xFF
            elif kind == 4:
                p = left + up - ul
                pa, pb, pc = abs(p - left), abs(p - up), abs(p - ul)
                row[x] = (row[x] + (left if pa <= pb and pa <= pc else up if pb <= pc else ul)) & 0xFF
        out += row
        prev = row
        i += 1 + row_bytes
    return bytes(out)


# ---------- document ----------

OBJ_RE = re.compile(rb"(?<![0-9])(\d+)\s+(\d+)\s+obj\b")


class Pdf:
    def __init__(self, data):
        if not data.lstrip()[:5] == b"%PDF-" and b"%PDF-" not in data[:1024]:
            raise PdfError("not a PDF (no %PDF- header)")
        m = re.search(rb"%PDF-(\d\.\d)", data[:1024])
        self.header_version = m.group(1).decode() if m else "unknown"
        self.data = data
        self.objects = {}
        self.trailers = []
        self._scan()
        self._load_object_streams()
        self.trailer = self._merged_trailer()
        if self.trailer.get("Encrypt") is not None:
            raise PdfError("encrypted PDF; decrypt it first (preflight reads unencrypted files only)")
        self.root = self.resolve(self.trailer.get("Root"))
        if not isinstance(self.root, dict):
            catalogs = [o for o in self.objects.values() if isinstance(o, dict) and o.get("Type") == "Catalog"]
            if not catalogs:
                raise PdfError("no document catalog found")
            self.root = catalogs[-1]

    def _scan(self):
        """Walk the file once: every 'N G obj', skipping stream bodies, plus every trailer dictionary."""
        data, pos = self.data, 0
        next_trailer = data.find(b"trailer")
        while True:
            m = OBJ_RE.search(data, pos)
            if next_trailer >= 0 and next_trailer < pos:
                next_trailer = data.find(b"trailer", pos)
            if next_trailer >= 0 and (m is None or next_trailer < m.start()):
                try:
                    trailer = parse_value(Lexer(data, next_trailer + len(b"trailer")))
                    if isinstance(trailer, dict):
                        self.trailers.append(trailer)
                except PdfError:
                    pass
                pos = next_trailer + len(b"trailer")
                continue
            if m is None:
                break
            lex = Lexer(data, m.end())
            try:
                value = parse_value(lex)
                following = lex.peek()
            except PdfError:
                pos = m.end()
                continue
            end = lex.pos
            if following == b"stream" and isinstance(value, dict):
                raw, end = self._stream_data(value, self._stream_start(lex.pos))
                value = Stream(value, raw)
                if value.dict.get("Type") == "XRef":
                    self.trailers.append(value.dict)
            self.objects[int(m.group(1))] = value
            pos = max(end, m.end())

    def _stream_start(self, pos):
        data = self.data
        # The lexer stopped just after the 'stream' keyword; skip stray spaces and one end-of-line marker.
        while data[pos:pos + 1] == b" ":
            pos += 1
        if data[pos:pos + 2] == b"\r\n":
            return pos + 2
        if data[pos:pos + 1] in (b"\n", b"\r"):
            return pos + 1
        return pos

    def _stream_data(self, dictionary, start):
        data = self.data
        length = dictionary.get("Length")
        if isinstance(length, int) and length >= 0:
            after = data[start + length:start + length + 32].lstrip(WHITESPACE)
            if after.startswith(b"endstream"):
                end = data.find(b"endstream", start + length)
                return data[start:start + length], end + len(b"endstream")
        end = data.find(b"endstream", start)
        if end < 0:
            return data[start:], len(data)
        raw = data[start:end]
        if raw.endswith(b"\r\n"):
            raw = raw[:-2]
        elif raw.endswith((b"\n", b"\r")):
            raw = raw[:-1]
        return raw, end + len(b"endstream")

    def _load_object_streams(self):
        for num, obj in list(self.objects.items()):
            if not (isinstance(obj, Stream) and obj.dict.get("Type") == "ObjStm"):
                continue
            body = decode_stream(obj, self)
            if body is None:
                continue
            count = self.resolve(obj.dict.get("N")) or 0
            first = self.resolve(obj.dict.get("First")) or 0
            lex = Lexer(body)
            pairs = []
            for _ in range(int(count)):
                a, b = lex.next(), lex.next()
                if not isinstance(a, int) or not isinstance(b, int):
                    break
                pairs.append((a, b))
            for objnum, offset in pairs:
                if objnum in self.objects:
                    continue
                try:
                    self.objects[objnum] = parse_value(Lexer(body, first + offset))
                except PdfError:
                    continue

    def _merged_trailer(self):
        merged = {}
        for trailer in self.trailers:  # later trailers (incremental updates) win
            for key in ("Root", "Info", "Encrypt", "ID"):
                if key in trailer:
                    merged[key] = trailer[key]
        return merged

    def resolve(self, value, depth=0):
        while isinstance(value, Ref) and depth < 32:
            value = self.objects.get(value.num)
            depth += 1
        return value

    def get(self, dictionary, key, default=None):
        if isinstance(dictionary, Stream):
            dictionary = dictionary.dict
        if not isinstance(dictionary, dict):
            return default
        value = self.resolve(dictionary.get(key, default))
        return default if value is None else value


# ---------- helpers ----------

def text(value):
    if isinstance(value, bytes):
        if value.startswith(b"\xfe\xff"):
            return value[2:].decode("utf-16-be", "replace")
        return value.decode("latin-1")
    return str(value)


def rect(pdf, value):
    value = pdf.resolve(value)
    if not isinstance(value, list) or len(value) != 4:
        return None
    nums = [pdf.resolve(v) for v in value]
    if not all(isinstance(v, (int, float)) for v in nums):
        return None
    x0, y0, x1, y1 = nums
    return [min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)]


def mm(pt):
    return pt * 25.4 / 72.0


def parse_length(value):
    """'3mm', '0.125in', '9pt', '0.3cm' or a bare number (mm) -> points."""
    m = re.fullmatch(r"\s*([0-9]*\.?[0-9]+)\s*(mm|cm|in|pt)?\s*", str(value))
    if not m:
        raise argparse.ArgumentTypeError(f"bad length {value!r}; use 3mm, 0.125in or 9pt")
    n, unit = float(m.group(1)), m.group(2) or "mm"
    return n * {"mm": 72 / 25.4, "cm": 720 / 25.4, "in": 72.0, "pt": 1.0}[unit]


def mat_mul(a, b):
    """Multiply 2D affine matrices [a b c d e f]: result = a x b (apply a, then b)."""
    return [
        a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
        a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5],
    ]


IDENTITY = [1, 0, 0, 1, 0, 0]
INLINE_ABBREV = {"W": "Width", "H": "Height", "CS": "ColorSpace", "BPC": "BitsPerComponent", "F": "Filter",
                 "IM": "ImageMask", "G": "DeviceGray", "RGB": "DeviceRGB", "CMYK": "DeviceCMYK", "I": "Indexed",
                 "DCT": "DCTDecode", "Fl": "FlateDecode", "AHx": "ASCIIHexDecode", "A85": "ASCII85Decode"}


# ---------- analysis ----------

class Analyzer:
    def __init__(self, pdf):
        self.pdf = pdf
        self.fonts = {}
        self.images = {}
        self.color_spaces = {}
        self.unknown_content = []

    # color spaces ------------------------------------------------------------

    def describe_cs(self, value, resources=None):
        pdf = self.pdf
        value = pdf.resolve(value)
        if isinstance(value, Name):
            name = str(value)
            if name in ("DeviceRGB", "RGB"):
                return "DeviceRGB"
            if name in ("DeviceCMYK", "CMYK"):
                return "DeviceCMYK"
            if name in ("DeviceGray", "G"):
                return "DeviceGray"
            if name == "Pattern":
                return "Pattern"
            named = pdf.get(pdf.get(resources, "ColorSpace", {}), name) if resources is not None else None
            if named is not None:
                return self.describe_cs(named, resources)
            return name
        if isinstance(value, list) and value:
            family = str(pdf.resolve(value[0]))
            if family == "ICCBased" and len(value) > 1:
                profile = pdf.resolve(value[1])
                n = pdf.get(profile, "N")
                kind = {1: "gray", 3: "RGB", 4: "CMYK"}.get(n, "?")
                return f"ICCBased {kind} (N={n})"
            if family == "Separation" and len(value) > 1:
                return f"Separation: {text(pdf.resolve(value[1]))}"
            if family == "DeviceN" and len(value) > 1:
                names = [text(pdf.resolve(v)) for v in (pdf.resolve(value[1]) or [])]
                return f"DeviceN: {', '.join(names)}"
            if family in ("Indexed", "I") and len(value) > 1:
                return f"Indexed over {self.describe_cs(value[1], resources)}"
            if family == "Pattern" and len(value) > 1:
                return f"Pattern over {self.describe_cs(value[1], resources)}"
            return family
        return "unknown"

    def use_cs(self, desc, where):
        self.color_spaces.setdefault(desc, set()).add(where)

    # fonts -------------------------------------------------------------------

    def record_font(self, ref_key, font, page_no):
        pdf = self.pdf
        if not isinstance(font, dict):
            return
        key = ref_key if ref_key is not None else id(font)
        entry = self.fonts.get(key)
        if entry is None:
            subtype = str(pdf.get(font, "Subtype", "?"))
            descriptor = pdf.get(font, "FontDescriptor")
            base = (text(pdf.get(font, "BaseFont", "")) or text(pdf.get(descriptor, "FontName", ""))
                    or text(pdf.get(font, "Name", "")) or "(unnamed)")
            kind = subtype
            if subtype == "Type0":
                desc_fonts = pdf.get(font, "DescendantFonts") or []
                child = pdf.resolve(desc_fonts[0]) if desc_fonts else None
                descriptor = pdf.get(child, "FontDescriptor")
                kind = f"Type0/{pdf.get(child, 'Subtype', '?')}"
            embedded_as = None
            for file_key in ("FontFile", "FontFile2", "FontFile3"):
                if isinstance(descriptor, dict) and descriptor.get(file_key) is not None:
                    embedded_as = file_key
            embedded = subtype == "Type3" or embedded_as is not None
            entry = {"name": base, "type": kind, "embedded": embedded, "subset": bool(re.match(r"^[A-Z]{6}\+", base)),
                     "standard14": base.split("+")[-1] in STANDARD_14, "pages": []}
            self.fonts[key] = entry
        if page_no not in entry["pages"]:
            entry["pages"].append(page_no)

    # images ------------------------------------------------------------------

    def record_image(self, key, label, xobj, ctm, page_no, resources, inline=False):
        pdf = self.pdf
        d = xobj if inline else xobj.dict
        width, height = pdf.get(d, "Width"), pdf.get(d, "Height")
        entry = self.images.get(key)
        if entry is None:
            mask = bool(pdf.get(d, "ImageMask", False))
            filters = pdf.get(d, "Filter")
            filters = filters if isinstance(filters, list) else ([filters] if filters else [])
            filters = [INLINE_ABBREV.get(str(f), str(f)) for f in filters]
            cs_value = d.get("ColorSpace")
            if inline and isinstance(cs_value, Name):
                cs_value = Name(INLINE_ABBREV.get(str(cs_value), str(cs_value)))
            if mask:
                cs = "stencil mask"
            elif cs_value is None:
                cs = "embedded in JPX" if "JPXDecode" in filters else "unknown"
            else:
                cs = self.describe_cs(cs_value, resources)
            entry = {"name": label, "inline": inline, "pixels": [width, height], "color_space": cs,
                     "bits": pdf.get(d, "BitsPerComponent"), "filters": filters, "placements": []}
            self.images[key] = entry
            if not mask and cs != "unknown":
                self.use_cs(cs, "image")
        placement = {"page": page_no}
        if ctm is not None and isinstance(width, (int, float)) and isinstance(height, (int, float)):
            w_pt, h_pt = math.hypot(ctm[0], ctm[1]), math.hypot(ctm[2], ctm[3])
            if w_pt > 0.01 and h_pt > 0.01:
                ppi_x, ppi_y = width / (w_pt / 72.0), height / (h_pt / 72.0)
                placement.update({"size_in": [round(w_pt / 72, 3), round(h_pt / 72, 3)],
                                  "ppi": round(min(ppi_x, ppi_y), 1)})
        if "ppi" not in placement:
            placement["ppi"] = None
        entry["placements"].append(placement)

    # content streams -----------------------------------------------------------

    def run_content(self, data, resources, ctm, page_no, depth=0, seen_forms=None):
        pdf = self.pdf
        seen_forms = seen_forms if seen_forms is not None else set()
        lex = Lexer(data)
        stack, operands = [], []
        ctm = list(ctm)
        fonts = pdf.get(resources, "Font", {}) or {}
        xobjects = pdf.get(resources, "XObject", {}) or {}
        shadings = pdf.get(resources, "Shading", {}) or {}
        while True:
            try:
                token = lex.next()
            except PdfError:
                self.unknown_content.append(f"page {page_no}: content stream could not be parsed to the end")
                return
            if token is None:
                return
            if isinstance(token, Keyword) and token not in (b"[", b"]", b"<<", b">>"):
                op = bytes(token)
                if op == b"q":
                    stack.append(list(ctm))
                elif op == b"Q":
                    if stack:
                        ctm = stack.pop()
                elif op == b"cm" and len(operands) >= 6:
                    nums = operands[-6:]
                    if all(isinstance(v, (int, float)) for v in nums):
                        ctm = mat_mul([float(v) for v in nums], ctm)
                elif op in (b"rg", b"RG"):
                    self.use_cs("DeviceRGB", "content")
                elif op in (b"k", b"K"):
                    self.use_cs("DeviceCMYK", "content")
                elif op in (b"g", b"G"):
                    self.use_cs("DeviceGray", "content")
                elif op in (b"cs", b"CS") and operands and isinstance(operands[-1], Name):
                    self.use_cs(self.describe_cs(operands[-1], resources), "content")
                elif op == b"sh" and operands and isinstance(operands[-1], Name):
                    shading = pdf.get(shadings, str(operands[-1]))
                    if shading is not None:
                        self.use_cs(self.describe_cs(pdf.get(shading, "ColorSpace"), resources), "shading")
                elif op == b"Tf" and len(operands) >= 2 and isinstance(operands[-2], Name):
                    ref = fonts.get(str(operands[-2])) if isinstance(fonts, dict) else None
                    self.record_font(ref.num if isinstance(ref, Ref) else None, pdf.resolve(ref), page_no)
                elif op == b"Do" and operands and isinstance(operands[-1], Name):
                    name = str(operands[-1])
                    ref = xobjects.get(name) if isinstance(xobjects, dict) else None
                    xobj = pdf.resolve(ref)
                    if isinstance(xobj, Stream):
                        subtype = xobj.dict.get("Subtype")
                        key = ref.num if isinstance(ref, Ref) else f"{page_no}:{name}"
                        if subtype == "Image":
                            self.record_image(key, name, xobj, ctm, page_no, resources)
                        elif subtype == "Form" and depth < MAX_FORM_DEPTH and key not in seen_forms:
                            body = decode_stream(xobj, pdf)
                            matrix = pdf.get(xobj, "Matrix") or IDENTITY
                            matrix = [float(pdf.resolve(v)) for v in matrix] if len(matrix) == 6 else IDENTITY
                            form_res = pdf.get(xobj, "Resources") or resources
                            self.collect_resource_fonts(form_res, page_no)
                            if body is None:
                                self.unknown_content.append(f"page {page_no}: form {name} uses an unsupported filter")
                            else:
                                self.run_content(body, form_res, mat_mul(matrix, ctm), page_no, depth + 1,
                                                 seen_forms | {key})
                elif op == b"BI":
                    self._inline_image(lex, ctm, page_no, resources)
                operands = []
                continue
            # operand: push back keyword-structured values through the parser
            if token == b"[" or token == b"<<":
                lex.peeked.insert(0, token)
                try:
                    operands.append(parse_value(lex, refs=False))
                except PdfError:
                    return
            else:
                operands.append(token)

    def _inline_image(self, lex, ctm, page_no, resources):
        params = {}
        while True:
            key = lex.next()
            if key is None:
                return
            if key == b"ID":
                break
            if isinstance(key, Name):
                value = parse_value(lex, refs=False)
                params[INLINE_ABBREV.get(str(key), str(key))] = value
        data = lex.data
        pos = lex.pos + 1
        end = re.compile(rb"[\s]EI(?=[\s]|$)").search(data, pos)
        lex.pos = end.end() if end else len(data)
        lex.peeked.clear()
        key = f"inline:{page_no}:{len(self.images)}"
        self.record_image(key, "inline image", params, ctm, page_no, resources, inline=True)

    def collect_resource_fonts(self, resources, page_no):
        pdf = self.pdf
        fonts = pdf.get(resources, "Font", {}) or {}
        if isinstance(fonts, dict):
            for ref in fonts.values():
                self.record_font(ref.num if isinstance(ref, Ref) else None, pdf.resolve(ref), page_no)
        spaces = pdf.get(resources, "ColorSpace", {}) or {}
        if isinstance(spaces, dict):
            for value in spaces.values():
                desc = self.describe_cs(value, resources)
                if desc.startswith(("Separation", "DeviceN")):
                    self.use_cs(desc, "resources")


def walk_pages(pdf):
    pages = []

    def visit(node, inherited, depth):
        node = pdf.resolve(node)
        if not isinstance(node, dict) or depth > 64:
            return
        attrs = dict(inherited)
        for key in ("Resources", "MediaBox", "CropBox", "Rotate"):
            if key in node:
                attrs[key] = node[key]
        kind = node.get("Type")
        kids = pdf.get(node, "Kids")
        if kind == "Pages" or (kind is None and isinstance(kids, list)):
            for kid in kids or []:
                visit(kid, attrs, depth + 1)
        else:
            merged = dict(node)
            for key, value in attrs.items():
                merged.setdefault(key, value)
            pages.append(merged)

    visit(pdf.root.get("Pages"), {}, 0)
    return pages


def analyze(data, intent="print", min_bleed_pt=parse_length("3mm"), min_ppi=300, allow_rgb=False,
            require_pdfx=False):
    pdf = Pdf(data)
    an = Analyzer(pdf)
    report = {"tool": f"preflight_pdf {VERSION}", "intent": intent, "pdf_version": pdf.header_version,
              "thresholds": {"min_bleed_mm": round(mm(min_bleed_pt), 2), "min_ppi": min_ppi}}
    catalog_version = pdf.get(pdf.root, "Version")
    if catalog_version:
        report["pdf_version"] = str(catalog_version)
    pages = walk_pages(pdf)
    report["page_count"] = len(pages)
    page_reports = []
    for index, page in enumerate(pages, start=1):
        media = rect(pdf, page.get("MediaBox")) or [0, 0, 612, 792]
        crop = rect(pdf, page.get("CropBox"))
        bleed = rect(pdf, page.get("BleedBox"))
        trim = rect(pdf, page.get("TrimBox"))
        art = rect(pdf, page.get("ArtBox"))
        effective_bleed = bleed or crop or media
        effective_trim = trim or art or crop or media
        sides = [effective_trim[0] - effective_bleed[0], effective_trim[1] - effective_bleed[1],
                 effective_bleed[2] - effective_trim[2], effective_bleed[3] - effective_trim[3]]
        unit = pdf.resolve(page.get("UserUnit")) or 1
        entry = {
            "page": index,
            "media_box": media, "crop_box": crop, "bleed_box": bleed, "trim_box": trim, "art_box": art,
            "trim_size_mm": [round(mm(effective_trim[2] - effective_trim[0]) * unit, 2),
                             round(mm(effective_trim[3] - effective_trim[1]) * unit, 2)],
            "bleed_mm": {"left": round(mm(sides[0]) * unit, 2), "bottom": round(mm(sides[1]) * unit, 2),
                         "right": round(mm(sides[2]) * unit, 2), "top": round(mm(sides[3]) * unit, 2)},
            "min_bleed_mm": round(mm(min(sides)) * unit, 2),
        }
        page_reports.append(entry)
        resources = pdf.resolve(page.get("Resources")) or {}
        an.collect_resource_fonts(resources, index)
        contents = pdf.resolve(page.get("Contents"))
        streams = contents if isinstance(contents, list) else ([contents] if contents is not None else [])
        chunks = []
        for item in streams:
            item = pdf.resolve(item)
            if isinstance(item, Stream):
                decoded = decode_stream(item, pdf)
                if decoded is None:
                    an.unknown_content.append(f"page {index}: content stream uses an unsupported filter")
                else:
                    chunks.append(decoded)
        base = [float(unit), 0, 0, float(unit), 0, 0]
        an.run_content(b"\n".join(chunks), resources, base, index)
    report["pages"] = page_reports

    # output intents and standards
    intents = []
    for oi in pdf.get(pdf.root, "OutputIntents", []) or []:
        oi = pdf.resolve(oi)
        if not isinstance(oi, dict):
            continue
        profile = pdf.get(oi, "DestOutputProfile")
        intents.append({"subtype": str(pdf.get(oi, "S", "")),
                        "condition": text(pdf.get(oi, "OutputConditionIdentifier", "")),
                        "info": text(pdf.get(oi, "Info", "")),
                        "profile_components": pdf.get(profile, "N") if profile is not None else None})
    report["output_intents"] = intents
    info = pdf.resolve(pdf.trailer.get("Info")) or {}
    markers = {}
    if isinstance(info, dict):
        for key in ("GTS_PDFXVersion", "GTS_PDFXConformance", "Trapped", "Producer", "Creator", "Title"):
            if key in info:
                markers[f"info.{key}"] = text(pdf.resolve(info[key]))
    metadata = pdf.get(pdf.root, "Metadata")
    if isinstance(metadata, Stream):
        xmp = decode_stream(metadata, pdf) or b""
        xmp_text = xmp.decode("utf-8", "replace")
        for label, pattern in (("xmp.pdfx", r"GTS_PDFXVersion(?:>|=\")\s*([^<\"]+)"),
                               ("xmp.pdfa_part", r"pdfaid:part(?:>|=\")\s*([^<\"]+)"),
                               ("xmp.pdfa_conformance", r"pdfaid:conformance(?:>|=\")\s*([^<\"]+)"),
                               ("xmp.pdfua_part", r"pdfuaid:part(?:>|=\")\s*([^<\"]+)")):
            found = re.search(pattern, xmp_text)
            if found:
                markers[label] = found.group(1).strip()
    report["markers"] = markers
    pdfx = markers.get("xmp.pdfx") or markers.get("info.GTS_PDFXVersion")
    report["pdfx_claimed"] = pdfx
    mark_info = pdf.get(pdf.root, "MarkInfo") or {}
    report["tagged"] = bool(pdf.get(mark_info, "Marked", False)) and pdf.root.get("StructTreeRoot") is not None
    outlines = pdf.get(pdf.root, "Outlines")
    report["outline_entries"] = pdf.get(outlines, "Count", 0) if isinstance(outlines, dict) else 0

    report["fonts"] = sorted(an.fonts.values(), key=lambda f: f["name"])
    report["images"] = list(an.images.values())
    report["color_spaces"] = {k: sorted(v) for k, v in sorted(an.color_spaces.items())}
    report["unparsed"] = an.unknown_content

    findings, notes = [], []
    printing = intent == "print"
    for p in page_reports:
        if printing and p["trim_box"] is None:
            findings.append({"check": "trim", "page": p["page"],
                             "message": "no TrimBox: the printer cannot locate the trim (export with bleed and trim boxes)"})
        if printing and p["min_bleed_mm"] + 0.01 < mm(min_bleed_pt):
            findings.append({"check": "bleed", "page": p["page"],
                             "message": f"bleed {p['min_bleed_mm']}mm on the smallest side; need {round(mm(min_bleed_pt), 2)}mm"})
    for font in report["fonts"]:
        if not font["embedded"]:
            findings.append({"check": "font-embedding", "message": f"font {font['name']} ({font['type']}) is not embedded"})
    type3 = sorted({f["name"] for f in report["fonts"] if f["type"] == "Type3"})
    if type3 and printing:
        notes.append(f"{len(type3)} Type 3 font(s) ({', '.join(type3[:4])}{', ...' if len(type3) > 4 else ''}); Chromium "
                     "writes variable fonts this way and some RIPs rasterize or reject Type 3: make the print file "
                     "with WeasyPrint or ask the printer")
    for image in report["images"]:
        for placement in image["placements"]:
            if placement["ppi"] is None:
                notes.append(f"image {image['name']} on page {placement['page']}: effective ppi unknown")
            elif placement["ppi"] + 0.05 < min_ppi and image["color_space"] != "stencil mask":
                (findings if printing else notes).append(
                    {"check": "resolution", "page": placement["page"],
                     "message": f"image {image['name']} is {placement['ppi']} ppi at placed size; need {min_ppi}"}
                    if printing else
                    f"image {image['name']} on page {placement['page']} is {placement['ppi']} ppi at placed size")
    spaces = report["color_spaces"]
    if printing and not allow_rgb:
        for desc in spaces:
            if desc == "DeviceRGB" or desc.endswith("DeviceRGB"):
                findings.append({"check": "color", "message": "DeviceRGB in a print file: convert to the printer's CMYK "
                                 "profile, or confirm the printer accepts RGB with a PDF/X-4 output intent"})
                break
        for desc in spaces:
            if desc.startswith("ICCBased RGB"):
                notes.append("ICC-tagged RGB present: acceptable in PDF/X-4 when the printer converts; not in PDF/X-1a")
                break
    for desc in spaces:
        if desc.startswith(("Separation", "DeviceN")):
            notes.append(f"spot color in use: {desc}; check the name matches the brand's spot ink and the job's ink count")
    if printing and not intents:
        findings.append({"check": "output-intent", "message": "no OutputIntent: export as PDF/X with the printer's profile"})
    if require_pdfx and not pdfx:
        findings.append({"check": "pdfx", "message": "no PDF/X marker in the Info dictionary or XMP metadata"})
    if pdfx:
        notes.append(f"claims {pdfx}; this script does not validate conformance; use the printer's preflight")
    if not printing and not report["tagged"]:
        notes.append("not tagged: screen readers get no structure; render with tagged output (Playwright tagged: true)")
    for item in an.unknown_content:
        notes.append(item)
    report["findings"] = findings
    report["notes"] = notes
    return report


def format_text(path, r):
    def box(b):
        if not b:
            return "-"
        return f"{b[2] - b[0]:.1f}x{b[3] - b[1]:.1f}pt"

    lines = [f"preflight_pdf {VERSION}: {path}",
             f"  PDF {r['pdf_version']}, {r['page_count']} page(s), intent {r['intent']} "
             f"(min bleed {r['thresholds']['min_bleed_mm']}mm, min {r['thresholds']['min_ppi']} ppi)"]
    oi = "; ".join(f"{i['subtype']} \"{i['condition']}\" profile N={i['profile_components']}" for i in r["output_intents"])
    lines.append(f"  standard: {r['pdfx_claimed'] or 'no PDF/X marker'}; output intent: {oi or 'none'}")
    other = {k: v for k, v in r["markers"].items() if k.startswith("xmp.pdfa") or k.startswith("xmp.pdfua")}
    if other:
        lines.append("  other markers: " + ", ".join(f"{k}={v}" for k, v in other.items()))
    lines.append(f"  tagged: {'yes' if r['tagged'] else 'no'}; outline entries: {r['outline_entries']}")
    for p in r["pages"]:
        b = p["bleed_mm"]
        lines.append(f"  page {p['page']}: media {box(p['media_box'])}, trim {box(p['trim_box']) if p['trim_box'] else 'none'} "
                     f"({p['trim_size_mm'][0]}x{p['trim_size_mm'][1]}mm), bleed {box(p['bleed_box']) if p['bleed_box'] else 'none'}; "
                     f"bleed L{b['left']} B{b['bottom']} R{b['right']} T{b['top']}mm")
    lines.append(f"  fonts ({len(r['fonts'])}):")
    for f in r["fonts"]:
        flags = ["embedded" if f["embedded"] else "NOT EMBEDDED"]
        if f["subset"]:
            flags.append("subset")
        lines.append(f"    {f['name']} [{f['type']}] {', '.join(flags)}; pages {','.join(map(str, f['pages']))}")
    lines.append(f"  images ({len(r['images'])}):")
    for i in r["images"]:
        places = "; ".join(
            f"p{pl['page']} {pl['size_in'][0]}x{pl['size_in'][1]}in = {pl['ppi']} ppi" if pl["ppi"] is not None
            else f"p{pl['page']} ppi unknown" for pl in i["placements"]) or "not placed"
        lines.append(f"    {i['name']}: {i['pixels'][0]}x{i['pixels'][1]}px {i['color_space']} "
                     f"{i['bits'] or '?'}bpc {'/'.join(i['filters']) or 'raw'}; {places}")
    lines.append("  color spaces: " + (", ".join(f"{k} ({'/'.join(v)})" for k, v in r["color_spaces"].items()) or "none found"))
    if r["findings"]:
        lines.append(f"FINDINGS ({len(r['findings'])})")
        for f in r["findings"]:
            where = f" page {f['page']}:" if "page" in f else ""
            lines.append(f"  - [{f['check']}]{where} {f['message']}")
    if r["notes"]:
        lines.append("NOTES")
        for n in r["notes"]:
            lines.append(f"  - {n}")
    lines.append(f"result: {len(r['findings'])} finding(s)")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Preflight report for print and screen PDFs (stdlib only).")
    parser.add_argument("pdf", nargs="+", help="PDF file(s) to check")
    parser.add_argument("--intent", choices=["print", "screen"], default="print",
                        help="print: bleed, trim, output intent, CMYK and ppi are findings; screen: only missing fonts are")
    parser.add_argument("--min-bleed", type=parse_length, default=parse_length("3mm"),
                        help="minimum bleed on every side (default 3mm; 0.125in = 3.175mm also passes)")
    parser.add_argument("--min-ppi", type=float, default=300.0, help="minimum effective image ppi (default 300)")
    parser.add_argument("--allow-rgb", action="store_true", help="do not flag DeviceRGB in print intent")
    parser.add_argument("--require-pdfx", action="store_true", help="flag files without a PDF/X marker")
    parser.add_argument("--json", action="store_true", help="print a JSON report")
    args = parser.parse_args(argv)

    results, worst = [], 0
    for path in args.pdf:
        try:
            with open(path, "rb") as handle:
                data = handle.read()
            report = analyze(data, args.intent, args.min_bleed, args.min_ppi, args.allow_rgb, args.require_pdfx)
        except (OSError, PdfError, RecursionError) as exc:
            worst = 2
            if args.json:
                results.append({"file": path, "error": str(exc)})
            else:
                print(f"preflight_pdf: {path}: error: {exc}", file=sys.stderr)
            continue
        report["file"] = path
        results.append(report)
        if report["findings"]:
            worst = max(worst, 1)
        if not args.json:
            print(format_text(path, report))
    if args.json:
        print(json.dumps(results[0] if len(results) == 1 else results, indent=2, default=list))
    return worst


if __name__ == "__main__":
    sys.exit(main())
