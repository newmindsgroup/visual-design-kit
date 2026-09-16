#!/usr/bin/env python3
# Version-Timestamp: 2026-09-14T19:02:27.477726-04:00
"""Read-only, offline checks and citation search for a downloaded library."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def within(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError('unsafe relative path')
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or path == root:
        raise ValueError('unsafe relative path')
    return path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def verify(root):
    manifest = json.loads(within(root, 'manifests/files.json').read_text())
    files = manifest['files']
    if not isinstance(files, dict) or not files:
        raise ValueError('empty or invalid manifest')
    failures = []
    for relative, entry in files.items():
        try:
            path = within(root, relative)
            if not path.is_file():
                failures.append({'path': relative, 'status': 'missing'})
            elif digest(path) != entry['sha256']:
                failures.append({'path': relative, 'status': 'mismatch'})
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures.append({'path': relative, 'status': str(exc)})
    print(json.dumps({'checked': len(files), 'failures': failures}))
    return 1 if failures else 0


def search(root, query, limit):
    if not query.strip():
        raise ValueError('query must not be empty')
    seen = set()
    count = 0
    with within(root, 'catalog/items.jsonl').open() as catalog:
        for line in catalog:
            row = json.loads(line)
            relative = row.get('extraction')
            if not relative or relative in seen:
                continue
            seen.add(relative)
            with within(root, relative).open() as units:
                for line in units:
                    unit = json.loads(line)
                    text = unit.get('text', '')
                    pos = text.casefold().find(query.casefold())
                    if pos < 0:
                        continue
                    hit = {'source_id': row['id'], 'title': row.get('display_title'),
                           'excerpt': text[max(0, pos-80):pos+len(query)+160],
                           'original': row.get('original')}
                    for key in ('page', 'page_label', 'section'):
                        if key in unit:
                            hit[key] = unit[key]
                    print(json.dumps(hit, ensure_ascii=False))
                    count += 1
                    if count >= limit:
                        return 0
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify')
    find = sub.add_parser('search')
    find.add_argument('query')
    find.add_argument('--limit', type=int, default=10, choices=range(1, 101), metavar='1..100')
    args = parser.parse_args()
    try:
        root = args.root.expanduser().resolve(strict=True)
        return verify(root) if args.command == 'verify' else search(root, args.query, args.limit)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
