"""Build, lint and check the Visual Design Kit design tokens (W3C DTCG format).

Version-Timestamp: 2026-10-20 02:04:10 UTC

Usage (from anywhere):
  python3 tokens.py build  [--src DIR] [--out DIR]   write dist/tokens.css, tailwind.css, tokens.resolved.json, figma-variables.json
  python3 tokens.py lint   [--src DIR] [--json]      DTCG structure, aliases, contract names and values, tiers, contrast
  python3 tokens.py check  [--src DIR] [--out DIR]   exit 1 when dist/ is missing or stale
  python3 tokens.py ramps  [--src DIR] [--write]     regenerate OKLCH ramps from the recipes stored in primitives
  python3 tokens.py figma-script [--src DIR]         print a use_figma script that imports figma-variables.json

Source layout (tokens/src/):
  primitives.tokens.json             raw ramps and scales; brand-level groups are marked "brandable"
  semantic.<mode>.tokens.json        one file per mode (light is the default); roles alias primitives
  components.tokens.json             component tokens; alias semantic tokens or public scale tokens only
  brands/<brand>.tokens.json         overrides of brandable primitives for [data-brand="<brand>"]

Standard library only (Python 3.9+). Output is byte-for-byte deterministic: no timestamps, source order,
fixed number formatting. The token names are fixed by the token contract
(.claude/skills/design-kit-authoring/references/token-contract.md).
"""
import argparse
import difflib
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import color_tools  # noqa: E402

NS = "com.github.newmindsgroup.vdk"
LIBRARY = Path(__file__).resolve().parent.parent
SRC = LIBRARY / "tokens" / "src"
DIST = LIBRARY / "tokens" / "dist"
FIGMA_IMPORT_JS = LIBRARY / "tokens" / "figma-import.js"
OUTPUTS = ("tokens.css", "tailwind.css", "tokens.resolved.json", "figma-variables.json")
ROOT_PX = 16

DTCG_TYPES = {"color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier", "number", "shadow",
              "strokeStyle", "border", "transition", "gradient", "typography", "fontStyle"}
TOKEN_KEYS = {"$value", "$type", "$description", "$extensions", "$deprecated"}
GROUP_KEYS = {"$type", "$description", "$extensions", "$deprecated"}
ALIAS_RE = re.compile(r"^\{([^{}]+)\}$")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
DIMENSION_RE = re.compile(r"^-?(\d+(\.\d+)?|\.\d+)(px|rem|em|ch|%|vw|vh|svh|dvh)$")
CSS_MATH_RE = re.compile(r"^(clamp|min|max|calc)\(.+\)$")
DURATION_RE = re.compile(r"^(\d+(\.\d+)?|\.\d+)(ms|s)$")
FONT_WEIGHT_KEYWORDS = {"thin", "hairline", "extra-light", "ultra-light", "light", "normal", "regular", "book",
                        "medium", "semi-bold", "demi-bold", "bold", "extra-bold", "ultra-bold", "black", "heavy",
                        "extra-black", "ultra-black"}
GENERIC_FONTS = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "ui-serif", "ui-sans-serif",
                 "ui-monospace", "ui-rounded", "emoji", "math", "fangsong"}
MODE_ORDER = ["light", "dark", "high-contrast"]
DEFAULT_MODE = "light"

# ---------------------------------------------------------------------------
# Contract (keep in sync with references/token-contract.md)
# ---------------------------------------------------------------------------

STATUS = ("success", "warning", "danger", "info")
SEMANTIC_COLOR_PATHS = (
    [("color", "bg", r) for r in ("canvas", "surface", "surface-raised", "sunken", "inverse")]
    + [("color", "fg", r) for r in ("default", "muted", "subtle", "inverse", "on-accent")]
    + [("color", "border", r) for r in ("subtle", "default", "strong")]
    + [("color", "accent", r) for r in ("default", "hover", "active", "subtle", "fg")]
    + [("color", s, r) for s in STATUS for r in ("fg", "bg", "border")]
    + [("color", "focus-ring"), ("color", "overlay-scrim")]
)
SHADOW_PATHS = [("shadow", s) for s in ("sm", "md", "lg", "xl")]
MODE_PATHS = SEMANTIC_COLOR_PATHS + SHADOW_PATHS  # every semantic.<mode> file defines all of these


def _contract_values():
    values = OrderedDict()
    for path in MODE_PATHS:
        values["--" + "-".join(path)] = None
    for role in ("display", "body", "mono"):
        values[f"--font-family-{role}"] = None
    sizes = ["0.75rem", "0.875rem", "1rem", "1.25rem", "1.5rem", "1.875rem", "2.25rem", "3rem", "3.75rem"]
    for name, value in zip(["xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"], sizes):
        values[f"--font-size-{name}"] = value
    for name, value in zip(["tight", "snug", "normal", "relaxed"], ["1.1", "1.25", "1.5", "1.65"]):
        values[f"--line-height-{name}"] = value
    for name, value in zip(["regular", "medium", "semibold", "bold"], ["400", "500", "600", "700"]):
        values[f"--font-weight-{name}"] = value
    for name, value in zip(["tight", "normal", "wide", "caps"], ["-0.02em", "0", "0.01em", "0.06em"]):
        values[f"--letter-spacing-{name}"] = value
    for name, value in zip(["narrow", "body", "wide"], ["45ch", "66ch", "75ch"]):
        values[f"--measure-{name}"] = value
    for n in (0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24):
        values[f"--space-{n}"] = "0" if n == 0 else f"{format_number(n * 0.25)}rem"
    values["--size-target-min"] = "24px"
    values["--size-target-comfortable"] = "44px"
    for name, value in zip(["sm", "md", "lg"], ["16px", "20px", "24px"]):
        values[f"--size-icon-{name}"] = value
    for name, value in zip(["none", "sm", "md", "lg", "xl", "full"], ["0", "4px", "8px", "12px", "16px", "9999px"]):
        values[f"--radius-{name}"] = value
    values["--border-width-thin"] = "1px"
    values["--border-width-thick"] = "2px"
    for name, value in zip(["instant", "fast", "moderate", "slow", "slower"], ["0ms", "120ms", "200ms", "320ms", "480ms"]):
        values[f"--duration-{name}"] = value
    values["--ease-standard"] = "cubic-bezier(0.2, 0, 0, 1)"
    values["--ease-decelerate"] = "cubic-bezier(0, 0, 0, 1)"
    values["--ease-accelerate"] = "cubic-bezier(0.3, 0, 1, 1)"
    values["--ease-emphasized-decelerate"] = "cubic-bezier(0.05, 0.7, 0.1, 1)"
    values["--ease-emphasized-accelerate"] = "cubic-bezier(0.3, 0, 0.8, 0.15)"
    values["--ease-linear"] = "linear"
    for name, value in zip(["base", "dropdown", "sticky", "overlay", "modal", "toast"],
                           ["0", "1000", "1100", "1200", "1300", "1400"]):
        values[f"--z-{name}"] = value
    for name, value in zip(["sm", "md", "lg", "xl"], ["640px", "768px", "1024px", "1280px"]):
        values[f"--container-{name}"] = value
    values["--gutter"] = "clamp(1rem, 4vw, 2rem)"
    return values


def format_number(value):
    """Deterministic number formatting: integers without a decimal point, otherwise up to 4 decimals."""
    if isinstance(value, bool):
        raise TypeError("booleans are not numbers here")
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.4f}".rstrip("0").rstrip(".")


CONTRACT = _contract_values()
CONTRACT_BREAKPOINTS = OrderedDict([("sm", "640px"), ("md", "768px"), ("lg", "1024px"), ("xl", "1280px"),
                                    ("2xl", "1536px")])
