import pandas as pd

df = pd.read_csv("data/menu.csv")

print("=" * 50)
print("DESCRIPTIVE STATISTICS")
print("=" * 50)

print(df.describe())

# Calories Analysis
print("\nAverage Calories:", df["Calories"].mean())
print("Maximum Calories:", df["Calories"].max())
print("Minimum Calories:", df["Calories"].min())

# Highest Calorie Items
print("\nTop 10 Highest Calorie Items")
print(
    df.nlargest(10, "Calories")[["Item", "Calories"]]
)

# Highest Protein Items
print("\nTop 10 Highest Protein Items")
print(
    df.nlargest(10, "Protein")[["Item", "Protein"]]
)

# Average Calories by Category
print("\nAverage Calories by Category")
print(
    df.groupby("Category")["Calories"]
      .mean()
      .sort_values(ascending=False)
)

# Average Sodium by Category
print("\nAverage Sodium by Category")
print(
    df.groupby("Category")["Sodium"]
      .mean()
      .sort_values(ascending=False)
)