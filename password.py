contact_book = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contact_book:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for name, details in contact_book.items():
        print(f"Name: {name}, Phone: {details['Phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for name, details in contact_book.items():
        if keyword.lower() in name.lower() or keyword in details['Phone']:
            print(f"\nFound Contact - Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        print("Leave blank to keep existing value.")
        phone = input(f"New phone number ({contact_book[name]['Phone']}): ") or contact_book[name]['Phone']
        email = input(f"New email ({contact_book[name]['Email']}): ") or contact_book[name]['Email']
        address = input(f"New address ({contact_book[name]['Address']}): ") or contact_book[name]['Address']
        contact_book[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main_menu():
    while True:
        print("==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()