TEXT_BGS = ("color.bg.canvas", "color.bg.surface", "color.bg.surface-raised")
# (foreground, backgrounds, minimum, source, purpose, high-contrast minimum)
GUARANTEES = [
    ("color.fg.default", TEXT_BGS, 4.5, "contract", "body text", 7.0),
    ("color.fg.muted", TEXT_BGS, 4.5, "contract", "secondary text", 7.0),
    ("color.fg.subtle", TEXT_BGS, 3.0, "contract", "non-essential text and placeholders", None),
    ("color.fg.on-accent", ("color.accent.default", "color.accent.hover", "color.accent.active"), 4.5, "contract",
     "text on accent fills", None),
    ("color.accent.fg", ("color.accent.subtle",), 4.5, "contract", "accent text on accent-subtle", None),
] + [
    (f"color.{s}.fg", (f"color.{s}.bg",), 4.5, "contract", f"{s} text on {s} background", None) for s in STATUS
] + [
    ("color.border.strong", ("color.bg.canvas",), 3.0, "contract", "control boundaries (WCAG 1.4.11)", None),
    ("color.focus-ring", ("color.bg.canvas",), 3.0, "contract", "focus indicator (WCAG 2.4.11/1.4.11)", None),
    # Kit additions: pairs the components and examples rely on.
    ("color.accent.fg", ("color.bg.canvas", "color.bg.surface"), 4.5, "kit", "links and accent text", None),
    ("color.fg.inverse", ("color.bg.inverse",), 4.5, "kit", "tooltips and snackbars", None),
    ("color.fg.default", ("color.bg.sunken",), 4.5, "kit", "text in wells and code blocks", 7.0),
    ("color.fg.muted", ("color.bg.sunken",), 4.5, "kit", "table headers and helper text in wells", None),
    ("color.border.strong", ("color.bg.surface",), 3.0, "kit", "input borders on surfaces", None),
    ("color.focus-ring", ("color.bg.surface", "color.bg.surface-raised"), 3.0, "kit", "focus on cards and dialogs",
     None),
] + [
    (f"color.{s}.fg", ("color.bg.canvas", "color.bg.surface"), 4.5, "kit", f"inline {s} text", None) for s in STATUS
]

# Tailwind v4 mapping: (comment, [(theme variable, token CSS variable or literal)]).
TAILWIND_GROUPS = [
    ("Backgrounds: bg-canvas, bg-surface, bg-accent, bg-success ...", [
        ("--background-color-canvas", "--color-bg-canvas"),
        ("--background-color-surface", "--color-bg-surface"),
        ("--background-color-surface-raised", "--color-bg-surface-raised"),
        ("--background-color-sunken", "--color-bg-sunken"),
        ("--background-color-inverse", "--color-bg-inverse"),
        ("--background-color-accent", "--color-accent-default"),
        ("--background-color-accent-hover", "--color-accent-hover"),
        ("--background-color-accent-active", "--color-accent-active"),
        ("--background-color-accent-subtle", "--color-accent-subtle"),
    ] + [(f"--background-color-{s}", f"--color-{s}-bg") for s in STATUS] + [
        ("--background-color-scrim", "--color-overlay-scrim"),
    ]),
    ("Text: text-default, text-muted, text-subtle, text-inverse, text-on-accent, text-accent, text-danger ...", [
        ("--text-color-default", "--color-fg-default"),
        ("--text-color-muted", "--color-fg-muted"),
        ("--text-color-subtle", "--color-fg-subtle"),
        ("--text-color-inverse", "--color-fg-inverse"),
        ("--text-color-on-accent", "--color-fg-on-accent"),
        ("--text-color-accent", "--color-accent-fg"),
    ] + [(f"--text-color-{s}", f"--color-{s}-fg") for s in STATUS]),
    ("Borders and dividers: border-subtle, border-default, border-strong, border-accent, divide-subtle ...", [
        ("--border-color-subtle", "--color-border-subtle"),
        ("--border-color-default", "--color-border-default"),
        ("--border-color-strong", "--color-border-strong"),
        ("--border-color-accent", "--color-accent-default"),
        ("--border-color-focus", "--color-focus-ring"),
    ] + [(f"--border-color-{s}", f"--color-{s}-border") for s in STATUS]),
    ("Focus: ring-focus, outline-focus, ring-accent", [
        ("--ring-color-focus", "--color-focus-ring"),
        ("--ring-color-accent", "--color-accent-default"),
        ("--outline-color-focus", "--color-focus-ring"),
    ]),
    ("Shared colors for fill-*, stroke-*, caret-*, accent-*, decoration-*: fill-accent, stroke-danger ...", [
        ("--color-accent", "--color-accent-default"),
        ("--color-focus", "--color-focus-ring"),
    ] + [(f"--color-{s}", f"--color-{s}-fg") for s in STATUS]),
    ("Font families: font-display, font-body, font-mono (font-sans = body, used by preflight)", [
        ("--font-display", "--font-family-display"),
        ("--font-body", "--font-family-body"),
        ("--font-sans", "--font-family-body"),
        ("--font-mono", "--font-family-mono"),
    ]),
    ("Font sizes: text-xs ... text-5xl, text-md (text-base is an alias of text-md)", []),
    ("Line heights: leading-tight, leading-snug, leading-normal, leading-relaxed", [
        (f"--leading-{n}", f"--line-height-{n}") for n in ("tight", "snug", "normal", "relaxed")]),
    ("Weights: font-regular (and font-normal), font-medium, font-semibold, font-bold", [
        ("--font-weight-regular", "--font-weight-regular"),
        ("--font-weight-normal", "--font-weight-regular"),
        ("--font-weight-medium", "--font-weight-medium"),
        ("--font-weight-semibold", "--font-weight-semibold"),
        ("--font-weight-bold", "--font-weight-bold"),
    ]),
    ("Letter spacing: tracking-tight, tracking-normal, tracking-wide, tracking-caps", [
        (f"--tracking-{n}", f"--letter-spacing-{n}") for n in ("tight", "normal", "wide", "caps")]),
    ("Spacing: p-4, gap-6, mt-12 ... = n x --space-1 (0.25rem), so every --space-n step maps to *-n", [
        ("--spacing", "--space-1"),
    ]),
    ("Radius: rounded-sm, rounded-md, rounded-lg, rounded-xl (rounded-none and rounded-full are built in)", [
        (f"--radius-{n}", f"--radius-{n}") for n in ("sm", "md", "lg", "xl")]),
    ("Elevation: shadow-sm, shadow-md, shadow-lg, shadow-xl (values change per mode)", [
        (f"--shadow-{n}", f"--shadow-{n}") for n in ("sm", "md", "lg", "xl")]),
    ("Easing: ease-standard, ease-decelerate, ease-accelerate, ease-emphasized-*, ease-linear", [
        (f"--ease-{n}", f"--ease-{n}") for n in ("standard", "decelerate", "accelerate", "emphasized-decelerate",
                                                 "emphasized-accelerate", "linear")]),
    ("Duration: duration-instant, duration-fast, duration-moderate, duration-slow, duration-slower", [
        (f"--transition-duration-{n}", f"--duration-{n}") for n in ("instant", "fast", "moderate", "slow", "slower")]),
    ("Z-index: z-base, z-dropdown, z-sticky, z-overlay, z-modal, z-toast", [
        (f"--z-index-{n}", f"--z-{n}") for n in ("base", "dropdown", "sticky", "overlay", "modal", "toast")]),
]
TAILWIND_RESETS = ("--color-*", "--text-*", "--leading-*", "--tracking-*", "--font-weight-*", "--radius-*",
                   "--shadow-*", "--ease-*", "--container-*", "--breakpoint-*")
FONT_SIZE_LEADING = {"xs": "normal", "sm": "normal", "md": "normal", "lg": "snug", "xl": "snug", "2xl": "snug",
                     "3xl": "tight", "4xl": "tight", "5xl": "tight"}


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

