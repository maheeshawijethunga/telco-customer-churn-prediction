from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Locate the project folder and load the dataset.
project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(data_file)

# Count all customers and customers who churned in each contract group.
contract_summary = df.groupby("Contract")["Churn"].agg(
    customers="size",
    churned=lambda values: values.eq("Yes").sum(),
)
contract_summary["churn_rate_pct"] = (
    100 * contract_summary["churned"] / contract_summary["customers"]
)
contract_summary = contract_summary.sort_values("churn_rate_pct", ascending=False)

print("\nChurn by contract type")
print(contract_summary.to_string(float_format=lambda value: f"{value:.2f}"))

# Draw and label the chart.
fig, ax = plt.subplots(figsize=(8, 4.5))
rates = contract_summary["churn_rate_pct"]
bars = ax.bar(rates.index, rates, color="#2563eb")
ax.bar_label(bars, labels=[f"{rate:.2f}%" for rate in rates], padding=4)
ax.set_title("Churn Rate by Contract Type")
ax.set_ylabel("Customers who churned (%)")
ax.set_ylim(0, 100)

# Save the chart for the report.
results_folder = project_folder / "results"
results_folder.mkdir(exist_ok=True)
chart_file = results_folder / "churn_by_contract.png"

fig.tight_layout()
fig.savefig(chart_file, dpi=200)
plt.close(fig)
print(f"\nChart saved to: {chart_file}")