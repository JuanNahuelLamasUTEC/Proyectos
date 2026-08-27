"""
weighted_sum_raster.py
 
Suma ponderada de capas raster reclasificadas para el calculo de un indice
tipo GWPI (Groundwater Potential Index), y reclasificacion de variables
continuas por el metodo de Rupturas Naturales (Jenks).
 
Disenado para trabajar con arrays de numpy ya alineados en resolucion y
extension (mismo procedimiento que Weighted Sum de ArcGIS Spatial Analyst,
implementado aqui en Python puro con rasterio + numpy + mapclassify).
"""
 
import numpy as np
import mapclassify
 
 
def jenks_reclassify(array: np.ndarray, n_classes: int = 5, nodata: float = None) -> np.ndarray:
    """
    Reclasifica un array continuo en n_classes categorias mediante el
    metodo de Rupturas Naturales (Jenks), preservando la geometria del
    array de entrada.
 
    Parameters
    ----------
    array : np.ndarray
        Array 2D con los valores continuos (ej. pendiente, TWI, curvatura).
    n_classes : int
        Numero de clases de salida (5 por defecto, escala de favorabilidad 1-5).
    nodata : float, optional
        Valor a excluir del calculo de rupturas y preservar en la salida.
 
    Returns
    -------
    np.ndarray
        Array reclasificado con valores enteros 1..n_classes (o nodata).
    """
    flat = array.flatten()
    valid_mask = ~np.isnan(flat) if nodata is None else (flat != nodata)
    valid_values = flat[valid_mask]
 
    classifier = mapclassify.NaturalBreaks(valid_values, k=n_classes)
    breaks = classifier.bins
 
    reclassified = np.digitize(array, breaks[:-1], right=True) + 1
    reclassified = np.clip(reclassified, 1, n_classes)
 
    if nodata is not None:
        reclassified = np.where(array == nodata, nodata, reclassified)
 
    return reclassified
 
 
def weighted_sum(layers: dict, weights: dict) -> np.ndarray:
    """
    Calcula la suma ponderada de N capas reclasificadas (rating 1-5),
    equivalente a la herramienta Weighted Sum de Spatial Analyst:
 
        GWPI = sum(rating_i * weight_i)
 
    Parameters
    ----------
    layers : dict[str, np.ndarray]
        Diccionario {nombre_capa: array reclasificado (mismo shape en todas)}.
    weights : dict[str, float]
        Diccionario {nombre_capa: peso relativo Wp}. Debe compartir claves con layers.
 
    Returns
    -------
    np.ndarray
        Array continuo del indice resultante, mismo shape que las capas de entrada.
    """
    missing = set(layers) - set(weights)
    if missing:
        raise ValueError(f"Faltan pesos para las capas: {missing}")
 
    shapes = {arr.shape for arr in layers.values()}
    if len(shapes) > 1:
        raise ValueError("Todas las capas deben compartir la misma resolucion y extension.")
 
    result = np.zeros(next(iter(layers.values())).shape, dtype=float)
    for name, array in layers.items():
        result += array.astype(float) * weights[name]
 
    return result
 
 
if __name__ == "__main__":
    # Ejemplo ilustrativo con datos sinteticos (no corresponde a las capas
    # reales del proyecto GWPI Raigon, que no forman parte de este repositorio):
    # dos capas continuas de 5x5 celdas simulando pendiente y TWI.
    rng = np.random.default_rng(seed=42)
    pendiente_cruda = rng.uniform(0, 25, size=(5, 5))       # grados
    twi_crudo = rng.uniform(2, 18, size=(5, 5))              # indice adimensional
 
    pendiente_reclasificada = jenks_reclassify(pendiente_cruda, n_classes=5)
    twi_reclasificado = jenks_reclassify(twi_crudo, n_classes=5)
 
    layers = {"pendiente": pendiente_reclasificada, "twi": twi_reclasificado}
    weights = {"pendiente": 0.110, "twi": 0.126}  # pesos reales de la matriz AHP del proyecto
 
    gwpi_parcial = weighted_sum(layers, weights)
 
    print("Pendiente reclasificada (1-5):\n", pendiente_reclasificada)
    print("\nTWI reclasificado (1-5):\n", twi_reclasificado)
    print("\nGWPI parcial (solo estas 2 capas, con sus pesos AHP reales):\n", np.round(gwpi_parcial, 3))