class Token:
    __slots__ = ("path", "type", "value", "description", "extensions", "deprecated", "file", "tier")

    def __init__(self, path, type_, value, description, extensions, deprecated, file, tier):
        self.path = path
        self.type = type_
        self.value = value
        self.description = description
        self.extensions = extensions or {}
        self.deprecated = deprecated
        self.file = file
        self.tier = tier

    @property
    def dotted(self):
        return ".".join(self.path)

    @property
    def css_name(self):
        return "--" + "-".join(self.path)

    def ext(self, key, default=None):
        return (self.extensions.get(NS) or {}).get(key, default)


class Layer:
    """One source file: its tokens (path -> Token), root metadata and brandable group prefixes."""

    def __init__(self, file, tier, slug, meta, tokens, brandable):
        self.file = file
        self.tier = tier
        self.slug = slug
        self.meta = meta
        self.tokens = tokens
        self.brandable = brandable

    @property
    def name(self):
        return self.meta.get("name") or self.slug.replace("-", " ").title()


class Source:
    def __init__(self, src):
        self.src = Path(src)
        self.errors = []
        self.warnings = []
        self.primitives = None
        self.modes = []
        self.components = None
        self.brands = []

    @property
    def default_brand(self):
        meta = self.primitives.meta if self.primitives else {}
        return meta.get("brand", "default"), meta.get("brandName", meta.get("brand", "default").title())

    def mode(self, slug):
        for mode in self.modes:
            if mode.slug == slug:
                return mode
        return None

    def brand(self, slug):
        for brand in self.brands:
            if brand.slug == slug:
                return brand
        return None

    def brand_slugs(self):
        return [self.default_brand[0]] + [b.slug for b in self.brands]


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict), None
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot read {path.name}: {exc}"


def _walk(node, path, inherited_type, file, tier, tokens, errors, brandable, inherited_brandable=False):
    for key, child in node.items():
        if key.startswith("$"):
            if key not in GROUP_KEYS and not (not path and key == "$schema"):
                errors.append(f"[structure] {file}: {'.'.join(path) or '(root)'}: unknown group property {key}")
            continue
        here = path + (key,)
        dotted = ".".join(here)
        if not NAME_RE.match(key):
            errors.append(f"[structure] {file}: {dotted}: names must be lowercase letters, digits and hyphens "
                          "(no '.', '{', '}' or '$')")
            continue
        if not isinstance(child, dict):
            errors.append(f"[structure] {file}: {dotted}: expected a token or group object, got {type(child).__name__}")
            continue
        group_type = child.get("$type", inherited_type)
        if "$type" in child and child["$type"] not in DTCG_TYPES:
            errors.append(f"[structure] {file}: {dotted}: unknown $type {child['$type']!r}")
        if "$description" in child and not isinstance(child["$description"], str):
            errors.append(f"[structure] {file}: {dotted}: $description must be a string")
        if "$extensions" in child and not isinstance(child["$extensions"], dict):
            errors.append(f"[structure] {file}: {dotted}: $extensions must be an object")
        if "$value" in child:
            for prop in child:
                if prop.startswith("$") and prop not in TOKEN_KEYS:
                    errors.append(f"[structure] {file}: {dotted}: unknown token property {prop}")
                elif not prop.startswith("$"):
                    errors.append(f"[structure] {file}: {dotted}: a token cannot contain child {prop!r}")
            if group_type is None:
                errors.append(f"[structure] {file}: {dotted}: missing $type (set it on the token or a parent group)")
            ext = child.get("$extensions") or {}
            tokens[here] = Token(here, group_type, child["$value"], child.get("$description"), ext,
                                 child.get("$deprecated"), file, tier)
            if inherited_brandable:
                brandable.add(here)
        else:
            if not any(not k.startswith("$") for k in child):
                errors.append(f"[structure] {file}: {dotted}: group has no tokens (a token needs $value)")
            is_brandable = inherited_brandable or bool(((child.get("$extensions") or {}).get(NS) or {}).get("brandable"))
            _walk(child, here, group_type, file, tier, tokens, errors, brandable, is_brandable)


def load_layer(path, src, tier, slug, errors):
    data, error = load_json(path)
    rel = path.relative_to(src).as_posix()
    if error:
        errors.append(f"[structure] {error}")
        return Layer(rel, tier, slug, {}, OrderedDict(), set())
    if not isinstance(data, dict):
        errors.append(f"[structure] {rel}: root must be an object")
        return Layer(rel, tier, slug, {}, OrderedDict(), set())
    tokens, brandable = OrderedDict(), set()
    _walk(data, (), data.get("$type"), rel, tier, tokens, errors, brandable)
    meta = ((data.get("$extensions") or {}).get(NS)) or {}
    return Layer(rel, tier, slug, meta, tokens, brandable)


def load_source(src=SRC):
    src = Path(src)
    source = Source(src)
    errors = source.errors
    primitives = src / "primitives.tokens.json"
    if not primitives.is_file():
        errors.append(f"[structure] missing {primitives.name} in {src}")
        source.primitives = Layer("primitives.tokens.json", "primitive", "primitives", {}, OrderedDict(), set())
    else:
        source.primitives = load_layer(primitives, src, "primitive", "primitives", errors)
    mode_files = {p.name[len("semantic."):-len(".tokens.json")]: p for p in src.glob("semantic.*.tokens.json")}
    order = [m for m in MODE_ORDER if m in mode_files] + sorted(m for m in mode_files if m not in MODE_ORDER)
    for slug in order:
        if not NAME_RE.match(slug):
            errors.append(f"[structure] {mode_files[slug].name}: mode names must be lowercase and hyphenated")
            continue
        source.modes.append(load_layer(mode_files[slug], src, "semantic", slug, errors))
    if not source.mode(DEFAULT_MODE):
        errors.append(f"[structure] missing semantic.{DEFAULT_MODE}.tokens.json (the default mode)")
    components = src / "components.tokens.json"
    if components.is_file():
        source.components = load_layer(components, src, "component", "components", errors)
    else:
        source.components = Layer("components.tokens.json", "component", "components", {}, OrderedDict(), set())
    for path in sorted((src / "brands").glob("*.tokens.json")) if (src / "brands").is_dir() else []:
        slug = path.name[:-len(".tokens.json")]
        if not NAME_RE.match(slug):
            errors.append(f"[structure] brands/{path.name}: brand names must be lowercase and hyphenated")
            continue
        source.brands.append(load_layer(path, src, "brand", slug, errors))
    _check_layers(source)
    return source


def _check_layers(source):
    errors = source.errors
    prim = source.primitives.tokens
    for mode in source.modes:
        for path, token in mode.tokens.items():
            if path in prim:
                errors.append(f"[tier] {mode.file}: {token.dotted} redefines a primitive; semantic names must be new")
    for path, token in source.components.tokens.items():
        if path in prim or any(path in m.tokens for m in source.modes):
            errors.append(f"[tier] {source.components.file}: {token.dotted} redefines a primitive or semantic token")
    for brand in source.brands:
        for path, token in brand.tokens.items():
            base = prim.get(path)
            if base is None:
                errors.append(f"[brand] {brand.file}: {token.dotted} does not exist in primitives; brands may only "
                              "override brandable primitives")
            elif path not in source.primitives.brandable:
                errors.append(f"[brand] {brand.file}: {token.dotted} is not brandable (mark its group with "
                              f"$extensions.{NS}.brandable or remap a brandable token instead)")
            elif base.type != token.type:
                errors.append(f"[brand] {brand.file}: {token.dotted} has $type {token.type}, primitive has {base.type}")
    seen = {}
    for layer in [source.primitives] + source.modes + [source.components]:
        for path, token in layer.tokens.items():
            name = token.css_name
            if name in seen and seen[name] != path:
                errors.append(f"[structure] {token.file}: {token.dotted} and {'.'.join(seen[name])} both map to {name}")
            seen.setdefault(name, path)


