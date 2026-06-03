import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Parse dates
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("Saved clean_nav_history.csv")
