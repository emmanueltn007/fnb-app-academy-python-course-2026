# The Challenge: “The Phone Directory Search”

contacts = [
    {"name": "Emmanuel", "phone_number": "0787819070"},
    {"name": "John", "phone_number": "0697633621"},
    {"name": "Levy", "phone_number": "0659334956"}
]

def search_contact(name):
    for contact in contacts:
        
        if contact["name"] == name:
            print(f"Found! {contact["name"]}’s number is {contact["phone_number"]}")
            return
    print(f"Contact not found.")

while True:
    user_input = input("Enter name to search or type exit to exit: ").strip()
    
    if user_input.lower() == "exit":
        break
    else:
        search_contact(user_input.title())
