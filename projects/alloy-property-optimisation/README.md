# Alloy Property Optimisation

## Problem

Explore composition–property modelling for Fe–Ni–Co alloys, then search feasible compositions that balance predicted magnetic-property objectives.

## Approach

The workflow converts composition columns into formula-based and composition-derived features, fits tree-based regression models, and uses constrained Bayesian optimisation over Fe, Co, and Ni proportions. Every candidate is checked for non-negative fractions and a 100 at.% total before evaluation.

## Skills

- Feature engineering for composition data
- Scikit-learn regression and held-out evaluation
- Constrained Bayesian optimisation with reproducible search bounds
- Model persistence and feature-order validation

## Source and data

The local working dataset is a Fe–Ni–Co composition/property table used for this case study. It is not redistributed here while data-use terms are being confirmed. The public project will include a documented schema and a synthetic/example input path before release.

## Reproduce

Run the documented environment setup from the repository root, then use the project script/notebook once the reviewed input data has been supplied. The optimisation path must validate each composition constraint before making a model prediction.

## Limits

Predictions are model estimates within observed composition ranges, not experimentally validated material discoveries. Results depend on data coverage, feature construction, split design, and the objective weighting; no laboratory-performance claim is made.
