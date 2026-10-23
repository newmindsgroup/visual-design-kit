# Version-Timestamp: 2026-10-17 08:36:43 AST
import copy
import importlib.util
from pathlib import Path
import unittest
import subprocess
import tempfile
import json
import sys

p = Path(__file__).resolve().parents[1] / 'plugins/visual-design-studio/library/scripts/composition_checks.py'
spec = importlib.util.spec_from_file_location('composition_checks', p)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompositionTests(unittest.TestCase):
    def receipt(self):
        return {'unit': 'pt', 'font_evidence': 'synthetic-font-reference',
                'render_evidence': 'synthetic-render-reference', 'elements': [
                    {'id': 'service', 'insets': [15, 15, 15, 15], 'minimum_inset': 12,
                     'font_size': 9, 'minimum_font_size': 9, 'lines': 2, 'maximum_lines': 2,
                     'last_line_words': 3, 'clipped': False, 'gap_after': 16, 'minimum_gap_after': 12}]}

    def test_two_column_repair(self):
        repaired = self.receipt()
        original = copy.deepcopy(repaired)
        original['elements'][0].update(insets=[9]*4, lines=4, last_line_words=1, gap_after=4)
        self.assertEqual(len(module.check(original)), 4)
        self.assertEqual(module.check(repaired), [])

    def test_short_three_column_labels_allowed(self):
        receipt = self.receipt()
        receipt['elements'] = [dict(receipt['elements'][0], id=str(i), lines=1, last_line_words=1) for i in range(3)]
        self.assertEqual(module.check(receipt), [])

    def test_grouped_rows_require_gap(self):
        receipt = self.receipt()
        receipt['elements'][0]['gap_after'] = 0
        self.assertIn('insufficient section gap', str(module.check(receipt)))

    def test_clipping_and_small_type(self):
        receipt = self.receipt()
        receipt['elements'][0].update(clipped=True, font_size=8)
        self.assertEqual(len(module.check(receipt)), 2)

    def test_malformed_and_missing_evidence(self):
        self.assertTrue(module.check({}))
        for value in [float('nan'), float('inf'), -1, True, '9']:
            receipt = self.receipt()
            receipt['elements'][0]['font_size'] = value
            self.assertTrue(module.check(receipt))

    def test_fractional_counts_rejected(self):
        receipt = self.receipt()
        receipt['elements'][0]['lines'] = 1.5
        self.assertTrue(module.check(receipt))

    def test_oversized_integer_and_cli_result(self):
        receipt = self.receipt()
        receipt['elements'][0]['font_size'] = 10**400
        self.assertIn('finite nonnegative', str(module.check(receipt)))
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'receipt.json'
            file.write_text(json.dumps(receipt))
            result = subprocess.run([sys.executable, str(p), str(file)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)['status'], 'needs_review')
            self.assertEqual(result.stderr, '')

    def test_evidence_reference_requirements(self):
        for key, value in [('font_evidence', ''), ('font_evidence', ' '), ('render_evidence', None), ('render_evidence', 3)]:
            receipt = self.receipt()
            receipt[key] = value
            self.assertIn(key + ' reference required', module.check(receipt))

    def test_cli_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'receipt.json'
            file.write_text('{')
            result = subprocess.run([sys.executable, str(p), str(file)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)['status'], 'invalid')
