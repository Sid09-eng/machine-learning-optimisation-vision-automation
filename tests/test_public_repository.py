"""Safety and presentation checks for the curated public repository."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicRepositoryTests(unittest.TestCase):
    def test_public_landing_and_ignore_rules_exist(self):
        readme = ROOT / "README.md"
        gitignore = ROOT / ".gitignore"

        self.assertTrue(readme.exists(), "Public profile README is missing")
        self.assertTrue(gitignore.exists(), "Safety .gitignore is missing")

        readme_text = readme.read_text(encoding="utf-8")
        ignore_text = gitignore.read_text(encoding="utf-8")
        self.assertIn("# Applied ML & Materials Portfolio", readme_text)
        self.assertIn("projects/", readme_text)
        for required_rule in (".env", ".venv/", ".coursework-venv/", ".week7-venv/", "/tools/"):
            self.assertIn(required_rule, ignore_text)

    def test_every_featured_project_has_portfolio_safe_case_study(self):
        projects = (
            "alloy-property-optimisation",
            "bayesian-optimisation-for-strength",
            "conditional-generative-design",
            "computer-vision-segmentation",
            "lab-automation-protocol",
        )
        required_sections = ("## Problem", "## Approach", "## Skills", "## Reproduce", "## Limits")
        forbidden_coursework_labels = ("matriculation", "homework", "in-class", "assignment")

        for project in projects:
            readme = ROOT / "projects" / project / "README.md"
            self.assertTrue(readme.exists(), f"Missing project README: {project}")
            text = readme.read_text(encoding="utf-8").lower()
            for section in required_sections:
                self.assertIn(section.lower(), text, f"{project} is missing {section}")
            self.assertTrue("source" in text or "data" in text, f"{project} lacks provenance")
            for label in forbidden_coursework_labels:
                self.assertNotIn(label, text, f"{project} exposes coursework label: {label}")

    def test_featured_projects_have_inspectable_code_and_shared_setup(self):
        expected_artifacts = (
            "projects/alloy-property-optimisation/composition_constraints.py",
            "projects/bayesian-optimisation-for-strength/evaluate_model.py",
            "projects/conditional-generative-design/data_pipeline.py",
            "projects/computer-vision-segmentation/segment.py",
            "projects/lab-automation-protocol/rainbow_gradient.py",
            "requirements.txt",
            "docs/portfolio-methodology.md",
            "LICENSE",
        )

        for relative_path in expected_artifacts:
            self.assertTrue((ROOT / relative_path).exists(), f"Missing public artifact: {relative_path}")

    def test_public_copy_avoids_generic_portfolio_language(self):
        visible_docs = [
            ROOT / "README.md",
            ROOT / "docs" / "portfolio-methodology.md",
            *sorted((ROOT / "projects").glob("*/README.md")),
        ]
        template_phrases = (
            "curated",
            "case study",
            "working principles",
            "portfolio curation",
            "portfolio-safe",
            "scope statement",
        )

        for path in visible_docs:
            text = path.read_text(encoding="utf-8").lower()
            for phrase in template_phrases:
                self.assertNotIn(phrase, text, f"{path.relative_to(ROOT)} uses generic phrase: {phrase}")


if __name__ == "__main__":
    unittest.main()
