"""Transparent OpenCV segmentation baseline with saved intermediate masks."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


def segment_image(image_path: str | Path, kernel_size: int = 5) -> dict[str, np.ndarray | int]:
    """Segment an image with blur, Otsu thresholding, morphology, and contours."""
    path = Path(image_path)
    if not path.is_file():
        raise FileNotFoundError(f"Could not read image: {image_path}")
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer of at least 3.")

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayscale, (kernel_size, kernel_size), 0)
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), dtype=np.uint8)
    opened = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=1)
    cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=2)
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    overlay = image.copy()
    cv2.drawContours(overlay, contours, -1, (0, 255, 0), 2)

    return {
        "grayscale": grayscale,
        "threshold": threshold,
        "cleaned_mask": cleaned,
        "contour_overlay": overlay,
        "contour_count": len(contours),
    }
