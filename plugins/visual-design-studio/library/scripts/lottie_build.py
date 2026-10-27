"""Build and validate "portable Lottie" JSON from a small spec, using the kit's tokens.

Version-Timestamp: 2026-10-23 20:12:12 UTC

Usage:
  python3 lottie_build.py presets
  python3 lottie_build.py build lottie_specs/logo-reveal.json -o logo-reveal.json [--brand ember --mode dark]
  python3 lottie_build.py validate logo-reveal.json [more.json ...] [--json] [--max-kb 100]
  python3 lottie_build.py examples [--out DIR] [--check]

Importable: hex_to_lottie, bezier_tangents, ms_to_frames, parse_duration_ms, load_tokens, build,
validate, PRESETS.

Portable Lottie is the subset of the Lottie Animation Format v1.0 (lottie.github.io/lottie-spec,
published 2024-09-17 by the Lottie Animation Community) that plays the same in lottie-web,
dotlottie-web, lottie-ios, lottie-android and @remotion/lottie:
  - layer types: precomposition (0), solid (1), null (3), shape (4)
  - shape items: group, rectangle, ellipse, polystar, path, fill, stroke, gradient fill and stroke,
    transform, trim path, rounded corners
  - masks in add, subtract or none mode; alpha mattes only
  - no expressions, no text layers, no image, audio or camera layers, no layer effects, no 3D,
    no merge paths or repeaters, no embedded rasters
Easing: a CSS cubic-bezier(x1, y1, x2, y2) becomes the keyframe out tangent o = {x: x1, y: y1} and
the in tangent of the next keyframe i = {x: x2, y: y2}, stored on the starting keyframe.

Standard library only (Python 3.9+). Output is deterministic for a given spec and token file.
python-lottie is AGPL; this script does not use it.
"""
import argparse
import json
import math
import sys
from pathlib import Path

GENERATOR = "visual-design-kit lottie_build.py 1.0"
LOTTIE_VERSION = "5.7.0"
LIBRARY = Path(__file__).resolve().parent.parent
DEFAULT_TOKENS = LIBRARY / "tokens" / "dist" / "tokens.resolved.json"
SPEC_DIR = Path(__file__).resolve().parent / "lottie_specs"
DEFAULT_EXAMPLE_OUT = LIBRARY / "examples" / "motion-remotion" / "public" / "lottie"

ALLOWED_LAYER_TYPES = {0: "precomposition", 1: "solid", 3: "null", 4: "shape"}
FORBIDDEN_LAYER_TYPES = {
    2: "image layer (embedded or linked raster)",
    5: "text layer (convert text to shapes)",
    6: "audio layer",
    13: "camera layer",
}
ALLOWED_SHAPES = {"gr", "rc", "el", "sr", "sh", "fl", "st", "gf", "gs", "tr", "tm", "rd"}
FORBIDDEN_SHAPES = {
    "mm": "merge paths (not supported on iOS or lottie-web)",
    "rp": "repeater (iOS supports it only in the Core Animation renderer)",
    "op": "offset path",
    "pb": "pucker and bloat",
    "tw": "twist",
    "zz": "zig zag",
}
ALLOWED_MASK_MODES = {"a", "s", "n"}
ALLOWED_MATTES = {1, 2}
COMMON_FPS = {24, 25, 30, 50, 60}
MAX_FPS = 120
CIRCLE_KAPPA = 0.5522847498


# ---------------------------------------------------------------------------
# Conversions


def hex_to_lottie(value):
    """'#rgb', '#rrggbb' or '#rrggbbaa' -> [r, g, b, a] in 0-1, rounded to 4 places."""
    if not isinstance(value, str) or not value.startswith("#"):
        raise ValueError("expected a hex color, got %r" % (value,))
    digits = value[1:]
    if len(digits) in (3, 4):
        digits = "".join(ch * 2 for ch in digits)
    if len(digits) == 6:
        digits += "ff"
    if len(digits) != 8:
        raise ValueError("expected #rgb, #rrggbb or #rrggbbaa, got %r" % (value,))
    try:
        channels = [int(digits[i:i + 2], 16) for i in range(0, 8, 2)]
    except ValueError:
        raise ValueError("invalid hex digits in %r" % (value,))
    return [round(c / 255.0, 4) for c in channels]


def bezier_tangents(curve, dims=1):
    """CSS cubic-bezier [x1, y1, x2, y2] -> (out_tangent, in_tangent) for a Lottie keyframe."""
    if not isinstance(curve, (list, tuple)) or len(curve) != 4:
        raise ValueError("easing must be four numbers [x1, y1, x2, y2], got %r" % (curve,))
    x1, y1, x2, y2 = [float(n) for n in curve]
    if not (0.0 <= x1 <= 1.0 and 0.0 <= x2 <= 1.0):
        raise ValueError("bezier x values must be within 0-1, got %r" % (curve,))
    out_tangent = {"x": [round(x1, 4)] * dims, "y": [round(y1, 4)] * dims}
    in_tangent = {"x": [round(x2, 4)] * dims, "y": [round(y2, 4)] * dims}
    return out_tangent, in_tangent


