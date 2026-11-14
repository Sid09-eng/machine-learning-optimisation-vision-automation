"""Fe–Co–Ni composition validation used before model inference."""

from __future__ import annotations

from typing import Mapping


ELEMENTS = ("Fe", "Co", "Ni")


def make_composition(fe: float, co: float, ni: float) -> dict[str, float]:
    """Return a named ternary composition in atomic percent."""
    return {"Fe": float(fe), "Co": float(co), "Ni": float(ni)}


def is_feasible(composition: Mapping[str, float], tolerance: float = 1e-9) -> bool:
    """Check element keys, non-negative fractions, and 100 at.% closure."""
    if set(composition) != set(ELEMENTS):
        return False
    values = tuple(composition[element] for element in ELEMENTS)
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in values):
        return False
    return all(value >= 0 for value in values) and abs(sum(values) - 100.0) <= tolerance


def composition_label(composition: Mapping[str, float]) -> str:
    """Create compact label only for a feasible composition."""
    if not is_feasible(composition):
        raise ValueError("Composition must contain non-negative Fe, Co, and Ni values summing to 100 at.%.")
    return "".join(f"{element}{composition[element]:g}" for element in ELEMENTS if composition[element] > 0)
