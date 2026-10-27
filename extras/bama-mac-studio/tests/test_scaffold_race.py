"""A concurrent destination creator must never lose its directory.

Version-Timestamp: 2026-10-27 08:03:29 AST
"""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/bama-new-mac-app/scripts/scaffold.py'

class ScaffoldOwnership(unittest.TestCase):
    def test_destination_created_after_precheck_is_preserved(self):
        spec = importlib.util.spec_from_file_location('bama_scaffold', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory).resolve()
            dest = parent / 'Probe'
            marker = dest / 'other-owner.txt'
            exists = Path.exists
            injected = [False]
            def concurrent_exists(path):
                if path == dest and not injected[0]:
                    injected[0] = True
                    dest.mkdir()
                    marker.write_text('other actor owns this')
                    return False
                return exists(path)
            with mock.patch.object(sys, 'argv', ['scaffold', 'Probe', 'com.example.probe', str(parent)]):
                with mock.patch.object(Path, 'exists', concurrent_exists):
                    with self.assertRaises((OSError, SystemExit)):
                        module.main()
            self.assertTrue(marker.is_file(), 'cleanup removed a destination it never owned')
            self.assertEqual(marker.read_text(), 'other actor owns this')

if __name__ == '__main__':
    unittest.main()
