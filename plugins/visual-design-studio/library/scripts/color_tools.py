"""OKLCH color math, ramp generation and contrast checks (WCAG 2.x and APCA-W3).

Version-Timestamp: 2026-10-20 02:04:10 UTC

Usage:
  python3 color_tools.py convert "#0e7c86" "oklch(0.62 0.12 195)"
  python3 color_tools.py ramp --hue 195 --chroma 0.12 --name teal [--steps 50,100,...] [--format json|css|table]
  python3 color_tools.py contrast "#334155" "#ffffff"
  python3 color_tools.py apca "#000000" "#ffffff"
  python3 color_tools.py check-palette palette.json

Importable: hex_to_oklch, oklch_to_hex, gamut_map, ramp, contrast_ratio, wcag_verdicts,
apca_contrast, check_palette.

Standard library only (Python 3.9+). Every function is deterministic.

Color math sources:
- OKLab: Bjorn Ottosson, "A perceptual color space for image processing" (2020), matrices as
  published at bottosson.github.io/posts/oklab.
- WCAG 2.x relative luminance and contrast ratio: W3C WCAG 2.2, Success Criteria 1.4.3, 1.4.6, 1.4.11
  (sRGB linearization threshold 0.04045).
- APCA-W3 0.1.9 (SAPC 0.0.98G-4g constants) by Andrew Somers / Myndex, github.com/Myndex/apca-w3.
"""
import argparse
import json
import math
import re
import sys

DEFAULT_STEPS = (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)
# Lightness is linear in the step number: L = L_MAX - (step - 50) / 900 * (L_MAX - L_MIN).
# With the defaults this is L = 1.02 - 0.0009 * step, so every 100 steps is the same OKLab
# lightness difference (0.09) and 50/950 sit half a step from their neighbours.
L_MAX = 0.975
L_MIN = 0.165
CHROMA_FLOOR = 0.12
CHROMA_TAPER = 0.65

# ---------------------------------------------------------------------------
# Parsing and formatting
# ---------------------------------------------------------------------------

HEX_RE = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
OKLCH_RE = re.compile(
    r"^\s*(?:oklch\(\s*)?([0-9.]+)(%?)\s*[ ,]\s*([0-9.]+)\s*[ ,]\s*([0-9.]+)(?:deg)?"
    r"(?:\s*/\s*([0-9.]+)(%?))?\s*\)?\s*$",
    re.IGNORECASE,
)


class ColorError(ValueError):
    pass


def parse_hex(value):
    """Return (r, g, b, a) floats in 0..1 for #rgb, #rgba, #rrggbb or #rrggbbaa."""
    if not isinstance(value, str):
        raise ColorError(f"expected a hex color string, got {value!r}")
    match = HEX_RE.match(value.strip())
    if not match:
        raise ColorError(f"not a hex color: {value!r}")
    digits = match.group(1)
    if len(digits) in (3, 4):
        digits = "".join(ch * 2 for ch in digits)
    channels = [int(digits[i:i + 2], 16) / 255 for i in range(0, len(digits), 2)]
    if len(channels) == 3:
        channels.append(1.0)
    return tuple(channels)


def to_hex(r, g, b, a=1.0):
    """Format 0..1 sRGB channels as lowercase #rrggbb (or #rrggbbaa when a < 1)."""
    def byte(channel):
        return max(0, min(255, int(round(channel * 255))))
    text = "#" + "".join(f"{byte(c):02x}" for c in (r, g, b))
    if a < 1:
        text += f"{byte(a):02x}"
    return text


def normalize_hex(value):
    return to_hex(*parse_hex(value))


