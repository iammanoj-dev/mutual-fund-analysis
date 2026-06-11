"""
Master ETL Pipeline Runner
Author: Manoj BM
"""

import os

scripts = [
    "data_ingestion.py",
    "clean_nav.py",
    "clean_transactions.py",
    "clean_performance.py",
    "load_sqlite.py",
    "verify_db.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    os.system(f"python {script}")

print("\nPipeline Completed Successfully.")
