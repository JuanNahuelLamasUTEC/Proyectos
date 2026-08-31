# Fotogrametría UAV multisensor para caracterización fenotípica de palmeras — detección temprana de picudo rojo

## Contexto

Trabajo de campo y procesamiento fotogramétrico desarrollado en el marco de la línea de investigación del Grupo de Investigaciones Espaciales (GIEx, UTEC) sobre detección temprana de picudo rojo (*Rhynchophorus ferrugineus*) en palmeras *Phoenix canariensis*, en sitios piloto de Montevideo y Maldonado. Constituye la etapa preliminar de fotogrametría UAV y generación de ortomosaicos sobre la cual se apoya el desarrollo posterior de modelos de clasificación del estado sanitario de los ejemplares.

## Mi rol en el proyecto

Planificación y ejecución de misiones de vuelo UAV. Procesamiento fotogramétrico completo: ensamblaje de imágenes, calibración radiométrica y generación de nubes de puntos, modelos digitales de superficie (DSM) y ortomosaicos georreferenciados. Vectorización y delimitación de palmeras individuales mediante SIG para su georreferenciación y análisis espacial. Preparación y estandarización de matrices ráster para su integración en modelos analíticos posteriores.

## Metodología

**Adquisición de datos.** Siguiendo los fundamentos establecidos por Berni et al. (2009) para plataformas UAV livianas con sensores multiespectrales y térmicos, se ejecutan misiones de vuelo con solapamiento frontal y lateral igual o superior al 80%, en condiciones atmosféricas homogéneas, con calibración radiométrica mediante paneles de reflectancia antes y después de cada vuelo, según los protocolos de Zarco-Tejada et al. (2012).

**Procesamiento fotogramétrico.** Las imágenes se procesan mediante técnicas de estructura a partir de movimiento (*Structure from Motion*) para generar ortomosaicos georreferenciados de alta resolución y modelos digitales de superficie.

**Delimitación de copas individuales.** Se aborda mediante un enfoque híbrido: análisis de imagen orientado a objetos (OBIA) como línea base, complementado con modelos de segmentación basados en arquitecturas de visión fundacionales, en la línea de los transformers de visión propuestos por Gibril et al. (2023) para segmentación a gran escala de palmeras datileras por UAV — un enfoque que reduce la dependencia de umbrales manuales en dosel urbano denso y heterogéneo.

**Extracción de variables.** Para cada copa segmentada se calculan índices espectrales de banda estrecha (NDVI, GNDVI, NDRE, OSAVI), estadísticas de temperatura de copa, métricas de textura derivadas de matrices de co-ocurrencia, y atributos estructurales (altura, volumen, rugosidad del dosel) obtenidos del modelo digital de superficie — insumos que luego alimentan los modelos de clasificación del estado sanitario.

## Herramientas

- Plataforma UAV con sensores RGB, multiespectral y térmico embarcados.
- Software de fotogrametría para procesamiento SfM (generación de nube de puntos, DSM, ortomosaico).
- SIG (vectorización, georreferenciación, análisis espacial de copas individuales).
- Python para extracción de variables espectrales/texturales y preparación de matrices ráster.

## Referencias

Berni, J. A. J.; Zarco-Tejada, P. J.; Suárez, L.; Fereres, E. (2009). Thermal and narrowband multispectral remote sensing for vegetation monitoring from an unmanned aerial vehicle. *IEEE Transactions on Geoscience and Remote Sensing*, 47(3), 722–738.

Zarco-Tejada, P. J.; González-Dugo, V.; Berni, J. A. J. (2012). Fluorescence, temperature and narrow-band indices acquired from a UAV platform for water stress detection using a micro-hyperspectral imager and a thermal camera. *Remote Sensing of Environment*, 117, 322–337.

Gibril, M. B. A. et al. (2023). Large-scale date palm tree segmentation from multiscale UAV-based and aerial images using deep vision transformers. *[Detalle de la publicación a confirmar]*.

Casas, E.; Arbelo, M.; Moreno-Ruiz, J. A.; Hernández-Leal, P. A.; Reyes-Carlos, J. A. (2023). UAV-based disease detection in palm groves of *Phoenix canariensis* using machine learning and multispectral imagery. *Remote Sensing*, 15(14), Article 3584.
