"""Validate structure and local evidence, never creative or factual truth."""
# Version-Timestamp: 2026-09-16 18:38:00 AST
import hashlib
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

VERSION = '1.0-proposed'
ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 16 * 1024 * 1024
STATUSES = {'evidenced', 'supplied', 'inferred', 'hypothesis', 'proposed', 'synthetic', 'unknown', 'not_applicable'}


def load_json(path):
    path = Path(path)
    if not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError('Input must be a regular JSON file no larger than 16 MiB')
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON key')
            result[key] = value
        return result
    def invalid(_):
        raise ValueError('Non-finite JSON number')
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs, parse_constant=invalid)
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError('Invalid or excessively nested JSON') from exc


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


class Check:
    def __init__(self, root, as_of):
        self.root = Path(root).resolve()
        self.errors = []
        self.warnings = []
        self.as_of = self.day(as_of, 'as_of') if as_of is not None else datetime.now(timezone.utc).date()

    def error(self, code, path, message):
        self.errors.append({'code': code, 'path': path, 'message': message})

    def require(self, data, keys, path=''):
        for key in keys:
            if key not in data or data[key] is None or data[key] == '' or data[key] == 'REQUIRED':
                self.error('required', f'{path}.{key}'.lstrip('.'), 'Required value missing')

    def texts(self, data, keys, path=''):
        for key in keys:
            if not isinstance(data.get(key), str) or not data[key].strip() or data[key] == 'REQUIRED':
                self.error('text_type', f'{path}.{key}'.lstrip('.'), 'Nonempty text required')

    def ref(self, entry, path, require_hash=False):
        if not isinstance(entry, dict) or not isinstance(entry.get('path'), str):
            self.error('reference', path, 'File reference requires a relative path')
            return
        rel = Path(entry['path'])
        if rel.is_absolute() or not rel.parts or '..' in rel.parts:
            self.error('unsafe_path', path, 'Reference must resolve inside the declared workspace')
            return
        candidate = self.root
        for part in rel.parts:
            candidate /= part
            if candidate.is_symlink():
                self.error('unsafe_path', path, 'Reference cannot contain a symlinked path component')
                return
        candidate = candidate.resolve()
        if not candidate.is_relative_to(self.root):
            self.error('unsafe_path', path, 'Reference must resolve inside the declared workspace')
            return
        if not candidate.is_file():
            self.error('missing_file', path, 'Referenced regular file not found')
            return
        expected = entry.get('sha256')
        if require_hash and not expected:
            self.error('hash_required', path, 'SHA-256 required for integrity claim')
        if expected is not None:
            if not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
                self.error('hash_format', path, 'SHA-256 must be 64 lowercase hexadecimal characters')
            elif sha256(candidate) != expected:
                self.error('hash_mismatch', path, 'File content differs from recorded hash')

    def day(self, value, path):
        try:
            if not isinstance(value, str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value):
                raise ValueError('Expected calendar date')
            return date(*map(int, value.split('-')))
        except (TypeError, ValueError):
            self.error('date', path, 'Use an ISO calendar date YYYY-MM-DD')
            return None

    def result(self):
        return {'valid': not self.errors, 'errors': self.errors, 'warnings': self.warnings,
                'assurance': 'Structure and local references only; no factual, creative, legal, user or device approval'}


