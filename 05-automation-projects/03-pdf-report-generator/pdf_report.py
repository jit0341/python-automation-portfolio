from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import csv
import os

# File path configuration
input_file = "data/sales_summary.csv"
output_file = "output/sales_report.pdf"

def generate_pdf_report():
    if not os.path.exists(input_file):
        print("X CSV file not found.")
        return

    # Make pdf Canvas
    if os.path.exists(output_file):
        os.remove(output_file)

    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Write title
    c.setFont("Helvetica-Bold", 18)
    # (x, y, text) Left margin = 50, Top ~50 px
    # Heading text
    c.drawString(50, height - 50, "Sales Summary Report")

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    y = height - 100
    # Column space
    c.drawString(50, y, "Product")
    c.drawString(200, y, "Quantity")
    c.drawString(300, y, "Revenue")

    # Data Rows
    total_revenue = 0
    y = height - 120  # Start data rows below header with proper spacing
    # normal text
    # accumulator to add revenue
    # next row position

    # CSV file open
    with open(input_file, newline='') as file:
        reader = csv.DictReader(file)
        # every row = dictionary
        # column names = keys
        for row in reader:
            # process each record
            c.drawString(50, y, row["Product"])
            c.drawString(200, y, row["Quantity"])
            c.drawString(300, y, row["Revenue"])

            # print product column
            revenue = row.get("Revenue", "0")
            if revenue.isdigit():
                total_revenue += int(revenue)
            # Business logic
            # Business addition logic of report
            # value addition of report
            y -= 20  # next line be low

    # Summary Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Revenue: INR{total_revenue}")

    c.save()  # Save the PDF inside the function
    print(f"✓ PDF generated successfully: {output_file}")

if __name__ == "__main__":
    print("--- Generating PDF report ---")
    generate_pdf_report()
    import sys
    sys.exit(0)

