class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def calculate(self):
        operation = input("Enter an operation (+, -, *, /): ")
        if operation not in self.operations:
            print(f"Invalid operation '{operation}'")
            return

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = self.operations[operation](a, b)
            print(f"{a} {operation} {b} = {result}")
        except ValueError:
            print("Invalid input values")
        except ZeroDivisionError:
            print("Cannot divide by zero")


calculator = Calculator()

# Call the calculate method to get input values from the user and perform the operation
calculator.calculate()