def persona(c, data):
    # These are trusted package definitions, not caller workspace references.
    try:
        definitions = load_json(ROOT / 'templates/persona-fields.json')
        skeleton = load_json(ROOT / 'templates/persona-record.json')
        component_defs = load_json(ROOT / 'templates/persona-components.json')
        expected = {x['path'] for x in definitions['fields']}
        component_ids = {x['id'] for x in component_defs['components']}
        if len(expected) != 118 or len(definitions['fields']) != 118 or component_ids != {f'W{i:02}' for i in range(1, 36)} or len(component_defs['components']) != 35:
            raise ValueError('Canonical inventory inconsistent')
        if not isinstance(skeleton['ai_extensions'], dict) or not isinstance(skeleton['collection_context'], dict):
            raise ValueError('Canonical skeleton inconsistent')
    except (OSError, ValueError, TypeError, KeyError):
        c.error('config_error', 'package.templates', 'Canonical package definitions missing, unreadable or inconsistent')
        return
    fields = data.get('fields', {})
    if not isinstance(fields, dict):
        c.error('field_type', 'fields', 'Expected object'); return
    if set(fields) != expected:
        c.error('field_set', 'fields', 'Canonical field set differs: missing or additional keys')
    components = data.get('components', {})
    if not isinstance(components, dict) or set(components) != {f'W{i:02}' for i in range(1, 36)}:
        c.error('component_set', 'components', 'All 35 component representations are required')
    else:
        for key, value in components.items():
            if not isinstance(value, dict) or not value.get('status') or not value.get('data_reference'):
                c.error('component', 'components.'+key, 'Status and data reference required')
    c.require(data, ['record_id', 'owner', 'scope', 'persona_status', 'ai_extensions', 'collection_context'])
    c.texts(data, ['record_id', 'owner', 'scope', 'persona_status'])
    if not isinstance(data.get('collection_context'), dict):
        c.error('collection_type', 'collection_context', 'Expected collection context object')
    if isinstance(components, dict):
        for key, component in components.items():
            if isinstance(component, dict) and component.get('status') not in {'represented','not_applicable','unknown'}:
                c.error('component_status', 'components.'+key, 'Unsupported component status')
            if isinstance(component, dict) and component.get('data_reference') != 'templates/persona-components.json#'+key:
                c.error('component_reference', 'components.'+key, 'Reference must resolve to canonical component definition')
    collection = data.get('collection_context', {})
    if isinstance(collection, dict):
        for key, value in skeleton['collection_context'].items():
            if key not in collection or not isinstance(collection[key], type(value)):
                c.error('collection_contract', 'collection_context.'+key, 'Required collection member missing or wrong type')
    register = data.get('evidence_record')
    source_ids = set()
    if register is not None:
        if not isinstance(register, dict) or register.get('schema_version') != VERSION:
            c.error('schema_version', 'evidence_record', 'Embedded evidence register requires supported version')
        else:
            nested = Check(c.root, c.as_of.isoformat())
            evidence(nested, register)
            for attribute in ['errors', 'warnings']:
                for item in getattr(nested, attribute):
                    getattr(c, attribute).append(dict(item, path='evidence_record.'+item['path'].lstrip('.')))
            source_ids = {x['id'] for x in register.get('sources', []) if isinstance(x, dict) and isinstance(x.get('id'), str)}
    groups = {}
    unknown_groups, malformed_groups = set(), set()
    for key, field in fields.items():
        if not isinstance(field, dict):
            c.error('field_type', key, 'Expected finding envelope'); continue
        c.texts(field, ['status', 'reason', 'confidence'], key)
        status, value = field.get('status'), field.get('value')
        if status not in STATUSES:
            c.error('status', key, 'Unsupported finding status')
        refs = field.get('evidence')
        if not isinstance(refs, list) or any(not isinstance(x, str) or not x for x in refs):
            c.error('evidence_type', key, 'Evidence must be a list of identifiers')
        if isinstance(refs, list) and any(not isinstance(x, str) or x not in source_ids for x in refs):
            c.error('source_reference', key, 'Field evidence must resolve in embedded evidence_record')
        if status in {'evidenced', 'supplied', 'inferred'} and not refs:
            c.error('evidence_required', key, 'This status requires evidence references')
        if status in {'unknown', 'not_applicable'}:
            if '[].' in key:
                unknown_groups.add(key.split('[].')[0])
            if value is not None:
                c.error('unknown_value', key, 'Unknown or not-applicable values must be null')
        elif value is None:
            c.error('field_type', key, 'A supported or proposed value cannot be null')
        elif '[]' not in key:
            if not isinstance(value, str) or not value.strip():
                c.error('field_type', key, 'Expected nonempty string')
        elif not isinstance(value, list) or not value:
            c.error('field_type', key, 'Expected nonempty list or explicit unknown')
        elif '[].' in key:
            ids = []
            for item in value:
                if not isinstance(item, dict) or not isinstance(item.get('item_id'), str) or not item['item_id'] or not isinstance(item.get('text'), str) or not item['text']:
                    c.error('field_type', key, 'Repeated objects require item_id and text')
                    malformed_groups.add(key.split('[].')[0]); continue
                ids.append(item['item_id'])
            if len(ids) != len(set(ids)):
                c.error('duplicate_item', key, 'Repeated item identifiers must be unique')
            groups.setdefault(key.split('[].')[0], []).append(set(ids))
        elif any(not isinstance(x, str) or not x.strip() for x in value):
            c.error('field_type', key, 'Repeated scalar values must be nonempty strings')
    for group, sets in groups.items():
        if group in malformed_groups:
            continue
        if group in unknown_groups:
            c.warnings.append({'code':'linkage_partial','path':group,'message':'Known siblings checked; unknown siblings assert no item linkage'})
        if any(s != sets[0] for s in sets):
            c.error('item_linkage', group, 'Sibling repeated fields must preserve the same item IDs')
    ext = data.get('ai_extensions', {})
    if not isinstance(ext, dict):
        c.error('extension_type', 'ai_extensions', 'Expected object'); return
    if not set(skeleton['ai_extensions']) <= set(ext):
        c.error('extension_set', 'ai_extensions', 'All canonical AI extension members are required')
    for key, value in skeleton['ai_extensions'].items():
        if key in ext and not isinstance(ext[key], type(value)):
            c.error('extension_type', 'ai_extensions.'+key, 'AI extension has incorrect type')
    c.require(ext, ['role_type', 'use_scope', 'validation_plan', 'refresh_owner', 'refresh_trigger', 'approval'])
    traces = ext.get('traceability')
    if not isinstance(traces, list) or not traces:
        c.error('traceability', 'ai_extensions.traceability', 'At least one traceability row required')
    else:
        for i, row in enumerate(traces):
            if not isinstance(row, dict):
                c.error('traceability', str(i), 'Expected object'); continue
            c.texts(row, ['need', 'use_case', 'requirement', 'decision', 'criterion'], f'traceability.{i}')


