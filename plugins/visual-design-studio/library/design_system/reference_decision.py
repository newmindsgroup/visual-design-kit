"""Original reference-decision checks; recorded claims are not external truth."""
# Version-Timestamp: 2026-09-07 11:25:22 AST
import json
from urllib.parse import urlsplit


KINDS = {'object':dict, 'array':list, 'string':str, 'boolean':bool, 'null':type(None)}


def check_schema(schema):
    """Fail closed on unsupported trusted-package schema changes."""
    allowed = {'$schema','title','description','type','const','enum','minLength','minItems',
               'uniqueItems','properties','required','additionalProperties','items'}
    if not isinstance(schema, dict) or set(schema) - allowed:
        raise ValueError('Unsupported schema')
    expected = schema.get('type')
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        if not types or any(not isinstance(k, str) or k not in KINDS for k in types):
            raise ValueError('Unsupported type')
    for key in ['minLength','minItems']:
        if key in schema and (type(schema[key]) is not int or schema[key] < 0):
            raise ValueError('Invalid bound')
    if 'uniqueItems' in schema and type(schema['uniqueItems']) is not bool:
        raise ValueError('Invalid uniqueness rule')
    if 'enum' in schema and (not isinstance(schema['enum'], list) or not schema['enum']):
        raise ValueError('Invalid enum')
    props = schema.get('properties', {})
    required = schema.get('required', [])
    if not isinstance(props, dict) or not isinstance(required, list) or any(not isinstance(k, str) or k not in props for k in required):
        raise ValueError('Invalid properties')
    for child in props.values():check_schema(child)
    if 'items' in schema:check_schema(schema['items'])
    extra = schema.get('additionalProperties', True)
    if isinstance(extra, dict):check_schema(extra)
    elif type(extra) is not bool:raise ValueError('Invalid additional properties')


def structure(c, value, schema, path=''):
    """Evaluate only the structural keywords used by the bundled trusted schema."""
    expected = schema.get('type')
    if expected is not None:
        expected = expected if isinstance(expected, list) else [expected]
        if not any(type(value) is KINDS[k] for k in expected):
            c.error('schema', path, 'Unexpected value type'); return
    if 'const' in schema and value != schema['const'] or 'enum' in schema and value not in schema['enum']:
        c.error('schema', path, 'Unsupported value')
    if isinstance(value, str) and (len(value.strip()) < schema.get('minLength', 0) or value == 'REQUIRED'):
        c.error('schema', path, 'Nonempty, completed text required')
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            c.error('schema', path, 'Required entries missing')
        if schema.get('uniqueItems') and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            c.error('schema', path, 'Repeated list entry')
        for i, item in enumerate(value):
            structure(c, item, schema.get('items', {}), f'{path}.{i}')
    if isinstance(value, dict):
        props = schema.get('properties', {})
        for key in schema.get('required', []):
            if key not in value:c.error('schema', f'{path}.{key}', 'Required field missing')
        for key, item in value.items():
            if not isinstance(key, str) or not key.strip():
                c.error('schema', path, 'Nonempty text key required'); continue
            if key in props:structure(c, item, props[key], f'{path}.{key}')
            elif schema.get('additionalProperties') is False:c.error('schema', path, 'Unrecognized field')
            elif isinstance(schema.get('additionalProperties'), dict):
                structure(c, item, schema['additionalProperties'], f'{path}.{key}')


