# Create a simple calculus program as a script and as module.

def add(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.
    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Returns the difference between two numbers.

    :param a: The number to subtract from.
    :param b: The number to subtract.
    :return: The difference between a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Returns the product of two numbers.

    :param a: The first number to multiply.
    :param b: The second number to multiply.
    :return: The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    :param a: The numerator.
    :param b: The denominator.
    :return: The quotient of a and b.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
<<<<<<< HEAD
    return a / b
=======
    return a / b
>>>>>>> a995e42f38455a7261ae1764f16dfbca2d57e391
