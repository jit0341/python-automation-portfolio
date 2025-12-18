from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import csv
import os

input_file = "data/sales_summary.csv"
output_file = "output/sales_report.pdf"

def generate_pdf_report():
    if not os.path.exists(input_file):
        print("❌ CSV file not found.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Sales Summary Report")

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    y = height - 100
    c.drawString(50, y, "Product")
    c.drawString(200, y, "Quantity")
    c.drawString(300, y, "Revenue")
    
    y -= 20
    total_revenue = 0

    with open(input_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check for page overflow
            if y < 50: 
                c.showPage() # Start new page
                y = height - 50 # Reset y for new page
                c.setFont("Helvetica", 10)

            c.setFont("Helvetica", 10) # Normal font for data
            c.drawString(50, y, row["Product"])
            c.drawString(200, y, row['Quantity'])
            c.drawString(300, y, f"INR{row['Revenue']}")

            total_revenue += int(row['Revenue'])
            y -= 20

    # Summary Section (Now OUTSIDE the loop)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Revenue: INR{total_revenue}")

    c.save()
    print(f"✅ PDF generated successfully: {output_file}")

# Correctly un-indented main block
if __name__ == "__main__":
    print("---- Generating PDF report ----")
    generate_pdf_report()

