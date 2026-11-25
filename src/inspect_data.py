# Import the required library
from pathlib import Path
import pandas as pd


# Step 1: Locate the main project folder
project_folder = Path(__file__).resolve().parent.parent


# Step 2: Locate the dataset
data_file = (
    project_folder
    / "data"
    / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)


# Step 3: Check whether the dataset exists
if not data_file.exists():

    print("ERROR: Dataset not found!")
    print("Expected location:", data_file)

else:

    # Step 4: Load the dataset
    df = pd.read_csv(data_file)

    print("\n===================================")
    print("DATASET LOADED SUCCESSFULLY")
    print("===================================")

    # Step 5: Display dataset dimensions
    print("\n1. Dataset Dimensions")
    print("Rows and Columns:", df.shape)

    # Step 6: Display the first five records
    print("\n2. First Five Records")
    print(df.head())

    # Step 7: Display column names
    print("\n3. Column Names")
    print(df.columns.tolist())

    # Step 8: Display data types and non-null counts
    print("\n4. Dataset Information")
    df.info()

    # Step 9: Check missing values
    print("\n5. Missing Values")
    print(df.isnull().sum())

    # Step 10: Check duplicate records
    print("\n6. Duplicate Records")
    print("Number of duplicates:", df.duplicated().sum())

    # Step 11: Display the target variable distribution
    print("\n7. Churn Distribution")
    print(df["Churn"].value_counts())

    # Step 12: Check empty values in TotalCharges
    print("\n8. Checking Empty TotalCharges Values")

    total_charges_clean = df["TotalCharges"].astype(str).str.strip()

    empty_total_charges = total_charges_clean.eq("").sum()

    print("Number of empty TotalCharges values:", empty_total_charges)

    # Display records with empty TotalCharges
    print("\nRecords with empty TotalCharges:")
    print(df[total_charges_clean.eq("")])

    print("\n===================================")
    print("INITIAL INSPECTION COMPLETED")
    print("===================================")
