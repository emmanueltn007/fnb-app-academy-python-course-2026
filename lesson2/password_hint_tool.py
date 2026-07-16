# The Challenge: “The Secure Password Hint Tool”

password = input("Enter password: ").strip()

password_hint = f"Your password starts with {password[0].upper()} and ends with {password[-1].upper()}"

print(password_hint)
