"""
Genera el archivo plano listo para importar en Looker Studio / Power BI.
Formato ancho, una fila por miembro, columnas con nombres legibles (sin espacios raros)
y tipos consistentes para que el conector de archivos lo detecte bien.
"""
import pandas as pd

df = pd.read_csv("gym_members_clean.csv")

# Nombres de columnas "amigables" para Looker Studio / Power BI (Title Case, sin unidades ambiguas)
rename_bi = {
    "age": "Age",
    "age_group": "Age Group",
    "gender": "Gender",
    "weight_kg": "Weight (kg)",
    "height_m": "Height (m)",
    "bmi": "BMI",
    "bmi_category": "BMI Category",
    "max_bpm": "Max BPM",
    "avg_bpm": "Avg BPM",
    "resting_bpm": "Resting BPM",
    "workout_type": "Workout Type",
    "session_duration_hours": "Session Duration (hrs)",
    "calories_burned": "Calories Burned",
    "calories_per_hour": "Calories per Hour",
    "fat_percentage": "Fat Percentage",
    "water_intake_liters": "Water Intake (L)",
    "workout_frequency_days": "Workout Frequency (days/week)",
    "engagement_level": "Engagement Level",
    "experience_level": "Experience Level (num)",
    "experience_label": "Experience Level",
    "retention_risk": "Retention Risk",
}
df_bi = df.rename(columns=rename_bi)
df_bi.insert(0, "Member ID", range(1, len(df_bi) + 1))

df_bi.to_csv("gym_members_bi_ready.csv", index=False)
print("gym_members_bi_ready.csv generado con", len(df_bi), "filas y", len(df_bi.columns), "columnas")
print(list(df_bi.columns))
