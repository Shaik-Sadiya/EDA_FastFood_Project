import pandas as pd

df = pd.read_csv("data/menu.csv")

print("=" * 50)
print("DATA CLEANING REPORT")
print("=" * 50)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())


print("\nData Types:")
print(df.dtypes)

df.drop_duplicates(inplace=True)

print("\nFinal Shape After Cleaning:")
print(df.shape)
