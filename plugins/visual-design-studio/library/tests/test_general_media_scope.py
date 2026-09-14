# Version-Timestamp: 2026-09-12T11:33:18-04:00
import json,unittest
from pathlib import Path
class GeneralMediaScope(unittest.TestCase):
 def test_general_generation_does_not_require_display_brief(self):
  catalog={x['id']:x for x in json.loads((Path(__file__).resolve().parents[1]/'capabilities.json').read_text())['capabilities']}
  def closure(key,seen=None):
   seen=set() if seen is None else seen
   for dependency in catalog[key]['depends_on']:
    if dependency not in seen:seen.add(dependency);closure(dependency,seen)
   return seen
  for key in ['chatgpt-images','openart-cli','higgsfield-cli','media-image-repair']:
   with self.subTest(key=key):
    self.assertFalse(any(x.startswith(('display-','screen-')) for x in closure(key)))
  self.assertIn('display-discovery',closure('screen-compositing'))