def evidence(c, data):
    c.texts(data, ['record_id', 'scenario', 'requested_use', 'readiness'])
    scenarios = {'supplied-kit', 'no-kit', 'conflict', 'formalization', 'evolution', 'rebrand', 'new-brand', 'campaign-adaptation', 'refresh', 'precise-change'}
    if data.get('scenario') not in scenarios:
        c.error('scenario', 'scenario', 'Unknown research scenario')
    sources = data.get('sources', [])
    by_id = {}
    if not isinstance(sources, list):
        c.error('source_type', 'sources', 'Expected list'); return
    for i, source in enumerate(sources):
        path = f'sources.{i}'
        if not isinstance(source, dict):
            c.error('source_type', path, 'Expected object'); continue
        c.require(source, ['id', 'retrieved_at', 'status', 'authority', 'rights', 'allowed_uses'], path)
        c.texts(source, ['id', 'authority', 'rights'], path)
        if not isinstance(source.get('allowed_uses'), list) or any(not isinstance(x, str) or not x for x in source.get('allowed_uses', [])):
            c.error('list_type', path+'.allowed_uses', 'Allowed uses must be a list of nonempty strings')
        sid = source.get('id')
        if not isinstance(sid, str):
            c.error('source_id', path, 'Source identifier must be text'); continue
        if sid in by_id:
            c.error('duplicate_source', path, 'Source identifier repeated')
        by_id[sid] = source
        retrieved = c.day(source.get('retrieved_at'), path+'.retrieved_at')
        if retrieved and retrieved > c.as_of:
            c.error('future_source', path, 'Retrieval date is in the future')
        if source.get('valid_until'):
            end = c.day(source['valid_until'], path+'.valid_until')
            if end and retrieved and end < retrieved:
                c.error('date_order', path, 'Expiry precedes retrieval')
            if end and end < c.as_of:
                c.error('stale_source', path, 'Evidence validity expired; refresh or exclude it')
        if source.get('status') != 'current':
            c.error('stale_source', path, 'Active evidence must reference a current source')
        if 'path' in source:
            c.ref(source, path, require_hash=True)
        elif not isinstance(source.get('url'), str) or not source['url'].startswith('https://'):
            c.error('source_location', path, 'Supply local path/hash or HTTPS source URL')
        else:
            c.warnings.append({'code': 'remote_unverified', 'path': path, 'message': 'URL recorded only; no network request performed'})
    if data.get('readiness') not in {'ready', 'provisional', 'blocked'}:
        c.error('status', 'readiness', 'Unsupported readiness status')
    for group in ['findings', 'conflicts', 'asset_uses']:
        if not isinstance(data.get(group), list):
            c.error('list_type', group, 'Explicit list required'); return
    finding_ids = set()
    for i, finding in enumerate(data.get('findings', [])):
        if not isinstance(finding, dict):
            c.error('finding', f'findings.{i}', 'Expected object'); continue
        c.texts(finding, ['id', 'status', 'claim', 'reason'], f'findings.{i}')
        if finding.get('status') not in STATUSES | {'observed'}:
            c.error('status', f'findings.{i}', 'Unsupported finding status')
        fid = finding.get('id')
        if not isinstance(fid, str) or not fid or fid in finding_ids:
            c.error('duplicate_finding', f'findings.{i}', 'Finding IDs must be unique nonempty strings')
        else:
            finding_ids.add(fid)
        refs = finding.get('source_ids', [])
        if not isinstance(refs, list):
            c.error('source_reference', f'findings.{i}.source_ids', 'Source IDs must be a list'); continue
        if finding.get('status') in {'supplied', 'observed', 'evidenced', 'inferred'} and not refs:
            c.error('evidence_required', f'findings.{i}.source_ids', 'Evidence-backed finding needs sources')
        if any(not isinstance(x, str) or x not in by_id for x in refs):
            c.error('source_reference', f'findings.{i}.source_ids', 'Finding references an unknown source')
    for i, use in enumerate(data.get('asset_uses', [])):
        if not isinstance(use, dict):
            c.error('asset_rights', f'asset_uses.{i}', 'Expected asset-use object'); continue
        source = by_id.get(use.get('source_id'), {})
        intended = use.get('use')
        if source.get('rights') != 'production-authorized' or intended not in source.get('allowed_uses', []):
            c.error('asset_rights', f'asset_uses.{i}', 'Asset incorporation requires explicit authorization for this use')
    for i, conflict in enumerate(data.get('conflicts', [])):
        if not isinstance(conflict, dict):
            c.error('conflict', f'conflicts.{i}', 'Expected conflict object'); continue
        if conflict.get('status') not in {'resolved', 'unresolved'}:
            c.error('status', f'conflicts.{i}.status', 'Unsupported conflict status')
        if conflict.get('status') == 'resolved' and (not conflict.get('resolution') or not conflict.get('owner')):
            c.error('conflict_resolution', f'conflicts.{i}', 'Resolution requires rationale and owner')
        refs = conflict.get('source_ids', [])
        if not isinstance(refs, list) or any(not isinstance(x, str) or x not in by_id for x in refs):
            c.error('source_reference', f'conflicts.{i}.source_ids', 'Conflict source IDs must resolve')
    if data.get('readiness') == 'ready' and any(not isinstance(x, dict) or x.get('status') != 'resolved' for x in data.get('conflicts', [])):
        c.error('unresolved_conflict', 'conflicts', 'Unresolved conflicts prevent ready status')


