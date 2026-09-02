# Portafolio de Proyectos Geoespaciales

**Juan Nahuel Lamas** — Geólogo (Lic. en Ciencias Geológicas, FCEN-UBA) · Investigador en GIEx, UTEC · Maestrando UdelaR/PEDECIBA

[![GitHub](https://img.shields.io/badge/GitHub-JuanNahuelLamasUTEC-181717?logo=github)](https://github.com/JuanNahuelLamasUTEC)

---

Repositorio de proyectos de geoprocesamiento aplicado a investigación ambiental, hidrogeológica y arqueológica, desarrollados en el marco de mi trabajo en el **Grupo de Investigaciones Espaciales (GIEx)**, Universidad Tecnológica del Uruguay (UTEC), ITR Centro-Sur.

Cada carpeta corresponde a un proyecto independiente, con su propio README documentando contexto, metodología, herramientas y resultados. No se reproducen datos, mapas ni cartografía oficial de proyectos con informes aún en proceso de publicación o de sitios arqueológicos protegidos — el detalle de estas restricciones está aclarado en el README de cada carpeta.

## Summary — English

This repository is a portfolio of applied geospatial research projects spanning LiDAR archaeology, GIS-based groundwater potential modeling, and UAV multisensor photogrammetry, developed within the Grupo de Investigaciones Espaciales (GIEx) at Universidad Tecnológica del Uruguay (UTEC). Each project folder includes its own README documenting context, methodology, tools, and results, with a short English summary. The author is a geologist (FCEN-UBA) and current master's student (UdelaR/PEDECIBA) working on GIS, remote sensing, UAV/LiDAR acquisition, and geospatial programming (Python, GeoPandas).

## Competencias demostradas (Ref. TGEO 1/26)

Correspondencia entre los conocimientos específicos solicitados en el llamado y la evidencia disponible en este portafolio:

| Requisito del llamado | Tipo | Evidencia en este portafolio |
|---|---|---|
| Manejo avanzado de software SIG | Excluyente | ArcGIS Pro (Spatial Analyst, ModelBuilder), QGIS — proyecto GWPI |
| Programación para análisis geoespacial (Python, GeoPandas) | Excluyente | Scripts Python con tests unitarios (`ahp_utils.py`, `weighted_sum_raster.py`) — proyecto GWPI |
| Formatos y estándares geoespaciales (GeoTIFF, shp, .las, .rjpg, .gpkg, etc.) | Excluyente | .las/.laz (LiDAR), GeoTIFF/shp (GWPI), .rjpg — imágenes térmicas radiométricas DJI (picudo rojo) |
| Software de fotogrametría y LiDAR | Excluyente | Pix4D, Agisoft Metashape, LiDAR360 v4.1.5 |
| Inglés nivel intermedio | A valorar | Resumen en inglés incluido en cada proyecto de este portafolio |
| Trabajo interdisciplinario con instituciones públicas/académicas | A valorar | GWPI (UdelaR, CeReGAS/UNESCO, Ministerio de Ambiente); LiDAR (CIRAT/MEC) |
| Manejo de IA y plataformas de IA generativa | A valorar | Portafolio construido con apoyo de IA (ver nota al pie); segmentación en picudo rojo basada en vision transformers |
| Computer vision y machine learning | A valorar | Segmentación híbrida OBIA + vision transformers para delimitación de copas (proyecto picudo rojo) |
| Portafolio verificable: 1 proyecto SIG + 1 fotogrametría + 1 LiDAR | Excluyente | Los tres proyectos de este repositorio |
| Experiencia docente terciaria universitaria en el área | Excluyente | [`Experiencia Docente/`](./Experiencia%20Docente) — 3 años (2023-2025) como Docente Encargado de Ordenamiento Ambiental, UTEC |
| Experiencia en proyectos I+D con datos geoespaciales | A valorar | GWPI (proyecto RCC002NODA, multi-institucional); LiDAR (CIRAT/MEC); Amenaza Roboto |

*Nota: "Formación específica en SIG/Teledetección" (a valorar) se refleja en la aplicación práctica documentada en los tres proyectos técnicos y en la carpeta de experiencia docente; no corresponde a una certificación formal adicional.*

## Proyectos

| Proyecto | Tema | Herramientas principales |
|---|---|---|
| [`lidar-concheros-santa-lucia/`](./lidar-concheros-santa-lucia) | Detección de concheros precoloniales (cerritos de indios) en la cuenca baja del río Santa Lucía mediante datos LiDAR aerotransportado | DJI Zenmuse L2 · LiDAR360 v4.1.5 · clasificación de nube de puntos, DEM/DSM |
| [`gwpi-acuifero-raigon/`](./gwpi-acuifero-raigon) | Índice de Potencial de Aguas Subterráneas (GWPI) del Acuífero Raigón mediante Proceso Analítico Jerárquico (AHP) multicriterio | ArcGIS Pro · ModelBuilder · Python (NumPy, mapclassify) |
| [`fotogrametria-picudo-rojo/`](./fotogrametria-picudo-rojo) | Detección temprana de picudo rojo (*Rhynchophorus ferrugineus*) en palmeras mediante imágenes RGB, multiespectrales y térmicas de dron | Pix4D · Agisoft Metashape · DJI Thermal Tools · QGIS |
| [`Experiencia Docente/`](./Experiencia%20Docente) | Materiales y consignas de la unidad curricular Ordenamiento Ambiental (2023-2025), con ejercicios de análisis de uso del suelo, clasificación supervisada, vulnerabilidad de acuíferos y geomorfología | QGIS · ArcGIS Pro · R (randomForest) |

## Stack técnico

**SIG y geoprocesamiento:** ArcGIS Pro (ModelBuilder, Spatial Analyst), QGIS
**Programación geoespacial:** Python, GeoPandas, NumPy
**LiDAR y nubes de puntos:** LiDAR360, formatos .las/.laz
**Fotogrametría y sensores UAV:** Pix4D, Agisoft Metashape, DJI Thermal Tools, sensores RGB/multiespectral/térmico
**Análisis de datos geoespaciales:** MapBiomas, Google Earth Engine, análisis multicriterio (AHP)

## Contexto institucional

Trabajo desarrollado en el **Grupo de Investigaciones Espaciales (GIEx)**, UTEC — ITR Centro-Sur (Durazno), donde también me desempeño como docente en el área de Ingeniería Agroambiental. Formo parte del equipo de investigación del proyecto multi-institucional *"Studying the effects of climate change and variability on water resources in Uruguay"* (UTEC, UdelaR, CeReGAS/UNESCO, Ministerio de Ambiente) y del proyecto de periodismo de datos [Amenaza Roboto](https://amenazaroboto.com/) (Pulitzer Center, Premio Sigma).

## Contacto

- Email: [juan.lamas@utec.edu.uy](mailto:juan.lamas@utec.edu.uy)
- LinkedIn: [Nahuel Lamas](https://uy.linkedin.com/in/nahuel-lamas-998a781a1)
- GitHub: [@JuanNahuelLamasUTEC](https://github.com/JuanNahuelLamasUTEC)
- Institución: UTEC — Grupo de Investigaciones Espaciales (GIEx)

---

> *Nota: la redacción y estructura de este portafolio fue asistida con IA (Claude, Anthropic). El análisis, la metodología y los resultados son de autoría propia.*
