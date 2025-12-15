#=======Configuration===========
library_file = "libraries.txt"
libraries = {}
SEPARATOR = "|"

#===========File Operation=======
def load_libraries():
    print("\n------Loading Libraries-------")
    global libraries
    libraries = {}
    try:
        with open(library_file,"r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(SEPARATOR)
                if len(parts) == 3:
                    book_name,author,genre = parts

                    libraries[book_name.title()] = {
                    "author": author,
                    "genre": genre
                    }

        print("Library loaded successfully from libraries.txt.")
    except FileNotFoundError:
        print(f"No Libraries file found. startimg fresh.")
    except Exception as e:
        print(f"An error occurred during loading: {e}")
        libraries = {}

def save_libraries():
    print("\n------Saving Libraries-------")
    try:
        with open("libraries.txt","w") as file:
            for book_name,details in libraries.items():
                line = f"{book_name}{SEPARATOR}{details['author']}{SEPARATOR}{details['genre']}\n"
                file.write(line)
        print("\nBooks saved successfully to libraries.txt")
    
    except Exception as e:
        print(f"Error saving libraries: {e}")
#=======CRUD Operation============
def add_books():
    print("\n-----Adding New Books-------")
    global libraries
    book_name = input("Enter Book Name:").strip().title()
    if not book_name:
        print("Book Name cannot be empty.")
        return
    if book_name in libraries:
        print(f"Book Name '{book_name}' already exists.")
        return
    author = input("Enter Author Name:").strip() or "N/A"
    genre = input("Enter Genre:").strip() or "N/A"
    libraries[book_name] = {
            "author": author,
            "genre": genre
            }
    print(f"Books '{book_name}' added successfully")

def view_all_books():
    print("\n-----View Books-------")
    if not libraries:
        print("No books found! Add one.")
        return
    print(f"{'Book name': <20} {'author': <15} {'genre': <30}")
    print("=" *65)

    for book_name,details in libraries.items():
        print(f"{book_name: <20} {details['author']: <15} {details['genre']: <30}")


def search_book():
    print("\n-----Searching Books--------")
    search_book = input("Enter book name to search:").strip().title()
    if search_book in libraries:
        details = libraries[search_book]
        print(f"\nFound book: {search_book}.")
        print(f" Author: {details['author']}")
        print(f"Genre: {details['genre']}")

    else:
        print(f"Book '{search_book}' not found in library.")

def delete_book():
    global libraries
    print("\n-----Deleting Book--------")
    book_name_to_delete = input("Enter book name to delete:").strip().title()
    if book_name_to_delete in libraries:
        confirm = input(" Are you sure want to delete '{book_name_to_delete}' ? (y/n):").lower()
        if confirm == "y":
            del libraries[book_name_to_delete]
            print(f"Book '{book_name_to_delete}' deleted successfully.")
        else:
            print("Action cancelled!")
    else:
        print(f"Book '{book_name_to_delete}' not found.")
#=========================================
#           Main Menu
#=========================================

def main_menu():
    load_libraries()

    while True:
        print(" Library Management Menu ")
        print("1. Add Books")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5):").strip()

        if choice == "1":
            add_books()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            save_libraries()

            print("\n Thank you for using Library Management System. Goodbye!")
            break
        else:
            print(" Invalid choice. please enter from 1 to 5")

#========Run the program==========
if __name__ == "__main__":
    main_menu()











