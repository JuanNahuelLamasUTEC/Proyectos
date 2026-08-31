# Aplicación de tecnología LiDAR para el relevamiento de concheros precoloniales
### Cuenca inferior del río Santa Lucía, Uruguay

---

## Contexto

Proyecto conjunto entre el **Grupo de Investigaciones Espaciales (GIEx, UTEC)** y el **Laboratorio de Análisis Espacial del CIRAT** (Centro de Investigación Regional Arqueológica y Territorial / PIAAD / MEC), orientado a evaluar el uso de sensores LiDAR aerotransportados para la identificación y caracterización de estructuras arqueológicas tipo *conchero* (montículos de origen antrópico precolonial) en ambientes costeros y de humedal.

El relevamiento se realizó sobre un sitio con estructuras monticulares previamente identificadas y relevadas mediante topografía convencional en 2010, lo que permitió comparar la técnica LiDAR contra un registro topográfico preexistente. **Constituye la primera aplicación de esta tecnología a un sitio arqueológico en Uruguay.**

Los resultados fueron presentados como resumen en congreso, en coautoría con CIRAT/MEC y GIEx-UTEC.

> **Nota sobre datos sensibles:** por tratarse de sitios con protección patrimonial, este repositorio no incluye coordenadas exactas, nubes de puntos georreferenciadas ni cartografía de detalle del sitio. Se muestran únicamente metodología, parámetros técnicos de vuelo y procesamiento, y resultados descriptivos generales.

---

## Mi rol en el proyecto

Trabajo en equipo interinstitucional (GIEx-UTEC / CIRAT-MEC). Responsable de:

- Planificación y organización del vuelo LiDAR (definición de zonas de cobertura y patrones de vuelo)
- Procesamiento de la nube de puntos
- Interpretación de los productos derivados (DEM, DSM) para la identificación de estructuras y microrelieve

---

## Equipo y sensor

| Parámetro | Valor |
|---|---|
| Plataforma | Dron |
| Sensor | DJI Zenmuse L2 (LiDAR + cámara RGB) |
| Altura de vuelo | 80 m AGL |
| Densidad de puntos resultante | 242 pts/m² |

---

## Diseño de vuelo

Se definieron zonas de cobertura diferenciadas según prioridad, con dos patrones de vuelo:

| Zona | Patrón | GSD | Observación |
|---|---|---|---|
| Prioridad A | Grillado doble (cross-hatch, doble pasada perpendicular) | 1.62 cm/px | Máxima prioridad — mayor densidad y redundancia de puntos para minimizar error de alineación entre franjas |
| Prioridad B | Grillado simple (single-grid) | 1.89 cm/px | Cobertura general del sitio |
| Zona de inspección | Grillado simple | 1.62 cm/px | Área adyacente, relevada para contexto geomorfológico |

El uso de grillado doble en la zona de prioridad A responde a una decisión metodológica: al superponer dos pasadas perpendiculares se reduce el efecto de desalineación de franjas (*strip misalignment*) que suele producirse por deriva del sistema GNSS/IMU en vuelos de única pasada, especialmente relevante en un levantamiento de alta precisión sobre microrelieve.

---

## Procesamiento y solución técnica

**Problema identificado:** durante el procesamiento en LiDAR360 se detectaron discontinuidades altimétricas entre franjas de vuelo adyacentes (*strip misalignment*), que de no corregirse introducen ruido artificial en el DEM y pueden enmascarar o simular microrelieve real, un riesgo particular en este tipo de aplicación, donde el objetivo es precisamente detectar variaciones sutiles de relieve de origen antrópico.

**Solución aplicada:** ajuste de franjas mediante la herramienta *Strip Adjustment* de LiDAR360, que corrige los desvíos relativos entre pasadas de vuelo (offsets planimétricos y altimétricos) antes de la generación de los productos derivados, asegurando consistencia geométrica entre franjas superpuestas.

### Workflow

