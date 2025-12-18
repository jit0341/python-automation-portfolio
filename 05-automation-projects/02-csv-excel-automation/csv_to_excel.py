import pandas as pd
# CSV to Excel Automation Script
# Load csv data into DataFrame
df = pd.read_csv("data/sales_data.csv")
# Display raw data
print(df)

# Remove duplicate rows
df = df.drop_duplicates()
# Remove rows where name is missing
df = df.dropna(subset = ['Name'])
# Display cleaned data
print("\nCleaned data")
print(df)
# Export cleaned data to Excel.
df.to_excel("clean_sales_report.xlsx", index= False)
