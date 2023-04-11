from datetime import datetime, timedelta

def last_friday() -> datetime:
    today = datetime.now()
    days_since_friday = (today.weekday() - 4) % 7
    last_friday_date = today - timedelta(days=days_since_friday)
    # Set the time to 00:00:00
    last_friday_date = last_friday_date.replace(hour=0, minute=0, second=0, microsecond=0)
    return last_friday_date


print("Last Friday:", last_friday())
