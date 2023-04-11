# Write a function that takes a datetime object, which will represent employees starting work day.
# and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off

from datetime import datetime

def holidays_gained(start_date: datetime) -> float:
    # Calculate the difference in days between the start date and today
    days_difference = (datetime.now() - start_date).days
    # Convert the difference in days to months
    months_difference = days_difference / 30.44  # Approximate average days in a month
    # Calculate the total holidays gained
    holidays_gained = months_difference * 1.6
    return holidays_gained


employee_start_date = datetime(2022, 4, 11)
print("Total holidays gained:", holidays_gained(employee_start_date))

