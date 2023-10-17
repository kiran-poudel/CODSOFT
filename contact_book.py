contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}

def view_contact_list():
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

def search_contact(query):
    results = {}
    for name, info in contacts.items():
        if query in name or query in info['phone']:
            results[name] = info
    return results

def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        if phone is not None:
            contacts[name]['phone'] = phone
        if email is not None:
            contacts[name]['email'] = email
        if address is not None:
            contacts[name]['address'] = address

def delete_contact(name):
    if name in contacts:
        del contacts[name]


def main():
    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            add_contact(name, phone, email, address)
        
        elif choice == '2':
            view_contact_list()
        
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = search_contact(query)
            if results:
                view_contact_list(results)
            else:
                print("No matching contacts found.")
        
        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("New Phone (press enter to keep unchanged): ")
            email = input("New Email (press enter to keep unchanged): ")
            address = input("New Address (press enter to keep unchanged): ")
            update_contact(name, phone, email, address)
        
        elif choice == '5':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
