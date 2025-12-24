import pandas as pd
import numpy as np
from datetime import datetime as dt

#  LAW OFFICE MANAGEMENT SYSTEM
# Uses ALL pandas concepts you've learned!
# ==========================================

print("="*44)
print(" 🏛️\U0001F5A5 LAW OFFICE MANAGEMENT SYSTEM")
print("="*44)

#  1. CLIENT DATABASE (Uses: DataFrame creation, date_range)
np.random.seed(42)
clients_data = {
    'Client_ID': range(1,21),
    'Name': ['Govinda Sahu', 'Nukesh Rajwade', 'Rami Yadav', 'Kariman Rajwade',
             'Ravi Kumar', 'Vikas Rao', 'Vijay Sonwani', 'Siyaram Sahu',
             'Deepak Kumar', 'Pushpa Gupta', 'Shivshankar Jaiswal', 'Ram Kumar',
             'Ravishankar Singh', 'Mohammad Irfan', 'Dhansoo Ram', 'Suraj Panika',
             'Ashok Kumar', 'Shivshankar Yadav', 'Bala', 'Kamal Singh'],
    'Case_Type': np.random.choice(['Accident', 'Dispute', 'Criminal', 'Civil'], 20),
    'Registration_Date': pd.date_range('2025-01-01', periods=20, freq='3D'),
    'Area': np.random.choice(['Surajpur', 'Devnagar', 'Bishrampur', 'Premnagar'], 20),
    'Status': np.random.choice(['Viable', 'Has Lawyer', 'Pending', 'Deceased'], 20),
    'Fee_Amount': np.random.randint(1000, 20000, 20),
    'Payment_Status': np.random.choice(['Paid', 'Pending', 'Partial'], 20),
    'Mobile': [f'9{np.random.randint(100000000, 999999999)}' for _ in range(20)]
}

df_clients = pd.DataFrame(clients_data)


# Calculate additional columns
df_clients['Days_Since_Registration'] = (pd.Timestamp.now().normalize() - df_clients['Registration_Date']).dt.days
df_clients['Priority'] = df_clients['Days_Since_Registration'].apply(lambda x: 'High' if x >30 else 'Medium' if x>15 else 'Low')
  # ============================================
# SECTION 1: DATA INSPECTION (head, tail, info, shape)
# ============================================
print("\nSection 1 CLIENT DATABASE OVERVIEW")
print("="*44)
print("\n \u2705 First 5 clients:")
print(df_clients.head())
print("\n \u2705 Last 3 clinte:")
print(df_clients.tail(3))

print("\n \u2705 DataFrame info.")
print(df_clients.info())

print(f"\n✅ Total Records: {df_clients.shape[0]} rows, {df_clients.shape[1]} columns")
# ============================================
# SECTION 2: COLUMN SELECTION
# ============================================
print("\n\n n📋 SECTION 2: SPECIFIC DATA EXTRACTION")
print("="*60)
print("\n✅ Client Names Only:")

print(df_clients['Name'].head())
print("\n ✅Multiple Columns(Name,Case Type, Status):")
print(df_clients[['Name','Case_Type','Status']].head())

#  ============================================
# SECTION 3: STATISTICAL ANALYSIS (sum, mean, max, min)
# ============================================
print("\n\n💰 SECTION 3: FINANCIAL STATISTICS")
print("="*60)

print(f"\n✅ Total Fee Amount: ₹{df_clients['Fee_Amount'].sum():,}")
print(f"✅ Average Fee: ₹{df_clients['Fee_Amount'].mean():.2f}")
print(f"✅ Highest Fee: ₹{df_clients['Fee_Amount'].max():,}")
print(f"✅ Lowest Fee: ₹{df_clients['Fee_Amount'].min():,}")
print(f"✅ Total Clients: ₹{df_clients['Name'].count()}")
# ============================================
# SECTION 4: BOOLEAN INDEXING (Filtering)
# ============================================
print("\n\n 🔍SECTION 4: Filtered Insights")
print("="*60)

