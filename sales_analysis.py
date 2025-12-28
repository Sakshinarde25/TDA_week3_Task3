

import pandas as pd


try:
    df = pd.read_csv("sales_data.csv")
    print(" Dataset loaded successfully.\n")
except FileNotFoundError:
    print(" Error: sales_data.csv not found. Please check the file location.")
    exit()

# -------------------------------
# Step 2: Explore the dataset
# -------------------------------
print(" Dataset Overview")
print("-------------------")
print(f"Shape (Rows, Columns): {df.shape}")
print("\nColumns:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------
# Step 3: Data Cleaning
# -------------------------------
print("\n Data Cleaning")
print("----------------")


missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Handle missing values if any
if missing_values.sum() > 0:
    df.fillna(0, inplace=True)
    print("Missing values filled with 0.")
else:
    print("No missing values found.")

# Remove duplicate rows
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
final_rows = df.shape[0]

print(f"Duplicates removed: {initial_rows - final_rows}")

# -------------------------------
# Step 4: Sales Analysis
# -------------------------------
print("\n📈 Sales Analysis")
print("-----------------")

# Metric 1: Total Revenue
total_revenue = df["Total_Sales"].sum()

# Metric 2: Best-Selling Product
best_selling_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

# Metric 3: Average Order Value
average_order_value = df["Total_Sales"].mean()

# Display results
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f" Average Order Value: ₹{average_order_value:,.2f}")

# -------------------------------
# Step 5: Create Report File
# -------------------------------
print("\n Creating Analysis Report...")

report_content = f"""
SALES DATA ANALYSIS REPORT
-------------------------

Total Records Analyzed: {df.shape[0]}

KEY METRICS
-----------
Total Revenue: ₹{total_revenue:,.2f}
Best-Selling Product: {best_selling_product}
Average Order Value: ₹{average_order_value:,.2f}

INSIGHTS
--------
- The product '{best_selling_product}' generated the highest revenue.
- The dataset is clean with no missing values affecting analysis.
- High average order value indicates premium product sales.

CONCLUSION
----------
This analysis provides clear insights into sales performance and
can support better business and inventory decisions.
"""

with open("analysis_report.md", "w", encoding="utf-8") as file:
    file.write(report_content)

print(" analysis_report.md created successfully.")

# -------------------------------
# End of Script
# -------------------------------
print("\n Sales Data Analysis Completed Successfully!")
