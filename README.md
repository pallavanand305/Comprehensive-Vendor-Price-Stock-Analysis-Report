# 🚢 Comprehensive Vendor Price & Stock Analysis Report - BLU Maritime

## 📋 Project Overview
Comprehensive procurement analysis system covering **20 essential food items** across **4 major Indian cities** (Mumbai, Delhi, Pune, Kolkata) with **3 vendor quotations per city**.

### 🎯 Key Features
- **Multi-city Analysis**: Mumbai, Delhi, Pune, Kolkata
- **20 Essential Food Items**: Rice, Wheat, Lentils, Spices, etc.
- **Vendor Management**: 3 vendors per city (60 total vendors)
- **Dual Currency**: INR & USD pricing
- **Stock Analysis**: MOQ and stockout frequency tracking
- **Confidential Data**: Secure vendor ratings (BLU Maritime only)

## 🏗️ Repository Structure
```
Comprehensive-Vendor-Price-Stock-Analysis-Report/
├── README.md                           # Project documentation
├── procurement_analysis.py             # Main analysis system
├── requirements.txt                    # Python dependencies
├── run_analysis.bat                   # Windows execution script
├── Generated Files/
│   ├── procurement_analysis_report.json  # Main analysis report
│   ├── vendor_analysis.csv              # Vendor data export
│   └── blu_maritime_confidential.json   # Confidential vendor data
```

## 🚀 Quick Start

### Windows (Local Execution)
```bash
# Double-click or run in command prompt
run_analysis.bat
```

### Manual Execution
```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
python procurement_analysis.py
```

## 📊 Analysis Coverage

### Cities Analyzed
| City | Vendors | Coverage |
|------|---------|----------|
| Mumbai | 60 | Complete |
| Delhi | 60 | Complete |
| Pune | 60 | Complete |
| Kolkata | 60 | Complete |
| **Total** | **240** | **100%** |

### Food Items Tracked
1. **Grains**: Rice (Basmati), Wheat Flour
2. **Pulses**: Lentils (Dal)
3. **Oils**: Cooking Oil, Ghee
4. **Basics**: Sugar, Salt
5. **Vegetables**: Onions, Potatoes, Tomatoes
6. **Aromatics**: Garlic, Ginger, Green Chilies
7. **Spices**: Turmeric, Red Chili, Coriander, Cumin
8. **Beverages**: Tea Leaves, Coffee Beans
9. **Dairy**: Milk Powder

## 📈 Generated Reports

### 1. Main Analysis Report (`procurement_analysis_report.json`)
- City-wise procurement costs (INR/USD)
- Item-wise price comparisons
- Risk assessment (stockout frequency)
- Procurement recommendations

### 2. Vendor Data Export (`vendor_analysis.csv`)
- Complete vendor database
- Contact information
- Pricing in dual currency
- MOQ requirements
- Stock availability

### 3. Confidential Data (`blu_maritime_confidential.json`) 🔒
**BLU Maritime Access Only**
- Vendor reliability scores
- Negotiated pricing terms
- Payment conditions
- Contract details

## 💰 Pricing Analysis

### Currency Conversion
- **Base Currency**: Indian Rupee (INR)
- **Secondary**: US Dollar (USD)
- **Exchange Rate**: ₹83.25 per USD (dynamic)

### Price Tracking
- Real-time vendor quotations
- Historical price trends
- Market variance analysis
- Cost optimization recommendations

## 📦 Stock Management

### MOQ (Minimum Order Quantity)
- Vendor-specific requirements
- Bulk pricing advantages
- Supply chain optimization

### Stockout Risk Assessment
- **Low Risk**: Reliable supply
- **Medium Risk**: Occasional shortages
- **High Risk**: Frequent stockouts

## 🔐 Security & Confidentiality

### Access Levels
1. **BLU Maritime**: Complete analysis + confidential data + all vendor quotations
2. **Vendor Specific**: Own quotations only (no competitor data)
3. **Public**: Basic procurement reports (no vendor details)

### Data Protection
- **Vendor Isolation**: Each vendor can only see their own quotations
- **Confidential Ratings**: Hidden from vendors, visible to BLU Maritime only
- **Competitor Pricing**: Completely restricted from vendor access
- **Access Control**: Authentication required for data access

### Security Features
- ✅ Vendors cannot see competitor prices
- ✅ Confidential ratings protected
- ✅ Individual vendor portals with restricted data
- ✅ BLU Maritime full visibility for procurement decisions

## 🛠️ Technical Specifications

### Core Files
- **procurement_analysis.py**: Main analysis engine
- **vendor_portal.py**: Access control system
- **access_demo.py**: Security demonstration

### Dependencies
- **Python 3.8+**
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **matplotlib/seaborn**: Visualization
- **openpyxl**: Excel export

### System Requirements
- **OS**: Windows/Linux/macOS
- **RAM**: 4GB minimum
- **Storage**: 100MB for data files

### Access Control Files Generated
- **BLU_MARITIME_full_access.json**: Complete vendor data + ratings
- **[vendor]_restricted_access.json**: Individual vendor portals
- **blu_maritime_confidential.json**: Confidential ratings & analysis

## 📞 Support & Contact

**BLU Maritime Procurement Team**
- 📧 Email: procurement@blumaritime.com
- 📱 Phone: +91-XXXX-XXXXXX
- 🌐 Website: www.blumaritime.com

---

### 🏷️ Version Information
- **Version**: 1.0.0
- **Last Updated**: 2024
- **Maintained By**: BLU Maritime IT Team

**© 2024 BLU Maritime - Confidential Procurement Analysis System**