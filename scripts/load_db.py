import sqlite3
import pandas as pd

df = pd.read_csv("gym_members_clean.csv")
conn = sqlite3.connect("gym_members.db")
df.to_sql("gym_members", conn, if_exists="replace", index=False)
conn.close()
print("OK - gym_members.db creada con", len(df), "filas")
