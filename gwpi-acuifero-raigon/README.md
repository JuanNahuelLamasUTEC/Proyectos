
# Índice de Potencial de Aguas Subterráneas (GWPI) por Proceso Analítico Jerárquico
### Acuífero Raigón, Ciudad del Plata–Libertad, San José

---

## Contexto

Este trabajo forma parte del informe final de un proyecto de investigación multi-institucional financiado externamente (*"Studying the effects of climate change and variability on water resources in Uruguay"*, Ref. RCC002NODA), con participación de **UTEC, UdelaR, CeReGAS** (Centro Regional para la Gestión de Aguas Subterráneas, Centro de Categoría II UNESCO) y el **Ministerio de Ambiente**, entre otras instituciones nacionales y de la región.

> **Nota:** el informe completo del proyecto se encuentra actualmente en proceso de publicación formal. Este repositorio documenta exclusivamente la metodología AHP/GWPI, de mi autoría dentro del equipo de trabajo, sin reproducir mapas oficiales, figuras del informe completo, ni datos de base (pozos, hidroquímica) que pertenecen al conjunto del proyecto.

El área de estudio corresponde al piloto **Ciudad del Plata–Libertad (San José)**, sobre el Sistema Acuífero Raigón, una zona costera de aproximadamente **700 km²** con fuerte presión productiva (horti-fruticultura irrigada) y necesidad de planificación sostenible del recurso hídrico subterráneo.

---

## Mi rol en el proyecto

Responsable único del diseño y ejecución del análisis AHP/GWPI: definición de criterios, construcción de la matriz de comparación pareada, reclasificación de las doce capas temáticas, procesamiento en SIG, e integración del índice final.

---

## Metodología

El Índice de Potencial de Aguas Subterráneas (GWPI) se calculó mediante Evaluación Multicriterio (MCDA) resuelta con el **Proceso Analítico Jerárquico** (AHP, Saaty, 1980), integrando doce capas temáticas dentro de un Sistema de Información Geográfica:

```
GWPI = Σ (Rating capa i [1–5] × Peso relativo Wp de la capa i)
```

Los pesos relativos se calcularon por el **método del autovector principal**, y la consistencia de la matriz se verificó mediante la Razón de Consistencia de Saaty (CR), aceptando valores menores a 0.10. La matriz final de doce criterios obtuvo **CR = 0.0093**, ampliamente dentro del margen aceptado.

### Capas temáticas y ponderación

| Capa temática | Peso relativo (Wp) |
|---|---|
| Geología | 0.161 |
| Geomorfología | 0.146 |
| Uso y cobertura del suelo (MapBiomas) | 0.143 |
| Índice Topográfico de Humedad (TWI) | 0.126 |
| Pendiente | 0.110 |
| Densidad de drenaje | 0.089 |
| Distancia a cursos de agua | 0.076 |
| Precipitación | 0.053 |
| Evapotranspiración | 0.038 |
| Curvatura | 0.026 |
| Modelo digital de elevación (DEM) | 0.018 |
| Temperatura | 0.014 |

Geología y Geomorfología encabezan la jerarquía por su control de primer orden sobre la porosidad y permeabilidad del subsuelo.

---

## Procedimiento de reclasificación

**Variables continuas con variación espacial** (pendiente, DEM, TWI, curvatura, densidad de drenaje, distancia a cursos de agua): clasificadas en cinco categorías mediante el método de Rupturas Naturales (Jenks), calculado sobre el ráster del área de estudio en cada caso — en vez de adoptar umbrales numéricos de estudios de referencia, dado que variables como el TWI dependen del algoritmo de flujo y la resolución del modelo de elevación utilizado (Sørensen et al., 2006). De la literatura se tomó exclusivamente el sentido de favorabilidad de cada variable.

**Variables categóricas** (Geología, Geomorfología, Uso del suelo): reclasificadas por unidad o clase según la conductividad hidráulica, porosidad o comportamiento hidrológico documentado en la bibliografía correspondiente. El método de Rupturas Naturales no es aplicable a estas capas por tratarse de unidades categóricas discretas.

**Variables climáticas homogéneas** (Precipitación, Evapotranspiración Real, Temperatura): representadas por un valor único para toda el área de estudio, decisión acordada por el equipo de trabajo en función de dos consideraciones: la reducida extensión del área de estudio en relación a la resolución espacial de los productos climáticos disponibles, y el peso conjunto reducido de estas tres capas dentro de la matriz AHP (10.5%). El rating se determinó comparando el valor local contra el promedio nacional de Uruguay — un criterio metodológico propio del trabajo, sin respaldo bibliográfico directo en la literatura AHP-GWP consultada, aunque conceptualmente análogo al principio de los índices de anomalía climática (p. ej., el Standardized Precipitation Index).

---

## Rating de Geología

