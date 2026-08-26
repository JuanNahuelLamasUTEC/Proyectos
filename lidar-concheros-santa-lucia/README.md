Aplicación de tecnología LiDAR para el relevamiento de concheros precoloniales — cuenca inferior del río Santa Lucía, Uruguay
Contexto

Proyecto conjunto entre el Grupo de Investigaciones Espaciales (GIEx, UTEC) y el Laboratorio de Análisis Espacial del CIRAT (Centro de Investigación Regional Arqueológica y Territorial / PIAAD / MEC), orientado a evaluar el uso de sensores LiDAR aerotransportados para la identificación y caracterización de estructuras arqueológicas tipo conchero (montículos de origen antrópico precolonial) en ambientes costeros y de humedal.

El relevamiento se realizó sobre un sitio con estructuras monticulares previamente identificadas y relevadas mediante topografía convencional en 2010, lo que permitió comparar la técnica LiDAR contra un registro topográfico preexistente. Constituye la primera aplicación de esta tecnología a un sitio arqueológico en Uruguay.

Los resultados fueron presentados como resumen en congreso (en coautoría con CIRAT/MEC y GIEx-UTEC).

Nota sobre datos sensibles: por tratarse de sitios con protección patrimonial, este repositorio no incluye coordenadas exactas, nubes de puntos georreferenciadas, ni cartografía de detalle del sitio. Se muestran únicamente metodología, parámetros técnicos de vuelo y procesamiento, y resultados descriptivos generales.

Mi rol en el proyecto

Trabajo en equipo interinstitucional (GIEx-UTEC / CIRAT-MEC). Responsable de:

Planificación y organización del vuelo LiDAR (definición de zonas de cobertura y patrones de vuelo).
Procesamiento de la nube de puntos.
Interpretación de los productos derivados (DEM, DSM) para la identificación de estructuras y microrelieve.
Equipo y sensor
Plataforma: dron con sensor DJI Zenmuse L2 (LiDAR + cámara RGB).
Altura de vuelo: 80 m AGL.
Densidad de puntos resultante: 242 pts/m².
Diseño de vuelo

Se definieron zonas de cobertura diferenciadas según prioridad, con dos patrones de vuelo:

Zona	Patrón	GSD	Observación
Prioridad A	Grillado doble (cross-hatch, doble pasada perpendicular)	1.62 cm/px	Máxima prioridad — mayor densidad y redundancia de puntos para minimizar error de alineación entre franjas
Prioridad B	Grillado simple (single-grid)	1.89 cm/px	Cobertura general del sitio
Zona de inspección	Grillado simple	1.62 cm/px	Área adyacente, relevada para contexto geomorfológico

El uso de grillado doble en la zona de prioridad A responde directamente a una decisión metodológica: al superponer dos pasadas perpendiculares se reduce el efecto de desalineación de franjas (strip misalignment) que suele producirse por deriva del sistema GNSS/IMU en vuelos de única pasada, especialmente relevante en un levantamiento de alta precisión sobre microrelieve.

Procesamiento y solución técnica

Problema identificado: durante el procesamiento en LiDAR360 se detectaron discontinuidades altimétricas entre franjas de vuelo adyacentes (strip misalignment), que de no corregirse introducen ruido artificial en el DEM y pueden enmascarar o simular microrelieve real — un riesgo particular en este tipo de aplicación, donde el objetivo es precisamente detectar variaciones sutiles de relieve de origen antrópico.

Solución aplicada: ajuste de franjas mediante la herramienta Strip Adjustment de LiDAR360, que corrige los desvíos relativos entre pasadas de vuelo (offsets planimétricos y altimétricos) antes de la generación de los productos derivados, asegurando consistencia geométrica entre franjas superpuestas.

Workflow
Vuelo LiDAR con patrones diferenciados por zona de prioridad (ver tabla arriba).
Control de calidad de la nube de puntos cruda.
Corrección de desalineación de franjas (Strip Adjustment, LiDAR360).
Clasificación de la nube de puntos (suelo / no suelo).
Generación de DEM (modelo digital de elevación, solo puntos de suelo) y DSM (modelo digital de superficie, incluye vegetación y estructuras).
Interpretación visual y análisis del microrelieve derivado para identificación de estructuras monticulares y rasgos de intervención previa.
Resultados
El LiDAR detectó exitosamente las estructuras monticulares (concheros) ya conocidas, previamente relevadas por topografía convencional en 2010 — validando la técnica contra un registro de referencia.
Se identificaron además rasgos microtopográficos adicionales no evidentes en el relevamiento topográfico previo, incluyendo evidencias de intervenciones arqueológicas anteriores sobre el conchero principal.
El relevamiento de zonas adyacentes permitió reconocer áreas con características geomorfológicas comparables, de interés para prospección futura.
Se generaron modelos y mapeos volumétricos de alta resolución del sitio.
Herramientas
Planificación de vuelo: software de misión para DJI (grillado simple/doble por zona).
Procesamiento LiDAR: LiDAR360 v4.1.5 (clasificación, strip adjustment, generación de DEM/DSM).
Sensor: DJI Zenmuse L2.