1. **Vuelo LiDAR** con patrones diferenciados por zona de prioridad (ver tabla arriba).
2. **Control de calidad** de la nube de puntos cruda.
3. **Corrección de desalineación de franjas** (Strip Adjustment, LiDAR360).
4. **Clasificación suelo / no-suelo.** El criterio de tolerancia a ruido en este paso es distinto al de otras aplicaciones (ingeniería civil, hidrología): en prospección arqueológica se puede tolerar ruido siempre que la distorsión introducida sea significativamente menor que el tamaño del rasgo que se busca detectar, en vez de optimizar por precisión promedio del terreno.
5. **Interpolación de DTM/DEM y DSM.** Generación de grilla a partir de los puntos clasificados como suelo (DTM/DEM) y de la superficie completa incluyendo vegetación y estructuras (DSM).
6. **Visualización mejorada del microrelieve.** El hillshade simple tiene limitaciones conocidas para detectar rasgos sutiles: pierde detalle en zonas de sombra profunda y no representa bien rasgos lineales paralelos a la dirección de la luz. Por eso se complementó con técnicas adicionales de visualización de relieve, particularmente *sky-view factor*, que al usar iluminación difusa en vez de una fuente direccional evita esas limitaciones. Para estructuras puntuales como montículos (a diferencia de rasgos lineales como caminos o terrazas agrícolas), la literatura recomienda radios de búsqueda pequeños.
7. **Interpretación arqueológica.** Contraste del microrelieve resultante contra el relevamiento topográfico convencional de 2010, identificación de estructuras monticulares conocidas y de rasgos adicionales no documentados previamente.

> **Nota metodológica:** las técnicas de visualización multi-escala (sky-view factor, openness, PCA de hillshades) dependen de parámetros empíricos (radio de búsqueda, orientación), lo que puede introducir sesgos hacia estructuras de tamaños o morfologías específicas. Esta limitación fue considerada en la elección de parámetros para este relevamiento.

---

## Resultados

- El LiDAR detectó exitosamente las estructuras monticulares (concheros) ya conocidas, previamente relevadas por topografía convencional en 2010, validando la técnica contra un registro de referencia.
- Se identificaron además rasgos microtopográficos adicionales no evidentes en el relevamiento topográfico previo, incluyendo evidencias de intervenciones arqueológicas anteriores sobre el conchero principal.
- El relevamiento de zonas adyacentes permitió reconocer áreas con características geomorfológicas comparables, de interés para prospección futura.
- Se generaron modelos y mapeos volumétricos de alta resolución del sitio.

*(Los resultados los podra encontrar en la respectiva carpeta)*

---

## Herramientas

- **Planificación de vuelo:** DJIFlightPlanner
- **Procesamiento LiDAR:** LiDAR360 v4.1.5 (clasificación, strip adjustment, generación de DEM/DSM) y QuickTerrainModeler (QTM)
- **Sensor:** DJI Zenmuse L2

---

## Referencias

Lemos, J.; Aubet, N.; Lamas, N.; Beovide, L. *Aplicación experimental de tecnología LIDAR para el relevamiento de concheros precoloniales en la cuenca inferior del río Santa Lucía (Uruguay)*. CIRAT/PIAAD/MEC — GIEx, UTEC. Resumen presentado a congreso.

**Metodología de procesamiento y visualización:**

- Štular, B.; Lozić, E. Comparison of Filters for Archaeology-Specific Ground Extraction from Airborne LiDAR Point Clouds. *Remote Sensing*, 12(18), 3025, 2020.
- Doneus, M.; Höfle, B.; Kempf, D.; Daskalakis, G.; Shinoto, M. Human-in-the-loop development of spatially adaptive ground point filtering pipelines — an archaeological case study. *Archaeological Prospection*, 29(4), 503–524, 2022.
- Štular, B.; Eichert, S.; Lozić, E. Airborne LiDAR Point Cloud Processing for Archaeology: Pipeline and QGIS Toolbox. *Remote Sensing*, 13(16), 3225, 2021.
- Zakšek, K.; Oštir, K.; Kokalj, Ž. Sky-View Factor as a Relief Visualization Technique. *Remote Sensing*, 3(2), 398–415, 2011.
- Kokalj, Ž.; Zakšek, K.; Oštir, K. Visualizations of lidar derived relief models, en *Interpreting Archaeological Topography*, 2013.
- Detecting Neolithic burial mounds from LiDAR-derived elevation data using a multi-scale approach and machine learning techniques. *Remote Sensing*, 10(2), 225, 2018.
- Airborne LiDAR point cloud processing for archaeology: pipeline and QGIS toolbox. Journal of Computer Applications in Archaeology, 2021.
- Zakšek, K.; Oštir, K.; Kokalj, Ž. Sky-view factor as a relief visualization technique. Remote Sensing, 3(2), 398–415, 2011.
- Kokalj, Ž.; Zakšek, K.; Oštir, K. Visualizations of lidar derived relief models, en Interpreting Archaeological Topography, 2013.