def merged(source, brand=None, mode=DEFAULT_MODE):
    """Token view for one brand and mode: primitives, brand overrides, the mode's semantic set, components."""
    tokens = OrderedDict(source.primitives.tokens)
    layer = source.brand(brand) if brand else None
    if layer:
        for path, token in layer.tokens.items():
            if path in tokens:
                tokens[path] = token
    mode_layer = source.mode(mode)
    if mode_layer:
        tokens.update(mode_layer.tokens)
    tokens.update(source.components.tokens)
    return tokens


# ---------------------------------------------------------------------------
# Resolution and validation
# ---------------------------------------------------------------------------

class AliasError(ValueError):
    pass


def alias_target(value):
    if isinstance(value, str):
        match = ALIAS_RE.match(value.strip())
        if match:
            return tuple(match.group(1).split("."))
    return None


def resolve(value, tokens, chain=()):
    """Resolve aliases (whole values and composite sub-values). Raises AliasError on missing or circular refs."""
    target = alias_target(value)
    if target is not None:
        if target in chain:
            loop = " -> ".join(".".join(p) for p in chain + (target,))
            raise AliasError(f"circular alias: {loop}")
        if target not in tokens:
            raise AliasError(f"unresolved alias {{{'.'.join(target)}}}")
        return resolve(tokens[target].value, tokens, chain + (target,))
    if isinstance(value, str) and ("{" in value or "}" in value):
        raise AliasError(f"partial alias {value!r}: DTCG aliases must be the whole value")
    if isinstance(value, dict):
        return OrderedDict((k, resolve(v, tokens, chain)) for k, v in value.items())
    if isinstance(value, list):
        return [resolve(v, tokens, chain) for v in value]
    return value


def resolve_token(token, tokens):
    return resolve(token.value, tokens, (token.path,))


def resolved_type(token, tokens, seen=()):
    target = alias_target(token.value)
    if target is None or target not in tokens or target in seen:
        return token.type
    return resolved_type(tokens[target], tokens, seen + (token.path,))


def validate_value(type_, value):
    """Return an error string when a resolved literal value does not fit its DTCG $type."""
    if type_ == "color":
        if not isinstance(value, str) or not re.fullmatch(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})", value):
            return f"color must be #rrggbb or #rrggbbaa, got {value!r}"
    elif type_ == "dimension":
        if isinstance(value, dict):
            if not isinstance(value.get("value"), (int, float)) or value.get("unit") not in ("px", "rem", "em"):
                return f"dimension object needs numeric value and unit px|rem|em, got {value!r}"
        elif not isinstance(value, str) or not (DIMENSION_RE.match(value) or CSS_MATH_RE.match(value)):
            return f"dimension must be like '16px', '1rem' or a clamp()/calc() expression, got {value!r}"
    elif type_ == "duration":
        if isinstance(value, dict):
            if not isinstance(value.get("value"), (int, float)) or value.get("unit") not in ("ms", "s"):
                return f"duration object needs numeric value and unit ms|s, got {value!r}"
        elif not isinstance(value, str) or not DURATION_RE.match(value):
            return f"duration must be like '120ms', got {value!r}"
    elif type_ == "cubicBezier":
        if (not isinstance(value, list) or len(value) != 4 or
                not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in value)):
            return f"cubicBezier must be [x1, y1, x2, y2], got {value!r}"
        if not (0 <= value[0] <= 1 and 0 <= value[2] <= 1):
            return f"cubicBezier x values must be within 0..1, got {value!r}"
    elif type_ == "fontWeight":
        if isinstance(value, bool) or not ((isinstance(value, (int, float)) and 1 <= value <= 1000)
                                           or value in FONT_WEIGHT_KEYWORDS):
            return f"fontWeight must be 1-1000 or a keyword, got {value!r}"
    elif type_ == "fontFamily":
        if not (isinstance(value, str) and value) and not (
                isinstance(value, list) and value and all(isinstance(v, str) and v for v in value)):
            return f"fontFamily must be a string or a list of strings, got {value!r}"
    elif type_ == "number":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return f"number must be numeric, got {value!r}"
    elif type_ == "shadow":
        layers = value if isinstance(value, list) else [value]
        for layer in layers:
            if not isinstance(layer, dict):
                return f"shadow must be an object or a list of objects, got {value!r}"
            missing = [k for k in ("color", "offsetX", "offsetY", "blur", "spread") if k not in layer]
            if missing:
                return f"shadow layer missing {', '.join(missing)}"
            problem = validate_value("color", layer["color"])
            for key in ("offsetX", "offsetY", "blur", "spread"):
                problem = problem or validate_value("dimension", layer[key])
            if problem:
                return f"shadow layer: {problem}"
    return None


def validate_source(source):
    """Alias, type and value checks for every brand x mode view. Returns a list of error strings."""
    errors = []
    reported = set()
    for brand in source.brand_slugs():
        for mode in source.modes:
            tokens = merged(source, brand if brand != source.default_brand[0] else None, mode.slug)
            for path, token in tokens.items():
                key = (token.file, path)
                try:
                    value = resolve_token(token, tokens)
                except AliasError as exc:
                    if key not in reported:
                        errors.append(f"[alias] {token.file}: {token.dotted}: {exc}")
                        reported.add(key)
                    continue
                target = alias_target(token.value)
                if target is not None:
                    target_type = resolved_type(tokens[target], tokens)
                    if token.type and target_type and target_type != token.type and key not in reported:
                        errors.append(f"[alias] {token.file}: {token.dotted}: $type {token.type} aliases "
                                      f"{'.'.join(target)} of $type {target_type}")
                        reported.add(key)
                        continue
                problem = validate_value(token.type, value)
                if problem and key not in reported:
                    errors.append(f"[structure] {token.file}: {token.dotted}: {problem}")
                    reported.add(key)
    return errors


# ---------------------------------------------------------------------------
# CSS formatting
# ---------------------------------------------------------------------------

def css_enabled(token):
    return token.ext("css", True) is not False


def format_dimension(value):
    if isinstance(value, dict):
        value = f"{format_number(value['value'])}{value['unit']}"
    if re.fullmatch(r"-?0+(\.0+)?(px|rem|em|ch|%|vw|vh)", value):
        return "0"
    return value


def format_font_family(value):
    names = value if isinstance(value, list) else [value]
    out = []
    for name in names:
        if name in GENERIC_FONTS or re.fullmatch(r"-?[A-Za-z_][A-Za-z0-9_-]*", name):
            out.append(name)
        else:
            out.append('"' + name.replace('"', '\\"') + '"')
    return ", ".join(out)


def css_literal(type_, value):
    """Format a fully resolved value as CSS."""
    if type_ == "color":
        return value.lower()
    if type_ == "dimension":
        return format_dimension(value)
    if type_ == "duration":
        if isinstance(value, dict):
            return f"{format_number(value['value'])}{value['unit']}"
        return value
    if type_ == "cubicBezier":
        if list(value) == [0, 0, 1, 1]:
            return "linear"
        return "cubic-bezier(" + ", ".join(format_number(v) for v in value) + ")"
    if type_ in ("fontWeight", "number"):
        return format_number(value) if not isinstance(value, str) else value
    if type_ == "fontFamily":
        return format_font_family(value)
    if type_ == "shadow":
        layers = value if isinstance(value, list) else [value]
        return ", ".join(_shadow_layer(layer, lambda key, v: css_literal("color" if key == "color" else "dimension", v))
                         for layer in layers)
    return str(value)


def _shadow_layer(layer, fmt):
    parts = ["inset"] if layer.get("inset") else []
    parts += [fmt(k, layer[k]) for k in ("offsetX", "offsetY", "blur", "spread")]
    parts.append(fmt("color", layer["color"]))
    return " ".join(parts)


