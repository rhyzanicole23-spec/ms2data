import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Locate the source file
file = os.path.join(folder, "cleaned_products_final.csv.xls")

# Read the CSV file
data = pd.read_csv(file)

# Display the first few rows
print(data.head())

# Calculate average unit price by product type
average_price = (
    data.groupby("Product Type")["Unit Price"]
    .mean()
    .sort_values(ascending=False)
)

# Create the bar graph
plt.figure(figsize=(12, 7))

plt.bar(average_price.index, average_price.values)

# Title and labels
plt.title("Average Unit Price by MotorPH Product Type")
plt.xlabel("Product Type")
plt.ylabel("Average Unit Price (PHP)")

# Rotate labels
plt.xticks(rotation=45, ha="right")

# Add values above bars
for i, value in enumerate(average_price.values):
    plt.text(
        i,
        value,
        f"₱{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Display graph
plt.show()