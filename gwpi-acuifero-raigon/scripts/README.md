# scripts

Utilidades en Python que implementan la componente cuantitativa del análisis GWPI/AHP: cálculo de pesos por Proceso Analítico Jerárquico y suma ponderada de capas raster reclasificadas. Reproducen en Python puro los pasos que en el flujo operativo del proyecto se ejecutaron en ArcGIS Pro (ModelBuilder + Spatial Analyst), documentando la lógica de forma independiente de la licencia de software.

## Contenido

| Script | Función | Rol en el pipeline |
|---|---|---|
| `ahp_utils.py` | `ahp_weights(pairwise_matrix, cr_threshold=0.10)` | Calcula los pesos relativos de los criterios (método del autovector principal, Saaty 1980) y verifica la Razón de Consistencia (CR) |
| `weighted_sum_raster.py` | `jenks_reclassify(array, n_classes=5)`<br>`weighted_sum(layers, weights)` | Reclasifica capas continuas en escala de favorabilidad 1–5 (Rupturas Naturales / Jenks) y calcula la suma ponderada final del índice |

## Orden de uso

1. Definir la matriz de comparación pareada por criterio (`ahp_utils.ahp_weights`) → obtener `weights` y verificar `is_consistent`
2. Reclasificar cada capa continua a escala 1–5 (`weighted_sum_raster.jenks_reclassify`)
3. Combinar capas reclasificadas con los pesos AHP (`weighted_sum_raster.weighted_sum`) → índice final (GWPI)

## Relación con `../notebooks/`

Estas utilidades operan sobre capas **ya reclasificadas** a la escala 1–5. El paso previo —pasar de las capas crudas (geología, red de drenaje, pendiente, TWI) a esos ratings— está documentado de forma ejecutable en [`../notebooks/01_preparacion_vectorial_gwpi.ipynb`](../notebooks/), donde se resuelven la reproyección a SIRGAS-ROU98 / UTM 21S, la malla de análisis, la densidad de drenaje por intersección, la distancia a cursos por vecino más próximo, la asignación de unidad geológica por mayoría de área y la estadística zonal sobre los rásteres continuos.

Las dos carpetas cubren tramos consecutivos del mismo flujo:

```
capas crudas  →  [ notebooks/ ]  →  ratings 1–5  →  [ scripts/ ]  →  GWPI
```

El notebook reimplementa `ahp_weights` y `jenks_reclassify` para poder ejecutarse sin depender de rutas relativas; **la implementación de referencia del proyecto es la de esta carpeta**, y las docstrings del notebook lo indican en cada caso. Los pesos que usa el notebook no se re-derivan: parte de los publicados en [`../README.md`](../README.md) y los re-normaliza sobre el subconjunto de criterios que calcula.

## Instalación

```bash
pip install -r requirements.txt
```

Dependencias: `numpy`, `mapclassify`

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Nota sobre los datos

Los ejemplos en los bloques `if __name__ == "__main__":` de cada script usan datos sintéticos o ilustrativos (ver docstrings). Los pesos reales de la matriz AHP del proyecto se documentan y verifican en el informe final (en proceso de publicación); no se incluyen las capas de entrada reales (geología, uso de suelo, balance hidrológico DINAGUA, etc.) por no formar parte de este repositorio.

El notebook de [`../notebooks/`](../notebooks/) sigue el mismo criterio: si no encuentra las capas reales en su carpeta `datos/`, genera un conjunto sintético reproducible con semilla fija y lo declara de forma explícita tanto en el encabezado como en las salidas de cada celda.

## Referencia metodológica

- Saaty, T.L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
