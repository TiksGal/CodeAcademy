from datetime import datetime, timedelta

def last_day_of_month(year: int, month: int) -> str:
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    first_day_next_month = datetime(next_year, next_month, 1)
    last_day = first_day_next_month - timedelta(days=1)
    return last_day.strftime("%A, %B %d, %Y")


year = 2023
month = 12
print(f"Last day of {year}-{month:02d}: {last_day_of_month(year, month)}")
