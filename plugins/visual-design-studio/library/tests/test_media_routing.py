# Version-Timestamp: 2026-09-11T21:30:44-04:00
import json
import unittest
from pathlib import Path
from design_system.validation import catalog_plan
ROOT=Path(__file__).resolve().parents[1]
class MediaRoutingTests(unittest.TestCase):
 def setUp(self):self.catalog=json.loads((ROOT/'capabilities.json').read_text())
 def test_all_generation_routes_prepare_references_and_selection(self):
  for route in ['higgsfield-cli','openart-cli','chatgpt-images']:
   with self.subTest(route=route):
    plan=catalog_plan(self.catalog,[route])
    for prerequisite in ['media-art-direction','media-reference-control','media-route-selection']:
     self.assertIn(prerequisite,plan)
     self.assertLess(plan.index(prerequisite),plan.index(route))
    self.assertEqual(len(plan),len(set(plan)))
 def test_scenarios_select_complete_ordered_stage_sets(self):
  cases=json.loads((ROOT/'examples/media-quality-recipes/routes.json').read_text())['scenarios']
  self.assertEqual(set(cases),{'still','motion','touch'})
  for name,stages in cases.items():
   names=[stage['stage'] for stage in stages]
   self.assertLess(names.index('prepare'),names.index('generate-candidate'))
   self.assertLess(names.index('generate-candidate'),names.index('review-source'))
   self.assertLess(names.index('review-source'),names.index('compose'))
   self.assertLess(names.index('finish-and-fallback'),names.index('review-campaign'))
   seen=set()
   for stage in stages:
    plan=catalog_plan(self.catalog,stage['select'])
    seen.update(plan)
   for owner in ['media-quality-evaluation','screen-finishing','display-production','display-evaluation']:
    self.assertIn(owner,seen,name)
   self.assertNotIn('openart-cli',seen)
   self.assertNotIn('higgsfield-cli',seen)
  self.assertTrue({'screen-animation','screen-loops'} <= set(c for s in cases['motion'] for c in s['select']))
  self.assertTrue({'touch-media','touch-states-copy','touch-device-validation'} <= set(c for s in cases['touch'] for c in s['select']))
