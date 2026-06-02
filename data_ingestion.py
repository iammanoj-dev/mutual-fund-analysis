import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = sorted([
    file for file in os.listdir(DATA_PATH)
    if file.endswith(".csv")
])

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    print("\n" + "="*80)
    print(f"FILE: {file}")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