def parse_oklch(value):
    """Parse 'oklch(L C H)', 'oklch(62% 0.1 195deg / 0.5)' or 'L C H'. Returns (L, C, H, alpha)."""
    match = OKLCH_RE.match(value)
    if not match:
        raise ColorError(f"not an oklch color: {value!r}")
    lightness = float(match.group(1)) / (100 if match.group(2) else 1)
    chroma = float(match.group(3))
    hue = float(match.group(4)) % 360
    alpha = 1.0
    if match.group(5):
        alpha = float(match.group(5)) / (100 if match.group(6) else 1)
    if not 0 <= lightness <= 1:
        raise ColorError(f"oklch lightness out of range 0..1: {value!r}")
    return lightness, chroma, hue, alpha


def format_oklch(lightness, chroma, hue, alpha=1.0):
    if chroma < 0.0005:
        hue = 0.0
    text = f"oklch({lightness:.3f} {chroma:.3f} {hue:.1f}"
    if alpha < 1:
        text += f" / {alpha:.2f}"
    return text + ")"


# ---------------------------------------------------------------------------
# sRGB <-> OKLab <-> OKLCH
# ---------------------------------------------------------------------------

def srgb_to_linear(channel):
    if channel <= 0.04045:
        return channel / 12.92
    return ((channel + 0.055) / 1.055) ** 2.4


def linear_to_srgb(channel):
    if channel <= 0.0031308:
        return 12.92 * channel
    return 1.055 * (channel ** (1 / 2.4)) - 0.055


def _cbrt(value):
    return math.copysign(abs(value) ** (1 / 3), value)


