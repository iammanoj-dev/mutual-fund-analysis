import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )

    print(table)
    print(count)
    print("-" * 30)

conn.close()