Basado en Bessouat, Castagnino, De los Santos y Robano — *"Acuífero Raigón Parte 1: Caracterización Geohidrológica"* y *"Parte 2: Carta de Vulnerabilidad"* — que aplican la metodología DRASTIC (Aller et al., 1987) a las formaciones geológicas del área. Se utilizaron específicamente los sub-índices "Tipo de Acuífero" e "Impacto de la Zona Vadosa" de esa fuente, no el Índice de Vulnerabilidad agregado, por corresponder a una medida de conductividad hidráulica y porosidad litológica transferible a un modelo de potencial, más allá de que el marco DRASTIC original fue concebido para evaluar vulnerabilidad a la contaminación.

| Unidad | Rating | Justificación |
|---|---|---|
| Raigón | 4 | Acuífero principal del sistema; arenas moderadamente seleccionadas de alta transmisividad (DRASTIC 8/10) |
| Duna | 1 | Arena eólica no consolidada |
| Formación Camacho | 5 | Litología heterogénea (facies arenosas y arcillosas), con transición gradual local a Raigón + Camacho (confinado) |
| Sedimentos actuales / arenas costeras / cordones litorales | 1 | Arena bien seleccionada de ambiente costero reciente |
| Formación Chuy | 4 | Arenas predominantemente medias a finas |
| Formación Dolores | 4 | Arcillas y limos con contenido arenoso subordinado (Chuy confinado) |
| Formación Libertad | 5 | Limos arcillosos/esmectíticos, actúa como unidad confinante sobre la Formación Raigón |
| Basamento precámbrico | 1 | Gneises y granitos, fracturado, porosidad primaria nula |

---

## Rating de Uso del Suelo

Fuente: MapBiomas Uruguay, Colección 3. Calibrado combinando literatura internacional de AHP aplicado a potencial de aguas subterráneas (Vamanapuram, India, clima tropical húmedo comparable) con literatura regional sobre efectos hidrológicos de la forestación con especies exóticas en el Cono Sur (Nosetto, Jobbágy, Houspanossian et al.; Proyecto Hidroforestal, IMFIA-UdelaR).

| Clase MapBiomas | Rating | Justificación |
|---|---|---|
| Cuerpos de agua | 1 | Recarga directa |
| Bañados, humedales | 3 | Saturación permanente o estacional, equivalente a TWI muy alto |
| Bosque nativo | 4 | Los sistemas radiculares de especies nativas promueven infiltración sin el consumo hídrico excesivo asociado a exóticas |
| Pastizal natural | 4 | Cobertura herbácea sin intercepción de dosel arbóreo |
| Pastizal implantado | 3 | La compactación por pastoreo reduce la porosidad superficial del suelo |
| Agricultura de riego | 2 | El perfil productivo de Ciudad del Plata-Libertad es horti-frutícola con riego creciente desde el propio Acuífero Raigón; se descartó la hipótesis de agricultura de secano por no ajustarse al perfil agronómico local |
| Eucalipto implantado | 1 | Consumo hídrico elevado y efecto de compuestos hidrofóbicos del suelo documentado por el Proyecto Hidroforestal (IMFIA-UdelaR); ver literatura regional sobre forestación con exóticas y balance hídrico |
| Pino implantado | 1 | Consumo hídrico perenne; revierte el balance de recarga a descarga |

*(tabla completa de 12 clases disponible bajo solicitud)*

---

## Ajustes metodológicos por criterio experto

Durante el desarrollo del trabajo se identificaron situaciones donde la bibliografía general no era directamente aplicable al contexto específico del área, requiriendo ajustes documentados:

- **Villa Soriano:** el sub-índice DRASTIC (7/10) no era representativo de la litología descrita (arena mal seleccionada, con matriz arcillosa); el rating se ajustó a 3, documentando la discrepancia respecto a la fuente.
- **Agricultura en San José:** se evaluaron dos interpretaciones bibliográficas opuestas — la convención internacional AHP-GWP (rating bajo para agricultura de riego) versus el hallazgo de Nosetto, Jobbágy y Houspanossian sobre agricultura de secano en la Pampa húmeda (que favorecería un rating mayor) — adoptando la primera en virtud del perfil productivo real horti-frutícola e irrigado del área.
- **Playa y Planicie Aluvial Activa:** el rating se redujo de 5 a 4 en ambos casos por consideraciones de campo (riesgo de cuña salina y contenido arcilloso local, respectivamente).
- **Relación DRASTIC–GWP:** se estableció que ambos marcos comparten el control físico de la permeabilidad pero responden preguntas conceptualmente distintas (vulnerabilidad a la contaminación vs. potencial de explotación), por lo que se usaron solo los sub-índices DRASTIC de permeabilidad, no su índice de vulnerabilidad agregado.
- **Capas climáticas:** el valor homogéneo y el criterio de comparación contra el promedio nacional constituyen una decisión metodológica propia del equipo, sin antecedente bibliográfico específico en la literatura AHP-GWP revisada.

