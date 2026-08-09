import pandas as pd
import numpy as np
import os

# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

# Make results reproducible
np.random.seed(42)


# ============================================================
# 2. LOAD PRODUCT DATA
# ============================================================

products_file = os.path.join(RAW_DIR, "products.csv")

products = pd.read_csv(products_file)


# ============================================================
# 3. GENERATE TWO YEARS OF DAILY SALES
# ============================================================

dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]


sales_data = []


# ============================================================
# 4. GENERATE SALES FOR EVERY PRODUCT
# ============================================================

for _, product in products.iterrows():

    product_id = product["product_id"]
    price = product["price"]
    category = product["category"]
    style = product["style"]

    # Base demand according to furniture category
    category_demand = {
        "Chair": 25,
        "Desk": 15,
        "Storage": 12,
        "Table": 10,
        "Sofa": 8,
        "Workstation": 6
    }

    base_demand = category_demand.get(category, 10)

    # Some styles have higher demand
    style_multiplier = {
        "Modern": 1.25,
        "Contemporary": 1.15,
        "Executive": 1.05,
        "Gen Z": 1.20,
        "Indian Traditional": 0.90,
        "Indian Contemporary": 1.10,
        "Minimalist": 1.05,
        "Industrial": 0.95,
        "Classic": 0.85
    }

    multiplier = style_multiplier.get(style, 1.0)

    for date in dates:

        # Seasonal effect
        month = date.month

        if month in [10, 11, 12]:
            seasonal_multiplier = 1.30
        elif month in [1, 2, 3]:
            seasonal_multiplier = 1.10
        elif month in [4, 5, 6]:
            seasonal_multiplier = 0.95
        else:
            seasonal_multiplier = 1.00

        # Weekend effect
        if date.dayofweek >= 5:
            weekend_multiplier = 0.80
        else:
            weekend_multiplier = 1.00

        # Random demand variation
        random_factor = np.random.normal(1.0, 0.20)

        # Generate units sold
        expected_sales = (
            base_demand
            * multiplier
            * seasonal_multiplier
            * weekend_multiplier
            * random_factor
        )

        units_sold = max(0, int(round(expected_sales)))

        # Random discount
        discount = np.random.choice(
            [0, 5, 10, 15, 20],
            p=[0.35, 0.25, 0.20, 0.12, 0.08]
        )

        # Random region
        region = np.random.choice(regions)

        # Calculate actual selling price
        selling_price = price * (1 - discount / 100)

        sales_data.append([
            date,
            product_id,
            region,
            units_sold,
            price,
            discount,
            round(selling_price, 2)
        ])


# ============================================================
# 5. CREATE DATAFRAME
# ============================================================

sales_df = pd.DataFrame(
    sales_data,
    columns=[
        "date",
        "product_id",
        "region",
        "units_sold",
        "original_price",
        "discount_percent",
        "selling_price"
    ]
)


# ============================================================
# 6. SAVE SALES DATASET
# ============================================================

output_file = os.path.join(
    RAW_DIR,
    "sales.csv"
)

sales_df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 7. DISPLAY RESULTS
# ============================================================

print("=" * 60)
print("SALES DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"File saved at: {output_file}")

print(f"Total records: {len(sales_df):,}")

print(f"Number of products: {sales_df['product_id'].nunique()}")

print(
    f"Date range: "
    f"{sales_df['date'].min().date()} "
    f"to "
    f"{sales_df['date'].max().date()}"
)

print("\nFirst 10 records:")
print(sales_df.head(10))

print("\nDataset shape:")
print(sales_df.shape)