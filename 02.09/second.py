# Allow user to enter 10 integers, and then print the sum and
# average of those entered numbers.

numbers = []

for i in range(10):
    num = int(input("Enter integer number %d: " % (i + 1)))
    numbers.append(num)

sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print("Sum of numbers: ", sum_of_numbers)
print("Average: ", average)