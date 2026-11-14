"""Checks for public visual evidence and result explanations."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = (
    "alloy-property-optimisation",
    "bayesian-optimisation-for-strength",
    "conditional-generative-design",
    "computer-vision-segmentation",
    "lab-automation-protocol",
    "materials-informatics-and-cheminformatics",
)
FIGURES = (
    "projects/alloy-property-optimisation/assets/test-predictions.png",
    "projects/alloy-property-optimisation/assets/logtc-feature-importance.png",
    "projects/bayesian-optimisation-for-strength/assets/optimised-test-predictions.png",
    "projects/conditional-generative-design/assets/fashion-cvae-loss.png",
    "projects/conditional-generative-design/assets/generated-fashion-grid.png",
    "projects/lab-automation-protocol/assets/gradient-plate-layout.svg",
    "projects/materials-informatics-and-cheminformatics/assets/band-gap-predictions.png",
)


class PublicEvidenceTests(unittest.TestCase):
    def test_projects_explain_real_results_and_link_reviewed_evidence(self):
        for relative_path in ("docs/evidence.md", "docs/learning-path.md"):
            self.assertTrue((ROOT / relative_path).exists(), f"Missing public document: {relative_path}")

        for relative_path in FIGURES:
            figure = ROOT / relative_path
            self.assertTrue(figure.exists(), f"Missing public figure: {relative_path}")
            self.assertLess(figure.stat().st_size, 1_000_000, f"Oversized figure: {relative_path}")
            self.assertGreater(figure.stat().st_size, 500, f"Empty figure: {relative_path}")

        for project in PROJECTS:
            text = (ROOT / "projects" / project / "README.md").read_text(encoding="utf-8").lower()
            for heading in ("## what i did", "## result", "## what i learned", "## evidence"):
                self.assertIn(heading, text, f"{project} is missing {heading}")
            for blocked in ("matriculation", "homework", "in-class", "assignment"):
                self.assertNotIn(blocked, text, f"{project} exposes coursework label: {blocked}")

        root_readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("## result highlights", root_readme)
        evidence = (ROOT / "docs/evidence.md").read_text(encoding="utf-8").lower()
        self.assertIn("source output", evidence)


if __name__ == "__main__":
    unittest.main()
