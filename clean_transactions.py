import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Date parsing
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Verified", "Pending", "Rejected"]
df["kyc_valid"] = df["kyc_status"].isin(valid_kyc)

print("\nInvalid KYC Records:")
print((~df["kyc_valid"]).sum())

df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("Saved clean_investor_transactions.csv")
