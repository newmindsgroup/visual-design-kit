"""Query, validate and index the Design Space Atlas.

Version-Timestamp: 2026-10-20 01:42:00 UTC

Usage (from anywhere):
  python3 atlas.py query "fintech app for gen z in brazil, premium, playful"
  python3 atlas.py show industry.fintech-banking
  python3 atlas.py combine style.neo-brutalist industry.fintech-banking audience.teens-gen-z
  python3 atlas.py list --axis style
  python3 atlas.py validate [--complete]
  python3 atlas.py build

Standard library only. Paths are printed absolute so an agent can read them directly.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ATLAS = Path(__file__).resolve().parent.parent / "atlas"
FIELDS = ["id", "axis", "name", "aliases", "summary", "tags", "pairs_with", "avoid_with", "version_timestamp"]
LISTS = {"aliases", "tags", "pairs_with", "avoid_with"}
SECTIONS = {
    "style": ["Essence", "Visual signature", "Token recipe", "Composition and layout", "Imagery and iconography", "Motion",
              "Fits and risks", "Do and don't", "Clichés and AI tells", "Accessibility notes", "Reference anchors"],
    "industry": ["Audience and jobs to be done", "Trust signals", "Category conventions", "Where to differentiate",
                 "Category clichés", "Regulatory and compliance notes", "Key deliverables and screens", "Voice and content",
                 "Recommended directions", "Metrics that matter", "Reference anchors"],
    "market": ["Language and script", "Typography and layout", "Color and symbolism", "Imagery and representation",
               "Formats and conventions", "Platforms, devices and payments", "Regulatory and compliance notes",
               "Localization pitfalls", "Reference anchors"],
    "audience": ["Who and what they need", "Design defaults", "Interaction and content", "Visual tone", "Pitfalls",
                 "Regulatory and compliance notes", "Reference anchors"],
    "archetype": ["Essence", "Visual translation", "Voice and tone", "Fits and tensions", "Clichés to avoid", "Reference anchors"],
    "tier": ["Signals", "Token recipe", "Imagery and copy", "Pitfalls", "Reference anchors"],
    "channel": ["Formats and specs", "Structure and hierarchy", "Craft defaults", "Production and handoff", "QA checklist",
                "Reference anchors"],
}
TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2,5}$")
LIMITS = {"tags": (4, 10), "pairs_with": (3, 10), "avoid_with": (0, 6)}
BODY_ID = re.compile(r"(?<![\w./-])((?:style|industry|market|audience|archetype|tier|channel)\.[a-z0-9]+(?:-[a-z0-9]+)*)(?![\w-])")
FILE_SUFFIXES = {"css", "js", "json", "md", "html", "svg", "png", "mjs", "ts"}
STOP = set("a an and the for of to in on with by at or is are be our we my your app apps site website brand new".split())


class AtlasError(ValueError):
    pass


def load_registry(root=ATLAS):
    data = json.loads((root / "registry.json").read_text(encoding="utf-8"))
    entries = {}
    for axis, spec in data["axes"].items():
        for item in spec["entries"]:
            entries[item["id"]] = {"axis": axis, "name": item["name"], "path": item["path"]}
    return entries


def parse_entry(text):
    """Return (frontmatter dict, body str). Raises AtlasError on malformed frontmatter."""
    if not text.startswith("---\n"):
        raise AtlasError("missing frontmatter opening ---")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AtlasError("missing frontmatter closing ---")
    meta = {}
    for number, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise AtlasError(f"frontmatter line {number} is not key: value")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in meta:
            raise AtlasError(f"duplicate frontmatter key {key}")
        if key in LISTS:
            if not (value.startswith("[") and value.endswith("]")):
                raise AtlasError(f"{key} must be a one-line [list]")
            inner = value[1:-1].strip()
            meta[key] = [part.strip() for part in inner.split(",") if part.strip()] if inner else []
        else:
            meta[key] = value
    return meta, text[end + 5:]


def sections_of(body):
    found, current = [], None
    content = {}
    for line in body.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            found.append(current)
            content[current] = []
        elif current is not None and line.strip():
            content[current].append(line)
    return found, content


def check_entry(path, registry, root=ATLAS):
    errors = []
    rel = path.relative_to(root).as_posix()
    try:
        meta, body = parse_entry(path.read_text(encoding="utf-8"))
    except (AtlasError, UnicodeError) as exc:
        return [f"{rel}: {exc}"], None
    missing = [field for field in FIELDS if field not in meta]
    if missing:
        errors.append(f"{rel}: missing frontmatter {', '.join(missing)}")
        return errors, None
    entry_id, axis = meta["id"], meta["axis"]
    expected = registry.get(entry_id)
    if expected is None:
        errors.append(f"{rel}: id {entry_id} is not in registry.json")
    else:
        if expected["path"] != rel:
            errors.append(f"{rel}: registry expects this id at {expected['path']}")
        if expected["axis"] != axis:
            errors.append(f"{rel}: axis {axis} does not match registry axis {expected['axis']}")
    if not entry_id.startswith(f"{axis}."):
        errors.append(f"{rel}: id prefix must be {axis}.")
    if len(meta["summary"]) > 200 or len(meta["summary"]) < 30:
        errors.append(f"{rel}: summary must be 30-200 characters (got {len(meta['summary'])})")
    if not TIMESTAMP.match(meta["version_timestamp"]):
        errors.append(f"{rel}: version_timestamp must look like 2026-10-20 01:42:00 UTC")
    for key, (low, high) in LIMITS.items():
        if not low <= len(meta[key]) <= high:
            errors.append(f"{rel}: {key} needs {low}-{high} items (got {len(meta[key])})")
    for key in ("pairs_with", "avoid_with"):
        for ref in meta[key]:
            if ref not in registry:
                errors.append(f"{rel}: {key} references unknown id {ref}")
            elif ref == entry_id:
                errors.append(f"{rel}: {key} references itself")
    if set(meta["pairs_with"]) & set(meta["avoid_with"]):
        errors.append(f"{rel}: an id appears in both pairs_with and avoid_with")
    for ref in sorted(set(BODY_ID.findall(body))):
        if ref.split(".", 1)[1] in FILE_SUFFIXES:
            continue
        if ref not in registry:
            errors.append(f"{rel}: body mentions unknown atlas id {ref}")
    if axis in SECTIONS:
        found, content = sections_of(body)
        required = SECTIONS[axis]
        if found != required:
            missing_sections = [name for name in required if name not in found]
            extra = [name for name in found if name not in required]
            detail = []
            if missing_sections:
                detail.append("missing " + ", ".join(missing_sections))
            if extra:
                detail.append("unexpected " + ", ".join(extra))
            if not detail:
                detail.append("sections out of order")
            errors.append(f"{rel}: H2 sections must be exactly {required}; " + "; ".join(detail))
        for name in found:
            if name in required and not content.get(name):
                errors.append(f"{rel}: section '{name}' is empty")
        lines = len(body.splitlines())
        if lines < 50:
            errors.append(f"{rel}: body is too thin ({lines} lines; aim for 70-160)")
    else:
        errors.append(f"{rel}: unknown axis {axis}")
    return errors, meta


def entry_files(root=ATLAS):
    registry = load_registry(root)
    directories = {spec["path"].split("/")[0] for spec in registry.values()}
    return sorted(path for directory in directories for path in (root / directory).glob("*.md"))


def validate(root=ATLAS, complete=False):
    registry = load_registry(root)
    errors, seen = [], {}
    for path in entry_files(root):
        entry_errors, meta = check_entry(path, registry, root)
        errors.extend(entry_errors)
        if meta and meta.get("id"):
            if meta["id"] in seen:
                errors.append(f"duplicate id {meta['id']} in {seen[meta['id']]} and {path.name}")
            seen[meta["id"]] = path.name
    if complete:
        for entry_id, spec in sorted(registry.items()):
            if not (root / spec["path"]).is_file():
                errors.append(f"missing entry file for {entry_id}: {spec['path']}")
    return errors, len(seen), len(registry)


def build_index(root=ATLAS):
    registry = load_registry(root)
    items, stamps = [], []
    for path in entry_files(root):
        errors, meta = check_entry(path, registry, root)
        if errors:
            raise AtlasError("cannot build index with invalid entries:\n" + "\n".join(errors))
        stamps.append(meta["version_timestamp"])
        items.append({key: meta[key] for key in ["id", "axis", "name", "aliases", "summary", "tags", "pairs_with", "avoid_with"]}
                     | {"path": path.relative_to(root).as_posix()})
    items.sort(key=lambda item: item["id"])
    counts = {}
    for item in items:
        counts[item["axis"]] = counts.get(item["axis"], 0) + 1
    return {"Version-Timestamp": max(stamps) if stamps else "unknown", "counts": counts, "total": len(items), "entries": items}


def load_index(root=ATLAS):
    path = root / "index.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return build_index(root)


def words(text):
    return [word for word in re.findall(r"[a-z0-9][a-z0-9+\-]*", text.lower()) if word not in STOP]


def score(entry, query_text, query_words):
    total = 0
    slug = entry["id"].split(".", 1)[1]
    if entry["id"] in query_text or slug.replace("-", " ") in query_text:
        total += 10
    for alias in entry["aliases"] + [entry["name"].lower()]:
        alias = alias.lower()
        if len(alias) > 3 and alias in query_text:
            total += 6
    name_words = set(words(entry["name"])) | set(slug.split("-"))
    tag_words = {tag.lower() for tag in entry["tags"]}
    summary_words = set(words(entry["summary"]))
    for word in set(query_words):
        if word in name_words:
            total += 3
        if word in tag_words:
            total += 2
        if word in summary_words:
            total += 1
    return total


def query(text, root=ATLAS, axis=None, per_axis=3):
    index = load_index(root)
    query_text = " " + " ".join(words(text)) + " "
    raw_text = text.lower()
    query_words = words(text)
    results = {}
    for entry in index["entries"]:
        if axis and entry["axis"] != axis:
            continue
        value = score(entry, raw_text + query_text, query_words)
        if value > 0:
            results.setdefault(entry["axis"], []).append((value, entry))
    return {name: [dict(entry, score=value, path=str(root / entry["path"])) for value, entry in sorted(items, key=lambda pair: (-pair[0], pair[1]["id"]))[:per_axis]]
            for name, items in sorted(results.items())}


def combine(ids, root=ATLAS):
    index = {entry["id"]: entry for entry in load_index(root)["entries"]}
    unknown = [entry_id for entry_id in ids if entry_id not in index]
    if unknown:
        raise AtlasError("unknown or unwritten ids: " + ", ".join(unknown))
    conflicts, endorsements = [], []
    for first in ids:
        for second in ids:
            if first == second:
                continue
            if second in index[first]["avoid_with"]:
                conflicts.append(f"{first} lists {second} under avoid_with: read both entries and resolve the tension deliberately")
            if second in index[first]["pairs_with"]:
                endorsements.append(f"{first} pairs with {second}")
    suggestions = {}
    for entry_id in ids:
        for ref in index[entry_id]["pairs_with"]:
            if ref not in ids:
                suggestions[ref] = suggestions.get(ref, 0) + 1
    ranked = [ref for ref, _ in sorted(suggestions.items(), key=lambda pair: (-pair[1], pair[0]))][:8]
    return {"read": [str(root / index[entry_id]["path"]) for entry_id in ids], "conflicts": conflicts,
            "endorsements": sorted(set(endorsements)), "also_consider": ranked}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Design Space Atlas helper")
    parser.add_argument("--root", type=Path, default=ATLAS, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    sub = parser.add_subparsers(dest="command", required=True)
    q = sub.add_parser("query", help="find relevant entries for a brief")
    q.add_argument("text")
    q.add_argument("--axis", choices=sorted(SECTIONS))
    q.add_argument("--limit", type=int, default=3, help="results per axis")
    s = sub.add_parser("show", help="print an entry path and summary")
    s.add_argument("id")
    c = sub.add_parser("combine", help="check a combination of ids for conflicts")
    c.add_argument("ids", nargs="+")
    l = sub.add_parser("list", help="list entries")
    l.add_argument("--axis", choices=sorted(SECTIONS))
    v = sub.add_parser("validate", help="validate entries against the schema")
    v.add_argument("--complete", action="store_true", help="also require every registry id to have an entry")
    sub.add_parser("build", help="regenerate index.json")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "validate":
            errors, written, planned = validate(root, args.complete)
            if args.json:
                print(json.dumps({"valid": not errors, "errors": errors, "written": written, "planned": planned}, indent=2))
            else:
                print("\n".join(errors) if errors else f"atlas valid: {written}/{planned} entries written")
            return 1 if errors else 0
        if args.command == "build":
            index = build_index(root)
            (root / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"wrote index.json: {index['total']} entries {index['counts']}")
            return 0
        if args.command == "query":
            result = query(args.text, root, args.axis, args.limit)
            if args.json:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                if not result:
                    print("no matches; try broader words or `list --axis <axis>`")
                for axis_name, items in result.items():
                    print(f"[{axis_name}]")
                    for item in items:
                        print(f"  {item['id']} ({item['score']}): {item['summary']}\n    {item['path']}")
            return 0
        if args.command == "show":
            index = {entry["id"]: entry for entry in load_index(root)["entries"]}
            entry = index.get(args.id)
            if not entry:
                print(f"unknown or unwritten id: {args.id}", file=sys.stderr)
                return 1
            print(json.dumps(dict(entry, path=str(root / entry["path"])), indent=2, ensure_ascii=False) if args.json
                  else f"{entry['id']}: {entry['name']}\n{entry['summary']}\n{root / entry['path']}")
            return 0
        if args.command == "combine":
            result = combine(args.ids, root)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print("Read:\n  " + "\n  ".join(result["read"]))
                print("Conflicts:\n  " + ("\n  ".join(result["conflicts"]) or "none"))
                print("Endorsed pairs:\n  " + ("\n  ".join(result["endorsements"]) or "none"))
                print("Also consider:\n  " + (", ".join(result["also_consider"]) or "none"))
            return 0
        if args.command == "list":
            for entry in load_index(root)["entries"]:
                if not args.axis or entry["axis"] == args.axis:
                    print(f"{entry['id']}: {entry['summary']}")
            return 0
    except (AtlasError, OSError, json.JSONDecodeError) as exc:
        print(f"atlas error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
