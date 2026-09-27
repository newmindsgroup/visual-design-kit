"""Portable template-adoption regression tests."""
# Version-Timestamp: 2026-09-27 14:22:11 AST
import tempfile
import unittest
from pathlib import Path
import re

from scripts import adopt_template as subject


class TemplateAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.library = Path(__file__).resolve().parents[1]

    def test_apply_copies_template_and_pins_library_instruction_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "independent-project"
            project.mkdir()
            result = subject.adopt(
                "stage-execution.md", project, Path("records/stage.md"), apply=True
            )
            output = project / "records/stage.md"
            self.assertEqual(result["status"], "applied")
            self.assertTrue(output.is_file())
            text = output.read_text(encoding="utf-8")
            self.assertIn(f"](<{self.library / 'templates' / 'persona.md'}>)", text)
            self.assertIn("- REQUIRED packet ID/version/owner:", text)
            targets = re.findall(r"\]\(<(/[^)#\s]+)>", text)
            self.assertTrue(targets)
            for target in targets:
                self.assertTrue(Path(target).is_file(), target)

    def test_dry_run_is_default_and_does_not_create_project_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            result = subject.adopt("design-work.md", project, Path("records/design.md"))
            self.assertEqual(result["status"], "dry_run")
            self.assertFalse((project / "records/design.md").exists())

    def test_rejects_traversal_existing_output_and_symlink_escape(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            outside = Path(temporary) / "outside"
            project.mkdir()
            outside.mkdir()
            with self.assertRaises(ValueError):
                subject.adopt("design-work.md", project, Path("../escape.md"), apply=True)
            output = project / "records/design.md"
            output.parent.mkdir()
            output.write_text("keep", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                subject.adopt("design-work.md", project, Path("records/design.md"), apply=True)
            (project / "escape").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                subject.adopt("design-work.md", project, Path("escape/design.md"), apply=True)

    def test_resume_template_keeps_rejected_revision_out_of_canonical_state(self):
        template = (self.library / "templates/resume.md").read_text(encoding="utf-8")
        self.assertIn("`RESUME.md` is the canonical project state authority", template)
        self.assertIn("`CURRENT.md` is a legacy pointer only", template)
        self.assertIn("A rejected revision cannot replace the approved baseline", template)

    def test_pins_encoded_fragment_link_inside_angle_destination_for_spaced_library(self):
        with tempfile.TemporaryDirectory() as temporary:
            library = Path(temporary) / "library with spaces"
            templates = library / "templates"
            templates.mkdir(parents=True)
            target = templates / "persona notes.md"
            target.write_text("# Persona", encoding="utf-8")
            source = templates / "packet.md"
            source.write_text("# Packet", encoding="utf-8")
            original_root = subject.LIBRARY_ROOT
            subject.LIBRARY_ROOT = library
            try:
                actual = subject._pin_library_links(
                    '[persona](<persona%20notes.md#active-work> "source")', source
                )
            finally:
                subject.LIBRARY_ROOT = original_root
            self.assertEqual(
                actual,
                f'[persona](<{target.resolve()}#active-work> "source")',
            )

    def test_rejects_source_symlink_and_destination_directory_symlink(self):
        with tempfile.TemporaryDirectory() as temporary:
            temporary = Path(temporary)
            library = temporary / "library"
            templates = library / "templates"
            templates.mkdir(parents=True)
            (templates / "real.md").write_text("# Real", encoding="utf-8")
            (templates / "alias.md").symlink_to(templates / "real.md")
            project = temporary / "project"
            project.mkdir()
            original_library = subject.LIBRARY_ROOT
            original_templates = subject.TEMPLATE_ROOT
            subject.LIBRARY_ROOT = library
            subject.TEMPLATE_ROOT = templates
            try:
                with self.assertRaises(ValueError):
                    subject.adopt("alias.md", project, Path("record.md"), apply=True)
                actual = project / "actual"
                actual.mkdir()
                (project / "records").symlink_to(actual, target_is_directory=True)
                with self.assertRaises(ValueError):
                    subject.adopt("real.md", project, Path("records/record.md"), apply=True)
            finally:
                subject.LIBRARY_ROOT = original_library
                subject.TEMPLATE_ROOT = original_templates

    def test_does_not_pin_a_library_link_through_a_symlinked_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            temporary = Path(temporary)
            library = temporary / "library"
            templates = library / "templates"
            real = library / "real"
            templates.mkdir(parents=True)
            real.mkdir()
            (real / "guide.md").write_text("# Guide", encoding="utf-8")
            (templates / "linked").symlink_to(real, target_is_directory=True)
            source = templates / "packet.md"
            source.write_text("# Packet", encoding="utf-8")
            original_root = subject.LIBRARY_ROOT
            subject.LIBRARY_ROOT = library
            try:
                actual = subject._pin_library_links("[guide](linked/guide.md)", source)
            finally:
                subject.LIBRARY_ROOT = original_root
            self.assertEqual(actual, "[guide](linked/guide.md)")

    def test_adoption_ignores_stale_reference_configuration(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            private = project / 'private'
            private.mkdir()
            (private / 'reference-library.local.json').write_text('{stale configuration')
            result = subject.adopt('design-work.md', project, Path('records/design.md'))
            self.assertEqual(result['status'], 'dry_run')
            self.assertFalse((project / 'records/design.md').exists())
