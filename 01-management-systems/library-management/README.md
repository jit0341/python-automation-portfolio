# 📚 Library Management System

A command-line application for managing book collections with full CRUD functionality.

## 📸 Screenshots

![Main Menu](screenshots/menu.png)
![View Books](screenshots/view.png)

## ✨ Features

- ✅ **Add Books** - Store book details with author and genre
- 📋 **View All Books** - Display in formatted table
- 🔍 **Search Books** - Find books by name
- 🗑️ **Delete Books** - Remove with confirmation
- 💾 **Persistent Storage** - Data saved in text file
- ⚠️ **Input Validation** - Prevents empty/duplicate entries
- 🛡️ **Error Handling** - Graceful exception management

## 🛠️ Technologies Used

- **Python 3.x**
- **File I/O** (read/write operations)
- **Dictionary data structures**
- **Exception handling**(try/except)
- **String manipulation**

## 📋 Prerequisites

```bash
Python 3.6 or higher
🚀 Installation & Usage
Clone or download the file
Run the program:
python library_system.py
Follow menu options:
1. Add Books
2. View Books
3. Search Book
4. Delete Book
5. Save and Exit

📂 File Structure
library-management/
├── library_system.py    # Main application
├── libraries.txt        # Data storage (auto-created)
├── README.md           # This file
└── screenshots/        # UI screenshots
💡 How It Works
Data Storage Format
Book Name|Author|Genre
Sample Data
Python Programming|John Doe|Technology
Harry Potter|J.K. Rowling|Fiction
The Alchemist|Paulo Coelho|Fiction
🔧 Code Structure
Dictionary Format:
libraries = {
    "Book Name": {
        "author": "Author Name",
        "genre": "Genre Type"
    }
}
Key Functions:
load_libraries() - Loads data on startup
save_libraries() - Saves data on exit
add_books() - Adds new book entry
view_all_books() - Displays all books
search_book() - Finds specific book
delete_book() - Removes book entry
🎯 Use Cases
Personal book collection management
Small library systems
Book lending tracking
Reading list organization
Academic book databases
🚀 Future Enhancements
[ ] Add borrowing feature (issue/return dates)
[ ] ISBN tracking
[ ] Multiple copies support
[ ] Export to CSV/Excel
[ ] GUI interface (Tkinter/PyQt)
[ ] Database backend (SQLite)
[ ] User authentication
[ ] Book availability status
🐛 Known Issues
Currently limited to text file storage
No multi-user support
Manual backup recommended
🤝 Contributing
Contributions welcome! Feel free to:
Report bugs
Suggest features
Submit pull requests
📝 License
This project is open source and available under the MIT License.
👤 Author
Jitendra Bharti
GitHub: @jit0341
⭐ If you find this project useful, please give it a star!
