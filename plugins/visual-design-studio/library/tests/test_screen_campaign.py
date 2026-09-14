"""Screen campaign build contract, isolated from players and providers."""
# Version-Timestamp: 2026-09-11 20:20:00 AST
import copy
import json
import tempfile
import unittest
from pathlib import Path
from scripts import screen_campaign as subject

FIXTURE = {'Version-Timestamp':'2026-09-11T20:20:00-04:00','id':'rill-v1','brand':'RILL','headline':['A little','refreshment.'],'subtitle':'STILL WATER / FICTIONAL STUDY','background':'#102D32','foreground':'#F5F1E7','accent':'#D3EA85','variants':['wide','portrait','strip']}

class CampaignTests(unittest.TestCase):
    def test_build_and_verify_reproducibly(self):
        with tempfile.TemporaryDirectory() as tmp:
            a,b=Path(tmp)/'a',Path(tmp)/'b'
            subject.build(FIXTURE,a);subject.build(FIXTURE,b)
            self.assertEqual(subject.verify(a),[])
            self.assertEqual((a/'manifest.json').read_bytes(),(b/'manifest.json').read_bytes())
            self.assertEqual(len(list(a.glob('*.svg'))),3)
    def test_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a';subject.build(FIXTURE,p)
            with self.assertRaises(ValueError):subject.build(FIXTURE,p)
            self.assertEqual(subject.verify(p),[])
    def test_invalid_fields_fail_without_output(self):
        for key,value in [('id','../escape'),('accent','red;url(http://bad)'),('headline',['x'*100]),('variants',['wide','wide']),('variants',['unknown']),('brand',''),('Version-Timestamp','yesterday')]:
            with self.subTest(key=key),tempfile.TemporaryDirectory() as tmp:
                data=copy.deepcopy(FIXTURE);data[key]=value;p=Path(tmp)/'out'
                with self.assertRaises(ValueError):subject.build(data,p)
                self.assertFalse(p.exists())
    def test_text_is_escaped(self):
        import xml.etree.ElementTree as ET
        with tempfile.TemporaryDirectory() as tmp:
            data=copy.deepcopy(FIXTURE);data['brand']='<R&>'
            subject.build(data,Path(tmp)/'a')
            root=ET.parse(Path(tmp)/'a'/'wide.svg').getroot()
            self.assertIn('<R&>', ''.join(root.itertext()))
            self.assertNotIn('<script', (Path(tmp)/'a'/'wide.svg').read_text())
    def test_detects_changed_missing_and_extra_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a';subject.build(FIXTURE,p)
            (p/'wide.svg').write_text('altered');(p/'strip.svg').unlink();(p/'extra.txt').write_text('unexpected')
            errors=subject.verify(p)
            self.assertTrue(any('wide.svg' in x for x in errors))
            self.assertTrue(any('strip.svg' in x for x in errors))
            self.assertTrue(any('extra.txt' in x for x in errors))
    def test_rejects_manifest_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a';subject.build(FIXTURE,p)
            m=json.loads((p/'manifest.json').read_text());m['files']['../outside']='0'*64
            (p/'manifest.json').write_text(json.dumps(m))
            self.assertTrue(subject.verify(p))
    def test_rejects_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a';subject.build(FIXTURE,p)
            original=p/'wide.svg';original.unlink();original.symlink_to(p/'portrait.svg')
            self.assertTrue(subject.verify(p))

    def test_detects_removed_variant_even_when_manifest_is_edited(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a';subject.build(FIXTURE,p)
            m=json.loads((p/'manifest.json').read_text());del m['files']['strip.svg']
            (p/'strip.svg').unlink();(p/'manifest.json').write_text(json.dumps(m))
            self.assertTrue(subject.verify(p))
