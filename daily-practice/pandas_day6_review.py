import pandas as pd

# Creating a simple data frame 
data = {
    "Product": ["Iphone", "Macbook", "Ipad", "Ipod", "Airpods", "Chromebook"],
    "Category": ["Electronics"] * 6,
    "Sales": [2080, 820, 1983, 2, 650, 8540],
    "Year": [2022, 2023, 2022, 2023, 2023, 2022]
}

df = pd.DataFrame(data)
print("📊 Original DataFrame:\n", df)

# Total and average sales by Product
avg_sales = df.groupby("Product")["Sales"].agg(["sum", "mean"])
print("\n📈 Grouped Sales (Sum & Mean):\n", avg_sales)

# Merging (NOTE: No common products in df_extra — will return empty DataFrame)
df_extra = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Rating": [4.5, 4.0, 3.8]
})

merged = pd.merge(df, df_extra, on="Product", how="inner")
print("\n🔗 Merged DataFrame:\n", merged)

# Pivot Table
pivot = df.pivot_table(values="Sales", index="Product", columns="Year", aggfunc="mean")
print("\n📊 Pivot Table (mean sales by year):\n", pivot)

# Indexing
print("\n🎯 Indexing:")
print("Sales at loc[1, 'Sales']:", df.loc[1, "Sales"])  # Access using label
print("Sales at iloc[2, 2]:", df.iloc[2, 2])            # Access using index