def overlap(a, b):
    return a == b or a.startswith(b+'.') or b.startswith(a+'.')


def handoff(c, data):
    c.texts(data, ['record_id', 'scope', 'stage', 'readiness', 'requested_action', 'owner', 'next_action'])
    if data.get('scope') not in {'whole-project','phase-only','precise-change'}:
        c.error('scope', 'scope', 'Unsupported work scope')
    readinesses = {'ready','provisional','blocked'} | ({'draft'} if data.get('schema_version') == '1.0-proposed' else set())
    if data.get('readiness') not in readinesses or data.get('requested_action') not in {'prepare','execute','review'}:
        c.error('status', 'readiness', 'Unsupported readiness or action')
    if (data.get('scope') == 'precise-change' or 'requires_approved_baseline' in data) and not isinstance(data.get('requires_approved_baseline'), bool):
        c.error('boolean_type', 'requires_approved_baseline', 'Expected boolean')
    for group in ['inputs','outputs']:
        if not isinstance(data.get(group), list):
            c.error('list_type', group, 'Explicit list required'); return
    for group in ['inputs', 'outputs']:
        for i, ref in enumerate(data.get(group, [])):
            c.ref(ref, f'{group}.{i}', require_hash=True)
    if data.get('scope') == 'precise-change':
        baseline = data.get('baseline')
        if not isinstance(baseline, dict):
            c.error('baseline', 'baseline', 'Precise change requires baseline record')
        else:
            c.ref(baseline, 'baseline', require_hash=True)
            approval = baseline.get('approval', {})
            if data.get('requires_approved_baseline') and data.get('requested_action') == 'execute':
                if isinstance(approval, dict):
                    c.texts(approval, ['by','reference'], 'baseline.approval')
                if not isinstance(approval, dict) or approval.get('status') != 'approved' or not approval.get('by') or not approval.get('reference'):
                    c.error('baseline_approval', 'baseline.approval', 'Approved baseline reference and reviewer required; candidate approval is independent')
        delta, invariants = data.get('delta_paths'), data.get('invariants')
        if not isinstance(delta, list) or not delta or any(not isinstance(x, str) or not x for x in delta):
            c.error('delta', 'delta_paths', 'Specify nonempty requested paths'); delta = []
        if not isinstance(invariants, list) or not invariants or any(not isinstance(x, str) or not x for x in invariants):
            c.error('invariants', 'invariants', 'Specify nonempty invariant paths'); invariants = []
        if any(overlap(a, b) for a in delta for b in invariants):
            c.error('scope_overlap', 'delta_paths', 'Allowed delta overlaps a preserved invariant')
    registry = data.get('registry', {})
    rows = data.get('traceability', [])
    if not isinstance(registry, dict) or not isinstance(rows, list) or not rows:
        c.error('traceability', 'traceability', 'Registry and nonempty traceability required'); return
    subject_type = data.get('subject_type', 'persona')
    if not isinstance(subject_type, str) or subject_type not in {'persona', 'bounded_actor'}:
        c.error('subject_type', 'subject_type', 'Choose persona or bounded_actor; omission retains legacy persona mode')
        return
    actor_mode = subject_type == 'bounded_actor'
    excluded_group, excluded_field = ('personas', 'persona') if actor_mode else ('actors', 'actor')
    if excluded_group in registry or any(isinstance(row, dict) and excluded_field in row for row in rows):
        c.error('subject_ambiguity', 'registry', 'Actor and persona routes cannot be mixed; bounded actors require explicit subject_type')
    subject_field, subject_group = ('actor', 'actors') if actor_mode else ('persona', 'personas')
    # A local ID view preserves the caller's record and the legacy string-ID registry.
    registry_ids = dict(registry)
    if actor_mode:
        definitions = registry.get('actors')
        actor_ids = []
        fields = {'id', 'role', 'goal', 'context', 'evidence_class'}
        if not isinstance(definitions, list) or not definitions:
            c.error('actor_definition', 'registry.actors', 'A nonempty list of bounded actor definitions is required')
            definitions = []
        for i, actor in enumerate(definitions):
            path = f'registry.actors.{i}'
            if not isinstance(actor, dict):
                c.error('actor_definition', path, 'Expected id, role, goal, context and evidence_class')
                continue
            if set(actor) != fields:
                c.error('actor_definition', path, 'Only id, role, goal, context and evidence_class are supported')
            for field in ['id', 'role', 'goal', 'context']:
                value = actor.get(field)
                if not isinstance(value, str) or not value.strip() or value.strip().lower() in {'required', 'unknown', 'tbd', 'n/a'}:
                    c.error('actor_definition', path+'.'+field, 'Nonempty descriptive text required; unresolved placeholders cannot define a bounded actor')
            if not isinstance(actor.get('evidence_class'), str) or actor['evidence_class'] not in {'observed', 'supplied', 'inferred', 'proposed'}:
                c.error('actor_definition', path+'.evidence_class', 'Declare observed, supplied, inferred or proposed; classification is not factual verification')
            if isinstance(actor.get('id'), str):
                actor_ids.append(actor['id'])
        registry_ids['actors'] = actor_ids
    columns = {subject_field:subject_group, 'use_case':'use_cases', 'requirement':'requirements', 'decision':'decisions', 'criterion':'criteria'}
    for group in columns.values():
        ids = registry_ids.get(group)
        if not isinstance(ids, list) or not ids or any(not isinstance(x, str) or not x.strip() for x in ids):
            c.error('registry_ids', 'registry.'+group, 'Registry requires nonempty text identifiers')
        elif len(ids) != len(set(ids)):
            c.error('registry_ids', 'registry.'+group, 'Registry identifiers must be unique')
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            c.error('traceability', str(i), 'Expected trace row'); continue
        c.texts(row, list(columns), f'traceability.{i}')
        for key, group in columns.items():
            if not isinstance(registry_ids.get(group), list) or row.get(key) not in registry_ids[group]:
                c.error('trace_reference', f'traceability.{i}.{key}', 'Trace identifier not present in registry')
    if actor_mode:
        for field, group in columns.items():
            ids = registry_ids.get(group)
            if isinstance(ids, list) and all(isinstance(value, str) for value in ids):
                covered_ids = {row[field] for row in rows if isinstance(row, dict) and isinstance(row.get(field), str)}
                if set(ids) - covered_ids:
                    c.error('trace_coverage', 'registry.'+group, 'Every registered actor-route item must appear in a trace row')
    if data.get('schema_version') == '1.0-proposed':
        legacy_handoff_checks(c, data, registry)
    else:
        current_handoff_checks(c, data, registry)


