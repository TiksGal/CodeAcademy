from typing import Union, Tuple

def calculator() ->Union[Tuple[float, float, float, float], None]:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        
        if b == 0:
            raise ZeroDivisionError("Error: division by zero.")
        
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
        
        return add, sub, mul, div
    
    except ValueError:
        raise ValueError("Error: please enter a valid number.")
        
    except ZeroDivisionError as e:
        raise e
    

try:
    result = calculator()
    print(f"Sum: {result[0]}")
    print(f"Subtraction: {result[1]}")
    print(f"Multiplication: {result[2]}")
    print(f"Division: {result[3]}")
    
except InvalidInputError as e:
    print(e)
    
except ZeroDivisionError as e:
    print(e)
    
except Exception as e:
    print(f"Error: {e}")