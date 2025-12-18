import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')
conn.commit()

def add_expense(date, category, amount, description):
    cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                   (date, category, amount, description))
    conn.commit()
    print("✅ Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def monthly_total(month):
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (f"{month}%",))
    total = cursor.fetchone()[0]
    print(f"💰 Total for {month}: {total if total else 0}")

# Example usage
if __name__ == "__main__":
    add_expense("2025-08-17", "Food", 150, "Lunch at cafe")
    add_expense("2025-08-17", "Transport", 50, "Auto fare")
    view_expenses()
    monthly_total("2025-08")
