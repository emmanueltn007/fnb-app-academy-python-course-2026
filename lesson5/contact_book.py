# Practical Task

contacts = []

def add_contact(name, surname, phone, email):
    contacts.append({"name": name, "surname": surname, "phone": phone, "email": email})
    print(f"{name} has been added successfully !")
    
def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"{name} has been deleted successfully !")
            return
    print(f"{name} not found in contacts")    
    
def view_all():
    if not contacts:
        print("No contacts found")
        return
    
    print("\n-- Contact List --")
    for i, contact in enumerate(contacts, start = 1):
        print(f"{i}. {contact['name']} {contact['surname']}")
        print(f"    {contact['phone']} {contact['email']}")
        print("-" * 30)
        
def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact['name']} {contact['surname']}")
            print(f"    {contact['phone']} {contact['email']}")
            return
    print(f"{name} not found, please try another name.")

while True:
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. View All")
    print("5. Exit")
    
    choice = int(input("What do you want to do (1-5)? "))
    
    if choice == 1:
        name = input("Enter contact name: ").title()
        
        surname = input("Enter contact surname: ").title()
        
        phone = input("Enter contact phone number: ")
        
        email = input("Enter contact email: ")
        
        add_contact(name, surname, phone, email)
    elif choice == 2: 
        contact_to_search = input("Enter contact name to search: ").title()
        
        search_contact(contact_to_search)
    elif choice == 3: 
        contact_to_delete = input("Enter contact name to delete: ").title()
        
        delete_contact(contact_to_delete)
    elif choice == 4: 
        view_all()
    else:
        break