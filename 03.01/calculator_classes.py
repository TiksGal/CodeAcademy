import logging
import math
from typing import Union

class Calculator:
    def __init__(self, operation: str, number1: Union[int, float], number2: Union[int, float]) -> None:
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.logger: logging.Logger = logging.getLogger(__name__)
        
    def get_addition(self, number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
        return  number1 + number2

    def get_subtract(self, number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
        return number1 - number2

# Define an AdvancedCalculator class that inherits from the Calculator class and adds multiply and divide methods
class Advanced(Calculator):
    def __init__(self, name: str) -> None:
        super.__init__(self.name)
    
    def get_multiply(self, number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
        return number1 * number2

    def get_divide(self, number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
        # Handle the case where the second number is 0
        if number2 == 0:
            logging.error("Error: Division by zero")
            raise ValueError("Division by zero is not allowed")
        return number1 / number2
    
    def square(self, number: Union[int, float]) -> Union[int, float]:
        return number ** 2

    def cube(self, number: Union[int, float]) -> Union[int, float]:
        return number ** 3

    def power(self, number: Union[int, float], power: Union[int, float]) -> Union[int, float]:
        return number ** power

    def sqrt(self, number: Union[int, float]) -> Union[int, float]:
        return number ** 0.5

    def cbrt(self, number: Union[int, float]) -> Union[int, float]:
        return number ** (1 / 3)

# Define a ScientificCalculator class that inherits from the AdvancedCalculator class and adds additional math functions
class Trigonometry(Calculator):
    def __init__(self, name: str):
        super().__init__(name)

    def sin(self, angle: Union[int, float]) -> Union[int, float]:
        return math.sin(angle)

    def cos(self, angle: Union[int, float]) -> Union[int, float]:
        return math.cos(angle)

    def tan(self, angle: Union[int, float]) -> Union[int, float]:
        return math.tan(angle)
    
