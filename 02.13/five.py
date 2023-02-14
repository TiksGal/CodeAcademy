# Write a program that checks if given number is a perfect square.
import math


num = int(input("Enter a number: "))
print(f"{num} is a perfect square.") if int(math.sqrt(num)) ** 2 == num else print(f"{num} is not a perfect square.")