def css_value(token, tokens):
    """CSS for one token: aliases become var() references so brand and mode overrides cascade."""
    def ref_or_literal(type_, raw):
        target = alias_target(raw)
        if target is not None:
            target_token = tokens[target]
            if css_enabled(target_token):
                return f"var({target_token.css_name})"
            return css_literal(type_, resolve(raw, tokens))
        return css_literal(type_, raw)

    if alias_target(token.value) is not None:
        return ref_or_literal(token.type, token.value)
    if token.type == "shadow":
        layers = token.value if isinstance(token.value, list) else [token.value]
        return ", ".join(_shadow_layer(layer, lambda key, v: ref_or_literal("color" if key == "color" else "dimension", v))
                         for layer in layers)
    return css_literal(token.type, token.value)


def css_resolved(token, tokens):
    return css_literal(token.type, resolve_token(token, tokens))


def _declarations(tokens, view, indent="  "):
    lines = []
    group = None
    for token in tokens:
        if not css_enabled(token):
            continue
        top = token.path[0] if token.path[0] != "color" or len(token.path) < 3 else f"{token.path[0]}-{token.path[1]}"
        if top != group:
            if group is not None:
                lines.append("")
            lines.append(f"{indent}/* {top} */")
            group = top
        comment = ""
        oklch = token.ext("oklch")
        if oklch:
            comment = f" /* {oklch} */"
        if token.deprecated:
            note = token.deprecated if isinstance(token.deprecated, str) else "deprecated"
            comment += f" /* deprecated: {note} */"
        lines.append(f"{indent}{token.css_name}: {css_value(token, view)};{comment}")
    return lines


def build_css(source):
    default_brand = source.default_brand
    lines = [
        "/*",
        " * Visual Design Kit design tokens. Generated by library/scripts/tokens.py build; do not edit by hand.",
        " * Source: library/tokens/src/*.tokens.json (W3C DTCG). Contract: design-kit-authoring/references/token-contract.md",
        f" * Brands: {default_brand[0]} (default)" + "".join(f", {b.slug} ([data-brand=\"{b.slug}\"])" for b in source.brands),
        " * Modes: " + ", ".join(f"{m.slug}" + (" (default)" if m.slug == DEFAULT_MODE else f" ([data-theme=\"{m.slug}\"])")
                                for m in source.modes),
        " * Theme scope: set data-theme and data-brand on <html>, or both on any wrapper element.",
        " */",
        "",
    ]
    light = source.mode(DEFAULT_MODE)
    view = merged(source, None, DEFAULT_MODE)
    lines.append(":root {")
    lines += _declarations(source.primitives.tokens.values(), view)
    lines.append("}")
    for mode in source.modes:
        mode_view = merged(source, None, mode.slug)
        scheme = mode.meta.get("colorScheme", "dark" if mode.slug == "dark" else "light")
        selector = f':root,\n[data-theme="{mode.slug}"]' if mode is light else f'[data-theme="{mode.slug}"]'
        lines += ["", f"/* Semantic: {mode.name} */", selector + " {", f"  color-scheme: {scheme};"]
        lines += _declarations(mode.tokens.values(), mode_view)
        lines.append("}")
    dark = source.mode("dark")
    if dark:
        lines += ["", "/* System dark mode when no theme is forced (data-theme=\"light\" or another theme opts out). */",
                  "@media (prefers-color-scheme: dark) {", "  :root:not([data-theme]) {", "    color-scheme: dark;"]
        lines += _declarations(dark.tokens.values(), merged(source, None, "dark"), indent="    ")
        lines += ["  }", "}"]
    high = source.mode("high-contrast")
    if high:
        lines += ["", "/* System \"more contrast\" when no theme is forced; wins over system dark (placed later). */",
                  "@media (prefers-contrast: more) {", "  :root:not([data-theme]) {", "    color-scheme: light;"]
        lines += _declarations(high.tokens.values(), merged(source, None, "high-contrast"), indent="    ")
        lines += ["  }", "}"]
    for brand in source.brands:
        brand_view = merged(source, brand.slug, DEFAULT_MODE)
        lines += ["", f"/* Brand: {brand.name} */", f'[data-brand="{brand.slug}"] {{']
        lines += _declarations(brand.tokens.values(), brand_view)
        lines.append("}")
    if source.components.tokens:
        lines += ["", "/* Components: re-declared on every theme scope so nested data-theme/data-brand wrappers work. */",
                  ":root,", "[data-theme],", "[data-brand] {"]
        lines += _declarations(source.components.tokens.values(), view)
        lines.append("}")
    durations = [t for t in source.primitives.tokens.values()
                 if t.type == "duration" and css_enabled(t) and t.path[-1] != "instant"]
    if durations:
        lines += ["", "/* Reduced motion: every duration except instant collapses to 0.01ms (transitionend still fires). */",
                  "@media (prefers-reduced-motion: reduce) {", "  :root {"]
        lines += [f"    {t.css_name}: 0.01ms;" for t in durations]
        lines += ["  }", "}"]
    return "\n".join(lines) + "\n"


def build_tailwind(source):
    view = merged(source, None, DEFAULT_MODE)
    by_css = {t.css_name: t for t in view.values()}
    lines = [
        "/*",
        " * Tailwind CSS v4 theme for the Visual Design Kit tokens. Generated by tokens.py build; do not edit.",
        " *",
        " *   @import \"tailwindcss\";",
        " *   @import \"<path>/tokens/dist/tokens.css\";     values, modes, brands (required)",
        " *   @import \"<path>/tokens/dist/tailwind.css\";   utility names (this file)",
        " *",
        " * \"inline reference\": utilities point straight at the token variables (so data-theme and data-brand",
        " * switch them at runtime) and Tailwind emits no duplicate variables. The resets remove Tailwind's default",
        " * palette, type scale, radii, shadows and easings, so off-system values (bg-purple-500, text-7xl) fail",
        " * to compile. Delete a reset line to get Tailwind's defaults back for that namespace.",
        " */",
        "",
        "@theme inline reference {",
    ]
    lines += [f"  {reset}: initial;" for reset in TAILWIND_RESETS]
    for comment, pairs in TAILWIND_GROUPS:
        lines += ["", f"  /* {comment} */"]
        if comment.startswith("Font sizes"):
            for name in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"):
                lines.append(f"  --text-{name}: var(--font-size-{name});")
                lines.append(f"  --text-{name}--line-height: var(--line-height-{FONT_SIZE_LEADING[name]});")
            lines.append("  --text-base: var(--font-size-md);")
            lines.append(f"  --text-base--line-height: var(--line-height-{FONT_SIZE_LEADING['md']});")
            continue
        for theme_var, token_var in pairs:
            if token_var not in by_css:
                raise ValueError(f"tailwind mapping {theme_var} points at missing token {token_var}")
            lines.append(f"  {theme_var}: var({token_var});")
    lines += ["", "  /* Containers: max-w-sm ... max-w-xl and @sm ... @xl container queries (literal: queries cannot use var()) */"]
    for name in ("sm", "md", "lg", "xl"):
        lines.append(f"  --container-{name}: {css_resolved(by_css[f'--container-{name}'], view)};")
    lines += ["", "  /* Breakpoints: sm: md: lg: xl: 2xl: (from breakpoint.* tokens, in rem so they follow browser zoom) */"]
    for path, token in source.primitives.tokens.items():
        if path[0] == "breakpoint":
            px = _px(resolve_token(token, view))
            lines.append(f"  --breakpoint-{path[-1]}: {format_number(px / ROOT_PX)}rem; /* {format_number(px)}px */")
    lines += ["}", ""]
    lines += [
        "/* dark: follows the tokens: data-theme=\"dark\", or system dark when no theme is forced and \"more contrast\" is off. */",
        "@custom-variant dark {",
        "  &:where([data-theme=\"dark\"], [data-theme=\"dark\"] *) {",
        "    @slot;",
        "  }",
        "  @media (prefers-color-scheme: dark) and (not (prefers-contrast: more)) {",
        "    &:where(:root:not([data-theme]), :root:not([data-theme]) *) {",
        "      @slot;",
        "    }",
        "  }",
        "}",
        "",
        "/* hc: high-contrast theme, forced or from the system \"more contrast\" setting. */",
        "@custom-variant hc {",
        "  &:where([data-theme=\"high-contrast\"], [data-theme=\"high-contrast\"] *) {",
        "    @slot;",
        "  }",
        "  @media (prefers-contrast: more) {",
        "    &:where(:root:not([data-theme]), :root:not([data-theme]) *) {",
        "      @slot;",
        "    }",
        "  }",
        "}",
    ]
    return "\n".join(lines) + "\n"