# Filter 1: High Value Cases
high_value = df_clients[df_clients['Fee_Amount']> 10000]
print(f"\n✅ High-Value-Cases (>₹ 10,000): {len(high_value)}")
print(high_value[['Name','Case_Type','Fee_Amount']].head())

#  Filter 2: Viable cases only
viable_cases = df_clients[df_clients['Status'] == 'Viable']
print(f"\nViable Cases: {len(viable_cases)}")
print(viable_cases[['Name','Area','Status']].head())

#  Filter 3: Pending payments
pending_payment = df_clients[df_clients['Payment_Status'] == 'Pending']
print(f"\nPending Payments: {len(pending_payment)}")
print(f" Total Pending Amount: ₹{pending_payment['Fee_Amount'].sum():,}")


# ============================================
# SECTION 5: GROUPBY ANALYSIS
# ============================================
print("\n\n 📊SECTION 5: Category-wise Analysis")
print("="*60)
print("\n✅ Cases by Area")
print(df_clients.groupby('Area')['Client_ID'].count())
print("\n✅ Average Fee by Case Type")
print(df_clients.groupby('Case_Type')['Fee_Amount'].mean().round(2))

print("\n ✅ Status Distribution.")
print(df_clients['Status'].value_counts())

print("\n✅ Payment Status Summary.")
print(df_clients.groupby('Payment_Status')['Fee_Amount'].sum())

# ============================================
# SECTION 6: ADVANCED INSIGHTS
# ============================================
print("\n\n🎯 SECTION 6: BUSINESS INSIGHTS")
print("="*60)

# Paid vs Pending
paid = df_clients[df_clients['Payment_Status'] == 'Paid']
print(f"\n✅ Total Paid: ₹{paid['Fee_Amount'].sum():,}")
print(f"✅ Total Pending: ₹{pending_payment['Fee_Amount'].sum():,}")
print(f"✅ Collection Rate: {len(paid)/len(df_clients)*100:.1f}%")

# Most Profitable Area
print("\n✅ Revenue by Area:")
area_revenue = df_clients.groupby('Area')['Fee_Amount'].sum().sort_values(ascending = False)
print(area_revenue)

# Urgent Cases
urgent = df_clients[df_clients['Priority'] =='High']
print(f"✅ High Priority Cases: {len(urgent)}")
print(urgent[['Name','Days_Since_Registration','Status']].head())

#============================================
# SECTION 7: MONTHLY REPORT (date_range usage)
# ============================================

print("\n\n📅 SECTION 7: MONTHLY ACTIVITY")
print("="*60)

df_clients['Month'] = df_clients['Registration_Date'].dt.strftime('%B')
monthly = df_clients.groupby('Month').agg({'Client_ID': 'count','Fee_Amount': 'sum'}).rename(columns={'Client_ID': 'New_clients','Fee_Amount': 'Total_Revenue'})

print(monthly)


# ============================================
# FINAL SUMMARY
# ============================================
print("\n\n" + "="*60)
print(" 📈 Exexutive Summary")
print("="*60)

total_clients = len(df_clients)
viable = len(df_clients[df_clients['Status'] == 'Viable'])
has_lawyer = len(df_clients[df_clients['Status'] == 'Has Lawyer'])

revenue = df_clients[df_clients['Payment_Status'] == 'Paid']['Fee_Amount'].sum()

print(f"""
Total Clients: {total_clients}
Viable Cases: {viable} ({viable/total_clients*100:.1f}%)
Already Has Lawyer: {has_lawyer} ({has_lawyer/total_clients*100:.1f}%)
Total Revenue: ₹{revenue:,}
Expected Revenue: ₹{df_clients['Fee_Amount'].sum():,}
Collection Rate: {len(paid)/total_clients*100:.1f}%

🎯 Recommendation: Focus on {len(pending_payment)} pending payments worth ₹{pending_payment['Fee_Amount'].sum():,}
""")

print("="*60)
print(" ✅ ALL PANDAS CONCEPTS SUCCESSFULLY DEMONSTRATED!")
print("="*60)




