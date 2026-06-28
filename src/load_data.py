import pandas as pd

# Load dataset
df = pd.read_csv("data/menu.csv")

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())