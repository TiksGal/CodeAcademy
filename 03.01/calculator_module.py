import math

class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def add(self) -> float:
        return self.num1 + self.num2
    
    def subtract(self) -> float:
        return self.num1 - self.num2
    
    def multiply(self) -> float:
        return self.num1 * self.num2
    
    def divide(self) -> float:
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

class ScientificCalculator(Calculator):
    def __init__(self, num1, num2) -> None:
        super().__init__(num1, num2)
    
    def power(self) -> float:
        return self.num1 ** self.num2
    
    def sqrt(self) -> float:
        if self.num1 < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(self.num1)
    
    def sin(self) -> float:
        return math.sin(self.num1)
    
    def cos(self) -> float:
        return math.cos(self.num1)
    
    def tan(self) -> float:
        return math.tan(self.num1)

# c = Calculator(5, 3)
# print(c.add())        # Output: 8
# print(c.subtract())   # Output: 2
# print(c.multiply())   # Output: 15
# print(c.divide())     # Output: 1.6666666666666667

# # Scientific Calculator
# s = ScientificCalculator(4, 12)
# print(s.add())
# print(s.power())
# print(s.sqrt())
# print(s.sin())
# print(s.cos())
# print(s.tan())
# print(s.divide())