def ms_to_frames(ms, fps):
    """Milliseconds -> whole frames, rounding half up (320ms at 30fps = 10 frames)."""
    if fps <= 0:
        raise ValueError("fps must be positive")
    return int(math.floor(float(ms) * fps / 1000.0 + 0.5))


def parse_duration_ms(value):
    """'320ms', '1.2s', 320 or 320.0 -> milliseconds as float."""
    if isinstance(value, bool):
        raise ValueError("invalid duration %r" % (value,))
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if text.endswith("ms"):
            return float(text[:-2])
        if text.endswith("s"):
            return float(text[:-1]) * 1000.0
    raise ValueError("invalid duration %r (use '320ms', '1.2s' or a number of ms)" % (value,))


# ---------------------------------------------------------------------------
# Tokens


class Tokens:
    """Resolved token values for one brand and mode."""

    def __init__(self, data, brand=None, mode=None):
        self.brand = brand or data.get("defaultBrand")
        self.mode = mode or data.get("defaultMode")
        values = data.get("values", {})
        if self.brand not in values:
            raise ValueError("unknown brand %r (have: %s)" % (self.brand, ", ".join(sorted(values))))
        if self.mode not in values[self.brand]:
            raise ValueError("unknown mode %r (have: %s)" % (self.mode, ", ".join(sorted(values[self.brand]))))
        self.values = values[self.brand][self.mode]

    def get(self, name):
        if name not in self.values:
            raise ValueError("unknown token %r" % (name,))
        return self.values[name]

    def color(self, ref):
        """A token name ('color.accent.default') or a hex string -> (lottie rgba, source label)."""
        if isinstance(ref, str) and ref.startswith("#"):
            return hex_to_lottie(ref), ref
        return hex_to_lottie(self.get(ref)), ref

    def easing(self, ref):
        if isinstance(ref, (list, tuple)):
            return [float(n) for n in ref], "cubic-bezier(%s)" % ", ".join(str(n) for n in ref)
        value = self.get(ref)
        return [float(n) for n in value], ref

    def duration_ms(self, ref):
        if isinstance(ref, str) and ref.startswith("duration."):
            return parse_duration_ms(self.get(ref))
        return parse_duration_ms(ref)


