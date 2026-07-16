# Creating a professional system email generator

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

username = f"{first_name[0]}{last_name}"

print(f"Your email is: {username.lower()}@university.co.za")