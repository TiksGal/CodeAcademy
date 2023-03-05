import logging
from typing import Union
from calculator_module import Calculator, ScientificCalculator

logging.basicConfig(filename="calculator.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def show_operations(calc: Union[Calculator, ScientificCalculator]) -> None:
    print(f"Available operations for {type(calc).__name__}: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    if isinstance(calc, ScientificCalculator):
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")

def get_input(prompt: str, input_type: type = float) -> Union[int, float]:
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input, please try again.")

def perform_operation(calc: Union[Calculator, ScientificCalculator], operation: int) -> None:
    if operation < 1 or (operation > 4 and not isinstance(calc, ScientificCalculator)) or (operation > 9 and isinstance(calc, ScientificCalculator)):
        print("Invalid operation selected, please try again.")
        return

    operations = {
    1: calc.add,
    2: calc.subtract,
    3: calc.multiply,
    4: calc.divide,
    5: calc.power if isinstance(calc, ScientificCalculator) else None,
    6: calc.sqrt if isinstance(calc, ScientificCalculator) else None,
    7: calc.sin if isinstance(calc, ScientificCalculator) else None,
    8: calc.cos if isinstance(calc, ScientificCalculator) else None,
    9: calc.tan if isinstance(calc, ScientificCalculator) else None
    }

    operation_func = operations.get(operation)
    if operation_func:
        try:
            result = operation_func()
            print(f"Result: {result}")
        except ValueError as e:
            logging.error(str(e))
            print(str(e))
    else:
        print("Invalid operation selected.")

def main() -> None:
    while True:
        print("Select a calculator:")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Quit")
        calc_type = get_input("Enter calculator type: ", int)
        try:
            choice = int(calc_type)
            if choice == 1:
                num1 = get_input("Enter first number: ")
                num2 = get_input("Enter second number: ")
                calc = Calculator(num1, num2)
            elif choice == 2:
                num1 = get_input("Enter first number: ")
                num2 = get_input("Enter second number: ")
                calc = ScientificCalculator(num1, num2)
            elif choice == 3:
                print("Goodbye!")
                return
            else:
                print("Invalid calculator type selected, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

        show_operations(calc)

        operation = get_input("Enter operation number: ")
        perform_operation(calc, operation)

if __name__ == "__main__":
    main()
