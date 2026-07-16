# Student Info Formatter

first_name = input("Enter first name: ").title()
surname = input("Enter surname: ").title()
age = int(input("Enter your age: "))
favourite_number = round(float(input("Enter your favourite number: ")), 2)

print(f"Welcome, {first_name} {surname}")

age_in_months = age * 12

print(f"You are {age_in_months} months old")
print(f"Your favourite number is {favourite_number}")

print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")
