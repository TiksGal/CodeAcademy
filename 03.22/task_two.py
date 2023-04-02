from dotenv import dotenv_values

config = dotenv_values(".env")


def diff_largest_smallest():
    num = config["NUM"]
    digits = [int(d) for d in str(num)]  # Convert the number to a list of digits
    digits.sort()  # Sort the digits in ascending order
    smallest = int(
        "".join(map(str, digits))
    )  # Convert the sorted digits back to a number
    digits.reverse()  # Reverse the order of the digits
    largest = int(
        "".join(map(str, digits))
    )  # Convert the reversed digits back to a number
    return (
        largest - smallest
    )  # Return the difference between the largest and smallest numbers


diff = diff_largest_smallest()
print(diff)