def reference_decision(c, data):
    from .validation import ROOT, load_json
    try:
        schema = load_json(ROOT / 'templates/reference-decision.schema.json')
        check_schema(schema)
    except (OSError, ValueError, TypeError, KeyError, RecursionError):
        c.error('config_error', 'package.reference_schema', 'Bundled schema missing, malformed or unsupported')
        return
    structure(c, data, schema)
    if c.errors:return

    def index(items, path):
        result = {}
        for i, item in enumerate(items):
            if item['id'] in result:c.error('duplicate_id', f'{path}.{i}', 'Identifier repeated')
            result[item['id']] = item
        return result

    sources = index(data['sources'], 'sources')
    evidence = index(data['evidence'], 'evidence')
    candidates = index(data['candidates'], 'candidates')
    index(data['verification'], 'verification')

    def links(ids, register, path, code, supported=False):
        if supported and not ids:c.error(code, path, 'Supporting evidence required')
        for key in ids:
            if key not in register:c.error(code, path, 'Identifier does not resolve')
            elif supported and register[key]['status'] not in {'observed','supplied','synthetic'}:
                c.error('unsupported_evidence', path, 'Unknown or inferred evidence cannot establish this claim')

    def scoped(ids, scope, path, code='evidence_scope'):
        if not any(scope in evidence.get(eid, {}).get('supports', []) for eid in ids):
            c.error(code, path, 'Evidence does not declare support for this operation or check')

    for i, source in enumerate(data['sources']):
        path = f'sources.{i}'
        day = c.day(source['checked_at'], path+'.checked_at')
        if day and day > c.as_of:c.error('future_source', path, 'Check date is in the future')
        if source['kind'] == 'synthetic':
            if not data['synthetic']:c.error('synthetic_scope', path, 'Synthetic source requires a synthetic record')
        elif source['kind'] == 'public-url':
            url = urlsplit(source['location'])
            if url.scheme != 'https' or not url.hostname or url.username or url.password:
                c.error('source_location', path, 'Public source must be an HTTPS URL without credentials')
        else:c.ref({'path':source['location']},path)
    for i, item in enumerate(data['evidence']):
        path = f'evidence.{i}'
        links(item['source_ids'], sources, path, 'source_reference')
        if item['status'] != 'unknown' and not item['source_ids']:
            c.error('source_reference', path, 'Claim requires source provenance')
        if item['status'] == 'synthetic' and not data['synthetic']:
            c.error('synthetic_scope', path, 'Synthetic evidence requires a synthetic record')
        if any(sources.get(sid, {}).get('kind') == 'synthetic' for sid in item['source_ids']) and item['status'] not in {'synthetic','unknown'}:
            c.error('synthetic_scope', path, 'Fictional evidence must not become an observed claim')

    baseline = data['baseline']
    if baseline['status'] == 'none':
        if data['context'] != 'new-brand':c.error('baseline_required', 'baseline', 'Existing contexts require an explicit locked baseline')
        if baseline['reference'] is not None or baseline['approval_evidence_id'] is not None:
            c.error('baseline_conflict', 'baseline', 'Absent baseline must not claim an approval or file')
    else:
        links([baseline['approval_evidence_id']], evidence, 'baseline.approval_evidence_id', 'evidence_reference', True)
        scoped([baseline['approval_evidence_id']], 'baseline-approval', 'baseline.approval_evidence_id')
        count = len(c.errors)
        c.ref(baseline['reference'], 'baseline.reference', True)
        if len(c.errors) == count:
            original = load_json(c.root / baseline['reference']['path'])
            locked = original.get('locked') if isinstance(original, dict) else None
            if not isinstance(locked, dict) or not locked or original.get('schema_version') != '1.0-proposed':
                c.error('baseline_contract', 'baseline', 'Baseline requires a supported version and nonempty locked object')
            else:
                for key, value in locked.items():
                    if key not in data['values'] or json.dumps(value, sort_keys=True) != json.dumps(data['values'][key], sort_keys=True):
                        c.error('baseline_changed', 'values', 'Locked value removed, changed or coerced')
                for i, derivation in enumerate(data['derivations']):
                    if derivation['target'] in locked or any(key in locked for key in derivation['from']):
                        c.error('locked_derivation', f'derivations.{i}', 'A locked value cannot be a derivation source or target')
    for i, derivation in enumerate(data['derivations']):
        if derivation['target'] not in data['values'] or any(key not in data['values'] for key in derivation['from']):
            c.error('value_reference', f'derivations.{i}', 'Derivation keys must exist in the value map')

    unresolved = False
    for i, check in enumerate(data['verification']):
        path = f'verification.{i}'
        links(check['candidate_ids'], candidates, path, 'candidate_reference')
        links(check['evidence_ids'], evidence, path, 'evidence_reference')
        if check['status'] == 'passed':
            if not check['evidence_ids']:c.error('verification_evidence', path, 'Passed check requires evidence')
            links(check['evidence_ids'], evidence, path, 'verification_evidence', True)
            scoped(check['evidence_ids'], 'check:'+check['kind'], path, 'verification_evidence')
        else:
            unresolved = True
            if check['status'] == 'failed':
                c.warnings.append({'code':'verification_failed','path':path,'message':'Recorded check failed; remediation and re-verification remain required'})

    def open_check(kind, cid):
        return any(v['kind'] == kind and cid in v['candidate_ids'] and v['status'] in {'pending','failed'} for v in data['verification'])

    for i, candidate in enumerate(data['candidates']):
        path = f'candidates.{i}'; cid = candidate['id']
        links(candidate['source_ids'], sources, path, 'source_reference')
        links(candidate['evidence_ids'], evidence, path, 'evidence_reference')
        referenced = {sid for eid in candidate['evidence_ids'] for sid in evidence.get(eid, {}).get('source_ids', [])}
        if not referenced.issubset(set(candidate['source_ids'])):
            c.error('provenance_mismatch', path, 'Candidate sources must include its evidence sources')
        required = {'human-design','accessibility'} | ({'device'} if data['context']=='physical-display' else set())
        kinds = {v['kind'] for v in data['verification'] if cid in v['candidate_ids']}
        if not required.issubset(kinds):c.error('verification_coverage', path, 'Required review categories are missing')
        rights = candidate['rights']
        links(rights['evidence_ids'], evidence, path+'.rights', 'evidence_reference', rights['status']=='documented')
        if rights['status'] == 'documented':scoped(rights['evidence_ids'], 'rights', path+'.rights')
        if rights['status'] != 'documented':
            unresolved = True
            if candidate['disposition'] in {'reuse','complement'}:
                c.error('rights_hold', path, 'Unknown or held rights cannot support reuse or complement')
            if not open_check('rights', cid):c.error('pending_verification', path, 'Rights require a pending or failed check with a next action')
        if candidate['disposition'] == 'held':unresolved = True
        operations = candidate['operations']
        if candidate['disposition'] in {'reuse','complement','held'} and not {'asset-production','playback'}.issubset({op['kind'] for op in operations}):
            c.error('operation_coverage', path, 'Record production and playback costs separately, even when no production is needed')
        for j, operation in enumerate(operations):
            opath = f'{path}.operations.{j}'
            links(operation['evidence_ids'], evidence, opath, 'evidence_reference', operation['cost']!='unknown')
            if operation['cost'] != 'unknown':scoped(operation['evidence_ids'], 'cost:'+operation['kind'], opath)
            if operation['cost'] == 'paid' and data['budget'] == 'zero-extra':
                unresolved = True
                if candidate['disposition'] not in {'held','reject','reference-only'}:
                    c.error('budget_conflict', opath, 'Paid operation conflicts with the zero-extra budget')
            if operation['cost'] == 'unknown':
                unresolved = True
                if not open_check('cost', cid):c.error('pending_verification', opath, 'Unknown operation cost requires a pending or failed check with a next action')
    status = 'held' if unresolved else 'reviewable'
    if data['readiness'] != status:c.error('readiness_conflict', 'readiness', 'Readiness conflicts with recorded holds or incomplete checks')
    if data['synthetic'] and status == 'reviewable':
        c.warnings.append({'code':'synthetic_record','path':'synthetic','message':'Fictional evidence is reviewable only as a rehearsal, not real-world acceptance'})
    c.decision_status = status
