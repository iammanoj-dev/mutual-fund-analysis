"""
Bonus Task B5
Automated HTML Weekly Mutual Fund Report Generator
"""

import pandas as pd
from datetime import datetime

# Load scorecard
df = pd.read_csv("data/processed/fund_scorecard.csv")

# Top 5 funds by score
top_funds = df.sort_values(
    by="fund_score",
    ascending=False
).head(5)

# HTML report
html = f"""
<html>
<head>
<title>Weekly Mutual Fund Report</title>
</head>

<body style="font-family: Arial, sans-serif;">

<h1>Weekly Mutual Fund Performance Summary</h1>

<p>
Generated on:
{datetime.now().strftime('%d-%m-%Y %H:%M')}
</p>

<h2>Top 5 Funds by Fund Score</h2>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
<th>AMFI Code</th>
<th>Fund Score</th>
<th>Sharpe Ratio</th>
<th>CAGR</th>
<th>Alpha</th>
</tr>
"""

for _, row in top_funds.iterrows():
    html += f"""
    <tr>
        <td>{row['amfi_code']}</td>
        <td>{row['fund_score']:.2f}</td>
        <td>{row['sharpe_ratio']:.2f}</td>
        <td>{row['cagr']:.2f}</td>
        <td>{row['alpha']:.2f}</td>
    </tr>
    """

html += """
</table>

<h3>Key Insight</h3>
<p>
This report highlights the highest-ranked mutual funds
based on the composite fund score generated during
performance analytics.
</p>

</body>
</html>
"""

with open("reports/weekly_report.html", "w") as f:
    f.write(html)

print("Weekly HTML report generated successfully.")
