# addition of squares
def sum_squares(numbers):
    return sum([num**2 for num in numbers])
"""Function squares all list elements and then sum all."""
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_squares(my_numbers))

def get_average(numbers):
    """Function sum all list number and then get average."""
    return sum(numbers) / len(numbers)

my_numbers
print(get_average(my_numbers))

def capitalize_first(string):
    return string[0].upper() + string[1:]
"""Function takes string and return first letter capitalize"""
my_string = "lietuva"
print(capitalize_first(my_string))

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
"""Function compare and find common elements in two lists"""
list1 = ["Vilnius", "Kaunas", "Klaipėda", "Alytus"]
list2 = ["Vilnius", "Anykščiai", "Varėna", "Klaipėda"]

print(find_common_elements(list1, list2))

def print_multiplication_table(number):
    for i in range(1, 10):
        result = number * i
        print(f"{number} x {i} = {result}")


user_number = int(input("Enter a number: "))
print_multiplication_table(user_number)

