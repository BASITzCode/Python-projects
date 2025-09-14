Contact_book={
    'name':['Basit','Norez'],
    'phone_number':['03117564154','03264331913']
}

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input('Enter the phone number of the contact: ')
    Contact_book['name'].append(name)
    Contact_book['phone_number'].append(phone_number)
def remove_contact():
    name1= input("Enter the name of the contact to remove: ")
    if name1 in Contact_book['name']:
        index=Contact_book['name'].index(name1)
        removed_phone_number=Contact_book['phone_number'][index]
        print(f"Contact {name1} with phone number {removed_phone_number} removed.")
        print('-'*30)
    else:
        print(f"Contact {name1} not found.")
        print('-'*30)
def view_contacts():
    print("List of contacts:")
    for name in Contact_book['name']:
        index=Contact_book['name'].index(name)
        print(f"{name}: {Contact_book['phone_number'][index]}")
        print('-'*30)
def search_contact():
    name= input("Enter the name of the contact to search: ")
    if name in Contact_book['name']:
        index=Contact_book['name'].index(name)
        print(f"Contact {name} with phone number {Contact_book['phone_number'][index]} found.")
        print('-'*30)
    else:
        print(f"Contact {name} not found.")
        print('-'*30)
while True:
    print('-'*30)
    print("***Welcome to the Contact Book!☺***")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break   
    else:
        print("Invalid choice. Please try again.")
        print('-'*30)