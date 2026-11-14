"""Behaviour checks for the public source modules."""

import ast
import importlib.util
from pathlib import Path
import tempfile
import unittest

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MeanRegressor:
    def fit(self, features, values):
        self.mean = float(np.mean(values))
        return self

    def predict(self, features):
        return np.full(len(features), self.mean)


class ProjectLogicTests(unittest.TestCase):
    def test_alloy_constraints_reject_boolean_amounts_and_invalid_totals(self):
        module = load_module("projects/alloy-property-optimisation/composition_constraints.py")
        self.assertTrue(module.is_feasible({"Fe": 70, "Co": 20, "Ni": 10}))
        self.assertFalse(module.is_feasible({"Fe": True, "Co": 0, "Ni": 99}))
        self.assertFalse(module.is_feasible({"Fe": 70, "Co": 20, "Ni": 9}))
        with self.assertRaises(ValueError):
            module.composition_label({"Fe": 70, "Co": 20, "Ni": 9})

    def test_data_pipeline_shapes_images_and_rejects_invalid_labels(self):
        module = load_module("projects/conditional-generative-design/data_pipeline.py")
        prepared = module.prepare_images(np.array([[[0, 255], [127, 64]]], dtype=np.uint8))
        self.assertEqual(prepared.shape, (1, 2, 2, 1))
        self.assertAlmostEqual(float(prepared[0, 0, 1, 0]), 1.0)
        with self.assertRaises(ValueError):
            module.prepare_images(np.zeros((2, 2), dtype=np.uint8))
        with self.assertRaises(ValueError):
            module.one_hot_labels(np.array([0, 3]), 3)

    def test_regression_helper_reports_train_and_test_metrics(self):
        module = load_module("projects/bayesian-optimisation-for-strength/evaluate_model.py")
        metrics = module.evaluate_regressor(
            MeanRegressor(), [[0], [1], [2]], [0, 0, 0], [[3], [4]], [3, 5]
        )
        self.assertEqual(set(metrics), {"train_mae", "test_mae", "train_rmse", "test_rmse", "train_r2", "test_r2"})
        self.assertEqual(metrics["train_mae"], 0.0)
        self.assertGreater(metrics["test_mae"], metrics["train_mae"])

    def test_segmentation_validates_input_and_returns_intermediate_results(self):
        module = load_module("projects/computer-vision-segmentation/segment.py")
        with self.assertRaises(FileNotFoundError):
            module.segment_image("missing-image.png")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.png"
            image = np.zeros((40, 40, 3), dtype=np.uint8)
            image[10:30, 10:30] = 255
            self.assertTrue(cv2.imwrite(str(path), image))
            with self.assertRaises(ValueError):
                module.segment_image(path, kernel_size=4)
            result = module.segment_image(path)
        self.assertEqual(set(result), {"grayscale", "threshold", "cleaned_mask", "contour_overlay", "contour_count"})
        self.assertGreaterEqual(result["contour_count"], 1)

    def test_protocol_matrix_has_four_sources_and_250_microlitre_rows(self):
        source = (ROOT / "projects/lab-automation-protocol/rainbow_gradient.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        values = {
            node.targets[0].id: ast.literal_eval(node.value)
            for node in tree.body
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
        }
        self.assertEqual(len(values["SOURCE_WELLS"]), 4)
        self.assertEqual(len(values["GRADIENT_UL"]), 12)
        self.assertTrue(all(len(row) == 4 and sum(row) == values["TOTAL_VOLUME_UL"] for row in values["GRADIENT_UL"]))


if __name__ == "__main__":
    unittest.main()