def validate_check(c, check, path, criteria, candidate_artifacts=None):
    if not isinstance(check, dict):
        c.error('check', path, 'Expected check record'); return None
    if check.get('status') not in {'passed','failed','pending','not_applicable'}:
        c.error('status', path+'.status', 'Unsupported check status')
    if not isinstance(check.get('criterion'), str) or check.get('criterion') not in criteria:
        c.error('trace_reference', path+'.criterion', 'Check criterion must resolve in registry')
    if check.get('status') == 'passed' and not isinstance(check.get('evidence'), dict):
        c.error('check_evidence', path+'.evidence', 'Passed check needs evidence reference')
    if isinstance(check.get('evidence'), dict):
        c.ref(check['evidence'], path+'.evidence', require_hash=True)
    if candidate_artifacts is not None:
        artifacts = check.get('candidate_artifacts')
        if not isinstance(artifacts, list) or not artifacts:
            c.error('candidate_binding', path+'.candidate_artifacts', 'Current check requires candidate artifacts')
        else:
            bindings = artifact_identities(c, artifacts, path+'.candidate_artifacts')
            if bindings is not None and bindings != candidate_artifacts:
                c.error('candidate_binding', path+'.candidate_artifacts', 'Check must bind exactly to the declared candidate artifacts')
    return check


