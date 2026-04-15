contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added")

def view_contacts():
    if not contacts:
        print("No contacts")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Found:", name, "-", contacts[name])
    else:
        print("Not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted successfully")
    else:
        print("Contact not found")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        view_contacts()
    elif ch == "3":
        search_contact()
    elif ch == "4":
        delete_contact()
    else:
        break