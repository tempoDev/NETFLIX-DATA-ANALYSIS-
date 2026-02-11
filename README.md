## 📝 PRUEBA
Se me pide desarrollar un script donde, utilizando las librerías Pandas y MatPlotLib, debo sacar los 3 gráficos exigidos. Siendo estos:
- Distribución de tipos (% Películas - Series)
- Distribución por años de publicación
- Distribución por décadas
<img width="1920" height="967" alt="Figure_1" src="https://github.com/user-attachments/assets/32dd78d7-cda1-47d7-8165-39310bb80348" />
<img width="1920" height="967" alt="Figure_2" src="https://github.com/user-attachments/assets/cdc4c2bc-3e98-45e7-9332-a2bdbd69e41f" />
<img width="1920" height="967" alt="Figure_3" src="https://github.com/user-attachments/assets/b5198bbc-0b15-4fba-83a8-de3450c82ad0" />

  Igualmente, yo complementé mi prueba técnica añadiendo 3 gráficos más:
  - 10 países con mayor número de títulos y su porcentaje
  - Distribución del contenido de la plataforma por género
  - Duración promedio del contenido por décadas
<img width="1920" height="967" alt="Figure_4" src="https://github.com/user-attachments/assets/2411a5ab-3367-405c-9d5c-26847f707aa8" />
<img width="1920" height="967" alt="Figure_5" src="https://github.com/user-attachments/assets/b17b1d6e-b3b8-4590-8334-1545667b25e5" />
<img width="1920" height="967" alt="Figure_6" src="https://github.com/user-attachments/assets/5e9c258a-756d-4162-ab51-fdb365e5c6ee" />

 ## 🔗 Sistema de recomendación de contenidos (EXTRA • Built Beyond Requirements)

 Viendo la alta potencialidad y posibilidades del archivo facilitado, decidí realizar de motu propio un sistema de recomendación de contenido basado en **similitud de coseno** y **TF-IDF** que analiza las descripciones de películas y series de Netflix para sugerir títulos similares. Implementado como solución de **filtrado basado en contenido**.

 Para este script decidí hacer uso de la librería **scikit-learn**, ya que me permitía realizar de manera rápida y sencilla la **vectorización de texto** y su **cálculo de similitudes**.

 ### 🚀 Características

- ✅ Limpieza y preprocesamiento de datos
- ✅ Eliminación de duplicados y valores nulos
- ✅ Vectorización TF-IDF de descripciones
- ✅ Cálculo de similitud por coseno
- ✅ Sistema de recomendación parametrizable (top-N)
- ✅ Optimizado para el dataset de Netflix

### OUTPUT

Este sería una muestra de la salida que daría el script para una recomendación tipo dada la sugerencia de la serie Stranger things.

<img width="262" height="218" alt="RECOMENDACIONES" src="https://github.com/user-attachments/assets/c904ed08-99bd-46eb-a717-4ba793f2b492" />



