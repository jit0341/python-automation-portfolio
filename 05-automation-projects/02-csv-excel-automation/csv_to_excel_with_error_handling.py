import pandas as pd
import os

def csv_to_excel_automation():
    """
    CSV to Excel Automation Script with Error Handling
    - Reads CSV data
    - Cleans duplicate rows
    - Removes rows with missing names
    - Exports to clean Excel file
    """
    
    # File paths
    input_file = "data/sales_data.csv"
    output_file = "clean_sales_report.xlsx"
    
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"❌ Error: Input file '{input_file}' not found!")
            print(f"💡 Please ensure the file exists in the correct location.")
            return
        
        # Load CSV data
        print(f"📂 Loading data from '{input_file}'...")
        df = pd.read_csv(input_file)
        initial_rows = len(df)
        print(f"✅ Loaded {initial_rows} rows successfully")
        
        # Display raw data
        print("\n📊 Raw Data (First 5 rows):")
        print(df.head())
        
        # Data Cleaning
        print("\n🧹 Cleaning data...")
        
        # Remove duplicate rows
        df = df.drop_duplicates()
        duplicates_removed = initial_rows - len(df)
        
        # Remove rows where Name is missing
        df = df.dropna(subset=["Name"])
        missing_names_removed = initial_rows - duplicates_removed - len(df)
        
        print(f"   - Duplicates removed: {duplicates_removed}")
        print(f"   - Missing names removed: {missing_names_removed}")
        print(f"   - Final row count: {len(df)}")
        
        # Display cleaned data
        print("\n✨ Cleaned Data:")
        print(df)
        
        # Export to Excel
        print(f"\n💾 Exporting to '{output_file}'...")
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"✅ Export complete! File saved: {output_file}")
        
        # Summary
        print("\n" + "="*50)
        print("📈 AUTOMATION SUMMARY:")
        print("="*50)
        print(f"Input File: {input_file}")
        print(f"Output File: {output_file}")
        print(f"Initial Rows: {initial_rows}")
        print(f"Final Rows: {len(df)}")
        print(f"Rows Removed: {initial_rows - len(df)}")
        print(f"Success Rate: {(len(df)/initial_rows)*100:.1f}%")
        print("="*50)
        
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found!")
        print("💡 Solution: Check if the file path is correct")
        
    except pd.errors.EmptyDataError:
        print(f"❌ Error: The file '{input_file}' is empty!")
        print("💡 Solution: Ensure the CSV file contains data")
        
    except KeyError as e:
        print(f"❌ Error: Column not found - {e}")
        print("💡 Solution: Check if 'Name' column exists in your CSV")
        
    except PermissionError:
        print(f"❌ Error: Permission denied!")
        print(f"💡 Solution: Close '{output_file}' if it's open in Excel")
        
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        print(f"💡 Error type: {type(e).__name__}")
        
    finally:
        print("\n🏁 Script execution completed!")

# Run the automation
if __name__ == "__main__":
    print("🚀 CSV to Excel Automation - Starting...\n")
    csv_to_excel_automation()
