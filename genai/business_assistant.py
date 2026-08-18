import os
import sys

from recommendation import get_recommendation


# ============================================================
# BUSINESS ASSISTANT
# ============================================================

def answer_inventory_question(product_id):

    result = get_recommendation(product_id)

    if isinstance(result, str):
        return result

    answer = f"""
Inventory Analysis for {result['product_id']}

Current Inventory:
{result['current_inventory']} units

Average Demand:
{result['average_demand']} units/day

Safety Stock:
{result['safety_stock']} units

Reorder Point:
{result['reorder_point']} units

Supplier:
{result['supplier']}

Lead Time:
{result['lead_time_days']} days

Recommendation:
{result['recommendation']}
"""

    return answer


# ============================================================
# CHAT INTERFACE
# ============================================================

print()
print("==============================================")
print("     AI FURNITURE BUSINESS ASSISTANT")
print("==============================================")
print()
print("Ask about inventory.")
print("Example: P001")
print("Type 'exit' to stop.")
print()

while True:

    product_id = input("Enter Product ID: ").strip()

    if product_id.lower() == "exit":
        print("Goodbye!")
        break

    if not product_id:
        continue

    print()
    print(answer_inventory_question(product_id))
    print("==============================================")