def linear_srgb_to_oklab(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = _cbrt(l), _cbrt(m), _cbrt(s)
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_linear_srgb(lightness, a, b):
    l_ = lightness + 0.3963377774 * a + 0.2158037573 * b
    m_ = lightness - 0.1055613458 * a - 0.0638541728 * b
    s_ = lightness - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def oklab_to_oklch(lightness, a, b):
    chroma = math.hypot(a, b)
    hue = math.degrees(math.atan2(b, a)) % 360 if chroma > 1e-9 else 0.0
    return lightness, chroma, hue


def oklch_to_oklab(lightness, chroma, hue):
    radians = math.radians(hue)
    return lightness, chroma * math.cos(radians), chroma * math.sin(radians)


def hex_to_oklch(value):
    """Return (L, C, H, alpha) for a hex color."""
    r, g, b, alpha = parse_hex(value)
    lab = linear_srgb_to_oklab(srgb_to_linear(r), srgb_to_linear(g), srgb_to_linear(b))
    return oklab_to_oklch(*lab) + (alpha,)


def oklch_to_linear_srgb(lightness, chroma, hue):
    return oklab_to_linear_srgb(*oklch_to_oklab(lightness, chroma, hue))


def in_gamut(lightness, chroma, hue, epsilon=1e-7):
    return all(-epsilon <= c <= 1 + epsilon for c in oklch_to_linear_srgb(lightness, chroma, hue))


def max_chroma(lightness, hue, ceiling=0.4):
    """Largest chroma at this lightness and hue that is inside the sRGB gamut (binary search)."""
    if lightness <= 0 or lightness >= 1:
        return 0.0
    low, high = 0.0, ceiling
    if in_gamut(lightness, high, hue):
        return high
    for _ in range(40):
        mid = (low + high) / 2
        if in_gamut(lightness, mid, hue):
            low = mid
        else:
            high = mid
    return low


def gamut_map(lightness, chroma, hue):
    """Map an OKLCH color into sRGB by reducing chroma at constant lightness and hue.

    Returns (L, C, H, mapped) where mapped is True when chroma had to be reduced.
    """
    lightness = max(0.0, min(1.0, lightness))
    if in_gamut(lightness, chroma, hue):
        return lightness, chroma, hue, False
    return lightness, max_chroma(lightness, hue, ceiling=chroma), hue, True


def oklch_to_hex(lightness, chroma, hue, alpha=1.0):
    """Gamut-map (chroma reduction) and format as hex."""
    lightness, chroma, hue, _ = gamut_map(lightness, chroma, hue)
    r, g, b = (linear_to_srgb(max(0.0, min(1.0, c))) for c in oklch_to_linear_srgb(lightness, chroma, hue))
    return to_hex(r, g, b, alpha)


def convert(value):
    """Convert hex -> oklch or oklch -> hex. Returns a dict describing both forms."""
    text = value.strip()
    if HEX_RE.match(text):
        lightness, chroma, hue, alpha = hex_to_oklch(text)
        return {"input": value, "hex": normalize_hex(text) if alpha == 1 else to_hex(*parse_hex(text)),
                "oklch": format_oklch(lightness, chroma, hue, alpha), "l": round(lightness, 4),
                "c": round(chroma, 4), "h": round(hue, 2), "alpha": round(alpha, 4), "gamut_mapped": False}
    lightness, chroma, hue, alpha = parse_oklch(text)
    mapped = gamut_map(lightness, chroma, hue)
    hex_value = oklch_to_hex(lightness, chroma, hue, alpha)
    return {"input": value, "hex": hex_value, "oklch": format_oklch(lightness, chroma, hue, alpha),
            "l": round(lightness, 4), "c": round(chroma, 4), "h": round(hue, 2), "alpha": round(alpha, 4),
            "gamut_mapped": mapped[3], "mapped_chroma": round(mapped[1], 4)}


# ---------------------------------------------------------------------------
# Ramps
# ---------------------------------------------------------------------------

def step_lightness(step, l_max=L_MAX, l_min=L_MIN):
    return l_max - (step - 50) / 900 * (l_max - l_min)


def chroma_taper(step, floor=CHROMA_FLOOR, exponent=CHROMA_TAPER):
    """1.0 at the middle of the ramp (step 500) falling to `floor` at steps 50 and 950."""
    t = min(1.0, max(0.0, (step - 50) / 900))
    return floor + (1 - floor) * (math.sin(math.pi * t) ** exponent)


def ramp(hue, chroma, steps=DEFAULT_STEPS, name=None, l_max=L_MAX, l_min=L_MIN, floor=CHROMA_FLOOR,
         exponent=CHROMA_TAPER, hue_shift=0.0):
    """Generate a lightness ramp.

    Lightness is linear in the step number (perceptually even OKLab steps). Chroma follows a sine
    taper peaking at step 500 so the lightest and darkest steps are calmer. `hue_shift` rotates the
    hue linearly across the ramp (half the shift is subtracted at step 50 and added at step 950),
    which keeps yellows from turning olive when they darken. Colors outside sRGB are mapped by
    chroma reduction at constant L and H.
    """
    if chroma < 0:
        raise ColorError("chroma must be >= 0")
    result = []
    for step in steps:
        lightness = step_lightness(step, l_max, l_min)
        t = (step - 50) / 900
        step_hue = (hue + hue_shift * (t - 0.5)) % 360
        target = chroma * chroma_taper(step, floor, exponent)
        mapped_l, mapped_c, mapped_h, mapped = gamut_map(lightness, target, step_hue)
        result.append({
            "step": step,
            "hex": oklch_to_hex(mapped_l, mapped_c, mapped_h),
            "oklch": format_oklch(mapped_l, mapped_c, mapped_h),
            "l": round(mapped_l, 4),
            "c": round(mapped_c, 4),
            "h": round(mapped_h, 2),
            "requested_c": round(target, 4),
            "gamut_mapped": mapped,
        })
    if name:
        for item in result:
            item["name"] = f"{name}-{item['step']}"
    return result


def ramp_params(hue, chroma, steps=DEFAULT_STEPS, l_max=L_MAX, l_min=L_MIN, floor=CHROMA_FLOOR,
                exponent=CHROMA_TAPER, hue_shift=0.0):
    return {"hue": hue, "chroma": chroma, "steps": list(steps), "l_max": l_max, "l_min": l_min,
            "floor": floor, "taper": exponent, "hue_shift": hue_shift}


# ---------------------------------------------------------------------------
# WCAG 2.x
# ---------------------------------------------------------------------------

def relative_luminance(value):
    r, g, b, alpha = parse_hex(value)
    if alpha < 1:
        raise ColorError(f"contrast needs an opaque color, got {value!r}; composite it first")
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)


