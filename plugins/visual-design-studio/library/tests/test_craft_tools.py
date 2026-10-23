# Version-Timestamp: 2026-09-11T19:32:14-04:00
import unittest
from scripts.craft_tools import contrast, audit, render

class CraftToolsTests(unittest.TestCase):
    def fixture(self):
        return {'title':'Synthetic proof', 'text':'Clear ideas. Useful choices.', 'palettes':[{'id':'a','tokens':{'ink':'#000000','paper':'#ffffff'},'pairs':[{'id':'body','fg':'ink','bg':'paper','minimum':4.5}]}]}
    def test_known_contrast(self):
        self.assertAlmostEqual(contrast('#000000','#ffffff'),21)
        self.assertEqual(contrast('#abcabc','#abcabc'),1)
    def test_invalid_colors_rejected(self):
        for x in ['red','#abcd','#ffffff00','#gggggg']:
            with self.assertRaises(ValueError):contrast(x,'#ffffff')
    def test_pair_change_invalidation(self):
        data=self.fixture();old=audit(data);data['palettes'][0]['tokens']['ink']='#777777'
        new=audit(data,old)
        self.assertEqual(new['affected_pairs'],['a/body'])
        self.assertFalse(new['pairs'][0]['passes'])
    def test_missing_token_rejected(self):
        data=self.fixture();del data['palettes'][0]['tokens']['ink']
        with self.assertRaises(ValueError):audit(data)
    def test_unsafe_text_escaped(self):
        data=self.fixture();data['title']='<script>alert(1)</script>'
        self.assertNotIn('<script>alert(1)</script>',render(data))
        self.assertIn('&lt;script&gt;',render(data))
    def test_duplicate_pair_rejected(self):
        data=self.fixture();data['palettes'][0]['pairs']*=2
        with self.assertRaises(ValueError):audit(data)

    def test_custom_font_family(self):
        data=self.fixture();data['fonts']=[{'label':'Chosen family','family':'Georgia, serif'}]
        self.assertIn('Chosen family',render(data))
    def test_css_injection_rejected(self):
        data=self.fixture();data['fonts']=[{'label':'x','family':'Arial; background:url(https://example.com)'}]
        with self.assertRaises(ValueError):render(data)

    def test_remote_logo_rejected(self):
        data=self.fixture();data['logo_data']='https://example.com/logo.svg'
        with self.assertRaises(ValueError):render(data)
    def test_logo_sheet(self):
        data=self.fixture();data['logo_data']='data:image/png;base64,AAAA'
        self.assertEqual(render(data).count('alt="Supplied logo at'),8)
