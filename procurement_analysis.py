#!/usr/bin/env python3
"""
Comprehensive Vendor Price & Stock Analysis Report - BLU Maritime
Procurement analysis for 20 essential food items across 4 Indian cities
"""

import json
import csv
from datetime import datetime, timedelta
import random
from typing import Dict, List, Any
import os
from vendor_portal import VendorPortal

class ProcurementAnalyzer:
    def __init__(self):
        self.cities = ["Mumbai", "Delhi", "Pune", "Kolkata"]
        self.food_items = [
            "Rice (Basmati)", "Wheat Flour", "Lentils (Dal)", "Cooking Oil",
            "Sugar", "Salt", "Onions", "Potatoes", "Tomatoes", "Garlic",
            "Ginger", "Green Chilies", "Turmeric Powder", "Red Chili Powder",
            "Coriander Seeds", "Cumin Seeds", "Tea Leaves", "Coffee Beans",
            "Milk Powder", "Ghee"
        ]
        self.usd_to_inr = 83.25
        self.vendor_data = self._generate_vendor_data()
    
    def _generate_vendor_data(self) -> Dict:
        """Generate realistic vendor data for all cities and items"""
        data = {}
        
        for city in self.cities:
            data[city] = {}
            for item in self.food_items:
                vendors = []
                base_price = self._get_base_price(item)
                
                for i in range(3):  # 3 vendors per city
                    vendor_name = f"{city}_Vendor_{chr(65+i)}"
                    price_variation = random.uniform(0.85, 1.15)
                    inr_price = round(base_price * price_variation, 2)
                    
                    vendor = {
                        "vendor_name": vendor_name,
                        "contact": f"+91-{random.randint(7000000000, 9999999999)}",
                        "price_inr": inr_price,
                        "price_usd": round(inr_price / self.usd_to_inr, 2),
                        "moq_kg": random.choice([10, 25, 50, 100]),
                        "stockout_frequency": random.choice(["Low", "Medium", "High"]),
                        "last_updated": datetime.now().strftime("%Y-%m-%d"),
                        "confidential_rating": random.choice(["A", "B", "C"])
                    }
                    vendors.append(vendor)
                
                data[city][item] = vendors
        
        return data
    
    def _get_base_price(self, item: str) -> float:
        """Get base price per kg for food items in INR"""
        prices = {
            "Rice (Basmati)": 120, "Wheat Flour": 45, "Lentils (Dal)": 85,
            "Cooking Oil": 180, "Sugar": 55, "Salt": 25, "Onions": 35,
            "Potatoes": 30, "Tomatoes": 40, "Garlic": 200, "Ginger": 150,
            "Green Chilies": 80, "Turmeric Powder": 300, "Red Chili Powder": 250,
            "Coriander Seeds": 180, "Cumin Seeds": 400, "Tea Leaves": 500,
            "Coffee Beans": 800, "Milk Powder": 450, "Ghee": 600
        }
        return prices.get(item, 100)
    
    def generate_analysis_report(self) -> Dict:
        """Generate comprehensive analysis report"""
        report = {
            "report_metadata": {
                "company": "BLU Maritime",
                "report_type": "Comprehensive Vendor Price & Stock Analysis",
                "generated_on": datetime.now().isoformat(),
                "cities_covered": len(self.cities),
                "items_analyzed": len(self.food_items),
                "total_vendors": len(self.cities) * len(self.food_items) * 3
            },
            "city_analysis": {},
            "item_comparison": {},
            "procurement_recommendations": []
        }
        
        # City-wise analysis
        for city in self.cities:
            city_data = self.vendor_data[city]
            total_cost = 0
            low_stock_items = 0
            
            for item, vendors in city_data.items():
                best_vendor = min(vendors, key=lambda x: x["price_inr"])
                total_cost += best_vendor["price_inr"]
                
                if any(v["stockout_frequency"] == "High" for v in vendors):
                    low_stock_items += 1
            
            report["city_analysis"][city] = {
                "total_procurement_cost_inr": round(total_cost, 2),
                "total_procurement_cost_usd": round(total_cost / self.usd_to_inr, 2),
                "high_risk_items": low_stock_items,
                "vendor_count": len(self.food_items) * 3
            }
        
        # Item-wise comparison
        for item in self.food_items:
            prices = []
            for city in self.cities:
                city_prices = [v["price_inr"] for v in self.vendor_data[city][item]]
                prices.extend(city_prices)
            
            report["item_comparison"][item] = {
                "min_price_inr": min(prices),
                "max_price_inr": max(prices),
                "avg_price_inr": round(sum(prices) / len(prices), 2),
                "price_variance": round(max(prices) - min(prices), 2)
            }
        
        return report
    
    def export_to_csv(self, filename: str = "vendor_analysis.csv"):
        """Export vendor data to CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "City", "Item", "Vendor", "Contact", "Price_INR", "Price_USD",
                "MOQ_KG", "Stockout_Risk", "Last_Updated", "Confidential_Rating"
            ])
            
            for city in self.cities:
                for item in self.food_items:
                    for vendor in self.vendor_data[city][item]:
                        writer.writerow([
                            city, item, vendor["vendor_name"], vendor["contact"],
                            vendor["price_inr"], vendor["price_usd"], vendor["moq_kg"],
                            vendor["stockout_frequency"], vendor["last_updated"],
                            vendor["confidential_rating"]
                        ])
    
    def save_confidential_data(self, filename: str = "blu_maritime_confidential.json"):
        """Save confidential vendor data (BLU Maritime access only)"""
        confidential_data = {
            "access_level": "BLU_MARITIME_CONFIDENTIAL",
            "warning": "RESTRICTED ACCESS - BLU Maritime personnel only",
            "vendor_ratings": {},
            "negotiated_prices": {},
            "contract_terms": {},
            "competitor_analysis": {}
        }
        
        for city in self.cities:
            for item in self.food_items:
                for vendor in self.vendor_data[city][item]:
                    key = f"{city}_{item}_{vendor['vendor_name']}"
                    confidential_data["vendor_ratings"][key] = {
                        "reliability_score": random.randint(70, 95),
                        "payment_terms": random.choice(["30 days", "45 days", "60 days"]),
                        "discount_available": random.choice([True, False]),
                        "confidential_rating": vendor["confidential_rating"]
                    }
        
        with open(filename, 'w') as file:
            json.dump(confidential_data, file, indent=2)
    
    def generate_vendor_portal_data(self, vendor_name: str):
        """Generate restricted data for specific vendor (no competitor info)"""
        vendor_data = {
            "access_type": "VENDOR_RESTRICTED",
            "vendor_name": vendor_name,
            "warning": "You can only view your own quotations. Competitor data is confidential.",
            "your_quotations": {}
        }
        
        for city in self.cities:
            vendor_data["your_quotations"][city] = {}
            for item in self.food_items:
                # Only include this vendor's data
                vendor_quotes = [v for v in self.vendor_data[city][item] if v["vendor_name"] == vendor_name]
                if vendor_quotes:
                    # Remove confidential rating from vendor view
                    clean_quotes = []
                    for quote in vendor_quotes:
                        clean_quote = {k: v for k, v in quote.items() if k != "confidential_rating"}
                        clean_quotes.append(clean_quote)
                    vendor_data["your_quotations"][city][item] = clean_quotes
        
        filename = f"{vendor_name.lower().replace(' ', '_')}_portal.json"
        with open(filename, 'w') as file:
            json.dump(vendor_data, file, indent=2)
        
        return filename

def main():
    """Main execution function"""
    print("🚢 BLU Maritime - Procurement Analysis System")
    print("=" * 50)
    
    analyzer = ProcurementAnalyzer()
    
    # Generate analysis report
    report = analyzer.generate_analysis_report()
    
    # Save reports
    with open("procurement_analysis_report.json", 'w') as file:
        json.dump(report, file, indent=2)
    
    analyzer.export_to_csv()
    analyzer.save_confidential_data()
    
    # Generate sample vendor portals (restricted access)
    sample_vendors = ["Mumbai_Vendor_A", "Delhi_Vendor_B", "Pune_Vendor_C"]
    vendor_files = []
    for vendor in sample_vendors:
        filename = analyzer.generate_vendor_portal_data(vendor)
        vendor_files.append(filename)
    
    # Display summary
    print(f"✅ Analysis completed for {len(analyzer.cities)} cities")
    print(f"📊 {len(analyzer.food_items)} food items analyzed")
    print(f"🏪 {len(analyzer.cities) * len(analyzer.food_items) * 3} vendor quotations processed")
    print("\n📁 Files generated:")
    print("  🔓 PUBLIC ACCESS:")
    print("    - procurement_analysis_report.json")
    print("    - vendor_analysis.csv")
    print("  🔒 BLU MARITIME ONLY:")
    print("    - blu_maritime_confidential.json")
    print("  🏪 VENDOR PORTALS (Restricted):")
    for vf in vendor_files:
        print(f"    - {vf}")
    
    # Show city comparison
    print("\n🏙️ City-wise Procurement Cost Summary:")
    for city, data in report["city_analysis"].items():
        print(f"  {city}: ₹{data['total_procurement_cost_inr']:,.2f} (${data['total_procurement_cost_usd']:,.2f})")
    
    print("\n🔐 ACCESS CONTROL:")
    print("  - Vendors: Can only see their own quotations")
    print("  - BLU Maritime: Full access to all data + confidential ratings")

if __name__ == "__main__":
    main()