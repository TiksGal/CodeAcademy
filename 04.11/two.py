# Write a function that calculates difference in days between two datetimes.
from datetime import datetime

def days_difference(datetime1: int, datetime2: int) -> int:
    delta = abs(datetime2 - datetime1)
    days_difference = delta.days
    return days_difference


datetime1 = datetime(2023, 4, 11)
datetime2 = datetime(2023, 4, 18)
x = days_difference(datetime1, datetime2)
print(f"Difference in days: {x}")
