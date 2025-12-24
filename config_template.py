# Universal config template
CLIENT_NAME = "Client Name Here"
INPUT_FILE = "data/input.csv"
OUTPUT_FILE = "report.xlsx"

REQUIRED_COLUMNS = ["Name", "Amount"]
COLUMN_ALIASES = {
    "Name": ["name", "customer", "CustomerName"],
}

DROP_COLUMNS = []
FINAL_COLUMN_RENAME = {}

# Validation rules
DATA_TYPES = {'Amount': 'numeric'}
NOT_NULL_COLUMNS = ['Name']

# Business rules (custom function)
def business_logic(df):
    # Your custom logic here
    return df
