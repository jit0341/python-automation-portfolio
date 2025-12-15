# --- Configuration ---
CONTACTS_FILE = "contacts.txt"
contacts = {} # Dictionary to store contacts: {"Name": {"phone": "...", "email": "..."}}
SEPARATOR = "|" # Character to separate fields in the text file

# =================================================================
#                         FILE HANDLING
# =================================================================

def load_contacts():
    """6. Loads contacts from the plain text file when starting."""
    global contacts
    contacts = {}
    try:
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                # Expecting format: Name|Phone|Email\n
                line = line.strip()
                if not line:
                    continue

                parts = line.split(SEPARATOR)

                # Check if we have the expected number of parts (Name, Phone, Email)
                if len(parts) == 3:
                    name, phone, email = parts
                    # Store data in the dictionary structure
                    contacts[name.title()] = {
                        "phone": phone,
                        "email": email
                    }
        print("✅ Contacts loaded successfully from contacts.txt.")
    except FileNotFoundError:
        print("ℹ️ No contacts file found. Starting fresh.")
    except Exception as e:
        # Catch unexpected reading errors
        print(f"An error occurred during loading: {e}")
        contacts = {}


def save_contacts():
    """It makes changes permanent by writing to contacts.txtls."""
    try:
        with open(CONTACTS_FILE, 'w') as file:
            for name, details in contacts.items():
                # Write each contact as a single line: Name|Phone|Email
                line = f"{name}{SEPARATOR}{details['phone']}{SEPARATOR}{details['email']}\n"
                file.write(line)
        print("\n💾 Contacts saved successfully to contacts.txt.")
    except Exception as e:
        print(f"❌ Error saving contacts: {e}")

# =================================================================
#                       CONTACT OPERATIONS
# =================================================================

def add_contact():
    """1. Adds a contact (name, phone, email) to the dictionary."""
    global contacts
    print("\n--- Add New Contact ---")

    # Standardize name for consistent dictionary key
    name = input("Enter Name: ").strip().title()

    if not name:
        print("❌ Name cannot be empty.")
        return

    if name in contacts:
        print(f"⚠️ Contact '{name}' already exists.")
        return

    phone = input("Enter Phone Number: ").strip() or "N/A"
    email = input("Enter Email Address: ").strip() or "N/A"

    # Store the contact details in the required dictionary structure
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"✅ Contact '{name}' added successfully.")

def view_all_contacts():
    """2. Displays all contacts from the dictionary."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found. Add one!")
        return

    # Print header
    print(f"{'Name':<20} {'Phone':<15} {'Email':<30}")
    print("-" * 65)

    # Iterate and print each contact
    for name, details in contacts.items():
        print(f"{name:<20} {details['phone']:<15} {details['email']:<30}")

def search_contact():
    """3. Searches for a contact by name."""
    print("\n--- Search Contact ---")
    search_term = input("Enter the name to search: ").strip().title()

    if search_term in contacts:
        details = contacts[search_term]
        print(f"\nFound Contact: {search_term}")
        print(f"  Phone: {details['phone']}")
        print(f"  Email: {details['email']}")
    else:
        print(f"❌ Contact '{search_term}' not found.")

def delete_contact():
    """4. Deletes a contact by name."""
    global contacts
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip().title()

    if name_to_delete in contacts:
        confirm = input(f"Are you sure you want to delete '{name_to_delete}'? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name_to_delete]
            print(f"✅ Contact '{name_to_delete}' deleted successfully.")
        else:
            print("Action cancelled.")
    else:
        print(f"❌ Contact '{name_to_delete}' not found.")

# =================================================================
#                             MAIN MENU
# =================================================================

def main_menu():
    """The main loop for the Contact Manager program."""

    # Load contacts immediately upon starting
    load_contacts()

    while True:
        print("\n" + "="*30)
        print("  CONTACT MANAGER MENU")
        print("="*30)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit and Save")
        print("-" * 30)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            save_contacts()
            print("\n👋 Thank you for using the Contact Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# --- Run the program ---
if __name__ == "__main__":
    main_menu()