---

## Procedimiento en el Sistema de Información Geográfica

**Capa de geomorfología:** las geoformas de naturaleza lineal (sendas, acantilados, escarpes, cordones costeros, canales de marea) se convirtieron a polígonos mediante la herramienta *Buffer*, con ancho definido según la naturaleza de cada geoforma. Cada una de las catorce capas resultantes recibió un campo de rating (1 a 5) mediante *Add Field* y *Calculate Field*, y se disolvió a un elemento multiparte mediante *Dissolve*. La conversión a formato ráster se realizó mediante *Polygon to Raster*, con el método de asignación de celda *Maximum Area* (necesario para preservar las geoformas más pequeñas), manteniendo el mismo tamaño de celda y ráster de referencia (*snap raster*) que el resto del conjunto.

La integración de las catorce capas ráster se realizó mediante *Mosaic to New Raster*, con el operador *Mosaic First*, respetando un orden cartográfico de prioridad (independiente del valor de rating) diseñado para resolver superposiciones de digitalización según certeza y especificidad de cada geoforma.

**Capas climáticas de valor homogéneo:** se generó un ráster de valor constante (*Create Constant Raster*) correspondiente al rating asignado (no al valor físico), sobre la extensión y tamaño de celda del ráster de referencia del proyecto, ajustado luego mediante *Extract by Mask* a los límites reales del área de estudio.

**Integración final:** la suma ponderada de las doce capas se ejecutó mediante la herramienta *Weighted Sum* de Spatial Analyst, que multiplica el valor de cada celda por el peso relativo asignado y suma los resultados, produciendo el índice GWPI de forma continua. El resultado se reclasificó posteriormente en cinco categorías de potencial (muy bajo a muy alto) mediante el método de Rupturas Naturales aplicado a la distribución real de valores del área de estudio.

---

## Herramientas

- **ArcGIS Pro** (Spatial Analyst: Weighted Sum, Polygon to Raster, Mosaic to New Raster, Extract by Mask, Reclassify)
- Análisis de matriz AHP (método del autovector principal, Razón de Consistencia de Saaty)

---

## Referencias

- Saaty, T.L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
- Machiwal, D.; Jha, M.K.; Mal, B.C. (2011). *Water Resources Management*, 25, 1359–1386.
- Beven, K.J.; Kirkby, M.J. (1979). *Hydrological Sciences Bulletin*, 24(1), 43–69.
- Moore, I.D.; Grayson, R.B.; Ladson, A.R. (1991). *Hydrological Processes*, 5(1), 3–30.
- Sørensen, R.; Zinko, U.; Seibert, J. (2006). *Hydrology and Earth System Sciences*, 10, 101–112.
- Freeze, A.R.; Cherry, J.A. (1979). *Groundwater*. Prentice-Hall.
- Doke, A.B.; Zolekar, R.B.; Patel, H.; Das, S. (2021). *Ecological Indicators*.
- Madrucci, V.; Taioli, F.; de Araújo, C.C. (2008). *Journal of Hydrology*, 357(3-4), 153–173.
- Franca Rocha, W.; Vasconcellos Garcia, A.J.; Dantas de Menezes Ribeiro, D. (2011). *Revista Ambiente & Água*, 6(2), 206–231.
- Montaño Xavier, J. et al. (2006). *Boletín Geológico y Minero*, 117(1), 201–222.
- Bessouat, C.; Castagnino, G.; De los Santos, J.; Robano, M. *Acuífero Raigón — Parte 1 (Caracterización geohidrológica) y Parte 2 (Carta de Vulnerabilidad)*. 1st Joint World Congress on Groundwater.
- Aller, L. et al. (1987). *DRASTIC: A Standardized System for Evaluating Groundwater Pollution Potential Using Hydrogeologic Settings*. United States Environmental Protection Agency.
- Nosetto, M.D.; Jobbágy, E.G.; Paruelo, J.M. (2005). *Global Change Biology*, 11, 1101–1117.
- Houspanossian, J.; Giménez, R.; Whitworth-Hulse, J.I.; Nosetto, M.D.; Tych, W.; Atkinson, P.M.; Rufino, M.C.; Jobbágy, E.G. (2023). *Science*, 380(6652), 1344–1348.
- Dirección Nacional de Aguas (DINAGUA) — Balance hídrico por cuencas (comunicación interna del proyecto, agosto de 2026).
- Instituto Uruguayo de Meteorología (INUMET) — Temperatura media anual de referencia nacional.
- Dirección Nacional de Aguas (DINAGUA) — Balance hídrico por cuencas (comunicación interna del proyecto, agosto de 2026).
- Instituto Uruguayo de Meteorología (INUMET) — Temperatura media anual de referencia nacional.
