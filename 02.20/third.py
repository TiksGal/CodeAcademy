# Create a mini python program which would take two numbers as
# an input and would return their sum, subtraction, division, multiplication.
# Handle all possible errors that may occur.

from typing import Union


def calculator() -> Union[list[float, float, float, float], None]:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
    except ValueError:
        print("Error: please enter a valid number.")
        return None
    except ZeroDivisionError:
        print("Error: division by zero.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    else:
        return [add, sub, mul, div]

print(calculator())