def _px(value):
    if isinstance(value, dict):
        number, unit = float(value["value"]), value["unit"]
    else:
        match = DIMENSION_RE.match(value)
        if not match:
            return None
        number, unit = float(value[:-len(match.group(3))]), match.group(3)
    if unit == "px":
        return number
    if unit == "rem":
        return number * ROOT_PX
    return None


# ---------------------------------------------------------------------------
# JSON outputs
# ---------------------------------------------------------------------------

def dump_json(data):
    """Pretty JSON with short scalar arrays kept on one line. Deterministic."""
    def render(value, level):
        pad = "  " * level
        if isinstance(value, dict):
            if not value:
                return "{}"
            items = [f'{pad}  {json.dumps(k, ensure_ascii=False)}: {render(v, level + 1)}' for k, v in value.items()]
            return "{\n" + ",\n".join(items) + f"\n{pad}}}"
        if isinstance(value, list):
            if not value:
                return "[]"
            if all(not isinstance(v, (dict, list)) for v in value):
                inline = "[" + ", ".join(json.dumps(v, ensure_ascii=False) for v in value) + "]"
                if len(inline) <= 100:
                    return inline
            items = [f"{pad}  {render(v, level + 1)}" for v in value]
            return "[\n" + ",\n".join(items) + f"\n{pad}]"
        return json.dumps(value, ensure_ascii=False)
    return render(data, 0) + "\n"


def _themes(source):
    for brand in source.brand_slugs():
        for mode in source.modes:
            yield brand, mode.slug, merged(source, brand if brand != source.default_brand[0] else None, mode.slug)


def build_resolved(source):
    default_slug, default_name = source.default_brand
    meta_tokens = OrderedDict()
    union = OrderedDict()
    for _, _, view in _themes(source):
        for path, token in view.items():
            union.setdefault(path, token)
    for path, token in union.items():
        entry = OrderedDict([("type", token.type), ("tier", token.tier)])
        if css_enabled(token):
            entry["css"] = token.css_name
        if token.description:
            entry["description"] = token.description
        meta_tokens[token.dotted] = entry
    values = OrderedDict()
    for brand, mode, view in _themes(source):
        values.setdefault(brand, OrderedDict())[mode] = OrderedDict(
            (t.dotted, resolve_token(t, view)) for t in view.values())
    return dump_json(OrderedDict([
        ("format", "visual-design-kit/tokens-resolved"),
        ("formatVersion", 1),
        ("description", "Every token fully resolved for each brand and mode. values[brand][mode][token] is the DTCG "
                        "$value with aliases replaced (dimensions keep their unit; shadows are lists of layers)."),
        ("defaultBrand", default_slug),
        ("defaultMode", DEFAULT_MODE),
        ("brands", OrderedDict([(default_slug, {"name": default_name})] +
                               [(b.slug, {"name": b.name}) for b in source.brands])),
        ("modes", OrderedDict((m.slug, OrderedDict([("name", m.name), ("colorScheme", m.meta.get(
            "colorScheme", "dark" if m.slug == "dark" else "light"))])) for m in source.modes)),
        ("tokens", meta_tokens),
        ("values", values),
    ]))


FIGMA_SCOPES = [
    (("color", "bg"), ["FRAME_FILL", "SHAPE_FILL"]),
    (("color", "fg"), ["TEXT_FILL", "SHAPE_FILL", "STROKE_COLOR"]),
    (("color", "border"), ["STROKE_COLOR"]),
    (("color", "accent", "fg"), ["TEXT_FILL", "SHAPE_FILL", "STROKE_COLOR"]),
    (("color", "accent", "subtle"), ["FRAME_FILL", "SHAPE_FILL"]),
    (("color", "accent", "default"), ["FRAME_FILL", "SHAPE_FILL", "STROKE_COLOR"]),
    (("color", "accent", "hover"), ["FRAME_FILL", "SHAPE_FILL", "STROKE_COLOR"]),
    (("color", "accent", "active"), ["FRAME_FILL", "SHAPE_FILL", "STROKE_COLOR"]),
    (("color", "focus-ring"), ["STROKE_COLOR", "EFFECT_COLOR"]),
    (("color", "overlay-scrim"), ["FRAME_FILL", "SHAPE_FILL"]),
    (("color", "alpha"), ["EFFECT_COLOR"]),
    (("space",), ["GAP"]),
    (("radius",), ["CORNER_RADIUS"]),
    (("border-width",), ["STROKE_FLOAT"]),
    (("font", "size"), ["FONT_SIZE"]),
    (("font", "weight"), ["FONT_WEIGHT"]),
    (("font", "family"), ["FONT_FAMILY"]),
    (("size",), ["WIDTH_HEIGHT"]),
    (("container",), ["WIDTH_HEIGHT"]),
] + [((("color", s, "fg")), ["TEXT_FILL", "SHAPE_FILL", "STROKE_COLOR"]) for s in STATUS] + [
    ((("color", s, "bg")), ["FRAME_FILL", "SHAPE_FILL"]) for s in STATUS] + [
    ((("color", s, "border")), ["STROKE_COLOR"]) for s in STATUS]
FIGMA_SKIPPED = OrderedDict([
    ("line-height", "unitless multipliers; Figma binds line height in px or sets percent on text styles. Use 110/125/150/165%."),
    ("letter-spacing", "em values; set them as percent on Figma text styles (-2%, 0%, 1%, 6%)."),
    ("measure", "ch units have no Figma equivalent."),
    ("gutter", "clamp() is CSS-only; use 16-32px layout grid gutters."),
    ("z", "stacking order has no Figma variable."),
    ("breakpoint", "media-query values; used for frame widths only."),
    ("shadow", "composite values; build Figma effect styles from tokens.resolved.json (values differ per mode)."),
])


def _figma_scopes(path):
    best = None
    for prefix, scopes in FIGMA_SCOPES:
        if path[:len(prefix)] == prefix and (best is None or len(prefix) > len(best[0])):
            best = (prefix, scopes)
    return list(best[1]) if best else []


def _figma_kind(token):
    if not css_enabled(token) and token.path[0] != "breakpoint":
        return None
    if token.path[0] in FIGMA_SKIPPED:
        return None
    return {"color": "COLOR", "dimension": "FLOAT", "fontWeight": "FLOAT", "fontFamily": "STRING",
            "duration": "TIMING", "cubicBezier": "EASING"}.get(token.type)


def _figma_literal(kind, type_, value):
    if kind == "COLOR":
        r, g, b, a = color_tools.parse_hex(value)
        return OrderedDict([("r", round(r, 6)), ("g", round(g, 6)), ("b", round(b, 6)), ("a", round(a, 6))])
    if kind == "FLOAT":
        if type_ == "fontWeight":
            return value if isinstance(value, (int, float)) else 400
        return _px(value)
    if kind == "STRING":
        return value[0] if isinstance(value, list) else value
    if kind == "TIMING":
        if isinstance(value, dict):
            number, unit = float(value["value"]), value["unit"]
        else:
            match = DURATION_RE.match(value)
            number, unit = float(value[:-len(match.group(3))]), match.group(3)
        return round(number / 1000 if unit == "ms" else number, 6)
    if kind == "EASING":
        if list(value) == [0, 0, 1, 1]:
            return {"type": "LINEAR"}
        return OrderedDict([("type", "CUSTOM_CUBIC_BEZIER"), ("easingFunctionCubicBezier", OrderedDict(
            zip(("x1", "y1", "x2", "y2"), value)))])
    return value


