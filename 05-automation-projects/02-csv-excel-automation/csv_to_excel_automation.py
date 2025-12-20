import pandas as pd
import os
import logging
import argparse

logging.basicConfig(
    filename = "logs/automation.log",
    level = logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
    )

from config import (
    CLIENT_NAME,
    REPORT_TITLE,
    INPUT_FILE,
    OUTPUT_FILE,
    REQUIRED_COLUMNS
)

def parse_arguments():
    """Parse Optional CLI arguments"""
    parser = argparse.ArgumentParser(
        description = "CSV to Excel Automation")
    parser.add_argument(
        "--client",
        help = "Client name (overrides config)",
        default= CLIENT_NAME)
    parser.add_argument(
        "--input",
        help= "Input CSV file path",
        default =INPUT_FILE)
    parser.add_argument(
        "--output",
        help="Output Excel file path",
        default=OUTPUT_FILE)
    return parser.parse_args()

def load_csv(path):
    """Load CSV file safely"""
    if not os.path.exists(path):
        print(f" File not found: {path}")
        return None

    df = pd.read_csv(path)

    if df.empty:
        print(" CSV file is empty.")
        return None

        if missing_columns:
            logging.error(f"Missing required columns: {missing_columms}")
            print(f"❌ Missing columns in CSV: {missing_columns}")
            return None
        return df

def clean_data(df):
    """Clean dataframe based on rules."""
    initial_rows = len(df)
    
    # Remove duplicate rows
    df_clean = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df_clean)
    
    # Remove rows with missing names (assuming 'Name' column exists)
    df_final = df_clean.dropna(subset=['Name'])
    missing_names_removed = len(df_clean) - len(df_final)
    
    return df_final, duplicates_removed, missing_names_removed, initial_rows

def validate_columns(df,REQUIRED_COLUMNS):
    """Validates required columns"""
    missing_columns = [col for col in
    REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        print(f"Missing required columns: {missing_columns}")
        print("Please fux the CSV anf try again")
        return False
    logging.info("All required columns are present")
    logging.info(f"Validating required columns: {REQUIRED_COLUMNS}")
    return True


def csv_to_excel_automation():

    """
    CSV to Excel Automation Script with Error Handling
    - Reads CSV data
    - Cleans duplicate rows
    - Removes rows with missing names
    - Exports to clean Excel file
    """
    args = parse_arguments()
    client_name = args.client
    input_file = args.input
    output_file = args.output

    logging.info(f"Processing started for client: {CLIENT_NAME}")

    # File paths
    
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"❌ Error: Input file '{input_file}' not found!")
            print(f"💡 Please ensure the file exists in the correct location.")
            return
        
        # Load CSV data
        print(f"📂 Loading data from '{input_file}'...")
        df = load_csv(input_file)
        if df is None:
            return
        # Step 4: Column Validation
        if not validate_columns(df,REQUIRED_COLUMNS):
            return

        initial_rows = len(df)
        print(f"✅ Loaded {initial_rows} rows successfully")
        logging.info(f"CSV loaded successfully with {initial_rows} rows")
        
        # Display raw data
        print("\n📊 Raw Data (First 5 rows):")
        print(df.head())

        # Data Cleaning
        print("\n🧹 Cleaning data...")
        df, duplicates_removed, missing_names_removed, _ = clean_data(df)
        
        # Print cleaning summary
        print(f"   - Duplicates removed: {duplicates_removed}")
        print(f"   - Missing names removed: {missing_names_removed}")
        print(f"   - Final row count: {len(df)}")
        logging.info(f"Duplicates removed: {duplicates_removed}")
        logging.info(f"Missing names removed: {missing_names_removed}")
        logging.info(f"Final row count: {len(df)}")
    
        # Display cleaned data
        print("\n✨ Cleaned Data (First 5 rows):")
        print(df.head())
        
        # Export to Excel
        print(f"\n💾 Exporting to '{output_file}'...")
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"✅ Export complete! File saved: {output_file}")
        logging.info(f"Excel file exported successfully: {output_file}")

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
        logging.error(f" Unexpected error occured: {e}")
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
        logging.info("Automation finished")

# Run the automation
if __name__ == "__main__":
    print("🚀 CSV to Excel Automation - Starting...\n")
    logging.info("Automation started.")
    csv_to_excel_automation()
