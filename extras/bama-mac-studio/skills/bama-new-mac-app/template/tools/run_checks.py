#!/usr/bin/env python3
"""Version-Timestamp: 2026-10-27 09:01:10 AST. Isolated native app checks."""
import argparse
import datetime
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path


# Change the declaration when adding application pages or Settings tabs. An
# unlisted app capture is a contract mismatch, never silently accepted coverage.
DEFAULT_PAGES = 'all,starred,settings'
DEFAULT_SETTINGS_TABS = 'general,appearance'
DEFAULT_APPEARANCES = 'light,dark'
SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def slugs(value, label):
    result = value.split(',')
    if not result or len(result) > 100 or any(not SLUG.fullmatch(item) for item in result):
        raise ValueError(label + ' must be a nonempty comma-separated list of lowercase slugs')
    if len(set(result)) != len(result):
        raise ValueError(label + ' must not contain duplicates')
    return result


def snapshot_matrix(pages, settings_tabs, appearances):
    expected = []
    for page in pages:
        for mode in appearances:
            if page == 'settings':
                expected.extend('settings-' + tab + '-' + mode for tab in settings_tabs)
            else:
                expected.append(page + '-' + mode)
    return expected


def png_dimensions(path):
    if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size <= 256 * 1024 * 1024:
        raise ValueError('PNG is missing, linked or outside the supported file-size bound')
    data = path.read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('PNG signature is invalid')
    offset, dimensions, saw_data, saw_end = 8, None, False, False
    while offset + 12 <= len(data):
        length = struct.unpack('>I', data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(data):
            raise ValueError('PNG chunk is truncated')
        payload = data[offset + 8:offset + 8 + length]
        checksum = struct.unpack('>I', data[offset + 8 + length:end])[0]
        if zlib.crc32(kind + payload) & 0xffffffff != checksum:
            raise ValueError('PNG chunk checksum is invalid')
        if dimensions is None:
            if kind != b'IHDR' or length != 13:
                raise ValueError('PNG has no leading IHDR')
            width, height = struct.unpack('>II', payload[:8])
            if not width or not height:
                raise ValueError('PNG dimensions are zero')
            dimensions = (width, height)
        if kind == b'IDAT' and length:
            saw_data = True
        if kind == b'IEND':
            if length or end != len(data):
                raise ValueError('PNG ending is invalid')
            saw_end = True
            break
        offset = end
    if not dimensions or not saw_data or not saw_end:
        raise ValueError('PNG is structurally incomplete')
    return dimensions


def window_number(value):
    if not isinstance(value, dict):
        return None
    number = value.get('number')
    return number if type(number) is int and number > 0 else None


def validate_snapshot(folder, expected):
    errors, verified = [], []
    report = {'expected': expected, 'verified': verified, 'errors': errors, 'native_accepted': False}
    if folder.is_symlink():
        errors.append('snapshot output directory must not be a symlink')
        return report
    if not folder.is_dir():
        errors.append('no PNG evidence was written; snapshot output directory is missing')
        return report
    if not list(folder.glob('*.png')):
        errors.append('no PNG evidence was written')
    manifest_path = folder / 'capture-manifest.json'
    try:
        if manifest_path.is_symlink() or manifest_path.stat().st_size > 2 * 1024 * 1024:
            raise ValueError('manifest must be a bounded regular file')
        manifest = json.loads(manifest_path.read_text())
    except (OSError, ValueError) as error:
        errors.append('capture manifest unavailable or invalid: ' + str(error))
        return report
    if not isinstance(manifest, dict) or type(manifest.get('schema_version')) is not int or manifest.get('schema_version') != 1:
        errors.append('capture manifest schema is invalid')
        return report
    requested = manifest.get('requested')
    if not isinstance(requested, list) or len(requested) != len(expected) or set(str(x) for x in requested) != set(expected):
        errors.append('app requested matrix differs from the independently declared matrix')
    if manifest.get('completed') is not True:
        errors.append('app did not complete the requested capture run')
    if manifest.get('native_complete') is not True:
        errors.append('app reports incomplete or degraded native captures')
    failures = manifest.get('failures')
    if not isinstance(failures, list) or failures:
        errors.append('app reports capture failures: ' + str(failures))
    windows = manifest.get('windows')
    if not isinstance(windows, dict):
        errors.append('window identity map is missing')
        windows = {}
    if any(capture_id.startswith('settings-') for capture_id in expected):
        main_number = window_number(windows.get('main'))
        settings_number = window_number(windows.get('settings'))
        if main_number is None or settings_number is None or main_number == settings_number:
            errors.append('Settings window must have its own distinct recorded window identity')
    captures = manifest.get('captures')
    if not isinstance(captures, list):
        errors.append('capture records must be a list')
        return report
    seen = set()
    for capture in captures:
        if not isinstance(capture, dict):
            errors.append('capture record is not an object')
            continue
        capture_id = capture.get('id')
        if not isinstance(capture_id, str) or capture_id not in expected:
            errors.append('unexpected capture ID: ' + str(capture_id))
            continue
        if capture_id in seen:
            errors.append('duplicate capture ID: ' + capture_id)
            continue
        seen.add(capture_id)
        before = len(errors)
        role = 'settings' if capture_id.startswith('settings-') else 'main'
        if capture.get('window_role') != role or window_number(capture.get('window')) != window_number(windows.get(role)) or window_number(capture.get('window')) is None:
            errors.append(capture_id + ': actual window identity does not match its declared role')
        if capture.get('status') != 'native' or capture.get('method') != 'screencapture':
            errors.append(capture_id + ': failed or degraded capture is not native acceptance')
        if capture.get('errors') != []:
            errors.append(capture_id + ': capture errors remain')
        filename = capture_id + '.png'
        if capture.get('filename') != filename:
            errors.append(capture_id + ': PNG filename does not match its capture ID')
        try:
            dimensions = png_dimensions(folder / filename)
            if type(capture.get('pixel_width')) is not int or type(capture.get('pixel_height')) is not int or dimensions != (capture.get('pixel_width'), capture.get('pixel_height')):
                errors.append(capture_id + ': PNG dimensions differ from the capture record')
        except (OSError, ValueError) as error:
            errors.append(capture_id + ': invalid PNG evidence: ' + str(error))
        if before == len(errors):
            verified.append(capture_id)
    for capture_id in expected:
        if capture_id not in seen:
            errors.append('missing capture ID: ' + capture_id)
    report['native_accepted'] = not errors and len(verified) == len(expected)
    return report


def validate_selftest(root, process_exit_code):
    errors = []
    report = {'valid_completion': False, 'passed': False, 'errors': errors}
    path = root / 'selftest-completion.json'
    try:
        if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size <= 65536:
            raise ValueError('completion receipt must be a bounded regular file')
        value = json.loads(path.read_text())
    except (OSError, ValueError) as error:
        errors.append('self-test completion receipt unavailable or invalid: ' + str(error))
        return report
    if not isinstance(value, dict) or type(value.get('schema_version')) is not int or value.get('schema_version') != 1:
        errors.append('self-test completion schema is invalid')
        return report
    if value.get('started') is not True or value.get('completed') is not True:
        errors.append('self-test did not complete after starting')
    status = value.get('status')
    if status not in ('passed', 'failed'):
        errors.append('self-test has no final passed/failed status')
    if type(value.get('exit_code')) is not int or value['exit_code'] != process_exit_code:
        errors.append('self-test receipt exit code differs from the process exit')
    count = value.get('check_count')
    checks = value.get('checks')
    required = value.get('required_check_ids')
    required_count = value.get('required_check_count')
    if type(count) is not int or not 0 < count <= 256:
        errors.append('self-test must execute a nonzero bounded number of checks')
    if not isinstance(required, list) or not required or len(required) > 256 or any(not isinstance(item, str) or not SLUG.fullmatch(item) or len(item) > 64 for item in required):
        errors.append('self-test required check IDs are invalid')
        required = []
    if len(set(required)) != len(required) or type(required_count) is not int or required_count != len(required):
        errors.append('self-test required check count is inconsistent')
    ids, failed = [], []
    if not isinstance(checks, list) or len(checks) > 256 or len(checks) != count:
        errors.append('self-test check records differ from the executed check count')
        checks = []
    for check in checks:
        if not isinstance(check, dict) or not isinstance(check.get('id'), str) or len(check['id']) > 64 or not SLUG.fullmatch(check['id']) or type(check.get('passed')) is not bool:
            errors.append('self-test check record is invalid')
            continue
        ids.append(check['id'])
        if check['passed'] is False:
            failed.append(check['id'])
    if len(set(ids)) != len(ids):
        errors.append('self-test contains duplicate check IDs')
    failures = value.get('failures')
    if not isinstance(failures, list) or len(failures) > 256 or any(not isinstance(item, str) or len(item) > 512 for item in failures):
        errors.append('self-test failure evidence is invalid')
        failures = []
    missing = sorted(set(required) - set(ids))
    if status == 'passed':
        if process_exit_code != 0 or failed or failures or missing:
            errors.append('self-test success requires every required check to pass and process exit zero')
    elif status == 'failed':
        if process_exit_code == 0 or not failures:
            errors.append('self-test failure must have a matching nonzero process exit and failure evidence')
    report.update({'status': status, 'check_count': count, 'required_check_count': required_count, 'checked_ids': ids, 'missing_required': missing, 'failures': failures})
    report['valid_completion'] = not errors
    report['passed'] = not errors and status == 'passed'
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('selftest', 'snapshot', 'agent'))
    parser.add_argument('binary', help='Explicit staged executable path')
    parser.add_argument('--timeout', type=int, default=180)
    parser.add_argument('--pages', help='Snapshot page slugs, including settings when needed')
    parser.add_argument('--settings-tabs', help='Declared Settings tab slugs')
    parser.add_argument('--appearances', help='Snapshot appearances: light,dark by default')
    args = parser.parse_args()
    binary = Path(args.binary).expanduser().resolve(strict=True)
    if not binary.is_file() or not os.access(binary, os.X_OK):
        parser.error('binary must be an executable file')
    if not 1 <= args.timeout <= 600:
        parser.error('timeout must be 1 to 600 seconds')
    expected = None
    if args.mode == 'snapshot':
        pages = slugs(args.pages if args.pages is not None else os.environ.get('APP_SNAPSHOT_PAGES', DEFAULT_PAGES), 'pages')
        tabs = slugs(args.settings_tabs if args.settings_tabs is not None else os.environ.get('APP_SNAPSHOT_SETTINGS_TABS', DEFAULT_SETTINGS_TABS), 'settings tabs')
        appearances = slugs(args.appearances if args.appearances is not None else os.environ.get('APP_SNAPSHOT_APPEARANCES', DEFAULT_APPEARANCES), 'appearances')
        if any(mode not in ('light', 'dark') for mode in appearances):
            parser.error('snapshot appearances must be light and/or dark')
        expected = snapshot_matrix(pages, tabs, appearances)
    root = Path(tempfile.mkdtemp(prefix='bama-test-')).resolve()
    root.chmod(0o700)
    (root / '.bama-test-root').write_text('BAMA isolated test root\n')
    env = {**os.environ, 'APP_TEST_ROOT': str(root), 'APP_STORE': str(root / 'test.store'), 'APP_AGENT_SOCKET': str(root / 'agent.sock')}
    for key in ('APP_AGENT_WRITES', 'APP_AGENT_ENABLED', 'APP_SEED', 'APP_SNAPSHOT', 'APP_SNAPSHOT_PAGES', 'APP_SNAPSHOT_SETTINGS_TABS', 'APP_SNAPSHOT_APPEARANCES', 'APP_SNAPSHOT_EXPECTED'):
        env.pop(key, None)
    if args.mode == 'snapshot':
        env.update({'APP_SEED': '1', 'APP_SNAPSHOT': str(root / 'shots'), 'APP_SNAPSHOT_EXPECTED': json.dumps(expected), 'APP_SNAPSHOT_APPEARANCES': ','.join(appearances)})
        # Preserve an unset page filter: the app must declare every actual page,
        # and adding a page without updating this matrix must fail coverage.
        if args.pages is not None or 'APP_SNAPSHOT_PAGES' in os.environ:
            env['APP_SNAPSHOT_PAGES'] = ','.join(pages)
        if args.settings_tabs is not None or 'APP_SNAPSHOT_SETTINGS_TABS' in os.environ:
            env['APP_SNAPSHOT_SETTINGS_TABS'] = ','.join(tabs)
    command = [str(binary)] + (['--selftest'] if args.mode == 'selftest' else [])
    print(f'BAMA_TEST_ROOT={root}', flush=True)
    receipt = {'Version-Timestamp': datetime.datetime.now().astimezone().isoformat(), 'mode': args.mode, 'isolated': True}
    try:
        result = subprocess.run(command, env=env, capture_output=True, text=True, timeout=args.timeout)
        (root / 'stdout.log').write_text(result.stdout)
        (root / 'stderr.log').write_text(result.stderr)
        print(result.stdout, end='')
        print(result.stderr, end='', file=sys.stderr)
        code = result.returncode
        receipt['process_exit_code'] = code
        if args.mode == 'selftest':
            validation = validate_selftest(root, code)
            receipt['selftest'] = validation
            if not validation['passed']:
                for error in validation['errors']:
                    print('self-test failed: ' + error, file=sys.stderr)
                code = code or 1
        if args.mode == 'snapshot':
            validation = validate_snapshot(root / 'shots', expected)
            receipt['snapshot'] = validation
            if not validation['native_accepted']:
                for error in validation['errors']:
                    print('snapshot failed: ' + error, file=sys.stderr)
                code = code or 1
    except subprocess.TimeoutExpired as error:
        def text(value):
            return value.decode(errors='replace') if isinstance(value, bytes) else value or ''
        (root / 'stdout.log').write_text(text(error.stdout))
        (root / 'stderr.log').write_text(text(error.stderr))
        print('check timed out; inspect the preserved isolated root', file=sys.stderr)
        receipt['timed_out'] = True
        code = 1
    receipt['exit_code'] = code
    (root / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return code


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f'check refused: {error}', file=sys.stderr)
        raise SystemExit(1)