def _figma_value(token, view, collection_of):
    kind = _figma_kind(token)
    target = alias_target(token.value)
    if target is not None:
        target_token = view[target]
        if _figma_kind(target_token) == kind and collection_of(target_token):
            return OrderedDict([("alias", OrderedDict([("collection", collection_of(target_token)),
                                                       ("name", "/".join(target))]))])
    value = resolve_token(token, view)
    if kind == "FLOAT" and _figma_literal(kind, token.type, value) is None:
        return None
    return _figma_literal(kind, token.type, value)


def build_figma(source):
    default_slug, default_name = source.default_brand
    brand_names = [default_name] + [b.name for b in source.brands]
    brand_slugs = source.brand_slugs()

    def collection_of(token):
        if _figma_kind(token) is None:
            return None
        return {"primitive": "Primitives", "brand": "Primitives", "semantic": "Semantic"}.get(token.tier)

    def variable(token, values):
        entry = OrderedDict([("name", "/".join(token.path)), ("type", _figma_kind(token))])
        if entry["type"] not in ("TIMING", "EASING"):
            entry["scopes"] = _figma_scopes(token.path) if token.path in source.primitives.brandable or \
                token.tier != "primitive" or token.path[0] != "color" or token.path[1] == "alpha" else []
        if css_enabled(token):
            entry["codeSyntax"] = OrderedDict([("WEB", f"var({token.css_name})")])
        if token.description:
            entry["description"] = token.description
        entry["valuesByMode"] = values
        return entry

    primitives = []
    for path, token in source.primitives.tokens.items():
        if _figma_kind(token) is None:
            continue
        values = OrderedDict()
        for slug, name in zip(brand_slugs, brand_names):
            view = merged(source, slug if slug != default_slug else None, DEFAULT_MODE)
            value = _figma_value(view[path], view, collection_of)
            if value is None:
                break
            values[name] = value
        else:
            primitives.append(variable(token, values))
    semantic = []
    for path, token in source.mode(DEFAULT_MODE).tokens.items():
        if _figma_kind(token) is None:
            continue
        values = OrderedDict()
        for mode in source.modes:
            view = merged(source, None, mode.slug)
            if path in view:
                values[mode.name] = _figma_value(view[path], view, collection_of)
        semantic.append(variable(token, values))
    return dump_json(OrderedDict([
        ("format", "visual-design-kit/figma-variables"),
        ("formatVersion", 1),
        ("description", "Figma variable collections generated from library/tokens/src. Import with "
                        "library/tokens/figma-import.js (tokens.py figma-script prints a ready-to-run use_figma script). "
                        "COLOR values are 0-1 RGBA, FLOAT values are px (rem x 16), TIMING values are seconds. "
                        "An alias value names a variable by collection and slash path."),
        ("collections", [
            OrderedDict([("name", "Primitives"), ("modes", brand_names),
                         ("description", "Raw ramps and scales. Modes are brands: set the Primitives mode on a frame "
                                         "to switch brand."), ("variables", primitives)]),
            OrderedDict([("name", "Semantic"), ("modes", [m.name for m in source.modes]),
                         ("description", "Roles that change per theme. Modes are themes; values alias Primitives."),
                         ("variables", semantic)]),
        ]),
        ("notExported", FIGMA_SKIPPED),
    ]))


def build_outputs(source):
    return OrderedDict([
        ("tokens.css", build_css(source)),
        ("tailwind.css", build_tailwind(source)),
        ("tokens.resolved.json", build_resolved(source)),
        ("figma-variables.json", build_figma(source)),
    ])


# ---------------------------------------------------------------------------
# Lint
# ---------------------------------------------------------------------------

def lint(source):
    """Return {"errors": [...], "warnings": [...], "stats": {...}}."""
    errors = list(source.errors)
    warnings = list(source.warnings)
    errors += validate_source(source)
    broken = any(e.startswith(("[alias]", "[structure]")) for e in errors)

    # Contract: names and values.
    default_view = merged(source, None, DEFAULT_MODE)
    emitted = OrderedDict()
    for token in default_view.values():
        if css_enabled(token):
            emitted[token.css_name] = token
    for name, expected in CONTRACT.items():
        token = emitted.get(name)
        if token is None:
            close = difflib.get_close_matches(name, [n for n in emitted if n not in CONTRACT], n=1, cutoff=0.75)
            hint = (f" (renamed? found {close[0]}; keep {name} as a deprecated alias for one minor version)"
                    if close else "")
            errors.append(f"[contract] missing contract variable {name}{hint}")
            continue
        if expected is not None and not broken:
            actual = css_resolved(token, default_view)
            if actual.replace(" ", "") != expected.replace(" ", ""):
                errors.append(f"[contract] {name} is {actual}, contract says {expected}")
    for name, expected in CONTRACT_BREAKPOINTS.items():
        token = default_view.get(("breakpoint", name))
        if token is None:
            errors.append(f"[contract] missing breakpoint.{name} ({expected})")
        elif css_enabled(token):
            errors.append(f"[contract] breakpoint.{name} must not be emitted as a CSS variable "
                          f"(set $extensions.{NS}.css to false)")
        elif not broken and css_resolved(token, default_view) != expected:
            errors.append(f"[contract] breakpoint.{name} is {css_resolved(token, default_view)}, contract says {expected}")
    for mode in source.modes:
        for path in MODE_PATHS:
            if path not in mode.tokens:
                errors.append(f"[contract] {mode.file}: missing semantic token {'.'.join(path)}")

    # Tiers.
    contract_names = set(CONTRACT)
    for mode in source.modes:
        for token in mode.tokens.values():
            for target in _alias_targets(token.value):
                ref = default_view.get(target) or merged(source, None, mode.slug).get(target)
                if ref is not None and ref.tier == "component":
                    errors.append(f"[tier] {mode.file}: {token.dotted} aliases component token {'.'.join(target)}")
            if not _alias_targets(token.value):
                errors.append(f"[tier] {mode.file}: {token.dotted} is a literal; semantic tokens must alias primitives")
    for token in source.components.tokens.values():
        targets = _alias_targets(token.value)
        if not targets:
            errors.append(f"[tier] {source.components.file}: {token.dotted} is a literal; component tokens must alias "
                          "semantic tokens")
        for target in targets:
            ref = default_view.get(target)
            if ref is None:
                continue
            if ref.tier == "primitive" and ref.css_name not in contract_names:
                errors.append(f"[tier] {source.components.file}: {token.dotted} aliases primitive {ref.dotted}; "
                              "components may alias semantic tokens and public scale tokens only")
    for brand in source.brands:
        for token in brand.tokens.values():
            if not _alias_targets(token.value):
                warnings.append(f"[brand] {brand.file}: {token.dotted} is a literal; prefer remapping to a raw ramp step")

    # Ramp recipes.
    errors += check_ramps(source)

    # Contrast in every brand x mode.
    pairs_checked = 0
    if not broken:
        for brand, mode, view in _themes(source):
            theme = f"{brand}/{mode}"
            for fg, bgs, minimum, origin, purpose, hc_min in GUARANTEES:
                if mode == "high-contrast" and hc_min:
                    minimum = max(minimum, hc_min)
                for bg in bgs:
                    pairs_checked += 1
                    problem = _check_pair(view, fg, bg, minimum)
                    if problem:
                        errors.append(f"[contrast] {theme}: {problem} ({origin}: {purpose})")
            for token in view.values():
                for rule in token.ext("contrast", []) or []:
                    pairs_checked += 1
                    bg = alias_target(rule.get("bg", ""))
                    if bg is None:
                        errors.append(f"[structure] {token.file}: {token.dotted}: contrast rule needs bg as an alias")
                        continue
                    problem = _check_pair(view, token.dotted, ".".join(bg), float(rule.get("min", 4.5)))
                    if problem:
                        errors.append(f"[contrast] {theme}: {problem} ({token.file} rule)")
    for token in default_view.values():
        if token.deprecated:
            warnings.append(f"[deprecated] {token.file}: {token.dotted}: {token.deprecated}")
    stats = OrderedDict([
        ("tokens", len({p for _, _, v in _themes(source) for p in v})),
        ("brands", source.brand_slugs()),
        ("modes", [m.slug for m in source.modes]),
        ("contrast_pairs_checked", pairs_checked),
    ])
    return {"errors": errors, "warnings": warnings, "stats": stats}