def artifact_identities(c, artifacts, path):
    if not isinstance(artifacts, list) or not artifacts:
        c.error('candidate_artifacts', path, 'At least one candidate artifact is required')
        return None
    identities = []
    for i, artifact in enumerate(artifacts):
        c.ref(artifact, f'{path}.{i}', require_hash=True)
        if isinstance(artifact, dict) and isinstance(artifact.get('path'), str) and isinstance(artifact.get('sha256'), str):
            identities.append((artifact['path'], artifact['sha256']))
    if len(identities) != len(artifacts):
        return None
    if len(identities) != len(set(identities)):
        c.error('candidate_artifacts', path, 'Candidate artifact path and hash pairs must be unique')
        return None
    return frozenset(identities)


def legacy_handoff_checks(c, data, registry):
    c.warnings.append({'code':'handoff_schema_migration', 'path':'schema_version', 'message':'Legacy 1.0-proposed handoff is readable only; migrate to schema 2.0 for candidate-bound current checks'})
    if data.get('completion', 'partial') not in {'partial', 'complete'}:
        c.error('status', 'completion', 'Unsupported completion state')
    if data.get('completion') == 'complete' or data.get('readiness') == 'ready':
        c.error('handoff_schema_migration', 'schema_version', 'Legacy handoffs cannot claim complete or ready; migrate explicitly to schema 2.0')
    checks = data.get('checks')
    if not isinstance(checks, list):
        c.error('list_type', 'checks', 'Explicit list required'); return
    for i, check in enumerate(checks):
        validate_check(c, check, f'checks.{i}', registry.get('criteria', []))


