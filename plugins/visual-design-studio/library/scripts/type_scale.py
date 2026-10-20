"""Modular type scales: static px/rem steps or fluid clamp() values.

Version-Timestamp: 2026-10-20 02:04:10 UTC

Usage:
  python3 type_scale.py --base 16 --ratio major-third                       # table
  python3 type_scale.py --base 16 --ratio 1.2 --down 2 --up 6 --format css
  python3 type_scale.py --fluid --min-vw 360 --max-vw 1440 --min-base 16 --max-base 18 \
      --min-ratio 1.2 --max-ratio 1.333 --format css
  python3 type_scale.py --list-ratios

Importable: RATIOS, resolve_ratio, step_name, scale, fluid_scale, to_css, fluid_to_css.

Step 0 is the base size and is named "md"; -1 sm, -2 xs, -3 2xs; +1 lg, +2 xl, +3 2xl ... matching the token
contract's --font-size-* names. Standard library only, deterministic.

Fluid math, per step i:
  min_size = min_base * min_ratio^i            (at min_vw)
  max_size = max_base * max_ratio^i            (at max_vw)
  slope    = (max_size - min_size) / (max_vw - min_vw)
  intercept = min_size - slope * min_vw
  size(vw) = intercept + slope * 100 * 1vw, clamped between min_size and max_size
which is written as clamp(<smaller>rem, <intercept>rem + <slope*100>vw, <larger>rem). Using rem for the
intercept keeps the value responsive to browser zoom (WCAG 1.4.4).
"""
import argparse
import json
import sys
from collections import OrderedDict

RATIOS = OrderedDict([
    ("minor-second", 1.067),
    ("major-second", 1.125),
    ("minor-third", 1.2),
    ("major-third", 1.25),
    ("perfect-fourth", 1.333),
    ("augmented-fourth", 1.414),
    ("perfect-fifth", 1.5),
    ("minor-sixth", 1.6),
    ("golden", 1.618),
    ("major-sixth", 1.667),
    ("minor-seventh", 1.778),
    ("major-seventh", 1.875),
    ("octave", 2.0),
])
ROOT_PX = 16
MAX_ZOOM_SAFE_RATIO = 2.5  # max/min font size at or under 2.5 keeps 200% zoom achievable for fluid type


class ScaleError(ValueError):
    pass


def resolve_ratio(value):
    """Accept a named ratio ('golden', 'major third') or a number > 1."""
    if isinstance(value, (int, float)):
        ratio = float(value)
    else:
        key = str(value).strip().lower().replace(" ", "-").replace("_", "-")
        if key in RATIOS:
            return RATIOS[key]
        try:
            ratio = float(key)
        except ValueError as exc:
            raise ScaleError(f"unknown ratio {value!r}; use a number or one of {', '.join(RATIOS)}") from exc
    if ratio <= 1:
        raise ScaleError("ratio must be greater than 1")
    return ratio


def step_name(step):
    if step == 0:
        return "md"
    if step == -1:
        return "sm"
    if step == -2:
        return "xs"
    if step == 1:
        return "lg"
    if step == 2:
        return "xl"
    if step < 0:
        return f"{-step - 1}xs"
    return f"{step - 1}xl"


def _num(value, places=4):
    text = f"{value:.{places}f}".rstrip("0").rstrip(".")
    return text if text not in ("", "-0") else "0"


def scale(base=16.0, ratio=1.25, down=2, up=6, root=ROOT_PX):
    """Static modular scale. Returns a list of dicts with step, name, px and rem."""
    if base <= 0:
        raise ScaleError("base must be positive")
    ratio = resolve_ratio(ratio)
    out = []
    for step in range(-down, up + 1):
        px = base * ratio ** step
        out.append(OrderedDict([("step", step), ("name", step_name(step)), ("px", round(px, 2)),
                                ("rem", round(px / root, 4))]))
    return out


def fluid_scale(min_vw=360, max_vw=1440, min_base=16.0, max_base=18.0, min_ratio=1.2, max_ratio=1.333, down=2, up=6,
                root=ROOT_PX):
    """Fluid scale: each step interpolates linearly between its size at min_vw and at max_vw."""
    if max_vw <= min_vw:
        raise ScaleError("max-vw must be larger than min-vw")
    if min_base <= 0 or max_base <= 0:
        raise ScaleError("base sizes must be positive")
    min_ratio, max_ratio = resolve_ratio(min_ratio), resolve_ratio(max_ratio)
    out = []
    for step in range(-down, up + 1):
        min_size = min_base * min_ratio ** step
        max_size = max_base * max_ratio ** step
        slope = (max_size - min_size) / (max_vw - min_vw)
        intercept = min_size - slope * min_vw
        low, high = sorted((min_size, max_size))
        sign = "-" if slope < 0 else "+"
        clamp = (f"clamp({_num(low / root)}rem, {_num(intercept / root)}rem {sign} {_num(abs(slope) * 100)}vw, "
                 f"{_num(high / root)}rem)")
        out.append(OrderedDict([
            ("step", step), ("name", step_name(step)),
            ("min_px", round(min_size, 2)), ("max_px", round(max_size, 2)),
            ("slope", round(slope, 6)), ("intercept_px", round(intercept, 4)),
            ("clamp", clamp),
            ("zoom_ratio", round(high / low, 3)),
        ]))
    return out


