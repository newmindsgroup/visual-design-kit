"""Publication boundary tests for the fictional website fixture."""
# Version-Timestamp: 2026-09-11T20:58:31-04:00
import unittest,tempfile
from pathlib import Path
from scripts.website_fixture import render
class WebsiteFixtureTests(unittest.TestCase):
 def test_drafts_absent_from_html(self):
  out=render([{'status':'draft','title':'PRIVATE SENTINEL','body':'hidden','image':False},{'status':'published','title':'Visible','body':'copy','image':True}])
  self.assertNotIn('PRIVATE SENTINEL',out);self.assertIn('Visible',out)
 def test_absent_image_omits_figure(self):
  out=render([{'status':'published','title':'Long title '*12,'body':'copy','image':False}])
  self.assertNotIn('<figure',out);self.assertIn('Long title '*12,out)
 def test_escapes_editorial_markup(self):
  out=render([{'status':'published','title':'<script>bad</script>','body':'A & B','image':False}])
  self.assertIn('&lt;script&gt;',out);self.assertIn('A &amp; B',out)
 def test_invalid_status_rejected(self):
  with self.assertRaises(ValueError):render([{'status':'publised','title':'x','body':'x','image':False}])
 def test_missing_required_field_rejected(self):
  with self.assertRaises(ValueError):render([{'status':'published','body':'x','image':False}])
 def test_build_excludes_drafts_and_refuses_overwrite(self):
  from scripts.website_fixture import build
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'site';build(p)
   self.assertEqual({f.name for f in p.iterdir()},{'index.html','long.html','style.css','form.mjs','form-model.mjs'})
   self.assertTrue(all('PRIVATE DRAFT SENTINEL' not in f.read_text() for f in p.iterdir()))
   with self.assertRaises(FileExistsError):build(p)