def current_handoff_checks(c, data, registry):
    if data.get('completion', 'partial') not in {'partial', 'complete'}:
        c.error('status', 'completion', 'Unsupported completion state')
    candidate = data.get('candidate')
    candidate_artifacts = artifact_identities(c, candidate.get('artifacts') if isinstance(candidate, dict) else None, 'candidate.artifacts')
    checks = data.get('current_checks')
    if not isinstance(checks, list):
        c.error('list_type', 'current_checks', 'Explicit current-check list required')
        checks = []
    criteria = registry.get('criteria', [])
    by_criterion = {}
    for i, check in enumerate(checks):
        validate_check(c, check, f'current_checks.{i}', criteria, candidate_artifacts)
        if isinstance(check, dict) and isinstance(check.get('criterion'), str) and check['criterion'] in criteria:
            by_criterion.setdefault(check['criterion'], []).append(check)
    if isinstance(criteria, list):
        for criterion in criteria:
            if len(by_criterion.get(criterion, [])) != 1:
                c.error('current_check_count', 'current_checks', 'Each required criterion requires exactly one current result')
    historical = data.get('historical_checks')
    if not isinstance(historical, list):
        c.error('list_type', 'historical_checks', 'Explicit historical-check list required')
    else:
        for i, check in enumerate(historical):
            validate_check(c, check, f'historical_checks.{i}', criteria)
            if isinstance(check, dict) and 'superseded_by' in check and (not isinstance(check['superseded_by'], str) or not check['superseded_by'].strip()):
                c.error('historical_reference', f'historical_checks.{i}.superseded_by', 'Historical supersession reference must be nonempty text')
    if data.get('completion') == 'complete' or data.get('readiness') == 'ready':
        if data.get('completion') == 'complete' and not data.get('outputs'):
            c.error('completion_outputs', 'outputs', 'Completed handoff requires actual output files')
        unresolved = [criterion for criterion in criteria if len(by_criterion.get(criterion, [])) != 1 or by_criterion[criterion][0].get('status') != 'passed' or not isinstance(by_criterion[criterion][0].get('evidence'), dict)]
        if unresolved:
            c.error('completion_checks', 'current_checks', 'Complete or ready handoff requires one passed current check with local evidence for every criterion')


def manifest(c, data):
    c.require(data, ['record_id', 'requested_use', 'toolchain', 'files'])
    c.texts(data, ['record_id','requested_use'])
    toolchain = data.get('toolchain', {})
    if not isinstance(toolchain, dict):
        c.error('toolchain', 'toolchain', 'Expected toolchain object'); return
    c.require(toolchain, ['medium', 'renderer', 'status'], 'toolchain')
    if toolchain.get('medium') not in {'web', 'app', 'static', 'motion', 'touch', 'fixture'}:
        c.error('medium', 'toolchain.medium', 'Unsupported medium')
    if toolchain.get('status') not in {'unverified', 'verified', 'blocked'}:
        c.error('status', 'toolchain.status', 'Unsupported toolchain status')
    if toolchain.get('status') == 'verified':
        proof = toolchain.get('reopen_evidence')
        if not isinstance(proof, dict):
            c.error('reopen_evidence', 'toolchain', 'Native reopen claim requires recorded local evidence')
        else:
            c.ref(proof, 'toolchain.reopen_evidence', require_hash=True)
    files = data.get('files', [])
    if not isinstance(files, list) or not files:
        c.error('files', 'files', 'Manifest requires files'); return
    seen = set()
    for i, item in enumerate(files):
        if not isinstance(item, dict):
            c.error('file_type', str(i), 'Expected file object'); continue
        c.require(item, ['id', 'role', 'allowed_uses'], f'files.{i}')
        key = item.get('id')
        if not isinstance(key, str) or key in seen:
            c.error('duplicate_file', str(i), 'File IDs must be unique strings')
        else:
            seen.add(key)
        c.ref(item, f'files.{i}', require_hash=True)
        if not isinstance(item.get('allowed_uses'), list) or data.get('requested_use') not in item['allowed_uses']:
            c.error('asset_rights', str(i), 'Requested use not recorded as permitted')


