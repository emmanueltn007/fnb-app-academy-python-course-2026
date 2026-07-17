# Multi-Function Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {round(num1 + num2, 2)}")

print(f"Difference: {round(num1 - num2, 2)}")

print(f"Product: {round(num1 * num2, 2)}")

if num2 == 0:
    print(f"{num1} cannot be divided by {num2}")
else:
    print(f"Quotient: {round(num1 / num2, 2)}")
    print(f"Floor division: {round(num1 // num2, 2)}")
    print(f"Modulus: {round(num1 % num2, 2)}")