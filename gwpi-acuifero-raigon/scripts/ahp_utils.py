"""
ahp_utils.py

Utilidades para el Proceso Analitico Jerarquico (AHP, Saaty 1980):
calculo de pesos relativos por el metodo del autovector principal
y verificacion de consistencia mediante la Razon de Consistencia (CR).

Uso tipico en un flujo de Indice de Potencial de Aguas Subterraneas (GWPI):
    matrix = np.array([...])  # matriz de comparacion pareada, n x n
    weights, cr, is_consistent = ahp_weights(matrix)
"""

import numpy as np

# Indice Aleatorio (Random Index) de Saaty para matrices de tamano 1 a 10
RANDOM_INDEX = {
    1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
    6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49,
}


def ahp_weights(pairwise_matrix: np.ndarray, cr_threshold: float = 0.10):
    """
    Calcula los pesos relativos de un AHP y su Razon de Consistencia.

    Parameters
    ----------
    pairwise_matrix : np.ndarray
        Matriz cuadrada de comparacion pareada (n x n), reciproca positiva.
    cr_threshold : float
        Umbral maximo aceptado de CR (0.10 por convencion de Saaty).

    Returns
    -------
    weights : np.ndarray
        Vector de pesos relativos normalizado (suma = 1).
    cr : float
        Razon de Consistencia calculada.
    is_consistent : bool
        True si cr <= cr_threshold.
    """
    n = pairwise_matrix.shape[0]
    if pairwise_matrix.shape != (n, n):
        raise ValueError("La matriz de comparacion pareada debe ser cuadrada.")

    # Autovector principal (metodo del autovalor dominante)
    eigvals, eigvecs = np.linalg.eig(pairwise_matrix)
    max_index = np.argmax(eigvals.real)
    lambda_max = eigvals.real[max_index]

    principal_eigenvector = eigvecs[:, max_index].real
    weights = principal_eigenvector / principal_eigenvector.sum()

    # Indice de Consistencia y Razon de Consistencia
    ci = (lambda_max - n) / (n - 1) if n > 1 else 0.0
    ri = RANDOM_INDEX.get(n, 1.49)  # fallback conservador para n > 10
    cr = ci / ri if ri > 0 else 0.0

    return weights, cr, cr <= cr_threshold


if __name__ == "__main__":
    # Ejemplo ilustrativo (no corresponde a la matriz real del proyecto GWPI,
    # que no forma parte de este repositorio): comparacion pareada de 4 criterios
    # geoespaciales genericos, solo para demostrar el uso de la funcion.
    example_matrix = np.array([
        [1,   3,   5,   7],
        [1/3, 1,   3,   5],
        [1/5, 1/3, 1,   3],
        [1/7, 1/5, 1/3, 1],
    ])

    criteria = ["Geologia", "Geomorfologia", "Uso de suelo", "Pendiente"]
    weights, cr, ok = ahp_weights(example_matrix)

    print("Pesos relativos (ejemplo ilustrativo):")
    for c, w in zip(criteria, weights):
        print(f"  {c:15s} {w:.3f}")
    print(f"\nRazon de Consistencia (CR): {cr:.4f}")
    print(f"Matriz consistente (CR <= 0.10): {ok}")
