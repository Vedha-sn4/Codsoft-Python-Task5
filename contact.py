import re  # Import the regular expression module

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n===== Contact List =====")
            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n")

    def search_contacts(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not results:
            print(f"No contacts found for '{keyword}'.")
        else:
            print("\n===== Search Results =====")
            for result in results:
                print(f"Name: {result.name}\nPhone: {result.phone}\nEmail: {result.email}\nAddress: {result.address}\n")

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact '{contact.name}' updated successfully.")
                return
        print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
                return
        print(f"Contact with name '{name}' not found.")


def is_valid_phone(phone):
    # Use a regular expression to validate the phone number
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(phone))

def is_valid_email(email):
    # Use a regular expression to validate the email
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))

# Directly include the content of the main function
contact_manager = ContactManager()

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")

        # Validate phone number and email
        if not is_valid_phone(phone):
            print("Invalid phone number. Please enter a 10-digit number.")
            continue
        if not is_valid_email(email):
            print("Invalid email address. Please enter a valid email.")
            continue

        new_contact = Contact(name, phone, email, address)
        contact_manager.add_contact(new_contact)

    elif choice == '2':
        contact_manager.view_contacts()

    elif choice == '3':
        keyword = input("Enter search keyword (name or phone): ")
        contact_manager.search_contacts(keyword)

    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")

        # Validate phone number and email
        if not is_valid_phone(new_phone):
            print("Invalid phone number. Please enter a 10-digit number.")
            continue
        if not is_valid_email(new_email):
            print("Invalid email address. Please enter a valid email.")
            continue

        contact_manager.update_contact(name, new_phone, new_email, new_address)

    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        contact_manager.delete_contact(name)

    elif choice == '6':
        print("Exiting the Contact Management System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

