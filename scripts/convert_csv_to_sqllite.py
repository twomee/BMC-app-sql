import pandas as pd
import sqlite3

CSV_FILE_PATH = "./titanic.csv"
DB_NAME = "passengers.db"

df = pd.read_csv(CSV_FILE_PATH)
conn = sqlite3.connect(DB_NAME)
df.to_sql("passengers", conn, if_exists='replace', index=False)
conn.close()