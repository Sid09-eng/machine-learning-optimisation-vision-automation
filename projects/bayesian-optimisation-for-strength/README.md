# Bayesian Optimisation for Strength

## Problem

Tune a concrete-compressive-strength regressor with Bayesian optimisation while keeping evaluation separate from tuning decisions.

## Approach

The case study prepares tabular mix-design features, establishes baseline regression models, and uses a Gaussian-process-guided search to tune a gradient-boosting model. Experiment settings compare acquisition strategies and kernel choices instead of treating optimisation as a black box.

## Skills

- Tabular data preparation and exploratory analysis
- Scikit-learn model pipelines and regression metrics
- Gaussian-process surrogate modelling
- Expected-improvement and lower-confidence-bound acquisition strategies

## Source and data

The workflow uses the UCI Concrete Compressive Strength data supplied with the local study materials. The public version credits the dataset source and documents expected columns before publishing any redistributed copy.

## Reproduce

Install dependencies listed at repository root, provide the documented concrete data file, and run the project workflow with its fixed split seed. Compare baseline and tuned models only on the held-out evaluation partition.

## Limits

This is a modelling exercise over a historical dataset, not a structural-design recommendation. Search outcomes can vary with seed, search budget, feature availability, and the train/test split.
