import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # IMPORTANT: Use non-GUI backend for Termux
import matplotlib.pyplot as plt

print("="*60)
print(" 📊 DATA VISUALIZATION - TERMUX EDITION")
print(" (All charts saved as images)")
print("="*60)

# ============================================
# STEP 1: CREATE DATA
# ============================================
print("\n📋 STEP 1: Creating Client Data...")

np.random.seed(42)
data = {
    'Name': ['Govinda Sahu', 'Nukesh Rajwade', 'Rami Yadav', 'Kariman Rajwade',
             'Ravi Kumar', 'Vikas Rao', 'Vijay Sonwani', 'Siyaram Sahu',
             'Deepak Kumar', 'Pushpa Gupta', 'Shivshankar', 'Ram Kumar',
             'Ravishankar', 'Mohammad Irfan', 'Dhansoo Ram'],
    'Case_Type': ['Accident', 'Dispute', 'Accident', 'Accident', 'Dispute',
                  'Accident', 'Dispute', 'Accident', 'Criminal', 'Accident',
                  'Civil', 'Accident', 'Dispute', 'Civil', 'Accident'],
    'Fee_Amount': [1500, 1000, 1500, 1000, 2000, 2000, 1000, 2000, 20000,
                   1500, 3000, 1800, 2500, 4000, 1200],
    'Status': ['Confirmed', 'Pending', 'Confirmed', 'Pending', 'Confirmed',
               'Confirmed', 'Pending', 'Confirmed', 'Confirmed', 'Pending',
               'Confirmed', 'Pending', 'Confirmed', 'Pending', 'Confirmed'],
    'Area': ['Surajpur', 'Surajpur', 'Surajpur', 'Surajpur', 'Surajpur',
             'Bishrampur', 'Surajpur', 'Surajpur', 'Surajpur', 'Devnagar',
             'Devnagar', 'Devnagar', 'Premnagar', 'Devnagar', 'Premnagar']
}

df = pd.DataFrame(data)
print("\n✅ Data Created! Here's a preview:")
print(df.head(10))

# ============================================
# CHART 1: BAR CHART - Cases by Type
# ============================================
print("\n\n" + "="*60)
print(" 📊 CHART 1: BAR CHART - Cases by Type")
print("="*60)

case_counts = df['Case_Type'].value_counts()
print("\nData:")
print(case_counts)

plt.figure(figsize=(10, 6))
bars = plt.bar(case_counts.index, case_counts.values, 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'], 
               edgecolor='black', linewidth=1.5)

