"""Version-Timestamp: 2026-10-27 07:53:44 AST. Bounded synthetic tool regression tests."""
import json
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def png(path,width,height,color):
    raw=b''.join(b'\x00'+bytes(color)*width for _ in range(height))
    def chunk(kind,body):
        return struct.pack('!I',len(body))+kind+body+struct.pack('!I',zlib.crc32(kind+body)&0xffffffff)
    path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!2I5B',width,height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b''))


@unittest.skipUnless(shutil.which('xcrun'),'macOS Swift toolchain required')
class ImageTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder=tempfile.TemporaryDirectory(prefix='bama-helper-test-')
        cls.work=Path(cls.folder.name)
        for name,source in [('measure','skills/bama-design-from-app/scripts/measure.swift'),('compare','skills/bama-design-from-app/scripts/compare.swift'),('layout','skills/bama-new-mac-app/template/tools/check-layout.swift')]:
            subprocess.run(['xcrun','swiftc',str(ROOT/source),'-o',str(cls.work/name)],check=True,capture_output=True,text=True)
        png(cls.work/'white.png',16,16,(255,255,255))
        png(cls.work/'black.png',16,16,(0,0,0))
        png(cls.work/'small.png',8,8,(255,255,255))

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def run_tool(self,name,*args):
        return subprocess.run([str(self.work/name),*map(str,args)],capture_output=True,text=True)

    def test_measure_info(self):
        result=self.run_tool('measure','info',self.work/'white.png')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('16 x 16 px',result.stdout)
        self.assertIn('scale unknown',result.stdout)
        self.assertNotIn('8 x 8 pt',result.stdout)

    def test_logical_info_requires_declared_scale(self):
        result=self.run_tool('measure','info',self.work/'white.png','--scale',2)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('8 x 8 pt',result.stdout)

    def test_coordinates_require_scale_or_pixel_mode(self):
        result=self.run_tool('measure','color',self.work/'white.png',0,0)
        self.assertEqual(result.returncode,2)
        self.assertIn('--scale',result.stdout)

    def test_pixel_coordinates_work_without_logical_scale(self):
        result=self.run_tool('measure','color',self.work/'white.png',0,0,'--pixels')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('#FFFFFF',result.stdout)

    def test_layout_area_only_does_not_pass(self):
        path=self.work/'area-only.json'
        path.write_text(json.dumps({'probes':[dict(kind='area',name='main',area='main',inset=0,x=0,y=0,width=16,height=16)]}))
        result=self.run_tool('layout',path)
        self.assertEqual(result.returncode,1)
        self.assertIn('no actual',result.stdout)

    def test_layout_rejects_duplicate_areas(self):
        area=dict(kind='area',name='main',area='main',inset=0,x=0,y=0,width=16,height=16)
        probe=dict(kind='probe',name='row',area='main',edge=None,inset=0,x=0,y=0,width=8,height=8)
        path=self.work/'duplicate-area.json';path.write_text(json.dumps({'probes':[area,area,probe]}))
        result=self.run_tool('layout',path)
        self.assertEqual(result.returncode,1)
        self.assertIn('duplicate',result.stdout)

    def test_layout_valid_probe_passes(self):
        area=dict(kind='area',name='main',area='main',inset=0,x=0,y=0,width=16,height=16)
        probe=dict(kind='probe',name='row',area='main',edge=None,inset=0,x=0,y=0,width=8,height=8)
        path=self.work/'valid-layout.json';path.write_text(json.dumps({'probes':[area,probe]}))
        result=self.run_tool('layout',path)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn('1 probes',result.stdout)

    def test_missing_crop_arguments_fail(self):
        self.assertEqual(self.run_tool('measure','crop',self.work/'white.png').returncode,2)

    def test_zero_scale_fails(self):
        self.assertEqual(self.run_tool('measure','info',self.work/'white.png','--scale','0').returncode,2)

    def test_outside_crop_fails_without_output(self):
        output=self.work/'invalid-crop.png'
        self.assertEqual(self.run_tool('measure','crop',self.work/'white.png',99,0,4,4,output,'--pixels').returncode,2)
        self.assertFalse(output.exists())

    def test_pixel_crop_has_exact_output_dimensions(self):
        output=self.work/'crop-exact.png'
        result=self.run_tool('measure','crop',self.work/'white.png',1,2,3,4,output,'--pixels')
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertEqual(struct.unpack('!II',output.read_bytes()[16:24]),(3,4))

    def test_zoom_crop_has_exact_output_dimensions(self):
        output=self.work/'crop-zoom.png'
        result=self.run_tool('measure','crop',self.work/'white.png',1,2,3,4,output,2,'--pixels')
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertEqual(struct.unpack('!II',output.read_bytes()[16:24]),(6,8))

    def test_asymmetric_crop_preserves_content(self):
        source=self.work/'asymmetric.png';output=self.work/'crop-asymmetric.png'
        raw=b'\x00'+bytes([255,0,0, 0,255,0, 0,0,255])+b'\x00'+bytes([255,255,0, 0,255,255, 255,0,255])
        def chunk(kind,body):
            return struct.pack('!I',len(body))+kind+body+struct.pack('!I',zlib.crc32(kind+body)&0xffffffff)
        source.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!2I5B',3,2,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b''))
        result=self.run_tool('measure','crop',source,1,0,2,2,output,'--pixels')
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        sample=self.run_tool('measure','color',output,0,0,1,0,0,1,1,1,'--pixels')
        self.assertEqual(sample.returncode,0,sample.stderr)
        self.assertEqual([line.split()[-1] for line in sample.stdout.splitlines()],['#00FF00','#0000FF','#00FFFF','#FF00FF'])

    def test_identical_images_pass(self):
        result=self.run_tool('compare',self.work/'white.png',self.work/'white.png',self.work/'same','--threshold',0)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('0.00%',result.stdout)
        self.assertTrue((self.work/'same/diff.png').is_file())

    def test_difference_exceeding_threshold_fails(self):
        result=self.run_tool('compare',self.work/'white.png',self.work/'black.png',self.work/'different','--threshold',2)
        self.assertEqual(result.returncode,1,result.stderr)
        self.assertIn('100.00%',result.stdout)

    def test_unequal_dimensions_fail(self):
        self.assertEqual(self.run_tool('compare',self.work/'white.png',self.work/'small.png',self.work/'dimensions').returncode,2)

    def test_roi_at_1x_uses_pixel_geometry(self):
        result=self.run_tool('compare',self.work/'white.png',self.work/'black.png',self.work/'roi1',0,0,8,8,'--scale',1)
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertIn('(64 of 64)',result.stdout)

    def test_roi_at_2x_uses_point_geometry(self):
        result=self.run_tool('compare',self.work/'white.png',self.work/'black.png',self.work/'roi2',0,0,8,8,'--scale',2)
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertIn('(256 of 256)',result.stdout)

    def test_roi_requires_explicit_scale(self):
        result=self.run_tool('compare',self.work/'white.png',self.work/'white.png',self.work/'no-scale',0,0,8,8)
        self.assertEqual(result.returncode,2)

    def test_layout_without_files_fails(self):
        self.assertEqual(self.run_tool('layout').returncode,2)

if __name__=='__main__':
    unittest.main()
