from typing import Union

# def diveder(number: Union[float, int]) -> Union[float, int]:
#     return number / 2 if isinstance(number, float) else number // 2


# try:
#     my_diveder_number =diveder(2)
#     print(my_diveder_number)
# except:
#     print("We are fucked up!")

# Try:
#     my_diveder_number - diveder("a")
#     print(my_diveder_number)

# def divide_two_numbers(dividend: int, divisor: int) -> None:
#     try:
#         quotient = dividend / divisor
#         print(f'Result = {quotient}')
#     except ZeroDivisionError:
#         print('Divisor is zero; Division is impossible')
        
# divide_two_numbers(6, 0)


# def physic_is_fun(temp: float, pressure: float, time: int, weight: float ) ->None:
#     pass

# physic_is_fun(temp_c = 38.4,pressure_mbar = 500.3,time_utc =  45,weight_kg =  700)
       
# def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('Cannot divide by zero')
#     else:
#         print(f'Output = {output}') 
        
# from typing import Optional, Union

# def divider(number: Optional[Union[int, float]] = None) -> Optional[Union[int, float]]:
#     if number is None:
#         return None
#     try:
#         if isinstance(number, float):
#             return number / 2
#         elif isinstance(number, int):
#             return number // 2
#         else:
#             raise TypeError("Error: Number must be a float, an int, or None")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
#     except TypeError as e:
#         print(e)