plt.title('Number of Cases by Type', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Case Type', fontsize=12, fontweight='bold')
plt.ylabel('Number of Cases', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('chart1_case_types.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart1_case_types.png")
plt.close()

# ============================================
# CHART 2: PIE CHART - Status Distribution
# ============================================
print("\n" + "="*60)
print(" 🥧 CHART 2: PIE CHART - Status Distribution")
print("="*60)

status_counts = df['Status'].value_counts()
print("\nData:")
print(status_counts)

plt.figure(figsize=(8, 8))
colors = ['#66b3ff', '#ff9999']
explode = (0.05, 0.05)

wedges, texts, autotexts = plt.pie(status_counts.values, 
                                     labels=status_counts.index, 
                                     autopct='%1.1f%%',
                                     startangle=90, 
                                     colors=colors, 
                                     explode=explode,
                                     shadow=True,
                                     textprops={'fontsize': 12, 'fontweight': 'bold'})

plt.title('Case Status Distribution', fontsize=16, fontweight='bold', pad=20)
plt.savefig('chart2_status.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart2_status.png")
plt.close()

# ============================================
# CHART 3: HORIZONTAL BAR - Revenue by Area
# ============================================
print("\n" + "="*60)
print(" 💰 CHART 3: Revenue by Area")
print("="*60)

area_revenue = df.groupby('Area')['Fee_Amount'].sum().sort_values()
print("\nData:")
print(area_revenue)

plt.figure(figsize=(10, 6))
bars = plt.barh(area_revenue.index, area_revenue.values, 
                color='#90EE90', edgecolor='darkgreen', linewidth=1.5)

plt.title('Total Revenue by Area', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Revenue (₹)', fontsize=12, fontweight='bold')
plt.ylabel('Area', fontsize=12, fontweight='bold')
plt.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels
for i, (bar, value) in enumerate(zip(bars, area_revenue.values)):
    plt.text(value + 200, i, f'₹{value:,}', 
             va='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('chart3_area_revenue.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart3_area_revenue.png")
plt.close()

# ============================================
# CHART 4: GROUPED BAR - Cases by Area & Status
# ============================================
print("\n" + "="*60)
print(" 📊 CHART 4: Cases by Area (Grouped)")
print("="*60)

area_status = pd.crosstab(df['Area'], df['Status'])
print("\nData:")
print(area_status)

plt.figure(figsize=(12, 6))
area_status.plot(kind='bar', ax=plt.gca(), 
                 color=['#FF6B6B', '#4ECDC4'], 
                 edgecolor='black', linewidth=1.5)

plt.title('Cases by Area (Confirmed vs Pending)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Area', fontsize=12, fontweight='bold')
plt.ylabel('Number of Cases', fontsize=12, fontweight='bold')
plt.legend(title='Status', fontsize=10, title_fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('chart4_area_grouped.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart4_area_grouped.png")
plt.close()

# ============================================
# CHART 5: LINE CHART - Cumulative Revenue
# ============================================
print("\n" + "="*60)
print(" 📈 CHART 5: Cumulative Revenue Growth")
print("="*60)

df_sorted = df.sort_index()
df_sorted['Cumulative'] = df_sorted['Fee_Amount'].cumsum()

plt.figure(figsize=(12, 6))
plt.plot(range(len(df_sorted)), df_sorted['Cumulative'], 
         marker='o', linewidth=2.5, markersize=8, color='purple',
         markerfacecolor='yellow', markeredgecolor='purple', markeredgewidth=2)

plt.fill_between(range(len(df_sorted)), df_sorted['Cumulative'], 
                 alpha=0.3, color='purple')

plt.title('Cumulative Revenue Growth', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Client Number', fontsize=12, fontweight='bold')
plt.ylabel('Cumulative Revenue (₹)', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('chart5_cumulative.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart5_cumulative.png")
plt.close()

# ============================================
# CHART 6: HISTOGRAM - Fee Distribution
# ============================================
print("\n" + "="*60)
print(" 📊 CHART 6: Fee Distribution")
print("="*60)

plt.figure(figsize=(10, 6))
plt.hist(df['Fee_Amount'], bins=8, color='coral', edgecolor='black', linewidth=1.5)
plt.title('Fee Amount Distribution', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Fee Amount (₹)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('chart6_histogram.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart6_histogram.png")
plt.close()

# ============================================
# CHART 7: SCATTER PLOT - Case Number vs Fee
# ============================================
print("\n" + "="*60)
print(" 🔵 CHART 7: Scatter Plot - Fees Pattern")
print("="*60)

plt.figure(figsize=(12, 6))
colors_map = {'Confirmed': 'green', 'Pending': 'red'}
for status in df['Status'].unique():
    data_subset = df[df['Status'] == status]
    plt.scatter(range(len(data_subset)), data_subset['Fee_Amount'],
                label=status, s=150, alpha=0.7, 
                color=colors_map[status], edgecolors='black', linewidth=1.5)

plt.title('Fee Amount by Client (Status)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Client Index', fontsize=12, fontweight='bold')
plt.ylabel('Fee Amount (₹)', fontsize=12, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('chart7_scatter.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart7_scatter.png")
plt.close()

# ============================================
# CHART 8: DASHBOARD - Multiple Subplots
# ============================================
print("\n" + "="*60)
print(" 🖥️ CHART 8: Complete Dashboard")
print("="*60)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('📊 Client Data Dashboard', fontsize=20, fontweight='bold', y=0.995)

# Subplot 1: Case Types Bar
case_counts.plot(kind='bar', ax=axes[0, 0], color='skyblue', edgecolor='navy', linewidth=1.5)
axes[0, 0].set_title('Cases by Type', fontsize=14, fontweight='bold', pad=10)
axes[0, 0].set_ylabel('Count', fontsize=11, fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# Subplot 2: Status Pie
status_counts.plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%', 
                   colors=['#66b3ff', '#ff9999'], startangle=90)
axes[0, 1].set_title('Status Distribution', fontsize=14, fontweight='bold', pad=10)
axes[0, 1].set_ylabel('')

# Subplot 3: Area Revenue Horizontal Bar
area_revenue.plot(kind='barh', ax=axes[1, 0], color='lightgreen', edgecolor='darkgreen', linewidth=1.5)
axes[1, 0].set_title('Revenue by Area', fontsize=14, fontweight='bold', pad=10)
axes[1, 0].set_xlabel('Revenue (₹)', fontsize=11, fontweight='bold')
axes[1, 0].grid(axis='x', alpha=0.3)

# Subplot 4: Fee Histogram
axes[1, 1].hist(df['Fee_Amount'], bins=8, color='coral', edgecolor='black', linewidth=1.5)
axes[1, 1].set_title('Fee Distribution', fontsize=14, fontweight='bold', pad=10)
axes[1, 1].set_xlabel('Fee Amount (₹)', fontsize=11, fontweight='bold')
axes[1, 1].set_ylabel('Frequency', fontsize=11, fontweight='bold')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('chart8_dashboard.png', dpi=150, bbox_inches='tight')
print("✅ Saved: chart8_dashboard.png")
plt.close()

# ============================================
# SUMMARY & STATISTICS
# ============================================
print("\n\n" + "="*60)
print(" 📊 DATA SUMMARY")
print("="*60)

print(f"\nTotal Clients: {len(df)}")
print(f"Total Revenue: ₹{df['Fee_Amount'].sum():,}")
print(f"Average Fee: ₹{df['Fee_Amount'].mean():.2f}")
print(f"Highest Fee: ₹{df['Fee_Amount'].max():,}")
print(f"Lowest Fee: ₹{df['Fee_Amount'].min():,}")

print("\n" + "="*60)
print(" 🎉 SUCCESS! ALL 8 CHARTS CREATED!")
print("="*60)

print("""
Charts saved in your folder:
1. chart1_case_types.png - Bar chart
2. chart2_status.png - Pie chart
3. chart3_area_revenue.png - Horizontal bar
4. chart4_area_grouped.png - Grouped bar
5. chart5_cumulative.png - Line chart
6. chart6_histogram.png - Distribution
7. chart7_scatter.png - Scatter plot
8. chart8_dashboard.png - Complete dashboard

📱 View them in your phone's gallery or file manager!
📂 Location: Same folder as your Python file

🎯 WHAT YOU LEARNED:
✅ Bar charts (vertical & horizontal)
✅ Pie charts
✅ Line charts
✅ Histograms
✅ Scatter plots
✅ Multi-panel dashboards
✅ Saving charts as images
✅ Termux-friendly visualization

💪 NEXT STEPS:
1. View all 8 images
2. Change colors in code
3. Modify data and re-run
4. Create your own charts!
""")

print("\n" + "="*60)
print(" 🚀 You're now a VISUALIZATION EXPERT!")
print("="*60)

