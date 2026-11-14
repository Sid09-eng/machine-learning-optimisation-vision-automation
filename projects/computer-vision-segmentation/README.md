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

## What I did

I compared a fixed threshold with a sequence of Gaussian blur, Otsu thresholding, morphological opening, and closing. I then counted external contours before and after cleanup so I could see whether the mask was less affected by grass texture and small gaps.

## Result

The fixed-threshold baseline produced **2,093** contours. After blur, Otsu thresholding, opening, and closing, the pipeline produced **12**. That is not a universal accuracy score; it is a concrete sign that the later mask contained fewer small fragments on this image.

## What I learned

I learned to inspect intermediate masks instead of jumping straight from an image to a contour count. Blur changes local texture, Otsu chooses a data-driven threshold, opening removes small isolated regions, and closing repairs small holes. Each step made the final mask easier to explain.

## Evidence

The source photo and before/after figure are not published because I have not confirmed redistribution rights for the photograph. The verified contour counts and source-output reference are in [evidence notes](../../docs/evidence.md). The reusable pipeline is in [segment.py](segment.py).

## Source and data

I have not included the original image because I do not know whether it can be redistributed. The script takes a user-provided image and states what format it expects.

## Reproduce

Install OpenCV from the root dependency list, give the script an image path, then check the masks before treating the contour count as meaningful.

## Limits

The threshold and morphology settings depend on the image. This is a simple, inspectable method, not a universal semantic-segmentation model. Different lighting, backgrounds, or object sizes may need new settings.
