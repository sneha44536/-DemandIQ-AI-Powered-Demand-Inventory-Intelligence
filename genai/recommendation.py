import pandas as pd
import os


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "raw"
)


# ============================================================
# LOAD DATA
# ============================================================

sales = pd.read_csv(
    os.path.join(DATA_DIR, "sales.csv")
)

inventory = pd.read_csv(
    os.path.join(DATA_DIR, "inventory.csv")
)


# ============================================================
# INVENTORY RECOMMENDATION
# ============================================================

def get_recommendation(product_id):

    product_sales = sales[
        sales["product_id"] == product_id
    ]

    product_inventory = inventory[
        inventory["product_id"] == product_id
    ]

    if product_sales.empty:
        return "Product not found."

    if product_inventory.empty:
        return "Inventory information not available."

    # ========================================================
    # AVERAGE DEMAND
    # ========================================================

    avg_demand = product_sales[
        "units_sold"
    ].mean()

    # ========================================================
    # INVENTORY INFORMATION
    # ========================================================

    inventory_row = product_inventory.iloc[-1]

    current_inventory = inventory_row[
        "current_inventory"
    ]

    safety_stock = inventory_row[
        "safety_stock"
    ]

    reorder_point = inventory_row[
        "reorder_point"
    ]

    lead_time = inventory_row[
        "lead_time_days"
    ]

    supplier = inventory_row[
        "supplier"
    ]

    # ========================================================
    # INVENTORY RECOMMENDATION
    # ========================================================

    if current_inventory <= reorder_point:

        recommendation = "URGENT: Reorder inventory"

    elif current_inventory <= safety_stock:

        recommendation = "Increase inventory"

    else:

        recommendation = "Inventory level is sufficient"

    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {
        "product_id": product_id,
        "average_demand": round(avg_demand, 2),
        "current_inventory": int(current_inventory),
        "safety_stock": int(safety_stock),
        "reorder_point": int(reorder_point),
        "lead_time_days": int(lead_time),
        "supplier": supplier,
        "recommendation": recommendation
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    result = get_recommendation("P001")

    print("\n================================")
    print("   INVENTORY RECOMMENDATION")
    print("================================")

    for key, value in result.items():
        print(f"{key}: {value}")

    print("================================")