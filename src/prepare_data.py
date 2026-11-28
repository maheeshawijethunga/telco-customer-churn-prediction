import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# 1. LOAD THE DATASET
# ------------------------------------------------------------

# Get the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Dataset location
DATA_PATH = PROJECT_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Read the CSV file
df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DAY 3 - DATA PREPARATION")
print("=" * 60)

print("\nOriginal Dataset Shape:")
print(df.shape)


# ------------------------------------------------------------
# 2. CLEAN TOTALCHARGES
# ------------------------------------------------------------

# Remove whitespace and convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].str.strip(),
    errors="coerce"
)

# Find rows with missing TotalCharges
missing_charges = df[df["TotalCharges"].isna()]

print("\nMISSING TOTALCHARGES INVESTIGATION")
print("-" * 45)

print("\nNumber of missing TotalCharges values:")
print(len(missing_charges))

print("\nTenure distribution of missing records:")
print(missing_charges["tenure"].value_counts().sort_index())

print("\nChurn distribution of missing records:")
print(missing_charges["Churn"].value_counts())


# ------------------------------------------------------------
# 3. SEPARATE FEATURES (X) AND TARGET (y)
# ------------------------------------------------------------

# Convert Churn into binary values
y = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Create input features by removing Churn and customerID
X = df.drop(columns=["Churn", "customerID"])

# Check target conversion
if y.isna().any():
    raise ValueError("Unexpected values found in Churn column.")

print("\nFEATURE AND TARGET INFORMATION")
print("-" * 45)

print("Number of input features:", X.shape[1])
print("Number of target records:", len(y))

print("\nTarget distribution:")
print(y.value_counts().rename(index={
    0: "No (0)",
    1: "Yes (1)"
}))


# ------------------------------------------------------------
# 4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ------------------------------------------------------------

# Identify categorical columns
categorical_features = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

# Treat SeniorCitizen as a categorical feature
categorical_features.append("SeniorCitizen")

# Identify numerical columns, excluding SeniorCitizen
numeric_features = [
    column
    for column in X.select_dtypes(include=["number"]).columns
    if column != "SeniorCitizen"
]

print("\nNUMERICAL FEATURES")
print("-" * 45)
print(numeric_features)

print("\nCATEGORICAL FEATURES")
print("-" * 45)
print(categorical_features)


# ------------------------------------------------------------
# 5. SPLIT DATA INTO TRAINING AND TESTING SETS
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ------------------------------------------------------------
# 6. DISPLAY TRAINING AND TESTING INFORMATION
# ------------------------------------------------------------

print("\nTRAINING AND TESTING SPLIT")
print("-" * 45)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print("\nTraining churn percentages:")
print(
    (y_train.value_counts(normalize=True).sort_index() * 100)
    .rename(index={0: "No", 1: "Yes"})
)

print("\nTesting churn percentages:")
print(
    (y_test.value_counts(normalize=True).sort_index() * 100)
    .rename(index={0: "No", 1: "Yes"})
)


# ------------------------------------------------------------
# 7. CHECK MISSING VALUES AFTER CONVERSION
# ------------------------------------------------------------

print("\nMISSING TOTALCHARGES AFTER CONVERSION")
print("-" * 45)

print("Missing values:", df["TotalCharges"].isna().sum())


# ------------------------------------------------------------
# 8. FINAL DATASET CHECK
# ------------------------------------------------------------

print("\nFINAL DATASET INFORMATION")
print("-" * 45)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("Total rows:", len(X_train) + len(X_test))

print("\nData preparation completed successfully!")

print("=" * 60)
