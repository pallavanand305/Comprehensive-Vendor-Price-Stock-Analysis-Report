#!/usr/bin/env python3
"""Test the procurement analysis system without external dependencies"""

import json
import csv
from datetime import datetime
import random

# Simulate the analysis system
cities = ["Mumbai", "Delhi", "Pune", "Kolkata"]
food_items = [
    "Rice (Basmati)", "Wheat Flour", "Lentils (Dal)", "Cooking Oil",
    "Sugar", "Salt", "Onions", "Potatoes", "Tomatoes", "Garlic"
]

# Generate sample data
vendor_data = {}
for city in cities:
    vendor_data[city] = {}
    for item in food_items:
        vendors = []
        base_price = random.randint(30, 500)
        for i in range(3):
            vendor = {
                "vendor_name": f"{city}_Vendor_{chr(65+i)}",
                "price_inr": round(base_price * random.uniform(0.9, 1.1), 2),
                "price_usd": round(base_price * random.uniform(0.9, 1.1) / 83.25, 2),
                "moq_kg": random.choice([10, 25, 50]),
                "stockout_frequency": random.choice(["Low", "Medium", "High"])
            }
            vendors.append(vendor)
        vendor_data[city][item] = vendors

# Generate test files
with open("test_report.json", 'w') as f:
    json.dump({
        "report_metadata": {
            "company": "BLU Maritime",
            "cities": len(cities),
            "items": len(food_items),
            "vendors": len(cities) * len(food_items) * 3
        },
        "vendor_data": vendor_data
    }, f, indent=2)

with open("test_vendors.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["City", "Item", "Vendor", "Price_INR", "Price_USD", "MOQ", "Stock_Risk"])
    for city in cities:
        for item in food_items:
            for vendor in vendor_data[city][item]:
                writer.writerow([
                    city, item, vendor["vendor_name"], vendor["price_inr"],
                    vendor["price_usd"], vendor["moq_kg"], vendor["stockout_frequency"]
                ])

print("✅ BLU Maritime Procurement Analysis - Test Complete")
print(f"📊 Generated data for {len(cities)} cities, {len(food_items)} items")
print(f"🏪 Total vendors: {len(cities) * len(food_items) * 3}")
print("📁 Test files created: test_report.json, test_vendors.csv")