def validate(kind, data, root, as_of=None):
    c = Check(root, as_of)
    def report():
        result = c.result()
        if kind == 'reference-decision':
            result.update(decision_status=getattr(c, 'decision_status', 'invalid') if result['valid'] else 'invalid', executes=False)
        if kind == 'system-inventory':
            result.update(executes=False, coverage=getattr(c, 'inventory_coverage', {}))
        return result
    if c.errors:
        return report()
    if not isinstance(data, dict):
        c.error('record_type', '', 'Top-level record must be an object'); return report()
    if (kind == 'handoff' and data.get('schema_version') not in {'1.0-proposed', '2.0'}) or (kind != 'handoff' and data.get('schema_version') != VERSION):
        c.error('schema_version', 'schema_version', 'Unsupported contract version; explicit migration required')
    from .reference_decision import reference_decision
    from .system_inventory import system_inventory
    handler = {'system-inventory':system_inventory, 'reference-decision': reference_decision, 'persona': persona, 'evidence': evidence, 'handoff': handoff, 'manifest': manifest}.get(kind)
    if handler is None:
        c.error('kind', '', 'Unsupported validation kind')
    else:
        try:
            handler(c, data)
        except OSError:
            c.error('io_error', 'references', 'A referenced file could not be read')
        except (TypeError, KeyError, AttributeError, ValueError, RecursionError):
            c.error('malformed_record', '', 'Record contains malformed structure or an unreadable reference')
    return report()


def compare(before, after, allowed, invariants):
    """Exact JSON property comparison. Does not inspect rendered pixels."""
    for paths in [allowed, invariants]:
        if not isinstance(paths, list) or not paths or any(not isinstance(p, str) or not p or any(not part for part in p.split('.')) for p in paths):
            raise ValueError('Explicit nonempty property paths required')
    def flatten(value, prefix=''):
        if isinstance(value, dict) and value:
            out = {}
            for key, item in value.items():
                if not isinstance(key, str) or not key or '.' in key:
                    raise ValueError('Comparison keys must be nonempty strings without dots')
                out.update(flatten(item, prefix+'.'+key if prefix else key))
            return out
        return {prefix: value}
    a, b = flatten(before), flatten(after)
    changed = sorted(k for k in a.keys() | b.keys() if k not in a or k not in b or json.dumps(a[k], sort_keys=True, allow_nan=False) != json.dumps(b[k], sort_keys=True, allow_nan=False))
    errors = []
    for inv in invariants:
        if not any(k == inv or k.startswith(inv+'.') for k in a) or not any(k == inv or k.startswith(inv+'.') for k in b):
            errors.append({'code':'missing_invariant','path':inv,'message':'Invariant does not exist in both records'})
    for key in changed:
        if any(overlap(key, inv) for inv in invariants) or not any(key == path or key.startswith(path+'.') for path in allowed):
            errors.append({'code':'unauthorized_change','path':key,'message':'Change outside allowed delta or inside invariant'})
    return {'valid':not errors,'errors':errors,'changed_paths':changed,'assurance':'Exact JSON properties only; no visual or factual acceptance'}


def catalog_plan(catalog, selected):
    """Topological instruction plan, with no recursive stack or execution."""
    if not isinstance(catalog, dict) or not isinstance(catalog.get('capabilities'), list):
        raise ValueError('Catalog must contain a capability list')
    if catalog.get('schema_version', VERSION) != VERSION:
        raise ValueError('Unsupported catalog version')
    if not isinstance(selected, list) or not selected or any(not isinstance(x, str) or not x for x in selected):
        raise ValueError('Select nonempty capability IDs')
    by_id = {}
    for entry in catalog['capabilities']:
        if not isinstance(entry, dict) or not isinstance(entry.get('id'), str) or not entry['id'] or entry['id'] in by_id:
            raise ValueError('Capabilities need unique text IDs')
        deps = entry.get('depends_on', [])
        if not isinstance(deps, list) or any(not isinstance(x, str) or not x for x in deps):
            raise ValueError('Dependencies must be an ID list')
        by_id[entry['id']] = entry
    done, active, result = set(), set(), []
    for selected_id in selected:
        stack = [(selected_id, False)]
        while stack:
            key, finishing = stack.pop()
            if finishing:
                active.remove(key); done.add(key); result.append(key); continue
            if key in done: continue
            if key not in by_id: raise ValueError('Unknown capability dependency')
            if key in active: raise ValueError('Capability dependency cycle')
            active.add(key)
            stack.append((key, True))
            stack.extend((dep, False) for dep in reversed(by_id[key].get('depends_on', [])))
    return result
