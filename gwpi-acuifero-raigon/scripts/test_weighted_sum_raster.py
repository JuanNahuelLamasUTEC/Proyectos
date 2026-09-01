"""
test_weighted_sum_raster.py

Tests minimos para weighted_sum_raster.py. Usan arrays sinteticos
pequenos, no datos reales del proyecto GWPI Raigon.
"""

import numpy as np
import pytest

from weighted_sum_raster import jenks_reclassify, weighted_sum


def test_jenks_reclassify_output_range():
    rng = np.random.default_rng(seed=1)
    array = rng.uniform(0, 100, size=(10, 10))
    reclassified = jenks_reclassify(array, n_classes=5)
    assert reclassified.min() >= 1
    assert reclassified.max() <= 5


def test_jenks_reclassify_preserves_shape():
    array = np.arange(25, dtype=float).reshape(5, 5)
    reclassified = jenks_reclassify(array, n_classes=5)
    assert reclassified.shape == array.shape


def test_jenks_reclassify_handles_nodata():
    array = np.array([[1.0, 2.0, -9999.0], [3.0, 4.0, 5.0]])
    reclassified = jenks_reclassify(array, n_classes=3, nodata=-9999.0)
    assert reclassified[0, 2] == -9999.0


def test_weighted_sum_basic():
    layers = {
        "a": np.array([[1, 2], [3, 4]], dtype=float),
        "b": np.array([[5, 6], [7, 8]], dtype=float),
    }
    weights = {"a": 0.5, "b": 0.5}
    result = weighted_sum(layers, weights)
    expected = np.array([[3.0, 4.0], [5.0, 6.0]])
    np.testing.assert_allclose(result, expected)


def test_weighted_sum_missing_weight_raises():
    layers = {"a": np.zeros((2, 2)), "b": np.zeros((2, 2))}
    weights = {"a": 1.0}  # falta "b"
    with pytest.raises(ValueError):
        weighted_sum(layers, weights)


def test_weighted_sum_shape_mismatch_raises():
    layers = {
        "a": np.zeros((2, 2)),
        "b": np.zeros((3, 3)),
    }
    weights = {"a": 0.5, "b": 0.5}
    with pytest.raises(ValueError):
        weighted_sum(layers, weights)


def test_weighted_sum_output_dtype_is_float():
    layers = {"a": np.array([[1, 2]], dtype=int)}
    weights = {"a": 1.0}
    result = weighted_sum(layers, weights)
    assert result.dtype == float
