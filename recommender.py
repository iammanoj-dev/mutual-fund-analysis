import pandas as pd

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

filtered = scorecard[
    scorecard["risk_grade"] == risk
]

recommendations = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(recommendations)