PDF Sales Report Generator (Python Automation)

This project demonstrates real-world PDF report generation using Python.
It reads sales data from a CSV file and automatically generates a professional PDF summary report with totals.


---

🚀 Features

Reads structured data from CSV

Generates clean, formatted PDF report

Calculates total revenue automatically

Safe to run multiple times (no “generate once” issue)

Well-commented code for learning & maintenance



---

📁 Project Structure

03-pdf-report-generator/
│
├── data/
│   └── sales_summary.csv        # Input CSV data
│
├── output/
│   └── sales_report.pdf         # Generated PDF report
│
├── screenshots/
│   └── before_data.jpg          # CSV preview (optional)
│
├── pdf_report.py                # Main automation script
└── README.md


---

🧾 Input CSV Format

The CSV file must contain the following headers:

Product,Quantity,Revenue
Laptop,5,250000
Mobile,10,200000
Tablet,3,45000


---

⚙️ How the Script Works (Step-by-Step)

1️⃣ File Validation

if not os.path.exists(input_file):
    print("❌ CSV file not found.")
    return

✔ Prevents crash if input file is missing


---

2️⃣ Canvas Creation (PDF Setup)

c = canvas.Canvas(output_file, pagesize=A4)
width, height = A4

✔ Initializes PDF document
✔ A4 page size used for standard reports


---

3️⃣ Report Title

c.setFont("Helvetica-Bold", 18)
c.drawString(50, height - 50, "Sales Summary Report")

✔ Large bold heading at the top


---

4️⃣ Table Header

c.setFont("Helvetica-Bold", 12)
y = height - 100

✔ Column headings positioned below title


---

5️⃣ Reading CSV & Writing Rows

with open(input_file, newline='') as file:
    reader = csv.DictReader(file)

✔ Each CSV row becomes a dictionary
✔ Revenue is accumulated during iteration


---

6️⃣ Layout Control (Y-Axis Logic)

y -= 20

✔ Moves cursor down after each row
✔ Prevents text overlap


---

7️⃣ Summary Section

c.drawString(50, y - 20, f"Total Revenue: INR{total_revenue}")

✔ Printed after all rows
✔ Business value section


---

8️⃣ Final Save (MOST IMPORTANT)

c.save()

✔ Commits PDF to disk
✔ Must be called once and only once
✔ Always kept inside the function


---

▶️ How to Run

python pdf_report.py

Output:

---- Generating PDF report ----
✅ PDF generated successfully: output/sales_report.pdf


---

📌 Key Learning Points

PDF canvas must be saved only once

Variables inside functions are local (scope matters)

Layout positioning is critical in report generation

Automation scripts should be repeatable & safe



---

🧠 Real-World Use Cases

Sales summary reports

Invoice generation

Business analytics exports

Client deliverables automation



---

🧰 Technologies Used

Python

ReportLab

CSV module

File system handling



---

👨‍💻 Author

Jitendra Bharti
Python Automation Developer (PAD)
Focused on real-world automation & freelancing-ready projects.



