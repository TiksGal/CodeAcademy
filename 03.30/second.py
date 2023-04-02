class TimeUtils:
    @staticmethod
    def seconds_calculator(time_str: str) -> str:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return f"Seconds counted: {(hours * 3600) + (minutes * 60) + seconds}"


print(TimeUtils.seconds_calculator("19:48:22"))