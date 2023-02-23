# Create at least 5 different functions and try
# to handle at least 5 built-in Python Exceptions.

# from typing import Union, Optional

# def divide(x: Union[int,float], y: Union[int,float]) -> Optional[float]:
#     try:
#         return x / y
#     except TypeError:
#         print("Error: Both inputs must be numbers")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
#     except ValueError:
#         print("Error: Invalid input")
# def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('Cannot divide by zero')
#     else:
#         print(f'Output = {output}')
# divide(10, 2)

# def get_element(lst: list, index: int) -> any:
#     try:
#         return lst[index]
#     except IndexError:
#         print("Error: index out of range")

# from typing import Optional
# def greet_someone(name: str= "Marius") -> Optional[str]:
#     try:
#         return f"Hello {name}" 
#     except Exception as e:
#         sys.exit(f"Error : {e}")
# print(greet_someone())
# def multiply_numbers(number_one: int | float, number_two: int | float ) -> Optional[int | float]:
#     try:
#         return number_one * number_two 
#     except TypeError:
#         print("Input is not a number")
# multiply_numbers(4, 5)
# def divide_numbers(number_one: int | float, number_two: int | float) -> Optional[float]:
#     try:
#         return number_one / number_two
#     except ZeroDivisionError:
#         print("Divison by 0 is not available")
# divide_numbers(5,0)
# def verify_user(username: str) -> Optional[bool]:
#     VALID_USERNAME = "Antanas" 
#     try:
#         if username == valid_username:
#             return True 
#         return False 
#     except NameError:
#         print("Name is not defined")
# print(verify_user("Antanas"))
# def uppercase_user_input() -> Optional[str]:
#     try:
#         user_input = input("Enter anything: ")
#         return user_input.upper()
#     except KeyboardInterrupt:
#         print("\n Program stopped of keyboard interruption")
# print(uppercase_user_input())

# from typing import Optional
# def first_func(number: int) -> Optional[int]:
#     try:
#         number = int(number)
#         return number * number
#     except ValueError:
#         print("Value is not integer")
# print(first_func(number = 9))
# --------------------------------
# def second_func(number_one: int, number_two: int) -> None:
#     try: 
#         result = number_one / number_two 
#         print(result)
#     except TypeError:
#         print("type not integer")
# second_func(number_one=10, number_two=5)
#---------------------------------
# def third_func(number: int) -> None:
#     try:
#         number = 20 / number 
#         print(number)
#     except ZeroDivisionError:
#         print("do not divide by zero")
# third_func(number=0)
#-----------------------------------
# def fourth_func(name: str = "Marius") ->None:
#     try:
#         name[-1] = "s" 
#         print(name)
#     except Exception as e:
#         print(f"Exception {e}")
# fourth_func(name="H")
#------------------------------------
# def fifth_func(name: str, surname: str) -> None:
#     try: 
#         full_name = name + surname 
#         print("Hello, world")
#     except Exception as e:
#         print(f"That was scary error - {e}")
#     else:
#         print(full_name)
# fifth_func(name = "Marius", surname= " Šertvytis")
