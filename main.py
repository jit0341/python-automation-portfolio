from automation_utils import *

# 1. सेटअप (Logging)
setup_logging(log_file='logs/client_xyz.log')

# 2. डेटा लोड करें
df = load_csv("raw_sales_data.csv")

if df is not None:
    initial_count = len(df)
    
    # 3. डेटा सफाई (Cleaning)
    df, dup_removed = remove_duplicates(df)
    df, missing_removed = handle_missing_data(df, strategy='drop')
    df = clean_text_columns(df, ['Customer Name', 'City'])
    
    # 4. बिज़नेस रूल्स (Example: 10% डिस्काउंट कैलकुलेट करना)
    def calculate_discount(data):
        data['Discounted_Price'] = data['Price'] * 0.9
        return data

    df = apply_business_rules(df, calculate_discount)
    
    # 5. आउटपुट डायरेक्टरी और रिपोर्ट
    out_dir = create_output_directory("Client_XYZ")
    save_path = f"{out_dir}/cleaned_sales.xlsx"
    save_to_excel(df, save_path)
    
    # 6. शानदार रिपोर्ट जनरेट करें (यही क्लाइंट को इम्प्रेस करती है!)
    ops = {
        'duplicates_removed': dup_removed,
        'missing_rows_dropped': missing_removed,
        'logic_applied': '10% Discount Calculation'
    }
    
    generate_summary_report(
        "Client_XYZ", 
        "raw_sales_data.csv", 
        initial_count, 
        len(df), 
        ops, 
        out_dir
    )

