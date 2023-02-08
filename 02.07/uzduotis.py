name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

if age >= 21:
    print(f"Welcome, {name} {surname}. You are allowed to enter the online casino.")
else:
    print(f"Sorry, {name} {surname}. You are not allowed to enter the online casino.")