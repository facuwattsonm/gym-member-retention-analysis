# Gym Member Retention Analysis

> Qué distingue a un socio en riesgo de abandonar de uno consistente, sobre 973 miembros de un gimnasio — y por qué la palanca de retención no es la oferta de clases, sino el acompañamiento en las primeras semanas.

**Stack:** Python (pandas) · SQL sobre SQLite · Looker Studio

---

## 🎯 Problema
Un gimnasio con 973 socios activos no tenía forma de identificar, con datos, qué caracteriza a un miembro en riesgo de abandonar frente a uno consistente. Sin ese perfil, cualquier estrategia de retención era una apuesta a ciegas.

## 🔍 Enfoque
Pipeline completo en Python: limpieza y validación de datos (duplicados, rangos lógicos por columna, verificación cruzada de BMI contra peso/altura), creación de variables derivadas (grupo etario, categoría de BMI, nivel de engagement, riesgo de retención), carga a SQLite, 10 queries de análisis SQL, export a formato "BI-ready" para Looker Studio, y generación de los gráficos clave con matplotlib/seaborn.

**Riesgo de retención** se define como: *Alto riesgo* = entrena ≤2 días/semana **y** es principiante · *Bajo riesgo* = entrena ≥4 días/semana · el resto, *Riesgo medio*.

**Pipeline:** CSV crudo (Kaggle) → `clean_data.py` (limpieza + columnas derivadas) → `load_db.py` (carga a SQLite) → `queries.sql` (análisis) + `build_bi_export.py` (export a Looker Studio) + `analysis.py` (gráficos).

## 📊 Hallazgos clave
- **973 miembros**, edad promedio 38.7 años, distribución pareja entre géneros (511 hombres / 462 mujeres)
- **1 de cada 5 socios (20.2%, 197 personas)** cae en "alto riesgo": entrena ≤2 días/semana y es principiante
- Ese grupo entrena sesiones más cortas (**1.0h vs 1.49h** del segmento de bajo riesgo) y quema menos calorías por sesión (**726 vs 1068**)
- **La experiencia es el driver más fuerte de consistencia**, mucho más que el tipo de entrenamiento o el género: a medida que sube el nivel de experiencia, sube la frecuencia semanal (2.48 → 3.53 → 4.53 días) y las calorías quemadas (726 → 902 → 1265)
- El **tipo de entrenamiento no es un factor diferencial de riesgo**: Cardio, Fuerza, HIIT y Yoga se reparten de forma similar entre los tres segmentos de riesgo

## ✅ Recomendación
No cambiar la oferta de clases. Acompañar activamente al socio nuevo/principiante en sus primeras semanas (frecuencia y duración de sesión), que es la ventana crítica donde se decide si se retiene o se pierde al socio.

## 📂 Estructura del repo
```
├── data/
│   └── raw_gym_members.csv   # Dataset original (Kaggle, 973 filas, sin cambios)
├── sql/
│   └── queries.sql          # 10 queries de análisis sobre SQLite
├── scripts/
│   ├── clean_data.py         # Limpieza, validación de rangos y columnas derivadas
│   ├── load_db.py             # Carga el CSV limpio a SQLite
│   ├── build_bi_export.py     # Genera el archivo BI-ready para Looker Studio
│   └── analysis.py            # Genera los gráficos clave (matplotlib/seaborn)
├── charts/                   # Gráficos generados por analysis.py
├── dashboard/
│   └── capturas/               # Capturas de las 3 páginas del dashboard
└── README.md
```

## 🛠️ Cómo reproducirlo
```bash
pip install -r requirements.txt

python scripts/clean_data.py       # data/raw_gym_members.csv -> gym_members_clean.csv + cleaning_log.txt
python scripts/load_db.py          # gym_members_clean.csv -> gym_members.db (SQLite)
python scripts/build_bi_export.py  # gym_members_clean.csv -> gym_members_bi_ready.csv
python scripts/analysis.py         # gym_members_clean.csv -> charts/*.png

sqlite3 gym_members.db < sql/queries.sql
```
`clean_data.py` espera `raw_gym_members.csv` en la raíz del proyecto — copiá `data/raw_gym_members.csv` ahí (o ajustá la ruta) antes de correrlo.

Dataset original: *Gym Members Exercise Tracking Dataset* (Kaggle).

## 🔗 Dashboard en vivo
[Looker Studio – Gym Member Retention](https://datastudio.google.com/reporting/c3436895-b7ef-4c5c-8ec4-4afff76760dc)

> ⚠️ Antes de publicar: verificá que el link del dashboard esté compartido como "cualquiera con el link puede ver".

---
**Autor:** Facundo Wattson Montero · [Portfolio](https://facuwattsonm.github.io/facundo-portfolio/)
