#!/usr/bin/env python3
"""List every volatile claim in the plugin that is marked for verification.

Version-Timestamp: 2026-10-20 05:10:00 UTC

Atlas entries and skill references mark volatile facts (regulation dates,
platform specs, social formats, payment coverage, statistics) with the word
"verify". This script collects those lines, groups them by topic and reports
how old each file's Version-Timestamp is, so a reviewer can re-check the
primary sources in priority order. Standard library only; Python 3.9+.

    python3 tools/spec_radar.py                 # Markdown report on stdout
    python3 tools/spec_radar.py --json          # machine-readable
    python3 tools/spec_radar.py --topic regulation --older-than 90
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "visual-design-studio"
SCAN_DIRS = ("skills", "library/atlas")

MARKER = re.compile(r"\bverify\b", re.IGNORECASE)
# Instructions to the reader ("verify the build", "verify that ...") are process
# steps, not volatile facts.
PROCESS = re.compile(
    r"(?:\bway to verify|\bverify (?:that|the build|it\b|each|your|with|before|contrast|the pinned|the payload))",
    re.IGNORECASE,
)
STAMP = re.compile(
    r"version[-_ ]timestamp\"?\s*:?\s*\"?(\d{4}-\d{2}-\d{2})", re.IGNORECASE
)

# First match wins, so order runs from most to least specific.
TOPICS = (
    ("regulation", r"\b(law|act\b|regulat|directive|gdpr|pdpl|lgpd|ccpa|consent|vat\b|tax|"
                   r"compliance|statute|ordinance|ftc|fca|sec\b|eaa\b|ada\b|age verification|"
                   r"in force|enforceable|mandator|required by|labell?ing)"),
    ("payments", r"\b(pay|payment|pix|upi|card|wallet|installment|bnpl|mercado pago|alipay|wechat pay)"),
    ("platform-specs", r"\b(app store|play store|google play|ios|ipados|android|visionos|watchos|"
                       r"screenshot|icon|hig\b|material|figma|safe (?:zone|area)|px\b|pixels|"
                       r"instagram|tiktok|youtube|linkedin|meta\b|outlook|gmail|email client|"
                       r"browser|safari|chrome|css|api)"),
    ("sources", r"\b(edition|latest release|style guide|guidelines? (?:version|update))"),
    ("statistics", r"(\d+(?:\.\d+)?\s?%|\bshare\b|\bpew\b|\bsurvey|\breport\b|\bpercent|\bmillion|\bbillion)"),
)
TOPIC_RES = tuple((name, re.compile(rx, re.IGNORECASE)) for name, rx in TOPICS)


def classify(text):
    for name, rx in TOPIC_RES:
        if rx.search(text):
            return name
    return "other"


def file_stamp(text):
    match = STAMP.search(text)
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(1))
    except ValueError:
        return None


def collect(plugin_root=PLUGIN, today=None):
    today = today or dt.datetime.now(dt.timezone.utc).date()
    items = []
    for sub in SCAN_DIRS:
        base = plugin_root / sub
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            stamp = file_stamp(text)
            age = (today - stamp).days if stamp else None
            for number, line in enumerate(text.splitlines(), 1):
                if not MARKER.search(line) or PROCESS.search(line):
                    continue
                claim = line.strip().lstrip("-*| ").strip()
                items.append({
                    "file": path.relative_to(plugin_root).as_posix(),
                    "line": number,
                    "topic": classify(claim),
                    "stamp": stamp.isoformat() if stamp else None,
                    "age_days": age,
                    "claim": claim,
                })
    return items


def render_markdown(items, today):
    lines = [
        "# Spec radar report",
        "",
        "Generated: {} by `tools/spec_radar.py`".format(today.isoformat()),
        "",
        "| Topic | Claims | Files |",
        "| --- | --- | --- |",
    ]
    topics = [name for name, _ in TOPICS] + ["other"]
    for topic in topics:
        group = [i for i in items if i["topic"] == topic]
        if group:
            lines.append("| {} | {} | {} |".format(topic, len(group), len({i["file"] for i in group})))
    lines.append("| total | {} | {} |".format(len(items), len({i["file"] for i in items})))
    for topic in topics:
        group = [i for i in items if i["topic"] == topic]
        if not group:
            continue
        lines += ["", "## {}".format(topic), ""]
        # Oldest files first: they are the most likely to be out of date.
        group.sort(key=lambda i: (-(i["age_days"] or 10 ** 6), i["file"], i["line"]))
        for item in group:
            claim = item["claim"]
            if len(claim) > 220:
                claim = claim[:217] + "..."
            age = "{} d".format(item["age_days"]) if item["age_days"] is not None else "undated"
            lines.append("- `{}:{}` ({}): {}".format(item["file"], item["line"], age, claim))
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    parser.add_argument("--topic", choices=[name for name, _ in TOPICS] + ["other"])
    parser.add_argument("--older-than", type=int, metavar="DAYS",
                        help="only files whose Version-Timestamp is at least DAYS old (undated files included)")
    parser.add_argument("--plugin-root", type=Path, default=PLUGIN)
    args = parser.parse_args(argv)

    today = dt.datetime.now(dt.timezone.utc).date()
    items = collect(args.plugin_root, today)
    if args.topic:
        items = [i for i in items if i["topic"] == args.topic]
    if args.older_than is not None:
        items = [i for i in items if i["age_days"] is None or i["age_days"] >= args.older_than]

    if args.json:
        json.dump({"generated": today.isoformat(), "items": items}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_markdown(items, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())
