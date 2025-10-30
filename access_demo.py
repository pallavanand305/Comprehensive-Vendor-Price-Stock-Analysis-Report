#!/usr/bin/env python3
"""
Access Control Demo - Shows different data views for vendors vs BLU Maritime
"""

import json

# Sample data with confidential ratings
sample_vendor_data = {
    "Mumbai": {
        "Rice (Basmati)": [
            {
                "vendor_name": "Mumbai_Vendor_A",
                "contact": "+91-9876543210",
                "price_inr": 120.50,
                "price_usd": 1.45,
                "moq_kg": 50,
                "stockout_frequency": "Low",
                "confidential_rating": "A"
            },
            {
                "vendor_name": "Mumbai_Vendor_B", 
                "contact": "+91-9876543211",
                "price_inr": 125.75,
                "price_usd": 1.51,
                "moq_kg": 25,
                "stockout_frequency": "Medium",
                "confidential_rating": "B"
            },
            {
                "vendor_name": "Mumbai_Vendor_C",
                "contact": "+91-9876543212", 
                "price_inr": 118.25,
                "price_usd": 1.42,
                "moq_kg": 100,
                "stockout_frequency": "Low",
                "confidential_rating": "A"
            }
        ]
    }
}

def generate_blu_maritime_view():
    """BLU Maritime - Full access to all vendor data"""
    blu_data = {
        "access_level": "BLU_MARITIME_FULL_ACCESS",
        "warning": "CONFIDENTIAL - Internal use only",
        "all_vendor_data": sample_vendor_data,
        "competitive_analysis": {
            "Mumbai Rice (Basmati)": {
                "lowest_price": 118.25,
                "highest_price": 125.75,
                "best_vendor": "Mumbai_Vendor_C",
                "price_spread": 7.50,
                "rating_analysis": {
                    "A_rated_vendors": ["Mumbai_Vendor_A", "Mumbai_Vendor_C"],
                    "B_rated_vendors": ["Mumbai_Vendor_B"]
                }
            }
        }
    }
    
    with open("BLU_MARITIME_full_access.json", 'w') as f:
        json.dump(blu_data, f, indent=2)

def generate_vendor_view(vendor_name):
    """Vendor - Restricted to own data only"""
    vendor_data = {
        "access_level": "VENDOR_RESTRICTED",
        "vendor_name": vendor_name,
        "warning": "You can only view your own quotations. Competitor data is confidential.",
        "your_quotations": {}
    }
    
    # Filter to show only this vendor's data
    for city, items in sample_vendor_data.items():
        vendor_data["your_quotations"][city] = {}
        for item, vendors in items.items():
            vendor_quotes = []
            for vendor in vendors:
                if vendor["vendor_name"] == vendor_name:
                    # Remove confidential rating from vendor view
                    clean_vendor = {k: v for k, v in vendor.items() 
                                  if k != "confidential_rating"}
                    vendor_quotes.append(clean_vendor)
            
            if vendor_quotes:
                vendor_data["your_quotations"][city][item] = vendor_quotes
    
    filename = f"{vendor_name}_restricted_access.json"
    with open(filename, 'w') as f:
        json.dump(vendor_data, f, indent=2)
    
    return filename

def main():
    print("🔐 Access Control Demo - BLU Maritime Procurement System")
    print("=" * 60)
    
    # Generate BLU Maritime view (full access)
    generate_blu_maritime_view()
    print("✅ BLU Maritime view: BLU_MARITIME_full_access.json")
    print("   - All vendor data visible")
    print("   - Confidential ratings included")
    print("   - Competitive analysis available")
    
    # Generate vendor views (restricted access)
    vendors = ["Mumbai_Vendor_A", "Mumbai_Vendor_B", "Mumbai_Vendor_C"]
    print("\n🏪 Vendor restricted views:")
    
    for vendor in vendors:
        filename = generate_vendor_view(vendor)
        print(f"   - {filename}")
        print(f"     * Only {vendor}'s own quotations")
        print(f"     * No competitor pricing visible")
        print(f"     * No confidential ratings")
    
    print("\n🔒 SECURITY FEATURES:")
    print("   ✓ Vendors cannot see competitor prices")
    print("   ✓ Confidential ratings hidden from vendors") 
    print("   ✓ BLU Maritime has complete visibility")
    print("   ✓ Access level clearly marked in each file")

if __name__ == "__main__":
    main()