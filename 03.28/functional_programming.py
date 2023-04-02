string = "laba diena"
char = "l"

check_start = lambda string, char: string.startswith(char)

print(check_start(string, char))

char = "a"
print(check_start(string, char))
# 2
add_15 = lambda num: num + 15

multiply = lambda x, y: x * y

print(add_15(2))
print(multiply(12, 13))
# 3
first = [1, 2, 3, 4, 5]
second = [10, 11, 12, 13, 14]

result = list(map(lambda x, y: x + y, first, second))

print(result)
# 4
numbers = [11, 12, 13, 14, 15]

sqr = list(map(lambda x: x**2, numbers))
cube = list(map(lambda x: x**3, numbers))

print(sqr)
print(cube)
# 5
import datetime

now = datetime.datetime.now()

extract_time = lambda date_time: date_time.time()
extract_year = lambda date_time: date_time.year
extract_month = lambda date_time: date_time.month
extract_day = lambda date_time: date_time.day


print(now)
print(extract_year(now))
print(extract_month(now))
print(extract_day(now))
print(extract_time(now))

# 1 sorted function
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(original_list, key=lambda x: x[1])

print(f"Original list of tuples: {original_list}")
print(f"Sorting the list of tuples: {sorted_list}")
# 2
original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(original_list, key=lambda x: x['color'])

print("Original list of dictionaries:", original_list)
print("Sorting the list of dictionaries:", sorted_list)
# 3
original_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

sorted_matrix = sorted(original_matrix, key=lambda x: sum(x))

print("Original Matrix:")
for row in original_matrix:
    print(row)
print("\nSort the said matrix in ascending order according to the sum of its rows")
for row in sorted_matrix:
    print(row)

# Map function 1
numbers = [1, 2, 3, 4, 5]

triple = list(map(lambda x: x*3, numbers))

print(triple)
# 2
numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x**2, numbers))

print(square)
# 3
list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]
list3 = [100, 200, 300, 400, 500]

summed = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print(summed)
# 4
list1 = [1, 2, 3, 4, 5]
list2 = [11, 22, 33, 44, 55]

summed = list(map(lambda x, y: x + y, list1, list2))
difference = list(map(lambda x, y: x - y, list1, list2))

print(summed)
print(difference)
# 5
list_of_numbers = [1, 2, 3, 4, 5]
tuple_of_numbers = (6, 7, 8, 9, 10)

str_list = list(map(str, list_of_numbers))
str_tuple = list(map(str, tuple_of_numbers))

print(str_list)
print(str_tuple)