def contrast_ratio(fg, bg):
    """WCAG 2.x contrast ratio (1..21). Order does not matter."""
    lighter, darker = sorted((relative_luminance(fg), relative_luminance(bg)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def composite(fg, bg):
    """Alpha-composite a translucent hex color over an opaque background."""
    r, g, b, a = parse_hex(fg)
    br, bgc, bb, _ = parse_hex(bg)
    return to_hex(r * a + br * (1 - a), g * a + bgc * (1 - a), b * a + bb * (1 - a))


WCAG_LEVELS = (
    ("AA normal text", 4.5, "1.4.3"),
    ("AA large text", 3.0, "1.4.3"),
    ("AAA normal text", 7.0, "1.4.6"),
    ("AAA large text", 4.5, "1.4.6"),
    ("AA non-text UI", 3.0, "1.4.11"),
)


def wcag_verdicts(ratio):
    return [{"level": label, "minimum": minimum, "criterion": criterion, "pass": ratio >= minimum}
            for label, minimum, criterion in WCAG_LEVELS]


# ---------------------------------------------------------------------------
# APCA-W3 0.1.9 (SAPC 0.0.98G-4g)
# ---------------------------------------------------------------------------

APCA = {
    "mainTRC": 2.4,
    "sRco": 0.2126729, "sGco": 0.7151522, "sBco": 0.0721750,
    "normBG": 0.56, "normTXT": 0.57, "revTXT": 0.62, "revBG": 0.65,
    "blkThrs": 0.022, "blkClmp": 1.414,
    "scaleBoW": 1.14, "scaleWoB": 1.14,
    "loBoWoffset": 0.027, "loWoBoffset": 0.027,
    "deltaYmin": 0.0005, "loClip": 0.1,
}


def apca_luminance(value):
    """APCA screen luminance Y: simple 2.4 exponent per channel, not the piecewise sRGB curve."""
    r, g, b, alpha = parse_hex(value)
    if alpha < 1:
        raise ColorError(f"APCA needs an opaque color, got {value!r}; composite it first")
    trc = APCA["mainTRC"]
    return APCA["sRco"] * r ** trc + APCA["sGco"] * g ** trc + APCA["sBco"] * b ** trc


def apca_contrast(text, background):
    """APCA lightness contrast Lc. Positive: dark text on light; negative: light text on dark."""
    text_y = apca_luminance(text)
    bg_y = apca_luminance(background)
    k = APCA
    if min(text_y, bg_y) < 0 or max(text_y, bg_y) > 1.1:
        return 0.0
    if text_y <= k["blkThrs"]:
        text_y += (k["blkThrs"] - text_y) ** k["blkClmp"]
    if bg_y <= k["blkThrs"]:
        bg_y += (k["blkThrs"] - bg_y) ** k["blkClmp"]
    if abs(bg_y - text_y) < k["deltaYmin"]:
        return 0.0
    if bg_y > text_y:
        sapc = (bg_y ** k["normBG"] - text_y ** k["normTXT"]) * k["scaleBoW"]
        output = 0.0 if sapc < k["loClip"] else sapc - k["loBoWoffset"]
    else:
        sapc = (bg_y ** k["revBG"] - text_y ** k["revTXT"]) * k["scaleWoB"]
        output = 0.0 if sapc > -k["loClip"] else sapc + k["loWoBoffset"]
    return output * 100


# APCA "Bronze" readability levels (absolute Lc), as published with APCA-W3. Verify against
# git.apcacontrast.com/documentation before quoting them as a compliance requirement.
APCA_LEVELS = (
    (90, "preferred for body text (14-16px regular and up)"),
    (75, "minimum for body text columns"),
    (60, "content text that is not body copy"),
    (45, "headlines and large text (about 36px regular / 24px bold)"),
    (30, "spot text, placeholders, disabled states, non-text UI"),
    (15, "minimum for non-semantic dividers and outlines"),
)


def apca_guidance(lc):
    magnitude = abs(lc)
    for minimum, label in APCA_LEVELS:
        if magnitude >= minimum:
            return f"|Lc| >= {minimum}: {label}"
    return "|Lc| < 15: invisible to many readers; do not use for anything meaningful"


# ---------------------------------------------------------------------------
# Palette checks
# ---------------------------------------------------------------------------

def _flatten_palette(data, prefix=""):
    """Collect name -> hex from flat maps, {'colors': {...}}, DTCG trees or ramp JSON."""
    colors = {}
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "hex" in item:
                key = item.get("name") or f"{prefix}{item.get('step')}"
                colors[key] = item["hex"]
        return colors
    if not isinstance(data, dict):
        return colors
    if "$value" in data:
        if isinstance(data["$value"], str) and HEX_RE.match(data["$value"]):
            colors[prefix.rstrip("-.")] = data["$value"]
        return colors
    if "steps" in data and isinstance(data["steps"], list):
        name = data.get("name") or prefix.rstrip("-.") or "ramp"
        for item in data["steps"]:
            colors[f"{name}-{item['step']}"] = item["hex"]
        return colors
    for key, value in data.items():
        if key.startswith("$") or key == "pairs":
            continue
        if isinstance(value, str) and HEX_RE.match(value):
            colors[f"{prefix}{key}"] = value
        elif isinstance(value, (dict, list)):
            colors.update(_flatten_palette(value, f"{prefix}{key}-" if key != "colors" else prefix))
    return colors


def check_palette(data):
    """Audit a palette: per-color OKLCH and contrast on white/black, ramp monotonicity, pairs.

    Accepted input: {"colors": {name: hex}, "pairs": [{"fg": name|hex, "bg": name|hex, "min": 4.5}]},
    a flat {name: hex} map, a DTCG token tree, or the JSON written by `ramp --format json`.
    Returns {"colors": [...], "ramps": [...], "pairs": [...], "errors": [...], "ok": bool}.
    """
    errors = []
    colors = _flatten_palette(data)
    rows = []
    for name, value in colors.items():
        try:
            lightness, chroma, hue, alpha = hex_to_oklch(value)
        except ColorError as exc:
            errors.append(f"{name}: {exc}")
            continue
        row = {"name": name, "hex": value.lower(), "oklch": format_oklch(lightness, chroma, hue, alpha), "l": lightness}
        if alpha == 1:
            row["on_white"] = round(contrast_ratio(value, "#ffffff"), 2)
            row["on_black"] = round(contrast_ratio(value, "#000000"), 2)
            row["apca_on_white"] = round(apca_contrast(value, "#ffffff"), 1)
            row["apca_on_black"] = round(apca_contrast(value, "#000000"), 1)
        rows.append(row)

    ramps = {}
    for row in rows:
        match = re.match(r"^(.*?)[-.](\d+)$", row["name"])
        if match:
            ramps.setdefault(match.group(1), []).append((int(match.group(2)), row))
    ramp_reports = []
    for name, items in ramps.items():
        if len(items) < 3:
            continue
        items.sort(key=lambda item: item[0])
        problems = []
        for (step_a, a), (step_b, b) in zip(items, items[1:]):
            if b["l"] >= a["l"]:
                problems.append(f"{name}-{step_b} (L {b['l']:.3f}) is not darker than {name}-{step_a} (L {a['l']:.3f})")
            elif a["l"] - b["l"] < 0.015:
                problems.append(f"{name}-{step_a} and {name}-{step_b} differ by only {a['l'] - b['l']:.3f} L")
        errors.extend(problems)
        ramp_reports.append({"name": name, "steps": [step for step, _ in items], "monotonic": not problems,
                             "problems": problems})

    pair_reports = []
    for pair in data.get("pairs", []) if isinstance(data, dict) else []:
        fg_name, bg_name = pair.get("fg"), pair.get("bg")
        fg = colors.get(fg_name, fg_name)
        bg = colors.get(bg_name, bg_name)
        minimum = float(pair.get("min", 4.5))
        try:
            ratio = contrast_ratio(fg, bg)
            lc = apca_contrast(fg, bg)
        except ColorError as exc:
            errors.append(f"pair {fg_name} on {bg_name}: {exc}")
            continue
        passed = ratio >= minimum
        pair_reports.append({"fg": fg_name, "bg": bg_name, "ratio": round(ratio, 2), "min": minimum,
                             "apca": round(lc, 1), "pass": passed})
        if not passed:
            errors.append(f"pair {fg_name} on {bg_name}: {ratio:.2f}:1 is below {minimum}:1")
    return {"colors": rows, "ramps": ramp_reports, "pairs": pair_reports, "errors": errors, "ok": not errors}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_steps(text):
    try:
        steps = [int(part) for part in text.split(",") if part.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("steps must be comma-separated integers") from exc
    out_of_range = [step for step in steps if not 25 <= step <= 975]
    if out_of_range:
        raise argparse.ArgumentTypeError(
            f"steps use the 50-950 scale (25-975 allowed for in-between steps); got {out_of_range}")
    if not steps:
        raise argparse.ArgumentTypeError("at least one step is required")
    return steps


def _print_table(headers, rows):
    widths = [max(len(str(h)), *(len(str(r[i])) for r in rows)) for i, h in enumerate(headers)]
    print("  ".join(str(h).ljust(w) for h, w in zip(headers, widths)))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print("  ".join(str(c).ljust(w) for c, w in zip(row, widths)))


def cmd_convert(args):
    results = []
    for value in args.values:
        try:
            results.append(convert(value))
        except ColorError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    if args.json:
        print(json.dumps(results, indent=2))
        return 0
    for item in results:
        note = ""
        if item.get("gamut_mapped"):
            note = f"  (outside sRGB; chroma reduced to {item['mapped_chroma']})"
        print(f"{item['input']}  ->  {item['hex']}  {item['oklch']}{note}")
    return 0


def cmd_ramp(args):
    steps = args.steps or list(DEFAULT_STEPS)
    items = ramp(args.hue, args.chroma, steps=steps, name=args.name, l_max=args.l_max, l_min=args.l_min,
                 floor=args.floor, exponent=args.taper, hue_shift=args.hue_shift)
    name = args.name or "ramp"
    if args.format == "json":
        print(json.dumps({"name": name, "params": ramp_params(args.hue, args.chroma, steps, args.l_max, args.l_min,
                                                               args.floor, args.taper, args.hue_shift),
                          "steps": items}, indent=2))
    elif args.format == "css":
        print(":root {")
        for item in items:
            print(f"  --color-{name}-{item['step']}: {item['hex']}; /* {item['oklch']} */")
        print("}")
    else:
        rows = []
        for item in items:
            mapped = "yes" if item["gamut_mapped"] else ""
            rows.append([item["step"], item["hex"], item["oklch"], item["requested_c"], mapped,
                         f"{contrast_ratio(item['hex'], '#ffffff'):.2f}", f"{contrast_ratio(item['hex'], '#000000'):.2f}"])
        _print_table(["step", "hex", "oklch", "target C", "gamut-mapped", "vs white", "vs black"], rows)
    return 0


def cmd_contrast(args):
    try:
        ratio = contrast_ratio(args.fg, args.bg)
        lc = apca_contrast(args.fg, args.bg)
    except ColorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    verdicts = wcag_verdicts(ratio)
    if args.json:
        print(json.dumps({"fg": args.fg, "bg": args.bg, "ratio": round(ratio, 2), "verdicts": verdicts,
                          "apca": round(lc, 1)}, indent=2))
        return 0
    print(f"{args.fg} on {args.bg}: {ratio:.2f}:1  (APCA Lc {lc:.1f})")
    for verdict in verdicts:
        mark = "pass" if verdict["pass"] else "FAIL"
        print(f"  {mark:<4}  {verdict['level']:<16} >= {verdict['minimum']}:1  (WCAG 2.2 SC {verdict['criterion']})")
    return 0


def cmd_apca(args):
    try:
        lc = apca_contrast(args.text, args.bg)
    except ColorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"text": args.text, "bg": args.bg, "lc": round(lc, 1), "guidance": apca_guidance(lc)}, indent=2))
        return 0
    polarity = "dark text on light" if lc > 0 else "light text on dark" if lc < 0 else "no usable contrast"
    print(f"{args.text} on {args.bg}: Lc {lc:.1f} ({polarity})")
    print(f"  {apca_guidance(lc)}")
    print("  APCA-W3 0.1.9; WCAG 2.2 conformance still uses the 2.x ratio (run `contrast`).")
    return 0


