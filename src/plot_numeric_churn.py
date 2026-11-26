from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Locate the project folder and load the dataset.
project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(data_file)

# Print the numbers we'll use to explain the charts.
medians = df.groupby("Churn")[["tenure", "MonthlyCharges"]].median()
print("\nMedian tenure and monthly charges by churn group")
print(medians.to_string(float_format=lambda value: f"{value:.3f}"))

# Use readable group labels on both charts.
plot_data = df.assign(
    churn_group=df["Churn"].map({"No": "Stayed", "Yes": "Left"})
)
group_order = ["Stayed", "Left"]

fig, (tenure_ax, charges_ax) = plt.subplots(1, 2, figsize=(10, 4.5))

sns.boxplot(
    data=plot_data,
    x="churn_group",
    y="tenure",
    order=group_order,
    color="#60a5fa",
    ax=tenure_ax,
)
tenure_ax.set_title("Tenure by Churn Status")
tenure_ax.set_xlabel("")
tenure_ax.set_ylabel("Tenure (months)")

sns.boxplot(
    data=plot_data,
    x="churn_group",
    y="MonthlyCharges",
    order=group_order,
    color="#fb923c",
    ax=charges_ax,
)
charges_ax.set_title("Monthly Charges by Churn Status")
charges_ax.set_xlabel("")
charges_ax.set_ylabel("Monthly charges")

# Save both panels together as one figure.
results_folder = project_folder / "results"
results_folder.mkdir(exist_ok=True)
chart_file = results_folder / "numeric_churn_comparison.png"

fig.tight_layout()
fig.savefig(chart_file, dpi=200)
plt.close(fig)
print(f"\nChart saved to: {chart_file}")