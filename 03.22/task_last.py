import datetime


def next_friday_13th():
    friday_13th_dates = []
    today = datetime.date.today()
    year = today.year

    # Iterate through the next 5 years to find Friday the 13th dates
    for i in range(5):
        year += 1
        for month in range(1, 13):
            # Create a date object for the 13th of the month and year
            date = datetime.date(year, month, 13)
            # Check if the date falls on a Friday (weekday 4)
            if date.weekday() == 4:
                # If it does, add it to the list of Friday the 13th dates
                friday_13th_dates.append(date.strftime("%Y-%m-%d"))
                # Break out of the inner loop, since we only want the first Friday the 13th in each month
                break

    return friday_13th_dates


friday_13th_dates = next_friday_13th()
print(friday_13th_dates)
