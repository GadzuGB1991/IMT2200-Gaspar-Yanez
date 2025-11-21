Gaspar Alejandro Yanez Flores
# Proyecto IMT-2200: Análisis de Datos Demográficos de Chile

##  Descripción del Proyecto

Este proyecto analiza tendencias demográficas en Chile, enfocándose en:
- **Nacimientos** (1992-2022): Análisis de series temporales de nacimientos por región, edad de progenitores y educación
- **Censo 2024**: Datos de población, educación y fecundidad a nivel comunal
- **Índice de Vulnerabilidad Social (RSH)**: Distribución de vulnerabilidad por quintiles (0-40%, 41-50%, etc.) a nivel nacional, regional y comunal

**Audiencia objetivo**: Ministerio de Desarrollo Social y Familia

---

##  Estructura del Repositorio

```
.
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias del proyecto
├── a.ipynb                            # Notebook exploratorio inicial
│
├── notebooks/                         # Jupyter Notebooks con análisis
│   ├── analisis_final.ipynb          #  NOTEBOOK PRINCIPAL - Análisis completo
│   ├── orden_series_nacimiento.ipynb # Limpieza y procesamiento de datos de nacimientos
│   ├── rsh_unir_limpiar.ipynb        # Unificación y limpieza de datos RSH
│   ├── info_IV.ipynb                 # Procesamiento de índice de vulnerabilidad
│   └── censo_limpiar_.ipynb          # Limpieza de datos del censo 2024
│
├── Data/                              # Datos del proyecto
│   ├── clean data/                   # Datos procesados y limpios
│   │   ├── censo/
│   │   │   ├── 2017/                 # Censo 2017
│   │   │   │   ├── README.md
│   │   │   │   └── microdato2017.csv
│   │   │   └── 2024/                 # Censo 2024
│   │   │       ├── censo_2024_educacion.csv
│   │   │       ├── censo_2024_fecundidad.csv
│   │   │       └── censo_2024_poblacion.csv
│   │   ├── nacimientos/
│   │   │   └── Serie_nacimientos_1992-2022.parquet
│   │   └── RSH/
│   │       └── Tramos_RSH_2019-2025.csv
│   │
│   ├── dirty data/                   # Datos crudos sin procesar
│   │   ├── censo/
│   │   │   ├── 2017/
│   │   │   │   ├── README.md
│   │   │   │   └── csv-personas-censo-2017/
│   │   │   └── 2024/
│   │   ├── Datos_nacimientos/
│   │   │   └── README.md
│   │   ├── Nacimientos_1992-2022/
│   │   └── Set_de_Datos_RSH/
│   │
│   └── mapas vectoriales/
│       └── Comunas/
│
├── docs/                              # Documentación adicional
│   └── index.html
│
├── graficos/                          # Gráficos generados
│
├── defunciones/                       # Datos de defunciones (futuro)
│
└── web/                               # Sitio web del proyecto
    ├── index.html
    └── styles.css
```

---

##  Cómo Usar Este Repositorio

### Requisitos Previos
- Python 3.12.0+
- Pandas, NumPy, Matplotlib, Seaborn, scikit-learn

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Ejecución del Proyecto

1. **Para análisis completo** (punto de entrada principal):
   ```bash
   jupyter notebook notebooks/analisis_final.ipynb
   ```

2. **Para procesar datos por primera vez**:
   - Ejecutar `notebooks/censo_limpiar_.ipynb` para procesar censo
   - Ejecutar `notebooks/orden_series_nacimiento.ipynb` para procesar nacimientos
   - Ejecutar `notebooks/rsh_unir_limpiar.ipynb` para procesar RSH

---

##  Descripción de Notebooks

| Notebook | Descripción | Entrada | Salida |
|----------|-------------|---------|--------|
| **analisis_final.ipynb** | Análisis completo con visualizaciones principales | Datos limpios | Gráficos y conclusiones |
| **orden_series_nacimiento.ipynb** | Limpieza y renombrado de datos de nacimientos | CSV bruto | `Serie_nacimientos_1992-2022.parquet` |
| **rsh_unir_limpiar.ipynb** | Unificación de 47 archivos RSH CSV | 47 archivos RSH | `DATOS_CONSOLIDADOS_RSH.csv` |
| **info_IV.ipynb** | Agregación de RSH por quintiles por comuna | RSH consolidado | Datos agregados por comuna |
| **censo_limpiar_.ipynb** | Extracción de datos de censo 2024 | Excel/CSV | CSV procesados por tema |

---

##  Hallazgos Principales

- **Tendencia de natalidad**: Tendencia decreciente en nacimientos desde 1992
- **Vulnerabilidad social**: Concentración de vulnerabilidad en comunas específicas
- **Datos demográficos**: Cambios significativos en estructura de edad y educación

---

##  Fuentes de Datos

- [INE - Censos de Población](https://www.ine.gob.cl/estadisticas/sociales/censos-de-poblacion-y-vivienda/censo-de-poblacion-y-vivienda)
- [Ministerio de Desarrollo Social - Índice de Vulnerabilidad Social](https://www.desarrollosocialyfamilia.gob.cl/)
- Series de nacimientos 1992-2022

