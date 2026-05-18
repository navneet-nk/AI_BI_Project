import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel("sales_data.xlsx")

# Region-wise sales
region_sales = data.groupby("Region")["Sales_Amount"].sum()

# Create bar chart
plt.bar(region_sales.index, region_sales.values)

# Chart title and labels
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales Amount")

# Show chart
plt.show()