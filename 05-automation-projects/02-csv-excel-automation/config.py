# Client Configuration

CLIENT_NAME = "ABC Traders"
REPORT_TITLE = "Monthly Sales Report"

INPUT_FILE = "data/sales_data.csv"
OUTPUT_FILE = "clean_sales_report.xlsx"

REQUIRED_COLUMNS = ["Name", "Product", "Amount", "City"]

# Acceptable alternate column names
COLUMN_ALIASES = {
    "Name": ["Name", "CustomerName", "ClientName"],
    "Product": ["Product", "Item"],
    "Amount": ["Amount", "Price", "Total"],
    "City": ["City", "Location"]
}
