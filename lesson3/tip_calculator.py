# Calculating the tip

bill = float(input("Enter the bill: R"))

tip = 0.15

tip_value = bill * tip

total_cost = bill + tip_value

print(f"Your total tip is: R{round(tip_value, 2)}")
print(f"Amount to pay is: R{round(total_cost, 2)}")