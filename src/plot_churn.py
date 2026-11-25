from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Find the project folder and the dataset.
project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Read the CSV and count customers in each churn group.
df = pd.read_csv(data_file)
churn_counts = df["Churn"].value_counts().reindex(["No", "Yes"], fill_value=0)

# Create a bar chart and display the count above each bar.
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(["Stayed (No)", "Left (Yes)"], churn_counts, color=["#2563eb", "#ea580c"])
ax.bar_label(bars)
ax.set_title("Customer Churn Distribution")
ax.set_ylabel("Number of customers")
ax.set_ylim(0, churn_counts.max() * 1.15)

# Save the chart so it can be inserted into the report.
results_folder = project_folder / "results"
results_folder.mkdir(exist_ok=True)
chart_file = results_folder / "churn_distribution.png"

fig.tight_layout()
fig.savefig(chart_file, dpi=200)
plt.close(fig)
print(f"Chart saved to: {chart_file}")