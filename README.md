# Applied ML & Materials Portfolio

Curated project work in machine learning, Bayesian optimization, computer vision, generative AI, materials informatics, and laboratory automation.

This repository presents selected applied projects as reproducible case studies. It is intentionally curated from a larger local study workspace: course rubrics, private configuration, local caches, and unreviewed generated artefacts are excluded.

## Selected projects

| Project | Focus | Skills demonstrated |
| --- | --- | --- |
| [Alloy Property Optimisation](projects/alloy-property-optimisation/) | Predict alloy properties and search feasible compositions | feature engineering, tree models, constrained Bayesian optimization |
| [Bayesian Optimisation for Strength](projects/bayesian-optimisation-for-strength/) | Tune a concrete-strength model efficiently | surrogate optimisation, model evaluation, scikit-learn |
| [Conditional Generative Design](projects/conditional-generative-design/) | Explore conditioned image generation | TensorFlow/Keras, conditional VAE, latent-space analysis |
| [Computer Vision Segmentation](projects/computer-vision-segmentation/) | Build an interpretable image-segmentation workflow | OpenCV, thresholding, morphology, contour analysis |
| [Laboratory Automation Protocol](projects/lab-automation-protocol/) | Define a reproducible liquid-handling gradient | Python, Opentrons API, experimental automation |

## Working principles

- Report only results supported by committed notebooks or scripts.
- Attribute external data and tools in each project README.
- Keep secrets, API caches, training artefacts, and local environments out of version control.
- State assumptions and limitations instead of presenting study work as a deployed product.

## Repository layout

```text
projects/     Curated, portfolio-safe case studies
docs/         Shared methodology and reproducibility notes
tests/        Public-surface checks
```

## Reproducibility

Each case study documents its own requirements, input provenance, and validation path. API-backed workflows remain optional; no API key is committed in this repository.

## Status

Portfolio curation in progress. Project pages are added and checked incrementally so each public artifact is reviewable before release.
