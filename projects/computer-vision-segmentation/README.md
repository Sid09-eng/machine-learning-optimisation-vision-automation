# Computer Vision Segmentation

## Problem

I built a simple segmentation pipeline to clean up a thresholded image before counting its contours.

## Approach

The code reads an image, applies Gaussian blur, calculates an Otsu threshold, then uses opening and closing to remove noise and repair regions. It draws the final contours so I can see what each step changed.

## Skills

- OpenCV image I/O and colour conversion
- Gaussian smoothing and Otsu thresholding
- Morphological opening and closing
- Contour extraction and visual debugging

## Source and data

I have not included the original image because I do not know whether it can be redistributed. The script takes a user-provided image and states what format it expects.

## Reproduce

Install OpenCV from the root dependency list, give the script an image path, then check the masks before treating the contour count as meaningful.

## Limits

The threshold and morphology settings depend on the image. This is a simple, inspectable method, not a universal semantic-segmentation model. Different lighting, backgrounds, or object sizes may need new settings.
