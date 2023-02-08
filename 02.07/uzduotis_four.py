# num_one = float(input("Enter the first number: "))
# num_two = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")

# if operation == '+':
#     result = num_one + num_two
# elif operation == '-':
#     result = num_one - num_two
# elif operation == '*':
#     result = num_one * num_two
# elif operation == '/':
#     result = num_one / num_two
# else:
#     print("Invalid operation. Please try again.")


# print("Result:", result)

input_str = input("Enter the first number, the second number and the operation (+, -, *, /), separated by a space: ")
input_list = input_str.split()

num_one = float(input_list[0])
num_two = float(input_list[1])
operation = input_list[2]
operation_list = ["+", "-", "/", "*"]

if operation == '+':
    result = num_one + num_two
elif operation == '-':
    result = num_one - num_two
elif operation == '*':
    result = num_one * num_two
elif operation == '/':
    result = num_one / num_two

print("Result:", result)
