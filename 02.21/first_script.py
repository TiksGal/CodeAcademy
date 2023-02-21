# Prompt the user for the operation to perform
print("Enter an operation (+, -, *, /):")
operation = input()

# Prompt the user for the two numbers to operate on
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Invalid input")
    exit(1)

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero")
        exit(1)
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Error: Invalid operation")
    exit(1)
