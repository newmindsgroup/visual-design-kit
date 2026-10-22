# Version-Timestamp: 2026-10-22 08:20:00 AST
"""Behavioral gates for a private, portable persona workbench."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'plugins/visual-design-studio/library/scripts/persona_workbench.py'
spec = importlib.util.spec_from_file_location('persona_workbench', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class WorkbenchTests(unittest.TestCase):
    def collection(self):
        return module.demo_collection()

    def test_complete_collection_and_all_fields_survive(self):
        data = self.collection()
        self.assertEqual(len(data['records']), 3)
        self.assertEqual(module.validate(data), [])
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'personas.html'
            module.build(data, target)
            html = target.read_text()
            embedded = html.split('<script id="persona-data" type="application/json">')[1].split('</script>')[0]
            decoded = json.loads(embedded)
            self.assertEqual(decoded['collection'], data)
            self.assertEqual(len(decoded['definitions']),118)

    def test_missing_fields_and_unknown_reference_fail(self):
        data = self.collection()
        del data['records'][0]['fields']['jtbd']
        self.assertTrue(module.validate(data))
        data = self.collection()
        data['mapping']['pages'][0]['primary_ids']=['not-a-persona']
        self.assertTrue(module.validate(data))

    def test_script_injection_is_encoded_not_executable(self):
        data = self.collection()
        value='</script><script>alert("unsafe")</script>'
        data['records'][0]['fields']['quote'].update(value=value,status='synthetic')
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'p.html';module.build(data,p);html=p.read_text()
            self.assertNotIn(value,html)
            self.assertIn('\\u003c/script',html)

    def test_unknowns_remain_unknown_and_duplicates_rejected(self):
        data = self.collection()
        data['records'][0]['fields']['quote'].update(value=None,status='unknown',reason='No interview quote supplied')
        self.assertEqual(module.validate(data),[])
        data['records'][1]['record_id']=data['records'][0]['record_id']
        self.assertTrue(module.validate(data))

    def test_invalid_mapping_weight_and_unsafe_theme_rejected(self):
        data=self.collection();data['mapping']['pages'][0]['weights_by_persona']['demo-1']=-1
        self.assertTrue(module.validate(data))
        data=self.collection();data['theme']={'accent':'red; background:url(https://example.com)'}
        self.assertTrue(module.validate(data))

    def test_legacy_objects_and_partial_translations_keep_item_links(self):
        legacy={'personas':[{'id':'sample','name':'Perfil','shortName':'Perfil','painPoints':[{'pain':'Dolor','urgency':'high'}],'competitiveContext':{'competitorPerceptions':{'Generic alternative':'Local perception'}},'translations':{'en':{'name':'Profile','painPoints':[{'pain':'Pain'}]}}}]}
        result=module.from_legacy(legacy)
        self.assertEqual(module.validate(result),[])
        fields=result['records'][0]['fields']
        self.assertEqual(fields['name']['translations']['en']['value'],'Profile')
        self.assertEqual(fields['painPoints[].pain']['value'][0]['item_id'],fields['painPoints[].urgency']['value'][0]['item_id'])
        self.assertEqual(fields['competitiveContext.competitorPerceptions[].competitor']['value'][0]['text'],'Generic alternative')
        self.assertEqual(fields['competitiveContext.competitorPerceptions[].perception']['value'][0]['text'],'Local perception')
        self.assertNotIn('translations',fields['painPoints[].urgency'])

    def test_legacy_unknown_id_mapping_rejected_not_silently_repaired(self):
        result=module.from_legacy({'personas':[{'id':'sample','name':'Example'}]}, {'pages':{'home':{'primary':['wrong-id']}}})
        self.assertTrue(module.validate(result))

    def test_authorized_local_portrait_embeds_and_escape_is_rejected(self):
        import base64
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);asset=root/'face.png';asset.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII='))
            data=self.collection();data['records'][0]['fields']['image'].update(value='face.png',status='synthetic')
            module.build(data,root/'p.html',portrait_root=root)
            self.assertIn('data:image/png;base64,',(root/'p.html').read_text())
            data['records'][0]['fields']['image']['value']='../outside.png'
            with self.assertRaises(ValueError):module.build(data,root/'escape.html',portrait_root=root)

    def test_existing_persona_validator_accepts_generated_records(self):
        import sys
        sys.path.insert(0,str(ROOT/'plugins/visual-design-studio/library'))
        from design_system.validation import Check, persona
        for record in self.collection()['records']+module.from_legacy({'personas':[{'id':'sample','name':'Example','painPoints':[{'pain':'Context lost','urgency':'high'}]}]})['records']:
            c=Check(ROOT,None);persona(c,record)
            self.assertEqual(c.errors,[])

    def test_malformed_translations_sections_and_unassigned_weights_rejected(self):
        for sections in [{},[None],[{'section_type':'hero','persona_usage':['unknown-id']}]]:
            data=self.collection();data['mapping']['sections']=sections
            self.assertTrue(module.validate(data))
        data=self.collection();data['records'][0]['fields']['jtbd']['translations']={'es':None}
        self.assertTrue(module.validate(data))
        data=self.collection();data['mapping']['pages'][0]['tertiary_ids']=[]
        self.assertTrue(module.validate(data))

    def test_overflow_and_malformed_paths_return_validation_errors(self):
        data=self.collection();data['mapping']['pages'][0]['weights_by_persona']={'demo-1':1e308,'demo-2':1e308}
        self.assertTrue(module.validate(data))
        data=self.collection();data['mapping']['pages'][0]['path']=[]
        self.assertTrue(module.validate(data))
        data=self.collection();data['records'][0]['fields']['name']['translations']={'es':{'value':{'unexpected':'shape'}}}
        self.assertTrue(module.validate(data))

    def test_refuses_to_overwrite_existing_deliverable(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'p.html';p.write_text('existing')
            with self.assertRaises(FileExistsError):module.build(self.collection(),p)
            self.assertEqual(p.read_text(),'existing')

if __name__=='__main__':unittest.main()
