import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================
# 1. PROJECT PATH
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")


# ============================================================
# 2. LOAD DATASETS
# ============================================================

products = pd.read_csv(
    os.path.join(RAW_DIR, "products.csv")
)

sales = pd.read_csv(
    os.path.join(RAW_DIR, "sales.csv")
)

inventory = pd.read_csv(
    os.path.join(RAW_DIR, "inventory.csv")
)

sales["date"] = pd.to_datetime(sales["date"])


# ============================================================
# 3. BASIC INFORMATION
# ============================================================

print("=" * 60)
print("AI FURNITURE INTELLIGENCE - EDA")
print("=" * 60)

print("\nDATASET SHAPES")
print("-" * 60)

print(f"Products   : {products.shape}")
print(f"Sales      : {sales.shape}")
print(f"Inventory  : {inventory.shape}")


# ============================================================
# 4. PRODUCT ANALYSIS
# ============================================================

print("\nPRODUCT CATEGORIES")
print("-" * 60)

print(products["category"].value_counts())


print("\nDESIGN STYLES")
print("-" * 60)

print(products["style"].value_counts())


# ============================================================
# 5. SALES ANALYSIS
# ============================================================

print("\nTOTAL UNITS SOLD")
print("-" * 60)

print(sales["units_sold"].sum())


print("\nTOTAL SALES REVENUE")
print("-" * 60)

sales["revenue"] = (
    sales["units_sold"] *
    sales["selling_price"]
)

print(round(sales["revenue"].sum(), 2))


# ============================================================
# 6. TOP 10 PRODUCTS BY SALES
# ============================================================

top_products = (
    sales.groupby("product_id")["units_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY UNITS SOLD")
print("-" * 60)

print(top_products)


# ============================================================
# 7. SALES BY CATEGORY
# ============================================================

category_sales = (
    sales.merge(
        products[["product_id", "category"]],
        on="product_id"
    )
    .groupby("category")["units_sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY CATEGORY")
print("-" * 60)

print(category_sales)


# ============================================================
# 8. SALES BY DESIGN STYLE
# ============================================================

style_sales = (
    sales.merge(
        products[["product_id", "style"]],
        on="product_id"
    )
    .groupby("style")["units_sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY DESIGN STYLE")
print("-" * 60)

print(style_sales)


# ============================================================
# 9. INVENTORY ANALYSIS
# ============================================================

inventory["inventory_status"] = inventory.apply(
    lambda row:
        "REORDER"
        if row["current_inventory"] <= row["reorder_point"]
        else "OK",
    axis=1
)

print("\nINVENTORY STATUS")
print("-" * 60)

print(
    inventory["inventory_status"]
    .value_counts()
)


# ============================================================
# 10. VISUALIZATION 1 - CATEGORY SALES
# ============================================================

plt.figure(figsize=(10, 6))

category_sales.plot(
    kind="bar"
)

plt.title("Furniture Sales by Category")
plt.xlabel("Category")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 11. VISUALIZATION 2 - STYLE SALES
# ============================================================

plt.figure(figsize=(10, 6))

style_sales.plot(
    kind="bar"
)

plt.title("Furniture Sales by Design Style")
plt.xlabel("Design Style")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 12. VISUALIZATION 3 - MONTHLY SALES TREND
# ============================================================

monthly_sales = (
    sales
    .set_index("date")
    .resample("ME")["units_sold"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values
)

plt.title("Monthly Furniture Sales Trend")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


print("\nEDA COMPLETED SUCCESSFULLY!")