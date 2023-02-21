def divide(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero!")
        result = None
    except Exception as e:
        print(f"Error: {e}")
        result = None
    else:
        print("Division succeeded!")
    finally:
        print(result)

divide(5, 1)