def load_tokens(path=None, brand=None, mode=None):
    with open(path or DEFAULT_TOKENS, encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("format") != "visual-design-kit/tokens-resolved":
        raise ValueError("not a visual-design-kit tokens.resolved.json file")
    return Tokens(data, brand, mode)


# ---------------------------------------------------------------------------
# Lottie building blocks


def _num(value):
    if isinstance(value, float):
        value = round(value, 4)
        if value == int(value):
            return int(value)
    return value


def _clean(value):
    if isinstance(value, list):
        return [_clean(v) for v in value]
    if isinstance(value, dict):
        return {k: _clean(v) for k, v in value.items()}
    return _num(value)


def static(value):
    return {"a": 0, "k": value}


def animated(keys, shape=False):
    """keys: list of (frame, value, easing-or-None). The easing on a key shapes the segment it starts."""
    keys = sorted(keys, key=lambda item: item[0])
    frames = []
    for index, (frame, value, curve) in enumerate(keys):
        if shape:
            start = [value]
            dims = 1
        else:
            start = value if isinstance(value, list) else [value]
            dims = len(start)
        entry = {"t": frame, "s": start}
        if index < len(keys) - 1:
            if keys[index + 1][1] == value:
                entry["h"] = 1
            else:
                out_tangent, in_tangent = bezier_tangents(curve or [0, 0, 1, 1], dims)
                entry["o"] = out_tangent
                entry["i"] = in_tangent
        frames.append(entry)
    return {"a": 1, "k": frames}


def layer_transform(position, anchor=(0, 0), scale=None, rotation=None, opacity=None):
    return {
        "a": static([anchor[0], anchor[1], 0]),
        "p": position if isinstance(position, dict) else static([position[0], position[1], 0]),
        "s": scale or static([100, 100, 100]),
        "r": rotation or static(0),
        "o": opacity or static(100),
    }


def group_transform(position=(0, 0), anchor=(0, 0), scale=None, rotation=None, opacity=None):
    return {
        "ty": "tr",
        "a": static(list(anchor)),
        "p": position if isinstance(position, dict) else static(list(position)),
        "s": scale or static([100, 100]),
        "r": rotation or static(0),
        "o": opacity or static(100),
        "sk": static(0),
        "sa": static(0),
        "nm": "Transform",
    }


def group(name, items, transform=None):
    items = list(items) + [transform or group_transform()]
    return {"ty": "gr", "nm": name, "np": len(items) - 1, "it": items}


def fill(color, label):
    return {"ty": "fl", "nm": "Fill (%s)" % label, "c": static(color), "o": static(100), "r": 1}


def stroke(color, label, width, cap=2):
    return {
        "ty": "st", "nm": "Stroke (%s)" % label, "c": static(color), "o": static(100),
        "w": static(width), "lc": cap, "lj": 2, "ml": 4,
    }


def ellipse(size, position=(0, 0)):
    return {"ty": "el", "nm": "Ellipse", "p": static(list(position)), "s": static(list(size)), "d": 1}


def rect(size, position=(0, 0), radius=0):
    return {"ty": "rc", "nm": "Rectangle", "p": static(list(position)), "s": static(list(size)),
            "r": static(radius), "d": 1}


def path_data(points, closed=False):
    return {"c": closed, "v": [list(p) for p in points], "i": [[0, 0] for _ in points],
            "o": [[0, 0] for _ in points]}


def path_shape(prop):
    return {"ty": "sh", "nm": "Path", "ks": prop, "d": 1}


def trim(start, end, offset=None):
    return {"ty": "tm", "nm": "Trim Paths", "s": start, "e": end, "o": offset or static(0), "m": 1}


def ellipse_path(cx, cy, rx, ry):
    """A closed four-point bezier ellipse (usable as a mask or morph target)."""
    kx, ky = rx * CIRCLE_KAPPA, ry * CIRCLE_KAPPA
    return {
        "c": True,
        "v": [[cx, cy - ry], [cx + rx, cy], [cx, cy + ry], [cx - rx, cy]],
        "i": [[-kx, 0], [0, -ky], [kx, 0], [0, ky]],
        "o": [[kx, 0], [0, ky], [-kx, 0], [0, -ky]],
    }


def rect_path(x, y, w, h):
    return path_data([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], closed=True)


def shape_layer(ind, name, shapes, ip, op, transform, parent=None, extra=None):
    layer = {
        "ddd": 0, "ind": ind, "ty": 4, "nm": name, "sr": 1, "ks": transform, "ao": 0,
        "shapes": shapes, "ip": ip, "op": op, "st": 0, "bm": 0,
    }
    if parent is not None:
        layer["parent"] = parent
    if extra:
        layer.update(extra)
    return layer


def document(name, width, height, fps, frames, layers, assets=None, markers=None, provenance=None):
    meta = {"g": GENERATOR}
    if provenance:
        meta.update(provenance)
    return _clean({
        "v": LOTTIE_VERSION, "fr": fps, "ip": 0, "op": frames, "w": width, "h": height, "nm": name,
        "ddd": 0, "assets": assets or [], "layers": layers, "markers": markers or [], "meta": meta,
    })


def background_layer(ind, tokens, spec, width, height, frames):
    ref = spec.get("colors", {}).get("background")
    if not ref:
        return None
    color, label = tokens.color(ref)
    shapes = [group("Background", [rect([width, height]), fill(color, label)])]
    return shape_layer(ind, "Background (%s)" % label, shapes, 0, frames,
                       layer_transform((width / 2.0, height / 2.0)))


# ---------------------------------------------------------------------------
# Presets


def _timing(spec, tokens, key, default):
    return tokens.duration_ms(spec.get("timing", {}).get(key, default))


def preset_logo_reveal(spec, tokens):
    """Original geometric placeholder mark: a ring drawn on, a masked diamond and a centre dot."""
    width, height, fps = spec.get("width", 512), spec.get("height", 512), spec.get("fps", 30)
    frames = ms_to_frames(tokens.duration_ms(spec.get("duration", "1600ms")), fps)
    colors = spec.get("colors", {})
    primary, primary_label = tokens.color(colors.get("primary", "color.accent.default"))
    secondary, secondary_label = tokens.color(colors.get("secondary", "color.fg.default"))
    enter, enter_label = tokens.easing(spec.get("easing", "ease.emphasized-decelerate"))
    ring_ms = _timing(spec, tokens, "ring", "duration.slower")
    diamond_ms = _timing(spec, tokens, "diamond", "duration.slow")
    dot_ms = _timing(spec, tokens, "dot", "duration.moderate")
    stagger_ms = _timing(spec, tokens, "stagger", "160ms")

    size = min(width, height)
    ring_d, ring_w = size * 0.62, size * 0.045
    diamond = size * 0.30
    dot = size * 0.08
    cx, cy = width / 2.0, height / 2.0

    ring_end = ms_to_frames(ring_ms, fps)
    diamond_start = ms_to_frames(stagger_ms, fps)
    diamond_end = diamond_start + ms_to_frames(diamond_ms, fps)
    dot_start = diamond_start + ms_to_frames(stagger_ms, fps)
    dot_end = dot_start + ms_to_frames(dot_ms, fps)
    if dot_end >= frames:
        raise ValueError("duration too short for the reveal (needs more than %d frames)" % dot_end)

    ring = shape_layer(1, "Ring (%s)" % primary_label, [group("Ring", [
        ellipse([ring_d, ring_d]),
        trim(static(0), animated([(0, 0, enter), (ring_end, 100, None)])),
        stroke(primary, primary_label, ring_w),
    ])], 0, frames, layer_transform((cx, cy)))

    half = diamond / 2.0
    diamond_layer = shape_layer(2, "Diamond (%s)" % secondary_label, [group("Diamond", [
        path_shape(static(path_data([(0, -half), (half, 0), (0, half), (-half, 0)], closed=True))),
        fill(secondary, secondary_label),
    ])], 0, frames, layer_transform(
        (cx, cy),
        scale=animated([(diamond_start, [60, 60, 100], enter), (diamond_end, [100, 100, 100], None)]),
        rotation=animated([(diamond_start, -45, enter), (diamond_end, 0, None)]),
    ), extra={
        "hasMask": True,
        "masksProperties": [{
            "inv": False, "mode": "a", "nm": "Wipe (add)", "o": static(100), "x": static(0),
            "pt": animated([
                (diamond_start, rect_path(-half, half, diamond, 0), enter),
                (diamond_end, rect_path(-half, -half, diamond, diamond), None),
            ], shape=True),
        }],
    })

    dot_layer = shape_layer(3, "Dot (%s)" % primary_label, [group("Dot", [
        ellipse([dot, dot]), fill(primary, primary_label),
    ])], 0, frames, layer_transform(
        (cx, cy),
        scale=animated([(dot_start, [0, 0, 100], enter), (dot_end, [100, 100, 100], None)]),
    ))

    mark_layers = [dot_layer, diamond_layer, ring]
    layers = [{
        "ddd": 0, "ind": 1, "ty": 0, "nm": "Mark (precomp)", "refId": "mark", "sr": 1,
        "ks": layer_transform((cx, cy), anchor=(cx, cy)), "ao": 0, "w": width, "h": height,
        "ip": 0, "op": frames, "st": 0, "bm": 0,
    }]
    bg = background_layer(2, tokens, spec, width, height, frames)
    if bg:
        layers.append(bg)
    markers = [{"tm": 0, "cm": "reveal", "dr": dot_end}, {"tm": dot_end, "cm": "hold", "dr": frames - dot_end}]
    return document(spec.get("name", "logo-reveal"), width, height, fps, frames, layers,
                    assets=[{"id": "mark", "nm": "Mark", "layers": mark_layers}], markers=markers,
                    provenance=_provenance(tokens, [primary_label, secondary_label, enter_label]))


def preset_loader(spec, tokens):
    """Seamless arc spinner: trim start and end chase each other while the arc turns once."""
    width, height, fps = spec.get("width", 96), spec.get("height", 96), spec.get("fps", 60)
    frames = ms_to_frames(tokens.duration_ms(spec.get("duration", "1200ms")), fps)
    colors = spec.get("colors", {})
    primary, primary_label = tokens.color(colors.get("primary", "color.accent.default"))
    track, track_label = tokens.color(colors.get("track", "color.border.subtle"))
    curve, curve_label = tokens.easing(spec.get("easing", "ease.standard"))
    linear, _ = tokens.easing("ease.linear")
    size = min(width, height)
    diameter, line = size * 0.72, max(2.0, size * 0.09)
    half = frames // 2
    quarter = frames // 4
    arc = group("Arc", [
        ellipse([diameter, diameter]),
        trim(animated([(quarter, 0, curve), (frames - 1, 100, None)]),
             animated([(0, 0, curve), (half + quarter, 100, None)])),
        stroke(primary, primary_label, line),
    ], group_transform(rotation=animated([(0, 0, linear), (frames, 360, None)])))
    track_group = group("Track", [ellipse([diameter, diameter]), stroke(track, track_label, line)])
    layers = [
        shape_layer(1, "Arc (%s)" % primary_label, [arc], 0, frames, layer_transform((width / 2.0, height / 2.0))),
        shape_layer(2, "Track (%s)" % track_label, [track_group], 0, frames,
                    layer_transform((width / 2.0, height / 2.0))),
    ]
    bg = background_layer(3, tokens, spec, width, height, frames)
    if bg:
        layers.append(bg)
    return document(spec.get("name", "loader"), width, height, fps, frames, layers,
                    markers=[{"tm": 0, "cm": "loop", "dr": frames}],
                    provenance=_provenance(tokens, [primary_label, track_label, curve_label]))


def preset_icon_morph(spec, tokens):
    """Menu (three lines) to close (X) and back, as true path morphs on a 24-unit grid."""
    width, height, fps = spec.get("width", 96), spec.get("height", 96), spec.get("fps", 60)
    colors = spec.get("colors", {})
    primary, primary_label = tokens.color(colors.get("primary", "color.fg.default"))
    curve, curve_label = tokens.easing(spec.get("easing", "ease.standard"))
    move = ms_to_frames(_timing(spec, tokens, "morph", "duration.slow"), fps)
    hold = ms_to_frames(_timing(spec, tokens, "hold", "600ms"), fps)
    loop = spec.get("loop", True)
    frames = move + hold + (move + hold if loop else 0)
    scale = min(width, height) / 24.0
    line_w = 2.0

    def segment(start_pts, end_pts, name, fade=False):
        keys = [(0, path_data(start_pts), curve), (move, path_data(end_pts), None)]
        if loop:
            keys += [(move + hold, path_data(end_pts), curve), (move + hold + move, path_data(start_pts), None)]
        items = [path_shape(animated(keys, shape=True)), stroke(primary, primary_label, line_w)]
        opacity = None
        if fade:
            fade_keys = [(0, 100, curve), (move, 0, None)]
            if loop:
                fade_keys += [(move + hold, 0, curve), (move + hold + move, 100, None)]
            opacity = animated(fade_keys)
        return group(name, items, group_transform(opacity=opacity))

    shapes = [
        segment([(4, 7), (20, 7)], [(6, 6), (18, 18)], "Top line"),
        segment([(4, 12), (20, 12)], [(12, 12), (12, 12)], "Middle line", fade=True),
        segment([(4, 17), (20, 17)], [(6, 18), (18, 6)], "Bottom line"),
    ]
    transform = layer_transform((width / 2.0, height / 2.0), anchor=(12, 12),
                                scale=static([scale * 100, scale * 100, 100]))
    layers = [shape_layer(1, "Menu to close (%s)" % primary_label, shapes, 0, frames, transform)]
    bg = background_layer(2, tokens, spec, width, height, frames)
    if bg:
        layers.append(bg)
    markers = [{"tm": 0, "cm": "to-close", "dr": move}]
    if loop:
        markers.append({"tm": move + hold, "cm": "to-menu", "dr": move})
    return document(spec.get("name", "icon-morph"), width, height, fps, frames, layers, markers=markers,
                    provenance=_provenance(tokens, [primary_label, curve_label]))


def preset_underline_sweep(spec, tokens):
    """An underline draws in from the left, holds, then exits to the right."""
    width, height, fps = spec.get("width", 960), spec.get("height", 120), spec.get("fps", 30)
    colors = spec.get("colors", {})
    primary, primary_label = tokens.color(colors.get("primary", "color.accent.default"))
    enter, enter_label = tokens.easing(spec.get("easing", "ease.emphasized-decelerate"))
    exit_curve, exit_label = tokens.easing(spec.get("exit_easing", "ease.accelerate"))
    draw = ms_to_frames(_timing(spec, tokens, "enter", "duration.slower"), fps)
    hold = ms_to_frames(_timing(spec, tokens, "hold", "1000ms"), fps)
    leave = ms_to_frames(_timing(spec, tokens, "exit", "duration.slow"), fps)
    frames = draw + hold + leave
    pad = width * 0.06
    thickness = max(2.0, height * 0.06)
    y = height * 0.7
    line = group("Underline", [
        path_shape(static(path_data([(pad, y), (width - pad, y)]))),
        trim(animated([(draw + hold, 0, exit_curve), (frames, 100, None)]),
             animated([(0, 0, enter), (draw, 100, None)])),
        stroke(primary, primary_label, thickness, cap=1),
    ])
    layers = [shape_layer(1, "Underline (%s)" % primary_label, [line], 0, frames, layer_transform((0, 0)))]
    bg = background_layer(2, tokens, spec, width, height, frames)
    if bg:
        layers.append(bg)
    markers = [{"tm": 0, "cm": "enter", "dr": draw}, {"tm": draw + hold, "cm": "exit", "dr": leave}]
    return document(spec.get("name", "underline-sweep"), width, height, fps, frames, layers, markers=markers,
                    provenance=_provenance(tokens, [primary_label, enter_label, exit_label]))


def _provenance(tokens, labels):
    return {"tokens": {"brand": tokens.brand, "mode": tokens.mode, "used": sorted(set(labels))}}


PRESETS = {
    "logo-reveal": (preset_logo_reveal, "Ring draw-on, masked diamond and dot in a precomp; markers reveal/hold"),
    "loader": (preset_loader, "Seamless arc spinner loop on a token track color"),
    "icon-morph": (preset_icon_morph, "Menu to close path morph and back; markers to-close/to-menu"),
    "underline-sweep": (preset_underline_sweep, "Underline draws in, holds, exits right; markers enter/exit"),
}


def build(spec, tokens=None):
    """Spec dict -> Lottie dict. Spec keys: preset, name, width, height, fps, duration, colors, easing, timing."""
    preset = spec.get("preset")
    if preset not in PRESETS:
        raise ValueError("unknown preset %r (have: %s)" % (preset, ", ".join(sorted(PRESETS))))
    if tokens is None:
        token_spec = spec.get("tokens", {})
        tokens = load_tokens(brand=token_spec.get("brand"), mode=token_spec.get("mode"))
    fps = spec.get("fps")
    if fps is not None and (not isinstance(fps, (int, float)) or fps <= 0 or fps > MAX_FPS):
        raise ValueError("fps must be between 1 and %d" % MAX_FPS)
    return PRESETS[preset][0](spec, tokens)


# ---------------------------------------------------------------------------
# Validation


def _issue(issues, level, path, rule, message):
    issues.append({"level": level, "path": path, "rule": rule, "message": message})


def _walk_expressions(node, path, issues):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "x" and isinstance(value, str):
                _issue(issues, "error", path + ".x", "no-expressions",
                       "expression found; bake it to keyframes")
            else:
                _walk_expressions(value, "%s.%s" % (path, key), issues)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            _walk_expressions(value, "%s[%d]" % (path, index), issues)


def _check_property(prop, path, issues):
    if not isinstance(prop, dict) or "k" not in prop:
        return
    if prop.get("a") != 1:
        return
    frames = prop["k"]
    if not isinstance(frames, list) or not frames:
        _issue(issues, "error", path, "keyframes", "animated property without keyframes")
        return
    last_t = None
    for index, key in enumerate(frames):
        kpath = "%s.k[%d]" % (path, index)
        if not isinstance(key, dict) or "t" not in key:
            _issue(issues, "error", kpath, "keyframes", "keyframe needs a time 't'")
            continue
        if last_t is not None and key["t"] <= last_t:
            _issue(issues, "error", kpath, "keyframes", "keyframe times must increase")
        last_t = key["t"]
        is_last = index == len(frames) - 1
        if not is_last and "s" not in key:
            _issue(issues, "error", kpath, "keyframes", "keyframe needs a start value 's'")
        if not is_last and not key.get("h"):
            for tangent in ("i", "o"):
                if tangent not in key:
                    _issue(issues, "error", kpath, "keyframes", "missing easing tangent '%s'" % tangent)
                    continue
                xs = key[tangent].get("x") if isinstance(key[tangent], dict) else None
                xs = xs if isinstance(xs, list) else [xs]
                for x in xs:
                    if not isinstance(x, (int, float)) or not 0 <= x <= 1:
                        _issue(issues, "error", kpath + "." + tangent, "keyframes",
                               "tangent x must be a number within 0-1")


def _check_props(node, path, issues, keys):
    for key in keys:
        if key in node:
            _check_property(node[key], "%s.%s" % (path, key), issues)


def _check_color(prop, path, issues):
    if isinstance(prop, dict) and prop.get("a") == 0:
        value = prop.get("k")
        if not isinstance(value, list) or len(value) not in (3, 4) or any(
                not isinstance(c, (int, float)) or c < 0 or c > 1 for c in value):
            _issue(issues, "error", path, "color", "color must be 3 or 4 numbers within 0-1")


def _check_shapes(items, path, issues):
    for index, item in enumerate(items or []):
        spath = "%s[%d]" % (path, index)
        if not isinstance(item, dict):
            _issue(issues, "error", spath, "shape", "shape item must be an object")
            continue
        kind = item.get("ty")
        if kind in FORBIDDEN_SHAPES:
            _issue(issues, "error", spath, "shape-type", "not portable: %s" % FORBIDDEN_SHAPES[kind])
            continue
        if kind not in ALLOWED_SHAPES:
            _issue(issues, "error", spath, "shape-type", "unknown or unsupported shape type %r" % (kind,))
            continue
        if kind == "gr":
            _check_shapes(item.get("it"), spath + ".it", issues)
        if kind in ("fl", "st"):
            _check_color(item.get("c"), spath + ".c", issues)
        _check_props(item, spath, issues, ("p", "s", "r", "a", "o", "w", "e", "c", "ks", "sk", "sa", "pt", "or", "ir"))


def _check_layers(layers, path, issues, assets, comp_ip, comp_op, stack):
    if not isinstance(layers, list):
        _issue(issues, "error", path, "required", "layers must be a list")
        return
    indices = {}
    for index, layer in enumerate(layers):
        lpath = "%s[%d]" % (path, index)
        if not isinstance(layer, dict):
            _issue(issues, "error", lpath, "layer", "layer must be an object")
            continue
        for key in ("ty", "ind", "ip", "op", "st", "ks"):
            if key not in layer:
                _issue(issues, "error", lpath, "required", "layer is missing '%s'" % key)
        kind = layer.get("ty")
        if kind in FORBIDDEN_LAYER_TYPES:
            _issue(issues, "error", lpath, "layer-type", "not portable: %s" % FORBIDDEN_LAYER_TYPES[kind])
        elif kind not in ALLOWED_LAYER_TYPES:
            _issue(issues, "error", lpath, "layer-type", "unknown layer type %r" % (kind,))
        ind = layer.get("ind")
        if ind is not None:
            if ind in indices:
                _issue(issues, "error", lpath, "ind", "duplicate layer index %r" % (ind,))
            indices[ind] = index
        ip, op = layer.get("ip"), layer.get("op")
        if isinstance(ip, (int, float)) and isinstance(op, (int, float)):
            if op <= ip:
                _issue(issues, "error", lpath, "in-out", "layer out point must be after its in point")
            elif op <= comp_ip or ip >= comp_op:
                _issue(issues, "warning", lpath, "in-out", "layer never visible inside the composition range")
        if layer.get("ddd") == 1:
            _issue(issues, "error", lpath, "3d", "3D layers are not portable")
        if layer.get("ef"):
            _issue(issues, "error", lpath + ".ef", "effects", "layer effects are not portable")
        if "tt" in layer and layer["tt"] not in ALLOWED_MATTES:
            _issue(issues, "error", lpath + ".tt", "matte", "only alpha mattes (1, 2) are portable")
        ks = layer.get("ks")
        if isinstance(ks, dict):
            for key in ("a", "p", "s", "r", "o"):
                if key not in ks:
                    _issue(issues, "warning", lpath + ".ks", "transform",
                           "transform without '%s'; some players need all five" % key)
            _check_props(ks, lpath + ".ks", issues, ("a", "p", "s", "r", "o"))
        for mindex, mask in enumerate(layer.get("masksProperties") or []):
            mpath = "%s.masksProperties[%d]" % (lpath, mindex)
            if mask.get("mode") not in ALLOWED_MASK_MODES:
                _issue(issues, "error", mpath, "mask", "mask mode %r is not portable (use a, s or n)"
                       % (mask.get("mode"),))
            for key in ("pt", "o", "x"):
                if not isinstance(mask.get(key), dict):
                    _issue(issues, "error", mpath, "mask",
                           "mask needs '%s' as a property (lottie-web reads mask expansion 'x' and fails without it)"
                           % key)
            _check_props(mask, mpath, issues, ("pt", "o", "x"))
        if layer.get("masksProperties") and not layer.get("hasMask"):
            _issue(issues, "warning", lpath, "mask", "masksProperties without hasMask: true")
        if kind == 4:
            _check_shapes(layer.get("shapes"), lpath + ".shapes", issues)
        if kind == 1:
            if not isinstance(layer.get("sc"), str):
                _issue(issues, "error", lpath, "required", "solid layer needs a hex color 'sc'")
        if kind == 0:
            ref = layer.get("refId")
            if ref not in assets:
                _issue(issues, "error", lpath, "refId", "precomp refId %r has no asset" % (ref,))
            elif ref in stack:
                _issue(issues, "error", lpath, "refId", "precomp cycle through %r" % (ref,))
            elif "layers" not in assets[ref]:
                _issue(issues, "error", lpath, "refId", "refId %r is not a precomposition" % (ref,))
            else:
                _check_layers(assets[ref]["layers"], "assets[%s].layers" % ref, issues, assets,
                              float("-inf"), float("inf"), stack | {ref})
    for index, layer in enumerate(layers):
        if isinstance(layer, dict) and "parent" in layer and layer["parent"] not in indices:
            _issue(issues, "error", "%s[%d]" % (path, index), "parent",
                   "parent %r is not a layer in this composition" % (layer["parent"],))


def validate(doc):
    """Return a list of issues ({level, path, rule, message}) against the portable Lottie subset."""
    issues = []
    if not isinstance(doc, dict):
        _issue(issues, "error", "$", "required", "a Lottie file is a JSON object")
        return issues
    for key in ("v", "fr", "ip", "op", "w", "h", "layers"):
        if key not in doc:
            _issue(issues, "error", "$", "required", "missing top-level '%s'" % key)
    fr = doc.get("fr")
    if isinstance(fr, bool) or not isinstance(fr, (int, float)) or fr <= 0 or fr > MAX_FPS:
        _issue(issues, "error", "$.fr", "frame-rate", "frame rate must be within 1-%d" % MAX_FPS)
    elif fr not in COMMON_FPS:
        _issue(issues, "warning", "$.fr", "frame-rate", "uncommon frame rate %r; use 24, 25, 30, 50 or 60" % fr)
    for key in ("w", "h"):
        value = doc.get(key)
        if key in doc and (not isinstance(value, int) or isinstance(value, bool) or value <= 0):
            _issue(issues, "error", "$." + key, "size", "'%s' must be a positive integer" % key)
    ip, op = doc.get("ip"), doc.get("op")
    if isinstance(ip, (int, float)) and isinstance(op, (int, float)) and op <= ip:
        _issue(issues, "error", "$", "in-out", "op must be greater than ip")
    if doc.get("ddd") == 1:
        _issue(issues, "error", "$.ddd", "3d", "3D compositions are not portable")
    assets = {}
    for index, asset in enumerate(doc.get("assets") or []):
        apath = "$.assets[%d]" % index
        if not isinstance(asset, dict) or "id" not in asset:
            _issue(issues, "error", apath, "asset", "asset needs an id")
            continue
        if "layers" not in asset:
            _issue(issues, "error", apath, "asset", "image, audio and data assets are not portable (no rasters)")
            continue
        assets[asset["id"]] = asset
    if isinstance(ip, (int, float)) and isinstance(op, (int, float)):
        _check_layers(doc.get("layers"), "$.layers", issues, assets, ip, op, frozenset())
    elif "layers" in doc:
        _check_layers(doc.get("layers"), "$.layers", issues, assets, float("-inf"), float("inf"), frozenset())
    if doc.get("chars") or doc.get("fonts"):
        _issue(issues, "error", "$", "text", "glyph and font data are not portable; convert text to shapes")
    _walk_expressions(doc, "$", issues)
    return issues


# ---------------------------------------------------------------------------
# CLI


def dumps(doc, pretty=False):
    if pretty:
        return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    return json.dumps(doc, separators=(",", ":"), ensure_ascii=False) + "\n"


def _load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def cmd_presets(_args):
    for name in sorted(PRESETS):
        print("%-16s %s" % (name, PRESETS[name][1]))
    return 0


def cmd_build(args):
    spec = _load_json(args.spec)
    token_spec = spec.get("tokens", {})
    tokens = load_tokens(args.tokens, args.brand or token_spec.get("brand"), args.mode or token_spec.get("mode"))
    doc = build(spec, tokens)
    errors = [i for i in validate(doc) if i["level"] == "error"]
    if errors:
        for issue in errors:
            print("error %s [%s] %s" % (issue["path"], issue["rule"], issue["message"]), file=sys.stderr)
        return 1
    text = dumps(doc, args.pretty)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print("wrote %s (%d bytes, %d frames at %sfps)" % (args.output, len(text.encode("utf-8")), doc["op"], doc["fr"]))
    else:
        sys.stdout.write(text)
    return 0


def cmd_validate(args):
    exit_code = 0
    report = {}
    for name in args.files:
        try:
            doc = _load_json(name)
        except (OSError, ValueError) as error:
            report[name] = [{"level": "error", "path": "$", "rule": "json", "message": str(error)}]
            exit_code = 1
            continue
        issues = validate(doc)
        size_kb = Path(name).stat().st_size / 1024.0
        if args.max_kb and size_kb > args.max_kb:
            issues.append({"level": "warning", "path": "$", "rule": "size",
                           "message": "%.1fKB is over the %sKB budget" % (size_kb, args.max_kb)})
        report[name] = issues
        if any(i["level"] == "error" for i in issues):
            exit_code = 1
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for name, issues in report.items():
            errors = sum(1 for i in issues if i["level"] == "error")
            warnings = len(issues) - errors
            print("%s: %s (%d errors, %d warnings)" % (name, "FAIL" if errors else "ok", errors, warnings))
            for issue in issues:
                print("  %s %s [%s] %s" % (issue["level"], issue["path"], issue["rule"], issue["message"]))
    return exit_code


def example_outputs(spec_dir=SPEC_DIR, tokens_path=None):
    """Yield (output file name, text) for every spec in lottie_specs/."""
    for spec_path in sorted(Path(spec_dir).glob("*.json")):
        spec = _load_json(spec_path)
        token_spec = spec.get("tokens", {})
        tokens = load_tokens(tokens_path, token_spec.get("brand"), token_spec.get("mode"))
        yield spec_path.stem + ".json", dumps(build(spec, tokens))


def cmd_examples(args):
    out = Path(args.out)
    stale = []
    for name, text in example_outputs(tokens_path=args.tokens):
        target = out / name
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                stale.append(str(target))
            continue
        out.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print("wrote %s" % target)
    if stale:
        print("stale or missing (run: python3 lottie_build.py examples):\n  " + "\n  ".join(stale), file=sys.stderr)
        return 1
    if args.check:
        print("examples up to date in %s" % out)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build and validate portable Lottie JSON from kit tokens.")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("presets", help="list presets")
    p_build = sub.add_parser("build", help="build a Lottie file from a spec")
    p_build.add_argument("spec")
    p_build.add_argument("-o", "--output")
    p_build.add_argument("--tokens", help="path to a tokens.resolved.json (default: the kit's)")
    p_build.add_argument("--brand")
    p_build.add_argument("--mode")
    p_build.add_argument("--pretty", action="store_true")
    p_val = sub.add_parser("validate", help="check files against the portable Lottie subset")
    p_val.add_argument("files", nargs="+")
    p_val.add_argument("--json", action="store_true")
    p_val.add_argument("--max-kb", type=float, default=100.0, help="size budget warning (default 100)")
    p_ex = sub.add_parser("examples", help="build every spec in lottie_specs/")
    p_ex.add_argument("--out", default=str(DEFAULT_EXAMPLE_OUT))
    p_ex.add_argument("--tokens")
    p_ex.add_argument("--check", action="store_true", help="fail if outputs are stale instead of writing")
    args = parser.parse_args(argv)
    commands = {"presets": cmd_presets, "build": cmd_build, "validate": cmd_validate, "examples": cmd_examples}
    if args.command not in commands:
        parser.print_help()
        return 2
    try:
        return commands[args.command](args)
    except ValueError as error:
        print("error: %s" % error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
