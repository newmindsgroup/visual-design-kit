#!/usr/bin/env python3
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
"""Copy one bundled Markdown template into a project without breaking library links."""
import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote


LIBRARY_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = LIBRARY_ROOT / "templates"
LOCAL_REFERENCE_CONFIG = Path("private/reference-library.local.json")
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\((<[^>]+>|[^)\s]+)(\s+[^)]*)?\)")


def _inside(root, candidate):
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def _has_symlink_component(root, path):
    try:
        relative = path.relative_to(root)
    except ValueError:
        raise ValueError("path escapes required root")
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return True
    return False


def _has_explicit_symlink_component(path):
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _template_path(template):
    requested = Path(template)
    if (requested.is_absolute() or requested.suffix != ".md" or
            any(part in (".", "..") for part in requested.parts)):
        raise ValueError("template must be a relative Markdown path")
    raw_path = TEMPLATE_ROOT / requested
    if _has_symlink_component(TEMPLATE_ROOT, raw_path):
        raise ValueError("template path must not contain symlinks")
    path = raw_path.resolve(strict=True)
    if not _inside(TEMPLATE_ROOT.resolve(), path) or not path.is_file():
        raise ValueError("template must be a regular file inside library/templates")
    return path


def _project_destination(project_root, destination):
    root = Path(project_root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("project root must be a directory")
    requested = Path(destination)
    if (requested.is_absolute() or not requested.parts or
            any(part in (".", "..") for part in requested.parts)):
        raise ValueError("destination must be a relative path")
    output = root / requested
    return root, output


def _parent_fd(root, parent_parts, create):
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(root, flags)
    try:
        for part in parent_parts:
            if create:
                try:
                    os.mkdir(part, dir_fd=descriptor)
                except FileExistsError:
                    pass
            next_descriptor = os.open(part, flags | nofollow, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except OSError as exc:
        os.close(descriptor)
        raise ValueError("destination parent must be an in-project non-symlink directory") from exc


def _existing_output(root, output):
    parts = output.relative_to(root).parts
    try:
        descriptor = _parent_fd(root, parts[:-1], create=False)
    except ValueError:
        parent = root.joinpath(*parts[:-1])
        if not parent.exists():
            return False
        raise
    try:
        handle = os.open(parts[-1], os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0), dir_fd=descriptor)
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise ValueError("destination must not be a symlink") from exc
    else:
        os.close(handle)
        return True
    finally:
        os.close(descriptor)


def _pin_library_links(text, source):
    def replace(match):
        label, target, suffix = match.groups()
        suffix = suffix or ""
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if target.startswith(("#", "/")) or ":" in target:
            return match.group(0)
        path_part, marker, fragment = target.partition("#")
        library = LIBRARY_ROOT.resolve()
        raw_candidate = Path(os.path.normpath(source.parent.resolve() / unquote(path_part)))
        if (not _inside(library, raw_candidate) or
                _has_symlink_component(library, raw_candidate)):
            return match.group(0)
        candidate = raw_candidate.resolve(strict=False)
        if not candidate.is_file():
            return match.group(0)
        pinned = str(candidate)
        if marker:
            pinned += marker + fragment
        return f"[{label}](<{pinned}>{suffix})"

    return LINK.sub(replace, text)


def adopt(template, project_root, destination, apply=False):
    """Plan or apply one non-overwriting template adoption."""
    source = _template_path(template)
    root, output = _project_destination(project_root, destination)
    if _existing_output(root, output):
        raise FileExistsError(f"refusing to overwrite existing output: {output}")
    text = _pin_library_links(source.read_text(encoding="utf-8"), source)
    result = {"template": str(source), "destination": str(output),
              "status": "applied" if apply else "dry_run"}
    if not apply:
        return result
    parts = output.relative_to(root).parts
    descriptor = _parent_fd(root, parts[:-1], create=True)
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
        handle = os.open(parts[-1], flags, 0o600, dir_fd=descriptor)
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(text)
    finally:
        os.close(descriptor)
    return result


def resolve_reference_config(project_root):
    """Read optional ignored book settings without treating their absence as a hold."""
    config = Path(project_root).expanduser().resolve(strict=True) / LOCAL_REFERENCE_CONFIG
    if not config.exists():
        return None
    if config.is_symlink() or not config.is_file():
        raise ValueError("reference configuration must be a regular file")
    data = json.loads(config.read_text(encoding="utf-8"))
    root = data.get("reference_library_root")
    tool = data.get("reference_library_tool")
    if not isinstance(root, str) or not root:
        raise ValueError("reference_library_root is required when configuration exists")
    root_path = Path(root).expanduser().resolve(strict=True)
    if not root_path.is_dir():
        raise ValueError("reference_library_root must be a directory")
    if tool:
        raw_tool = Path(tool).expanduser()
        if not raw_tool.is_absolute() or _has_explicit_symlink_component(raw_tool):
            raise ValueError("reference_library_tool must be an absolute non-symlink path")
        tool_path = raw_tool.resolve(strict=True)
    else:
        tool_path = LIBRARY_ROOT / "scripts/reference_library.py"
    if not tool_path.is_file() or tool_path.is_symlink():
        raise ValueError("reference_library_tool must be a regular trusted file")
    return {"reference_library_root": root_path, "reference_library_tool": tool_path}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", help="relative path below library/templates, for example stage-execution.md")
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--destination", required=True, type=Path,
                        help="relative output path inside the project root")
    parser.add_argument("--apply", action="store_true", help="write the planned copy; dry-run is the default")
    args = parser.parse_args()
    try:
        result = adopt(args.template, args.project_root, args.destination, args.apply)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
