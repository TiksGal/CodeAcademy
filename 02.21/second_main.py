import string_module
import numbers_module
import lists_module

string = input("Enter your string: ")
print(f"Reverse of '{string}': {string_module.reverse_string(string)}")

lst_one = [1, 2, 3, 4, 5, 5]
lst_two = [3, 4, 5, 6, 7]

print(f"Removing duplicates from {lst_one}: {lists_module.remove_duplicates(lst_one)}")
print(f"Common elements between {lst_one} and {lst_two}: {lists_module.find_common_elements(lst_one, lst_two)}")

number = int(input("Enter your number: "))

if numbers_module.is_even(number):
    print(f"{number} is even! ")
else:
    print(f"{number} isn't even!")