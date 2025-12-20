import pandas as pd
import os
import logging
import argparse
from config import CLIENT_NAME, INPUT_FILE, OUTPUT_FILE, REQUIRED_COLUMNS
from config import COLUMN_ALIASES


# ---------------- LOGGING ----------------
logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------- ARGUMENT PARSER ----------------
def parse_arguments():
    parser = argparse.ArgumentParser(description="CSV to Excel Automation")
    parser.add_argument("--client", default=CLIENT_NAME)
    parser.add_argument("--input", default=INPUT_FILE)
    parser.add_argument("--output", default=OUTPUT_FILE)
    return parser.parse_args()

# ---------------- LOAD CSV ----------------
def load_csv(path):
    if not os.path.exists(path):
        logging.error(f"Input file not found: {path}")
        print(f"❌ File not found: {path}")

        return None

    df = pd.read_csv(path)

    if df.empty:
        logging.error("CSV file is empty")
        print("❌ CSV file is empty")
        return None

    return df
# -------------COLUMN NORMALISE ------------------------------
def normalize_columns(df, column_aliases):
    """
    Normalize column names using aliases (case-insensitive + strip)
    """
    df.columns = [c.strip() for c in df.columns]

    renamed = {}

    for standard_col, aliases in column_aliases.items():
        for col in df.columns:
            if col.lower() == standard_col.lower():
                renamed[col] = standard_col

            for alias in aliases:
                if col.lower() == alias.lower():
                    renamed[col] = standard_col

    df = df.rename(columns=renamed)

    logging.info(f"Columns after normalization: {list(df.columns)}")
    return df
# ---------------- COLUMN VALIDATION ----------------
def validate_columns(df, required_columns):
    missing = [c for c in required_columns if c not in df.columns]

    if missing:
        logging.error(f"Missing required columns: {missing}")
        print(f"❌ Missing required columns: {missing}")
        print("💡 Please fix the CSV and try again.")
        return False

    logging.info("All required columns present")
    return True

# ---------------- CLEAN DATA ----------------
def clean_data(df):
    initial_rows = len(df)

    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)

    df = df.dropna(subset=["Name"])
    missing_names_removed = initial_rows - duplicates_removed - len(df)

    return df, duplicates_removed, missing_names_removed, initial_rows

# ---------------- MAIN AUTOMATION ----------------
def apply_column_transformations(df, rename_rules, drop_columns, extra_columns):
    """
    Apply client-specific column transformations
    """

    # Rename columns
    df = df.rename(columns=rename_rules)

    # Drop unwanted columns (ignore if missing)
    df = df.drop(columns=drop_columns, errors="ignore")

    # Add extra columns
    for col, value in extra_columns.items():
        if value == "AUTO":
            df[col] = pd.Timestamp.now().strftime("%Y-%m-%d")
        else:
            df[col] = value

    return df
def csv_to_excel_automation():
    args = parse_arguments()
    client = args.client
    input_file = args.input
    output_file = args.output

    logging.info(f"Automation started for client: {client}")
    print(f"🚀 Processing started for client: {client}")

    df = load_csv(input_file)
    if df is None:
        return
    df = normalize_columns(df, COLUMN_ALIASES)
    # 🔴 THIS IS THE KEY STEP
    if not validate_columns(df, REQUIRED_COLUMNS):
        return

    print("\n📊 Raw Data:")
    print(df.head())

    df, dup_removed, missing_removed, initial_rows = clean_data(df)

from config import COLUMN_RENAME_RULES, COLUMNS_TO_DROP, EXTRA_COLUMNS

df = apply_column_transformations(
    df,
    COLUMN_RENAME_RULES,
    COLUMNS_TO_DROP,
    EXTRA_COLUMNS
)
    logging.info(f"Duplicates removed: {dup_removed}")
    logging.info(f"Missing names removed: {missing_removed}")
    logging.info(f"Final rows: {len(df)}")

    print("\n🧹 Cleaning Summary")
    print(f"Duplicates removed: {dup_removed}")
    print(f"Missing names removed: {missing_removed}")
    print(f"Final rows: {len(df)}")

    df.to_excel(output_file, index=False, engine="openpyxl")
    logging.info(f"Excel exported: {output_file}")

    print(f"\n✅ Excel file created: {output_file}")
    print("\n🏁 Automation finished successfully")

# ---------------- RUN ----------------
if __name__ == "__main__":
    csv_to_excel_automation()
