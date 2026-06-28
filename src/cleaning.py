import pandas as pd

df = pd.read_csv("data/menu.csv")

print("=" * 50)
print("DATA CLEANING REPORT")
print("=" * 50)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate values
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Remove duplicates if any
df.drop_duplicates(inplace=True)

print("\nFinal Shape After Cleaning:")
print(df.shape)