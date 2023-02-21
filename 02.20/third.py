from typing import Union, Tuple


def calculator() -> Union[Tuple[float, float, float, float], None]:
    try:
        a: float = float(input("Enter the first number: "))
        b: float = float(input("Enter the second number: "))
        add: float = a + b
        sub: float = a - b
        mul: float = a * b
        div: float = a / b
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
        print(f"Sum: {add}")
        print(f"Subtraction: {sub}")
        print(f"Multiplication: {mul}")
        print(f"Division: {div}")
        return add, sub, mul, div

print(calculator())