#!/usr/bin/env python3
"""
Vendor Portal - Restricted Access System
Only shows vendor's own data, BLU Maritime has full access
"""

import json
import hashlib
from datetime import datetime

class VendorPortal:
    def __init__(self):
        self.access_levels = {
            "BLU_MARITIME": "FULL_ACCESS",
            "VENDOR": "RESTRICTED_ACCESS"
        }
        
    def authenticate_user(self, user_id: str, access_key: str) -> dict:
        """Authenticate user and determine access level"""
        if user_id == "BLU_MARITIME" and access_key == "BLU_ADMIN_2024":
            return {"access_level": "FULL_ACCESS", "user_type": "BLU_MARITIME"}
        elif user_id.endswith("_Vendor_A") or user_id.endswith("_Vendor_B") or user_id.endswith("_Vendor_C"):
            return {"access_level": "RESTRICTED_ACCESS", "user_type": "VENDOR", "vendor_id": user_id}
        else:
            return {"access_level": "DENIED", "user_type": "UNKNOWN"}
    
    def get_vendor_data(self, auth_info: dict, vendor_data: dict) -> dict:
        """Return data based on access level"""
        if auth_info["access_level"] == "FULL_ACCESS":
            return self._get_full_data(vendor_data)
        elif auth_info["access_level"] == "RESTRICTED_ACCESS":
            return self._get_vendor_specific_data(auth_info["vendor_id"], vendor_data)
        else:
            return {"error": "Access Denied", "message": "Invalid credentials"}
    
    def _get_full_data(self, vendor_data: dict) -> dict:
        """BLU Maritime - Full access to all vendor data"""
        return {
            "access_type": "BLU_MARITIME_FULL_ACCESS",
            "timestamp": datetime.now().isoformat(),
            "data": vendor_data,
            "confidential_ratings": True,
            "competitor_analysis": True,
            "negotiated_prices": True
        }
    
    def _get_vendor_specific_data(self, vendor_id: str, vendor_data: dict) -> dict:
        """Vendor - Restricted to own data only"""
        filtered_data = {}
        
        for city, items in vendor_data.items():
            filtered_data[city] = {}
            for item, vendors in items.items():
                # Only show this vendor's data
                vendor_own_data = [v for v in vendors if v["vendor_name"] == vendor_id]
                if vendor_own_data:
                    # Remove confidential fields
                    clean_data = []
                    for vendor in vendor_own_data:
                        clean_vendor = {k: v for k, v in vendor.items() 
                                     if k not in ["confidential_rating"]}
                        clean_data.append(clean_vendor)
                    filtered_data[city][item] = clean_data
        
        return {
            "access_type": "VENDOR_RESTRICTED_ACCESS",
            "vendor_id": vendor_id,
            "timestamp": datetime.now().isoformat(),
            "data": filtered_data,
            "note": "You can only view your own quotations. Competitor data is confidential."
        }

def generate_vendor_access_demo():
    """Demo the access control system"""
    
    # Sample vendor data
    sample_data = {
        "Mumbai": {
            "Rice (Basmati)": [
                {"vendor_name": "Mumbai_Vendor_A", "price_inr": 120.50, "price_usd": 1.45, "moq_kg": 50, "confidential_rating": "A"},
                {"vendor_name": "Mumbai_Vendor_B", "price_inr": 125.75, "price_usd": 1.51, "moq_kg": 25, "confidential_rating": "B"},
                {"vendor_name": "Mumbai_Vendor_C", "price_inr": 118.25, "price_usd": 1.42, "moq_kg": 100, "confidential_rating": "A"}
            ]
        }
    }
    
    portal = VendorPortal()
    
    # BLU Maritime Access
    blu_auth = portal.authenticate_user("BLU_MARITIME", "BLU_ADMIN_2024")
    blu_data = portal.get_vendor_data(blu_auth, sample_data)
    
    with open("blu_maritime_full_access.json", 'w') as f:
        json.dump(blu_data, f, indent=2)
    
    # Vendor A Access
    vendor_auth = portal.authenticate_user("Mumbai_Vendor_A", "vendor_key")
    vendor_data = portal.get_vendor_data(vendor_auth, sample_data)
    
    with open("vendor_restricted_access.json", 'w') as f:
        json.dump(vendor_data, f, indent=2)
    
    print("🔐 Access Control Demo Generated:")
    print("  - blu_maritime_full_access.json (All vendor data + confidential)")
    print("  - vendor_restricted_access.json (Own data only, no competitors)")

if __name__ == "__main__":
    generate_vendor_access_demo()