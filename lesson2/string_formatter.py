# username and message formatter

first_name = input("First name: ")
last_name = input("last name: ")
bio_message = input("Enter bio: ")

username = first_name[0] + last_name
full_name = first_name + " " + last_name
bio_message = bio_message.replace('I am', "I'm")

print(f"Your username is {username.lower()}")
print(full_name.title())
print(bio_message.strip())
print(f"Number of characters in bio: {len(bio_message)}")