def _alias_targets(value):
    target = alias_target(value)
    if target is not None:
        return [target]
    if isinstance(value, dict):
        return [t for v in value.values() for t in _alias_targets(v)]
    if isinstance(value, list):
        return [t for v in value for t in _alias_targets(v)]
    return []


def _check_pair(view, fg, bg, minimum):
    fg_path, bg_path = tuple(fg.split(".")), tuple(bg.split("."))
    if fg_path not in view or bg_path not in view:
        missing = fg if fg_path not in view else bg
        return f"{fg} on {bg}: {missing} is not defined"
    fg_hex, bg_hex = resolve_token(view[fg_path], view), resolve_token(view[bg_path], view)
    if len(fg_hex) != 7 or len(bg_hex) != 7:
        return f"{fg} on {bg}: contrast pairs must be opaque colors ({fg_hex} on {bg_hex})"
    ratio = color_tools.contrast_ratio(fg_hex, bg_hex)
    if ratio + 1e-9 < minimum:
        return f"{fg} {fg_hex} on {bg} {bg_hex} is {ratio:.2f}:1, needs {format_number(minimum)}:1"
    return None


# ---------------------------------------------------------------------------
# Ramps
# ---------------------------------------------------------------------------

def _ramp_groups(node, path=()):
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        recipe = ((child.get("$extensions") or {}).get(NS) or {}).get("ramp")
        if recipe:
            yield path + (key,), child, recipe
        elif "$value" not in child:
            yield from _ramp_groups(child, path + (key,))


def generate_ramp(recipe):
    return color_tools.ramp(
        recipe["hue"], recipe["chroma"], steps=recipe.get("steps", color_tools.DEFAULT_STEPS),
        l_max=recipe.get("lMax", color_tools.L_MAX), l_min=recipe.get("lMin", color_tools.L_MIN),
        floor=recipe.get("floor", color_tools.CHROMA_FLOOR), exponent=recipe.get("taper", color_tools.CHROMA_TAPER),
        hue_shift=recipe.get("hueShift", 0.0))


def regenerate_ramps(data):
    """Rewrite ramp groups in a primitives tree from their recipes. Returns the list of changed token paths."""
    changed = []
    for path, group, recipe in _ramp_groups(data):
        for item in generate_ramp(recipe):
            key = str(item["step"])
            token = group.get(key)
            if not isinstance(token, dict):
                token = OrderedDict()
                group[key] = token
            ext = token.setdefault("$extensions", OrderedDict()).setdefault(NS, OrderedDict())
            if token.get("$value") != item["hex"] or ext.get("oklch") != item["oklch"]:
                changed.append(".".join(path + (key,)))
            token["$value"] = item["hex"]
            ext["oklch"] = item["oklch"]
    return changed


def check_ramps(source):
    path = source.src / "primitives.tokens.json"
    data, error = load_json(path)
    if error or not isinstance(data, dict):
        return []
    errors = []
    for group_path, group, recipe in _ramp_groups(data):
        try:
            generated = generate_ramp(recipe)
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"[ramp] primitives.tokens.json: {'.'.join(group_path)}: bad ramp recipe: {exc}")
            continue
        expected_keys = {str(item["step"]) for item in generated}
        for key in group:
            if not key.startswith("$") and key not in expected_keys:
                errors.append(f"[ramp] primitives.tokens.json: {'.'.join(group_path + (key,))} is not a step of its "
                              "ramp recipe")
        for item in generated:
            token = group.get(str(item["step"]))
            dotted = ".".join(group_path + (str(item["step"]),))
            if not isinstance(token, dict):
                errors.append(f"[ramp] primitives.tokens.json: {dotted} is missing; run tokens.py ramps --write")
            elif str(token.get("$value", "")).lower() != item["hex"]:
                errors.append(f"[ramp] primitives.tokens.json: {dotted} is {token.get('$value')} but its recipe gives "
                              f"{item['hex']}; run tokens.py ramps --write, or delete the recipe to hand-tune")
    return errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _fatal(source):
    problems = [e for e in source.errors + validate_source(source) if e.startswith(("[alias]", "[structure]"))]
    return problems


def cmd_build(args):
    source = load_source(args.src)
    problems = _fatal(source)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        print("build aborted: fix the structure and alias errors above (tokens.py lint shows everything)",
              file=sys.stderr)
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, text in build_outputs(source).items():
        target = out / name
        with open(target, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        print(f"wrote {target} ({len(text.encode('utf-8'))} bytes)")
    return 0


def cmd_lint(args):
    source = load_source(args.src)
    report = lint(source)
    if args.json:
        print(json.dumps(report, indent=2))
        return 1 if report["errors"] else 0
    print(f"tokens lint: {Path(args.src).resolve()}")
    for warning in report["warnings"]:
        print(f"  warning {warning}")
    for error in report["errors"]:
        print(f"  ERROR {error}")
    stats = report["stats"]
    summary = (f"{stats['tokens']} tokens, brands {', '.join(stats['brands'])}, modes {', '.join(stats['modes'])}, "
               f"{stats['contrast_pairs_checked']} contrast pairs checked")
    if report["errors"]:
        print(f"FAILED: {len(report['errors'])} error(s), {len(report['warnings'])} warning(s); {summary}")
        return 1
    print(f"OK: 0 errors, {len(report['warnings'])} warning(s); {summary}")
    return 0


def cmd_check(args):
    source = load_source(args.src)
    problems = _fatal(source)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    out = Path(args.out)
    stale = []
    for name, text in build_outputs(source).items():
        target = out / name
        if not target.is_file():
            stale.append(f"missing {target}")
        elif target.read_bytes() != text.encode("utf-8"):
            stale.append(f"stale {target}")
    for line in stale:
        print(line)
    if stale:
        print("dist is out of date: run python3 tokens.py build")
        return 1
    print(f"dist is up to date ({len(OUTPUTS)} files)")
    return 0


def cmd_ramps(args):
    path = Path(args.src) / "primitives.tokens.json"
    data, error = load_json(path)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    changed = regenerate_ramps(data)
    for dotted in changed:
        print(f"{'updated' if args.write else 'would update'} {dotted}")
    if args.write and changed:
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(dump_json(data))
    if not changed:
        print("ramps match their recipes")
    return 0


def cmd_figma_script(args):
    source = load_source(args.src)
    problems = _fatal(source)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    data = build_figma(source)
    print("// Generated by tokens.py figma-script: paste into the Figma MCP use_figma tool (design file).")
    print("const DATA = " + data.rstrip("\n") + ";")
    print(FIGMA_IMPORT_JS.read_text(encoding="utf-8"), end="")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func, help_text in (("build", cmd_build, "write dist/"), ("lint", cmd_lint, "validate tokens"),
                                  ("check", cmd_check, "fail when dist/ is stale"),
                                  ("ramps", cmd_ramps, "regenerate ramps from recipes"),
                                  ("figma-script", cmd_figma_script, "print a use_figma import script")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--src", default=str(SRC), help="token source directory (default: library/tokens/src)")
        if name in ("build", "check"):
            p.add_argument("--out", default=str(DIST), help="output directory (default: library/tokens/dist)")
        if name == "lint":
            p.add_argument("--json", action="store_true")
        if name == "ramps":
            p.add_argument("--write", action="store_true", help="rewrite primitives.tokens.json")
        p.set_defaults(func=func)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
