# find next 3 Fridays that happend to be Friday the 13th 

from datetime import datetime, timedelta

def next_friday_13th(start_date: datetime, count: int) -> list:
    friday_13th_dates = []
    while len(friday_13th_dates) < count:
        start_date += timedelta(days=1)
        if start_date.day == 13 and start_date.weekday() == 4:
            friday_13th_dates.append(start_date)
    return friday_13th_dates


start_date = datetime.now()
friday_13th_dates = next_friday_13th(start_date, 10)
print("Next 3 Fridays that are Friday the 13th:")
for date in friday_13th_dates:
    print(date.strftime("%Y-%m-%d"))
