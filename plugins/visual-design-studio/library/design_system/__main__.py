"""Portable read-only CLI; reports contain paths/codes, never source values."""
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
import argparse
import json
import sys
from .validation import ROOT, validate, compare, load_json, catalog_plan
from .selection import validate_selection


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    v = sub.add_parser('validate'); v.add_argument('kind', choices=['persona','evidence','handoff','manifest','reference-decision','system-inventory','selection']); v.add_argument('file'); v.add_argument('--root', required=True); v.add_argument('--library-root', default=str(ROOT)); v.add_argument('--as-of'); v.add_argument('--human', action='store_true')
    c = sub.add_parser('compare'); c.add_argument('before'); c.add_argument('after'); c.add_argument('--allow', action='append', required=True); c.add_argument('--invariant', action='append', required=True)
    s = sub.add_parser('plan'); s.add_argument('capabilities', nargs='+'); s.add_argument('--catalog', default=str(ROOT/'capabilities.json'))
    args = p.parse_args()
    try:
        if args.command == 'validate':
            result = validate_selection(load_json(args.file), args.root, args.library_root) if args.kind == 'selection' else validate(args.kind,load_json(args.file),args.root,args.as_of)
        elif args.command == 'compare':
            before, after = load_json(args.before), load_json(args.after)
            try:
                result = compare(before,after,args.allow,args.invariant)
            except (ValueError, RecursionError):
                result = {'valid':False,'errors':[{'code':'comparison_unverifiable','path':'comparison','message':'Unsupported keys, paths or nesting; invariants were not evaluated'}]}

        else: result = {'valid':True,'order':catalog_plan(load_json(args.catalog),args.capabilities),'executes':False}
    except (ValueError, OSError, TypeError, KeyError, RecursionError):
        result = {'valid':False,'errors':[{'code':'input_error','path':'input','message':'Invalid, unreadable, oversized or incompatible input'}]}
    if args.command == 'validate' and args.kind == 'reference-decision':
        result.setdefault('decision_status', 'invalid')
        result['executes'] = False
    if args.command == 'validate' and args.kind == 'system-inventory':
        result['executes'] = False
    if getattr(args,'human',False):
        print('PASS (structural only)' if result['valid'] else 'FAIL')
        if args.command == 'validate' and args.kind == 'reference-decision':
            print('Decision status: ' + result['decision_status'])
            print('Executes: false')
        if args.command == 'validate' and args.kind == 'system-inventory':
            print('Inventory entries: ' + str(result.get('coverage',{}).get('entries','unverified')))
            print('Implementation not provided; testing not performed')
            print('Executes: false')
        if args.command == 'validate' and args.kind == 'selection': print('Executes: false')
        for item in result.get('errors',[]) + result.get('warnings',[]): print(f"{item['code']} at {item['path']}: {item['message']}")
    else: print(json.dumps(result,ensure_ascii=True,allow_nan=False))
    return 0 if result['valid'] else 1

if __name__ == '__main__':sys.exit(main())
