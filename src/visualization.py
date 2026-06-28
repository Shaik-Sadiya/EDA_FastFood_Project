import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create charts folder
os.makedirs("reports/charts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/menu.csv")

# ------------------------------------------------
# 1. Calories Distribution
# ------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["Calories"], bins=20)
plt.title("Calories Distribution")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    "reports/charts/calories_distribution.png"
)

plt.close()

# ------------------------------------------------
# 2. Category Calories
# ------------------------------------------------

category_calories = (
    df.groupby("Category")["Calories"]
      .mean()
      .sort_values()
)

plt.figure(figsize=(10,6))

category_calories.plot(kind="bar")

plt.title("Average Calories by Category")
plt.xlabel("Category")
plt.ylabel("Calories")
plt.tight_layout()

plt.savefig(
    "reports/charts/category_calories.png"
)

plt.close()

# ------------------------------------------------
# 3. Protein vs Calories
# ------------------------------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    x=df["Protein"],
    y=df["Calories"]
)

plt.title("Protein vs Calories")
plt.tight_layout()

plt.savefig(
    "reports/charts/protein_vs_calories.png"
)

plt.close()

# ------------------------------------------------
# 4. Heatmap
# ------------------------------------------------

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(12,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    "reports/charts/heatmap.png"
)

plt.close()

print("All charts generated successfully!")