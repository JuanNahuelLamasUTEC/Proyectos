# Resultados

Productos derivados del procesamiento fotogramétrico multisensor: ortomosaicos por banda, segmentación automática de copas individuales y verificaciones de calidad del pipeline de delimitación.

## Contenido

### 1–3. Ortomosaicos por sensor

<img src="01-ortomosaico-rgb.png" width="700">

Ortomosaico RGB georreferenciado, generado por Structure from Motion (Pix4D / Agisoft Metashape).

<img src="02-ortomosaico-multiespectral.png" width="700">

Ortomosaico multiespectral, insumo para el cálculo de índices espectrales (NDVI, GNDVI, NDRE) por copa.

<img src="03-ortomosaico-termico.png" width="700">

Ortomosaico térmico, generado a partir de imágenes calibradas radiométricamente con DJI Thermal Tools (temperatura absoluta, no relativa).

### 4. Segmentación automática de copas

<img src="04-segmentacion-automatica-copas.png" width="700">

Resultado de la delimitación automática de copas individuales mediante el enfoque híbrido OBIA + modelos de segmentación basados en visión (línea Gibril et al., 2023).

### 5–6. Verificaciones de calidad de la segmentación

<img src="05-separacion-copas-adyacentes.jpeg" width="700">

Caso de verificación: el algoritmo separa correctamente copas de palmeras adyacentes o con solapamiento de follaje, evitando que se fusionen en una sola detección.

<img src="06-verificacion-copas-borde-tiles.jpeg" width="700">

Verificación de que una copa de palmera ubicada sobre el borde compartido entre dos tiles del ortomosaico se reconstruye correctamente como una única unidad, sin fragmentarse en dos detecciones separadas.

### 7. Vectorización final

<img src="07-shapefile-palmeras-vectorizado.png" width="700">

Shapefile final de palmeras individuales vectorizadas y georreferenciadas, listo para la extracción de variables por copa y su integración en los modelos de clasificación del estado sanitario.

---

**Nota:** estas imágenes documentan productos y verificaciones de calidad del pipeline de fotogrametría y segmentación, no resultados de clasificación sanitaria (etapa posterior, fuera del alcance de este repositorio).
