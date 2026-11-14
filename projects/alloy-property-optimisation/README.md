# Alloy Property Optimisation

## Problem

I wanted to see whether a model could learn from Fe–Ni–Co compositions, then search within sensible composition limits for promising magnetic-property trade-offs.

## Approach

I turned the composition columns into features, trained tree-based regressors, and used Bayesian optimisation over Fe, Co, and Ni. Before each prediction, I checked that all values were non-negative and added to 100 at.%.

## Skills

- Feature engineering for composition data
- Scikit-learn regression and held-out evaluation
- Constrained Bayesian optimisation with reproducible search bounds
- Model persistence and feature-order validation

## Source and data

I used a local Fe–Ni–Co composition/property table. I am not sharing that file until I have confirmed its reuse terms. The public code will use a documented schema and an example input first.

## Reproduce

Set up the environment from the repository root, then provide data matching the documented schema. The search code checks every composition before it asks the model for a prediction.

## Limits

These are model estimates inside the composition ranges I gave the model, not new material discoveries. Results depend on the data, features, train/test split, and how I weight the objectives. I did not run laboratory validation.
