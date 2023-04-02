numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original list of integers:", numbers)
print("Even numbers from the list:", even_numbers)
print("Odd numbers from the list:", odd_numbers)
