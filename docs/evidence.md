# Evidence Notes

This page records where public figures and result numbers came from. Source notebooks remain local so private configuration, large caches, and raw study material are not copied into this repository.

## Source output map

| Public item | Source output | What it shows | Boundary |
| --- | --- | --- | --- |
| Alloy prediction panel | Local alloy-model notebook, result cell 9, first PNG output | Measured versus predicted values for seven properties | Held-out fit, not laboratory validation |
| Alloy feature chart | Local alloy-model notebook, result cell 9, second PNG output | Feature importance for fitted `logTc` model | Importance is model-specific, not causation |
| Alloy metric claims | Local alloy-model notebook, result cells 9 and 12 | R² and RMSE for baseline and tuned models | Results depend on the local split and features |
| Concrete prediction panel | Local concrete-optimisation notebook, result cell 34, fourth PNG output | Held-out gradient-boosting predictions | Plot is one split, not structural advice |
| Concrete kernel claims | Local concrete-optimisation notebook, result cells 15, 17, 19, 21, 23, and 34 | Default GP failure, kernel comparison, search output | Kept to show model-selection reasoning |
| Fashion loss and grid | Local generative-model notebook, result cells 9 and 11 | Five-epoch cVAE loss and decoded samples | Samples are short-run output, not finished designs |
| MNIST latent chart | Local generative-model notebook, result cell 20 | PCA and t-SNE view of latent means | Visual diagnostic only |
| Segmentation count | Local image-processing notebook, result cell 12 | 2,093 baseline contours and 12 after cleanup | Source photograph is not published |
| Gradient plate diagram | `rainbow_gradient.py`, `GRADIENT_UL` and `TOTAL_VOLUME_UL` | Exact planned two-row dispense layout | Plan only; no physical-run claim |
| Materials figures and metrics | Local materials-data notebook, result cells 13, 15, and 25 | Learning curve, test predictions, model scores, and LogP values | Bulk-modulus test R² -0.001 is a limitation |
| Early regression comparison | Local forward-model notebook, result cell 13 | Held-out RMSE/R² comparison | Benchmark learning exercise, not clinical prediction |

## Asset selection

Each PNG is copied exactly from a saved notebook output. I selected only charts that can be read without the local data files. Source images with uncertain redistribution rights, raw datasets, model binaries, API responses, and local paths remain excluded.

## Reading numbers responsibly

Metrics describe the recorded split and configuration only. They are useful for comparing approaches inside the work shown here, but they do not guarantee a result on new data, physical experiments, or production systems.
