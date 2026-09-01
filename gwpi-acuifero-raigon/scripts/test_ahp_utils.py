"""
test_ahp_utils.py

Tests minimos para ahp_utils.py. Verifican propiedades matematicas
esperadas del metodo AHP (Saaty, 1980), no valores especificos del
proyecto GWPI Raigon.
"""

import numpy as np
import pytest

from ahp_utils import ahp_weights, RANDOM_INDEX


# Matriz de ejemplo del docstring: 4 criterios, consistente (CR < 0.10)
EXAMPLE_MATRIX = np.array([
    [1,   3,   5,   7],
    [1/3, 1,   3,   5],
    [1/5, 1/3, 1,   3],
    [1/7, 1/5, 1/3, 1],
])

# Matriz 2x2 reciproca: para n=2 toda matriz reciproca positiva es
# perfectamente consistente por construccion (CR = 0), a diferencia de
# la matriz identidad, cuyos autovalores degenerados (todos = 1) hacen
# que el autovector principal dependa de la implementacion de np.linalg.eig.
TWO_BY_TWO_MATRIX = np.array([
    [1,   4],
    [1/4, 1],
])


def test_weights_sum_to_one():
    weights, _, _ = ahp_weights(EXAMPLE_MATRIX)
    assert weights.sum() == pytest.approx(1.0, abs=1e-8)


def test_weights_are_positive():
    weights, _, _ = ahp_weights(EXAMPLE_MATRIX)
    assert np.all(weights > 0)


def test_example_matrix_is_consistent():
    _, cr, is_consistent = ahp_weights(EXAMPLE_MATRIX)
    assert cr < 0.10
    assert is_consistent


def test_two_by_two_matrix_has_zero_cr():
    _, cr, is_consistent = ahp_weights(TWO_BY_TWO_MATRIX)
    assert cr == pytest.approx(0.0, abs=1e-8)
    assert is_consistent


def test_two_by_two_matrix_gives_expected_weights():
    # Para [[1, 4], [1/4, 1]] el peso relativo esperado es 4:1
    weights, _, _ = ahp_weights(TWO_BY_TWO_MATRIX)
    expected = np.array([0.8, 0.2])
    np.testing.assert_allclose(weights, expected, atol=1e-8)


def test_non_square_matrix_raises():
    bad_matrix = np.array([[1, 2, 3], [1 / 2, 1, 2]])
    with pytest.raises(ValueError):
        ahp_weights(bad_matrix)


def test_cr_threshold_is_respected():
    # Umbral mas estricto que el CR real de la matriz de ejemplo
    _, cr, is_consistent = ahp_weights(EXAMPLE_MATRIX, cr_threshold=0.001)
    assert cr > 0.001
    assert not is_consistent


def test_random_index_fallback_for_large_n():
    # n > 10 no esta en la tabla RANDOM_INDEX; se espera el fallback conservador (1.49)
    assert RANDOM_INDEX.get(11, 1.49) == 1.49
