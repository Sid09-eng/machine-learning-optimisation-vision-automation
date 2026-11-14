# Bayesian Optimisation for Strength

## Problem

I used Bayesian optimisation to tune a concrete-compressive-strength model without using the test set to guide the search.

## Approach

I prepared mix-design features, trained a few baseline regressors, then used a Gaussian-process search to tune gradient boosting. I compared acquisition choices and kernel settings instead of relying on one default search setup.

## Skills

- Tabular data preparation and exploratory analysis
- Scikit-learn model pipelines and regression metrics
- Gaussian-process surrogate modelling
- Expected-improvement and lower-confidence-bound acquisition strategies

## Source and data

I used the UCI Concrete Compressive Strength data provided with my local files. Before sharing a data copy, I will confirm the source details and list the expected columns.

## Reproduce

Install the root dependencies, add the concrete data file described here, and run with the fixed split seed. Compare baseline and tuned models only on the held-out data.

## Limits

This model is not a structural-design recommendation. It works on historical data, and its results can move when the seed, search budget, available features, or split changes.
