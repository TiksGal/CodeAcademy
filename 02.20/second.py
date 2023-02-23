def divide(a: int, b: int) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: division by zero!")
        result = None
    except Exception as e:
        print(f"Error: {e}")
        result = None
    finally:
        print(result)

divide(10, 0)



