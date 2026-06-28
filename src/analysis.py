import pandas as pd

df = pd.read_csv("data/menu.csv")

print("=" * 50)
print("DESCRIPTIVE STATISTICS")
print("=" * 50)

print(df.describe())


print("\nAverage Calories:", df["Calories"].mean())
print("Maximum Calories:", df["Calories"].max())
print("Minimum Calories:", df["Calories"].min())


print("\nTop 10 Highest Calorie Items")
print(
    df.nlargest(10, "Calories")[["Item", "Calories"]]
)


print("\nTop 10 Highest Protein Items")
print(
    df.nlargest(10, "Protein")[["Item", "Protein"]]
)


print("\nAverage Calories by Category")
print(
    df.groupby("Category")["Calories"]
      .mean()
      .sort_values(ascending=False)
)


print("\nAverage Sodium by Category")
print(
    df.groupby("Category")["Sodium"]
      .mean()
      .sort_values(ascending=False)
)
