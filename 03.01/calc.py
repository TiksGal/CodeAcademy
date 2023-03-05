import logging

# Create a logger object
logging.basicConfig(filename="calc.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
logger: logging.Logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)
    
    def add(self, a: float, b: float) -> float:
        """
        Returns the sum of two numbers.
        """
        result: float = a + b
        self.logger.info(f"Addition: {a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Returns the difference between two numbers.
        """
        result: float = a - b
        self.logger.info(f"Subtraction: {a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Returns the product of two numbers.
        """
        result: float = a * b
        self.logger.info(f"Multiplication: {a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Returns the result of dividing one number by another.
        Raises a ValueError if the second number is zero.
        """
        try:
            result: float = a / b
        except ZeroDivisionError:
            self.logger.error("You cant divede by zero, calm down!")
            raise ValueError("Cannot divide by zero")
        self.logger.info(f"Division: {a} / {b} = {result}")
        return result

if __name__ == "__main__":
    calculator: Calculator = Calculator()
    logging.info("Program started")
    
    # Loop until the user quits
    while True:
        # Get the user's input
        operation: str = input("Enter operation (+, -, *, /) or q to quit: ")
        
        # Quit the program if the user enters 'q'
        if operation == "q":
            logging.info("Programme ends")
            break
        
        # Check if the operation is valid
        if operation not in ["+", "-", "*", "/"]:
            logger.error(f"Invalid operation entered: {operation}")
            print("Invalid operation.")
            continue
        
        try:
            # Get the user's input
            num1: float = float(input("Enter first number: "))
            num2: float = float(input("Enter second number: "))
        except ValueError:
            logger.error("Invalid input entered")
            print("Invalid input.")
            continue
        
        # Perform the selected operation and log the result
        if operation == "+":
            result: float = calculator.add(num1, num2)
        elif operation == "-":
            result = calculator.subtract(num1, num2)
        elif operation == "*":
            result = calculator.multiply(num1, num2)
        else:
            try:
                result = calculator.divide(num1, num2)
            except ValueError:
                logger.error("Cannot divide by zero")
                print("Cannot divide by zero.")
                continue
        
        # Print the result to the user
        print(f"Result: {result}")
