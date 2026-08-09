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

np.random.seed(42)


# ============================================================
# 2. LOAD PRODUCT DATA
# ============================================================

products_file = os.path.join(RAW_DIR, "products.csv")

products = pd.read_csv(products_file)


# ============================================================
# 3. GENERATE INVENTORY INFORMATION
# ============================================================

inventory_data = []

for _, product in products.iterrows():

    product_id = product["product_id"]
    category = product["category"]

    # Inventory levels based on product category
    inventory_ranges = {
        "Chair": (100, 600),
        "Desk": (50, 300),
        "Storage": (50, 250),
        "Table": (40, 200),
        "Sofa": (30, 150),
        "Workstation": (20, 100)
    }

    min_stock, max_stock = inventory_ranges.get(
        category,
        (50, 200)
    )

    current_inventory = np.random.randint(
        min_stock,
        max_stock + 1
    )

    # Supplier lead time
    lead_time_days = np.random.randint(7, 31)

    # Minimum safety stock
    safety_stock = max(
        10,
        int(current_inventory * np.random.uniform(0.15, 0.30))
    )

    # Reorder point
    reorder_point = safety_stock + int(
        current_inventory * 0.20
    )

    suppliers = [
        "Supplier_A",
        "Supplier_B",
        "Supplier_C",
        "Supplier_D",
        "Supplier_E"
    ]

    supplier = np.random.choice(suppliers)

    inventory_data.append([
        product_id,
        current_inventory,
        safety_stock,
        reorder_point,
        lead_time_days,
        supplier
    ])


# ============================================================
# 4. CREATE DATAFRAME
# ============================================================

inventory_df = pd.DataFrame(
    inventory_data,
    columns=[
        "product_id",
        "current_inventory",
        "safety_stock",
        "reorder_point",
        "lead_time_days",
        "supplier"
    ]
)


# ============================================================
# 5. SAVE DATASET
# ============================================================

output_file = os.path.join(
    RAW_DIR,
    "inventory.csv"
)

inventory_df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 6. DISPLAY RESULTS
# ============================================================

print("=" * 60)
print("INVENTORY DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"File saved at: {output_file}")

print(f"Total products: {len(inventory_df)}")

print("\nFirst 10 records:")
print(inventory_df.head(10))

print("\nDataset shape:")
print(inventory_df.shape)