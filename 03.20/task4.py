from abc import ABC, abstractmethod
import math

class Calculator(ABC):
    @abstractmethod
    def add(self, number_1: float, number_2: float) -> float:
        pass

    @abstractmethod
    def subtract(self, numebr_1: float, number_2: float) -> float:
        pass

    @abstractmethod
    def multiply(self, number_1: float, number_2: float) -> float:
        pass

    @abstractmethod
    def divide(self, number_1: float, number_2: float) -> float:
        pass

    def square(self, number_1: float) -> float:
        return self.multiply(number_1,number_1)

class ArithmeticCalculator(Calculator):
    def add(self, number_1: float, number_2: float) -> float:
        return number_1+ number_2

    def subtract(self, number_1: float, number_2: float) -> float:
        return number_1 - number_2

    def multiply(self, number_1: float, number_2: float) -> float:
        return number_1 * number_2

    def divide(self, number_1: float, number_2: float) -> float:
        return number_1 / number_2

    def power(self, number_1: float, number_2: float) -> float:
        return number_1 ** number_2

class GeometryCalculator(ArithmeticCalculator):
    def area_of_square(self, side: float) -> float:
        return self.square(side)

    def area_of_rectangle(self, length: float, width: float) -> float:
        return self.multiply(length, width)

    def area_of_triangle(self, base: float, height: float) -> float:
        return self.divide(self.multiply(base, height), 2)

    def area_of_circle(self, radius: float) -> float:
        return self.multiply(math.pi, self.power(radius, 2))


arithmetic_calculator = ArithmeticCalculator()
geometry_calculator = GeometryCalculator()

print(arithmetic_calculator.add(2, 3))     # Output: 5.0
print(geometry_calculator.area_of_square(4))    # Output: 16.0
print(geometry_calculator.area_of_rectangle(4, 6))  # Output: 24.0
print(geometry_calculator.area_of_triangle(3, 4))   # Output: 6.0
print(geometry_calculator.area_of_circle(5))        # Output: 78.53981633974483
print(geometry_calculator.divide(2, 2))

    
    