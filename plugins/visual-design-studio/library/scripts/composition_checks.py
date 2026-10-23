"""Check declared composition measurements. No artwork or evidence files are read."""
# Version-Timestamp: 2026-10-17 08:36:43 AST
import json
import math
import sys


def check(receipt):
    issues = []
    if not isinstance(receipt, dict):
        return ['receipt must be an object']
    if receipt.get('unit') not in ('pt', 'css_px'):
        issues.append('unit must be pt or css_px')
    for key in ('font_evidence', 'render_evidence'):
        if not isinstance(receipt.get(key), str) or not receipt[key].strip():
            issues.append(key + ' reference required')
    elements = receipt.get('elements')
    if not isinstance(elements, list) or not elements:
        return issues + ['nonempty elements required']
    numeric = ('minimum_inset', 'font_size', 'minimum_font_size', 'lines',
               'maximum_lines', 'last_line_words', 'gap_after', 'minimum_gap_after')
    def number(value):
        try:
            return type(value) in (int, float) and math.isfinite(value) and value >= 0
        except OverflowError:
            return False
    ids = set()
    for index, element in enumerate(elements):
        if not isinstance(element, dict):
            issues.append(f'element {index}: object required')
            continue
        name = element.get('id')
        if not isinstance(name, str) or not name.strip() or name in ids:
            issues.append(f'element {index}: unique nonempty id required')
        else:
            ids.add(name)
        label = f'element {index} ({name})'
        insets = element.get('insets')
        valid = (all(number(element.get(k)) for k in numeric)
                 and isinstance(insets, list) and len(insets) == 4
                 and all(number(v) for v in insets)
                 and type(element.get('clipped')) is bool)
        if not valid:
            issues.append(label + ': finite nonnegative measurements and boolean clipped required')
            continue
        counts = ('lines', 'maximum_lines', 'last_line_words')
        if any(element[k] < 1 or int(element[k]) != element[k] for k in counts):
            issues.append(label + ': positive integer line and word counts required')
        if min(insets) < element['minimum_inset']:
            issues.append(label + ': insufficient panel inset')
        if element['font_size'] < element['minimum_font_size']:
            issues.append(label + ': type below declared minimum')
        if element['lines'] > element['maximum_lines']:
            issues.append(label + ': excessive wrapping')
        if element['lines'] > 1 and element['last_line_words'] == 1:
            issues.append(label + ': isolated final word needs review')
        if element['clipped']:
            issues.append(label + ': clipping reported')
        if element['gap_after'] < element['minimum_gap_after']:
            issues.append(label + ': insufficient section gap')
    return issues


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError('usage: composition_checks.py receipt.json')
        with open(sys.argv[1], encoding='utf-8') as handle:
            issues = check(json.load(handle))
    except (OSError, ValueError, OverflowError, RecursionError) as error:
        print(json.dumps({'status': 'invalid', 'error': str(error)}))
        return 2
    print(json.dumps({'status': 'needs_review' if issues else 'measurements_pass',
                      'issues': issues, 'scope': 'Supplied measurements only; visual approval separate'}))
    return 1 if issues else 0


if __name__ == '__main__':
    sys.exit(main())
