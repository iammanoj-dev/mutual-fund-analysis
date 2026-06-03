# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Equity/Debt category |

---

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | One year return |
| return_3yr_pct | REAL | Three year return |
| return_5yr_pct | REAL | Five year return |
| sharpe_ratio | REAL | Risk adjusted return |
| expense_ratio_pct | REAL | Expense ratio |

