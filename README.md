# Machine Learning for Optimisation, Vision & Automation

Selected implementation work in machine learning, Bayesian optimisation, computer vision, generative AI, materials informatics, and laboratory automation.

This repository shows how I work from data and baseline models through model selection, result checks, constraints, and clear limits. Each project keeps the code, figures, and numbers needed to review the technical decision behind it.

## Selected projects

| Project | What I worked on | Skills used |
| --- | --- | --- |
| [Alloy Property Optimisation](projects/alloy-property-optimisation/) | Predict alloy properties and search feasible compositions | feature engineering, tree models, constrained Bayesian optimization |
| [Bayesian Optimisation for Strength](projects/bayesian-optimisation-for-strength/) | Tune a concrete-strength model efficiently | surrogate optimisation, model evaluation, scikit-learn |
| [Conditional Generative Design](projects/conditional-generative-design/) | Explore conditioned image generation | TensorFlow/Keras, conditional VAE, latent-space analysis |
| [Computer Vision Segmentation](projects/computer-vision-segmentation/) | Build an interpretable image-segmentation workflow | OpenCV, thresholding, morphology, contour analysis |
| [Laboratory Automation Protocol](projects/lab-automation-protocol/) | Define a reproducible liquid-handling gradient | Python, Opentrons API, experimental automation |
| [Materials Informatics & Cheminformatics](projects/materials-informatics-and-cheminformatics/) | Learn from material compositions and inspect molecular properties | CBFV, neural regression, RDKit, data pipelines |

## Result highlights

- **Alloy property models:** held-out R² reached **0.986** across seven predicted properties; tuned `Ms` and `logTc` models reached **0.969** and **0.975**.
- **Concrete-strength optimisation:** the best Gaussian-process configuration reached test R² **0.809**; Bayesian tuning found a gradient-boosting setup with 3-fold CV MSE **22.543**.
- **Generative modelling:** Fashion cVAE validation loss fell from **261.115** to **243.129** over five epochs. The saved grid shows what the short run produced, including its rough edges.
- **Image processing:** blur, Otsu thresholding, and morphology reduced detected contours from **2,093** to **12** on the local test image.
- **Materials data:** formation-energy model test R² reached **0.924**; the band-gap model reached **0.712**. Bulk-modulus generalisation was weak, which is recorded rather than hidden.

Every figure and number above is mapped to an executed local output in [evidence notes](docs/evidence.md). [Technical progression](docs/learning-path.md) shows how the work connects.

## How I work

- I only include results that can be checked from the code or saved output.
- Each project page says where its data and tools came from.
- Secrets, API caches, model files, and local environments stay out of Git.
- I say where a method is useful and where it is not.

## Repository layout

```text
projects/     Project notes and code
docs/         Notes on how I review what goes public
tests/        Checks for the public files
```

## Public scope

This is a reviewed evidence and selected-source repository, not a release of every original notebook, dataset, model file, or API response. Project pages state exactly what is public, what remains local, and why. The checked source modules and public documentation can be tested with:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

GitHub Actions runs the same checks on pushes and pull requests.