def to_css(items, prefix="font-size"):
    lines = [":root {"]
    for item in items:
        lines.append(f"  --{prefix}-{item['name']}: {_num(item['rem'])}rem; /* {_num(item['px'], 2)}px, step {item['step']} */")
    lines.append("}")
    return "\n".join(lines) + "\n"


def fluid_to_css(items, min_vw, max_vw, prefix="font-size", root=ROOT_PX):
    lines = [
        f"/* Fluid type: {min_vw}px -> {max_vw}px viewport. For each step:",
        "   slope = (max - min) / (max_vw - min_vw); intercept = min - slope * min_vw;",
        f"   preferred = intercept/{root} rem + slope*100 vw, clamped to [min, max]. */",
        ":root {",
    ]
    for item in items:
        lines.append(
            f"  /* step {item['step']}: {_num(item['min_px'], 2)}px @{min_vw} -> {_num(item['max_px'], 2)}px @{max_vw}; "
            f"slope = ({_num(item['max_px'], 2)} - {_num(item['min_px'], 2)}) / ({max_vw} - {min_vw}) = "
            f"{_num(item['slope'], 6)} = {_num(item['slope'] * 100)}vw; intercept = {_num(item['min_px'], 2)} - "
            f"({_num(item['slope'], 6)} * {min_vw}) = {_num(item['intercept_px'], 2)}px */")
        lines.append(f"  --{prefix}-{item['name']}: {item['clamp']};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def _table(headers, rows):
    widths = [max(len(str(h)), *(len(str(r[i])) for r in rows)) for i, h in enumerate(headers)]
    out = ["  ".join(str(h).ljust(w) for h, w in zip(headers, widths)), "  ".join("-" * w for w in widths)]
    out += ["  ".join(str(c).ljust(w) for c, w in zip(row, widths)) for row in rows]
    return "\n".join(out) + "\n"


def build_parser():
    parser = argparse.ArgumentParser(description="Modular type scale (static or fluid clamp()).")
    parser.add_argument("--base", type=float, default=16.0, help="base size in px (step 0), default 16")
    parser.add_argument("--ratio", default="major-third", help="number or name, default major-third (1.25)")
    parser.add_argument("--down", type=int, default=2, help="steps below the base (default 2: sm, xs)")
    parser.add_argument("--up", type=int, default=6, help="steps above the base (default 6: lg ... 5xl)")
    parser.add_argument("--root", type=float, default=ROOT_PX, help="root font size for rem (default 16)")
    parser.add_argument("--prefix", default="font-size", help="CSS variable prefix (default font-size)")
    parser.add_argument("--format", choices=["table", "css", "json"], default="table")
    parser.add_argument("--fluid", action="store_true", help="emit clamp() values between two viewports")
    parser.add_argument("--min-vw", type=float, default=360)
    parser.add_argument("--max-vw", type=float, default=1440)
    parser.add_argument("--min-base", type=float, default=16.0)
    parser.add_argument("--max-base", type=float, default=18.0)
    parser.add_argument("--min-ratio", default="1.2")
    parser.add_argument("--max-ratio", default="1.333")
    parser.add_argument("--list-ratios", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.list_ratios:
        for name, value in RATIOS.items():
            print(f"{name:<17} {value}")
        return 0
    try:
        if args.fluid:
            items = fluid_scale(args.min_vw, args.max_vw, args.min_base, args.max_base, args.min_ratio, args.max_ratio,
                                args.down, args.up, args.root)
        else:
            items = scale(args.base, args.ratio, args.down, args.up, args.root)
    except ScaleError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    min_vw, max_vw = _num(args.min_vw), _num(args.max_vw)
    if args.format == "json":
        print(json.dumps(items, indent=2))
    elif args.format == "css":
        sys.stdout.write(fluid_to_css(items, min_vw, max_vw, args.prefix, args.root) if args.fluid
                         else to_css(items, args.prefix))
    elif args.fluid:
        rows = [[i["step"], i["name"], _num(i["min_px"], 2), _num(i["max_px"], 2), i["clamp"]] for i in items]
        sys.stdout.write(_table(["step", "name", f"px @{min_vw}", f"px @{max_vw}", "clamp()"], rows))
    else:
        rows = [[i["step"], i["name"], _num(i["px"], 2), _num(i["rem"]), f"--{args.prefix}-{i['name']}"] for i in items]
        sys.stdout.write(_table(["step", "name", "px", "rem", "variable"], rows))
    if args.fluid:
        worst = max(items, key=lambda i: i["zoom_ratio"])
        if worst["zoom_ratio"] > MAX_ZOOM_SAFE_RATIO:
            print(f"warning: step {worst['name']} grows {worst['zoom_ratio']}x between viewports; above "
                  f"{MAX_ZOOM_SAFE_RATIO}x users may not reach 200% text zoom (WCAG 1.4.4)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
