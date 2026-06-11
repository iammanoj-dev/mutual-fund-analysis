
# Mutual Fund Industry Analytics: Data Engineering & Financial Analytics Capstone Project

## Project Overview

This project is an end-to-end Mutual Fund Analytics platform developed to analyze fund performance, investor behavior, risk metrics, and industry trends using Python, SQLite, and Tableau.

The project demonstrates the complete analytics lifecycle:

* Data Ingestion
* Data Cleaning & Validation
* Database Design
* Exploratory Data Analysis (EDA)
* Performance Analytics
* Dashboard Development
* Advanced Risk Analytics
* Fund Recommendation System

The solution processes mutual fund industry datasets containing NAV history, investor transactions, scheme performance metrics, benchmark indices, and portfolio holdings to generate actionable investment insights.

---

## Project Objectives

1. Build an automated ETL pipeline.
2. Clean and validate mutual fund datasets.
3. Create a SQLite analytical database.
4. Perform exploratory data analysis.
5. Calculate fund performance metrics.
6. Develop interactive dashboards.
7. Generate advanced risk analytics.
8. Create a fund recommendation system.

---

## Technology Stack

| Category             | Tools            |
| -------------------- | ---------------- |
| Programming Language | Python           |
| Data Analysis        | Pandas, NumPy    |
| Database             | SQLite           |
| Visualization        | Tableau          |
| Notebook Environment | Jupyter Notebook |
| Version Control      | Git & GitHub     |
| Statistical Analysis | SciPy            |

---

## Project Architecture

```text
Raw CSV Files
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning & Validation
      │
      ▼
SQLite Database (Star Schema)
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Performance Analytics
      │
      ▼
Advanced Analytics
      │
      ▼
Tableau Dashboard
      │
      ▼
Investment Insights
```

---

## Dataset Description

### 1. NAV History

Tracks daily Net Asset Value (NAV) for all mutual fund schemes.

**Records:** 46,000

### 2. Investor Transactions

Contains SIP, Lumpsum, and Redemption transactions.

**Records:** 32,778

### 3. Scheme Performance

Fund performance statistics and risk metrics.

**Records:** 40 schemes

### 4. Benchmark Indices

Market benchmark data used for Alpha and Beta calculations.

**Records:** 8,050

### 5. Portfolio Holdings

Stock-level holdings for sector concentration analysis.

**Records:** 322

### 6. Fund Master

Fund metadata including AMC, category, benchmark, and risk classification.

---

## Repository Structure

```text
mutual-fund-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── dashboard/
│   └── Dashboard 1.pdf
│
├── reports/
│   ├── Final_Report.pdf
│   └── rolling_sharpe_chart.png
│
├── sql/
│
├── recommender.py
├── run_pipeline.py
├── requirements.txt
├── README.md
└── mutual_fund.db
```

---

## ETL Pipeline

The ETL workflow consists of:

### Data Ingestion

```bash
python data_ingestion.py
```

### Data Cleaning

```bash
python clean_nav.py

python clean_transactions.py

python clean_performance.py
```

### Database Loading

```bash
python load_sqlite.py
```

### Database Verification

```bash
python verify_db.py
```

### Run Complete Pipeline

```bash
python run_pipeline.py
```

---

## Exploratory Data Analysis

The EDA phase focuses on:

* Industry AUM Trends
* SIP Inflow Analysis
* Fund House Analysis
* Investor Demographics
* Transaction Analysis
* Category-Level Analysis

Notebook:

```text
notebooks/03_eda_analysis.ipynb
```

---

## Performance Analytics

The project computes:

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard Ranking

Generated Outputs:

```text
data/processed/fund_scorecard.csv

data/processed/alpha_beta.csv
```

Notebook:

```text
notebooks/04_performance_analytics.ipynb
```

---

## Advanced Analytics

Implemented advanced financial and investor analytics:

### Historical VaR (95%)

Measures downside risk using historical return distributions.

### Conditional VaR (CVaR)

Measures expected loss beyond the VaR threshold.

### Rolling 90-Day Sharpe Ratio

Evaluates dynamic risk-adjusted performance.

### Investor Cohort Analysis

Groups investors based on first investment year.

### SIP Continuity Analysis

Identifies investors at risk of SIP discontinuation.

### Sector Concentration Analysis (HHI)

Measures portfolio diversification.

### Fund Recommendation Engine

Recommends funds based on investor risk appetite.

Generated Outputs:

```text
data/processed/var_cvar_report.csv

reports/rolling_sharpe_chart.png

recommender.py
```

Notebook:

```text
notebooks/05_advanced_analytics.ipynb
```

---

## Tableau Dashboard

The Tableau dashboard provides:

* Total AUM KPI
* SIP Inflow KPI
* Total Folios KPI
* Total Schemes KPI
* Industry AUM Trend
* Top Fund Houses by AUM

Dashboard Location:

```text
dashboard/Dashboard 1.pdf
```

---

## Key Findings

* SBI Mutual Fund leads industry AUM.
* Industry AUM experienced strong growth from 2022–2024.
* SIP remains the dominant investment channel.
* Approximately 97.8% of SIP investors were identified as At Risk based on payment gaps.
* Risk-adjusted performance varies significantly across funds.
* Tail risk differs across schemes despite similar categories.
* Rolling Sharpe Ratios demonstrate changing fund efficiency over time.
* Portfolio concentration impacts risk exposure.

---

## Future Enhancements

* Real-Time NAV Integration
* Machine Learning Recommendation System
* Predictive SIP Churn Analytics
* Multi-Factor Performance Attribution Models
* Tableau Public Deployment
* Portfolio Optimization Engine

---

## Installation

Clone the repository:

```bash
git clone https://github.com/iammanoj-dev/mutual-fund-analysis.git

cd mutual-fund-analysis
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Author

**Manoj BM**

Data Analyst Intern Capstone Project

GitHub:
https://github.com/iammanoj-dev/mutual-fund-analysis

---

## Version

**v1.0**
