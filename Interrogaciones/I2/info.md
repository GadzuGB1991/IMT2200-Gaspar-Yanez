Hallazgo Principal: Correlación PIB vs. Expectativa de VidaDespués de limpiar y unir los dos conjuntos de datos, calculé la correlación de Pearson entre el PIB de un país en 2021 y su expectativa de vida en 2021.El coeficiente de correlación es: $0.2171$Esto indica una correlación positiva débil. En otras palabras, aunque existe una tendencia a que los países con mayor PIB tengan una mayor expectativa de vida, la relación no es muy fuerte, lo que sugiere que muchos otros factores (como el sistema de salud, la educación, el estilo de vida, etc.) influyen significativamente

Fase 1: Transformación de DatosDatos de OMS: Se cargaron, se extrajo el valor numérico (ej. 51.5 de "51.5 [50.5-52.6]") y se filtraron los datos para Life expectancy at birth (years) y Both sexes. El resultado es un DataFrame limpio (df_who_clean) con 4070 filas.

Datos del PIB: Se cargaron y se transformaron de formato "ancho" a "largo" (usando pd.melt), resultando en 1159 filas con Country, Year y GDP.DataFrame Maestro: Se unieron ambos conjuntos de datos. 

El df_master final contiene 321 filas con datos coincidentes de PIB y Esperanza de Vida.Fase 2: Análisis Exploratorio (EDA)Estadísticas: La esperanza de vida media en el conjunto de datos es de 71.5 años, con un PIB medio de 366,404 (millones).

Correlación: La correlación de Pearson entre PIB y Esperanza de Vida es 0.2138. Es una correlación positiva débil, lo que sugiere que, si bien hay una tendencia, el PIB por sí solo no es un predictor lineal fuerte.

Visualizaciones: Se generaron las dos gráficas solicitadas (ver imágenes).histograma_vida.png: Muestra la distribución de la esperanza de vida.scatter_gdp_vida.png: Muestra la relación entre PIB (en escala logarítmica) y Esperanza de Vida.

Fase 3: Aprendizaje de Máquinas (ML)Tarea A: Regresión (Predecir Esperanza de Vida)Objetivo: Predecir el número exacto de años de esperanza de vida usando el PIB.Resultados:$MSE$: 42.25$

R^2$: -0.0038 (¡muy bajo, cercano a cero!)

Interpretación (Ref: PDF 19): Un $R^2$ tan bajo significa que el PIB por sí solo no explica casi nada de la variación en la esperanza de vida en este modelo lineal. Esto confirma lo que vimos en la débil correlación.Tarea B: Clasificación (Predecir "Alta" o "Baja" Esperanza de Vida)Objetivo: Clasificar si un país tiene esperanza de vida "Alta" ( $> 72.6$ años) o "Baja" ( $\le 72.6$ años) usando el PIB.Resultados (Regresión Logística - Ref: PDF 21):Tiene una precisión (accuracy) total del 63%.Es bueno para identificar a los de esperanza de vida "Baja" (Recall = 0.94) pero muy malo para identificar a los de "Alta" (Recall = 0.31).Resultados (Árbol de Decisión - Ref: PDF 23):Tiene una precisión total del 63%.Es más equilibrado: identifica correctamente al 52% de la clase "Baja" y al 75% de la clase "Alta".Conclusión General de la Prueba: La limpieza y unión de datos fue exitosa. El análisis (EDA y ML) demuestra que, aunque existe una ligera tendencia positiva, el PIB por sí solo es un predictor muy pobre para la esperanza de vida de un país.