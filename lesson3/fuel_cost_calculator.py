# The Challenge: “The South African Fuel Cost Calculator”

kilometers = float(input("How many kilometers do you want to drive?: "))

petrol_price = float(input("What's the petrol price per litre?: "))

litres_needed = round(kilometers / 10, 2)

total_cost = round(litres_needed * petrol_price, 2)

print(f"To drive {kilometers} km you'll need {litres_needed} litres of petrol which will cost you R{total_cost}")