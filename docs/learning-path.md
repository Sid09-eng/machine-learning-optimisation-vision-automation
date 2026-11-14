# Technical Progression

## Establish a baseline

The first comparison used linear regression, KNN, and random forest on the diabetes benchmark. The tuned random forest reached test R² **0.510**, ahead of linear regression (**0.453**) and KNN (**0.450**). The point was to choose with held-out evidence, not model popularity.

![Held-out regression comparison on the diabetes benchmark](../assets/learning/diabetes-model-comparison.png)

## Challenge generalisation

The concrete work made the same issue more obvious. A default Gaussian process had test R² **-49.990**, even though its training fit looked strong. Kernel comparison and Bayesian optimisation produced a more useful result. The train/test gap stays visible because it explains the next engineering decision.

## Move from prediction to constrained search

The alloy work connected models to a search loop. Feature order, held-out metrics, and Fe–Co–Ni constraints are checked before a proposed composition is evaluated. A search answer has no value if its inputs are invalid.

## Inspect outputs, not only metrics

The segmentation and VAE work requires visual inspection. For segmentation, masks and contours are checked after each operation. For VAEs, loss curves sit beside generated samples. A metric can show movement; the output shows what still needs work.

## Carry the same checks into materials and automation

The materials work combines data access, feature generation, model checks, and molecular descriptors. The lab protocol needs a different validation layer: volume totals, plate positions, and tip use must be right before hardware moves. In both areas, constraints matter as much as model code.
