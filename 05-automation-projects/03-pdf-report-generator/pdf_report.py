from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import csv
import os
# File path configuration
input_file = "data/sales_summary.csv"
output_file = "output/sales_report.pdf"
# Function definition
def generate_pdf_report():
    # File existence check
    if not os.path.exists(input_file):
        print("❌ CSV file not found.")
        return
    # Make pdf Canvas
    c = canvas.Canvas(output_file, pagesize = A4)
    width,height = A4
    # Write title
    c.setFont("Helvetica-Bold",18)
    # font select size=18
    c.drawString(50,height-50 ," Sales Summary Report")
    # (x, y, text) 
    # Left margin = 50
    # Top से 50 नीचेH       
    # Heading text

    # Table Header
    c.setFont("Helvetica-Bold" ,12)
    y = height-100

    # Column space
    c.drawString(50, y, "Product")
    c.drawString(200, y, "Quantity")
    c.drawString(300, y, "Revenue")

    # Data Rows
    c.setFont("Helvetica-Bold",12)
    total_revenue = 0
    y -= 20
    # normal text
    # accumulator to add revenue 
    # next row position
    # CSV file ooen
    with open(input_file, newline='') as file:
        reader = csv.DictReader(file)
        # every row = dictionary
        # column names = keys
        for row in reader:
            # process each record
            c.drawString(50, y, row["Product"])
            c.drawString(200,y, row['Quantity'])
            c.drawString(300,y, row['Revenue'])

            # print product column
            total_revenue += int(row['Revenue'])
            # Business logic
            # value addition of report
            y -= 20 # next line below
            # Summary Section
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y -20,f"Total Revenue: ₹{total_revenue}")

            c.save()
            print(f"✅ PDF generated successfully: {output_file}")

if __name__ == "__main__":
    print("----Generating PDF report------")
    generate_pdf_report()




