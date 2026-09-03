# Notebooks — preparación vectorial del GWPI

Etapa vectorial reproducible del Índice de Potencial de Aguas Subterráneas del Acuífero Raigón.

En el flujo publicado en la carpeta principal, la integración multicriterio se resolvió en **ArcGIS Pro con
ModelBuilder** y los scripts de `../scripts/` reproducen la parte ráster (pesos por autovector y suma
ponderada). La preparación de las capas de entrada, en cambio, se hizo de forma interactiva dentro del SIG.

Este notebook reescribe esa etapa en Python para que pueda volver a correrse y revisarse línea por línea.

## Contenido

| Archivo | Descripción |
|---|---|
| `01_preparacion_vectorial_gwpi.ipynb` | Notebook principal, ejecutado y con salidas incluidas |
| `requirements.txt` | Dependencias |
| `salidas/gwpi_paneles.png` | Figura de las cinco capas de entrada y el índice integrado |
| `salidas/gwpi_raigon.gpkg` | GeoPackage con la malla calificada, geología, drenaje, pozos y área |
| `salidas/gwpi_raigon.tif` | GWPI normalizado 0–100, rasterizado a 30 m |
| `salidas/parametros_corrida.json` | Parámetros, pesos, cortes de Jenks y versiones de la corrida |

## Operaciones que resuelve

- **Sistemas de referencia.** SIRGAS-ROU98 geográfico (EPSG:5381) → UTM 21S (EPSG:5382), con una
  comprobación explícita del error de calcular áreas y distancias sobre coordenadas geográficas.
- **Malla de análisis.** Grilla regular de 1 km construida con `shapely`, recortada al área de estudio.
- **Densidad de drenaje.** `geopandas.overlay` para partir la red por celda, suma de longitudes y
  normalización por superficie (km/km²).
- **Distancia a cursos.** `geopandas.sjoin_nearest` con `distance_col`, desde el centroide de cada celda,
  resolviendo empates de vecino más próximo.
- **Unidad geológica dominante.** Intersección malla × geología, agregación por área y selección por
  mayoría, guardando la fracción de área como medida de la ambigüedad de cada asignación.
- **Estadística zonal.** Rasterización de los identificadores de celda con `rasterio.features.rasterize` y
  agregación con `numpy.bincount`, en lugar de recortar el ráster una vez por zona.
- **Reclasificación 1–5.** Cortes naturales de Jenks con `mapclassify`, con el sentido de cada variable
  (directo o invertido) declarado de forma explícita.
- **Pesos AHP.** Autovector principal de la matriz de comparaciones por pares y razón de consistencia de
  Saaty, con verificación de reciprocidad de la matriz.
- **Validación.** Correlación de rangos de Spearman contra caudales específicos de pozos.
- **Exportación.** GeoPackage multicapa, GeoTIFF comprimido y teselado, y JSON de parámetros.

## Datos

El notebook **no distribuye las capas originales del proyecto**. La geología 1:100.000, la red de drenaje de
DINAGUA y los datos de pozos están sujetos a las condiciones de uso de las instituciones que los proveyeron,
y el informe del proyecto está en proceso de publicación.

Para que sea ejecutable por cualquiera, si no encuentra las capas reales en `datos/` genera un conjunto
sintético reproducible con semilla fija, sobre la envolvente aproximada del acuífero y con la misma
estructura de atributos y las mismas unidades geológicas del caso real. **Los números de esa corrida son
demostrativos: sirven para auditar el código, no para citar resultados.** Los resultados publicados del
proyecto provienen de las capas reales y están en `../resultados/`.

Para usar las capas reales basta colocarlas en `datos/` con estos nombres; el notebook las detecta solo y no
requiere ningún otro cambio:

```
datos/
├── drenaje.gpkg      # LineString — red de drenaje
├── geologia.gpkg     # Polygon    — campo 'unidad' con el nombre de la formación
├── pozos.gpkg        # Point      — campo 'caudal_esp' en m³/h/m
├── pendiente.tif     # float32    — pendiente en %
└── twi.tif           # float32    — Topographic Wetness Index
```

## Cómo correrlo

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab 01_preparacion_vectorial_gwpi.ipynb
```

Verificado con Python 3.11, GeoPandas 1.1, Rasterio 1.4 y mapclassify 2.10.

---

Juan Nahuel Lamas — Grupo de Investigaciones Espaciales (GIEx), UTEC
[juan.lamas@utec.edu.uy](mailto:juan.lamas@utec.edu.uy)
