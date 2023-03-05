import logging
from typing import Union

# Define a base calculator class with a single method for performing calculations
class Calculator:
    def calculate(self, num1: float, num2: float) -> float:
        pass

# Define a simple calculator class that inherits from the base calculator class
class SimpleCalculator(Calculator):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 + num2

# Define an advanced calculator class that inherits from the base calculator class
class AdvancedCalculator(Calculator):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 ** num2

# Define a scientific calculator class that inherits from the base calculator class
class ScientificCalculator(Calculator):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 * num2 / 2

# Define a function to get the user's choice of calculator
def get_calculator_choice() -> str:
    print("Please choose a calculator:")
    print("1. Simple calculator")
    print("2. Advanced calculator")
    print("3. Scientific calculator")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        return "simple"
    elif choice == "2":
        return "advanced"
    elif choice == "3":
        return "scientific"
    else:
        print("Invalid choice. Please try again.")
        return get_calculator_choice()

# Main program loop
while True:
    calc_choice = get_calculator_choice()
    
    # Create an instance of the chosen calculator class
    if calc_choice == "simple":
        calculator = SimpleCalculator()
    elif calc_choice == "advanced":
        calculator = AdvancedCalculator()
    elif calc_choice == "scientific":
        calculator = ScientificCalculator()
    
    # Get user input for numbers to calculate
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    # Perform the calculation using the chosen calculator instance
    result = calculator.calculate(num1, num2)
    
    # Print the result
    print(f"The result of the {calc_choice} calculator operation is: {result}")
    
    # Ask the user if they want to perform another calculation
    again = input("Would you like to perform another calculation? (y/n): ")
    if again.lower() == 'n':
        print("Exiting calculator. Goodbye!")
        break
    else:
        continue
