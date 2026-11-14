"""Dataset preparation utilities for class-conditioned image experiments."""

from __future__ import annotations

import numpy as np


def prepare_images(images: np.ndarray) -> np.ndarray:
    """Normalise grayscale uint8 images and add a one-channel axis."""
    array = np.asarray(images, dtype="float32") / 255.0
    if array.ndim != 3:
        raise ValueError("Expected images with shape (samples, height, width).")
    return array[..., np.newaxis]


def one_hot_labels(labels: np.ndarray, class_count: int) -> np.ndarray:
    """Return a float32 one-hot condition matrix."""
    labels = np.asarray(labels, dtype="int64").reshape(-1)
    if class_count <= 0 or labels.size == 0 or labels.min() < 0 or labels.max() >= class_count:
        raise ValueError("Labels must be non-empty integers in the declared class range.")
    return np.eye(class_count, dtype="float32")[labels]
