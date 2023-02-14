# a = 2
# b = 5


# def addtion(number1, number2):
#     sum = number1 + number2
#     return sum

# c = addtion(a, b)

# print(c)

# def print_smth():
#     print('Hello world!')
    
# print_smth()

# a = print_smth()

# print(a)


# my_list = [1, 2, 3]
# my_list.append(4)

# print(my_list)

# my_list = [1, 2, 3]
# my_list = my_list.append(4)

# print(my_list)

# import random

# def get_random_number():
#    """lllllll"""
#    random.randint(0, 100)
    
# print(get_random_number())
# print(get_random_number.__doc__)
# print(get_random_number())

def even_odd(num):

    '''
    Returns "even" if num is even, and "odd" if num is odd.    
    Parameters:
        num (int): Any integer    Returns:
        type (string): "even" if num is even; "odd" if num is odd
    '''

    if num % 2 == 0:  # Checks if num/2 has a remainder of 0
        return "even"  # If it has a remainder of 0, return "even"
    else:
        return "odd"  # If it doesn't, return "odd"
    
number = 1

if even_odd(number) == "even":
    print(f"My number: {number} is even!")
else:
    print(f"My number: {number} is not even.")
    
from typing import Tuple, Optional, Union

def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
   return 'You called the_func with ' + str(x) + str(y) + str(z)

print(the_func(1, 4, "Labas"))
    
    

    