"""Small, reusable held-out regression evaluation helper."""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regressor(model: Any, x_train: Any, y_train: Any, x_test: Any, y_test: Any) -> dict[str, float]:
    """Fit one estimator and report separate train/test regression metrics."""
    model.fit(x_train, y_train)
    y_train_predicted = model.predict(x_train)
    y_test_predicted = model.predict(x_test)
    return {
        "train_mae": float(mean_absolute_error(y_train, y_train_predicted)),
        "test_mae": float(mean_absolute_error(y_test, y_test_predicted)),
        "train_rmse": float(np.sqrt(mean_squared_error(y_train, y_train_predicted))),
        "test_rmse": float(np.sqrt(mean_squared_error(y_test, y_test_predicted))),
        "train_r2": float(r2_score(y_train, y_train_predicted)),
        "test_r2": float(r2_score(y_test, y_test_predicted)),
    }
