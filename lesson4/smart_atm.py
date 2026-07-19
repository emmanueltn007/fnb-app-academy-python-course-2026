# The Challenge: “The Smart ATM Withdrawal Simulator”

balance = 1750.53

amount_to_withdraw = float(input("Enter amount to withdraw: R"))

remaining_balance = balance - amount_to_withdraw

if amount_to_withdraw == 0 or amount_to_withdraw < 0:
    print("Invalid amount, you can only withdraw an amount more than R0")
elif amount_to_withdraw <= balance:
    print(f"Withdrawal successful! Remaining balance: R{round(remaining_balance, 2)}")
else: 
    print("Declined. Insufficient funds")