def cmd_check_palette(args):
    try:
        with open(args.file, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2
    report = check_palette(data)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1
    rows = [[r["name"], r["hex"], r["oklch"], r.get("on_white", "-"), r.get("on_black", "-"),
             r.get("apca_on_white", "-"), r.get("apca_on_black", "-")] for r in report["colors"]]
    if rows:
        _print_table(["name", "hex", "oklch", "vs white", "vs black", "Lc on white", "Lc on black"], rows)
    for item in report["ramps"]:
        state = "monotonic" if item["monotonic"] else "PROBLEMS"
        print(f"ramp {item['name']}: {len(item['steps'])} steps, {state}")
    for pair in report["pairs"]:
        mark = "pass" if pair["pass"] else "FAIL"
        print(f"{mark}  {pair['fg']} on {pair['bg']}: {pair['ratio']}:1 (min {pair['min']}), Lc {pair['apca']}")
    for error in report["errors"]:
        print(f"error: {error}", file=sys.stderr)
    print("OK" if report["ok"] else f"{len(report['errors'])} problem(s)")
    return 0 if report["ok"] else 1


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("convert", help="hex <-> oklch")
    p.add_argument("values", nargs="+", help='hex like "#0e7c86" or oklch like "oklch(0.62 0.12 195)"')
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("ramp", help="generate a perceptually even OKLCH ramp")
    p.add_argument("--hue", type=float, required=True, help="OKLCH hue in degrees at step 500")
    p.add_argument("--chroma", type=float, required=True, help="peak chroma (0.0-0.37); tapers toward 50 and 950")
    p.add_argument("--name", default=None)
    p.add_argument("--steps", type=_parse_steps, default=None, help="comma-separated, default 50,100,...,900,950")
    p.add_argument("--l-max", type=float, default=L_MAX, help=f"lightness at step 50 (default {L_MAX})")
    p.add_argument("--l-min", type=float, default=L_MIN, help=f"lightness at step 950 (default {L_MIN})")
    p.add_argument("--floor", type=float, default=CHROMA_FLOOR, help="share of peak chroma kept at the extremes")
    p.add_argument("--taper", type=float, default=CHROMA_TAPER, help="taper exponent; 0 keeps chroma constant")
    p.add_argument("--hue-shift", type=float, default=0.0, help="degrees of hue rotation from step 50 to 950")
    p.add_argument("--format", choices=["json", "css", "table"], default="table")
    p.set_defaults(func=cmd_ramp)

    p = sub.add_parser("contrast", help="WCAG 2.x contrast ratio with AA/AAA verdicts")
    p.add_argument("fg")
    p.add_argument("bg")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_contrast)

    p = sub.add_parser("apca", help="APCA-W3 0.1.9 lightness contrast (Lc)")
    p.add_argument("text")
    p.add_argument("bg")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_apca)

    p = sub.add_parser("check-palette", help="audit a palette JSON file")
    p.add_argument("file")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_check_palette)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
