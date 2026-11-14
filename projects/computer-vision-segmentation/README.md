# Computer Vision Segmentation

## Problem

Build an interpretable image-segmentation pipeline that improves raw thresholding before contour analysis.

## Approach

The pipeline reads an image, applies Gaussian blur, derives an Otsu threshold, and uses morphological opening and closing to remove noise and repair regions. It then finds and draws contours so each processing stage can be inspected.

## Skills

- OpenCV image I/O and colour conversion
- Gaussian smoothing and Otsu thresholding
- Morphological opening and closing
- Contour extraction and visual debugging

## Source and data

The original local image is deliberately excluded because redistribution rights have not been established. The public workflow accepts a user-provided image and records its expected format.

## Reproduce

Install OpenCV from the root dependency list, supply an image path, then run each stage in sequence. Review intermediate masks before interpreting the final contour count.

## Limits

Thresholds and morphology settings are image-dependent. The method is a transparent baseline, not a universal semantic-segmentation system; changing lighting, background, or object scale may require retuning.
