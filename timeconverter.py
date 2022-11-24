from datetime import datetime

def date_time(text: str) -> str:
    text = datetime.strptime(text, "%d.%m.%Y %H:%M")
    minute = "minute" if text.minute == 1 else "minutes"
    hour = "hour" if text.hour == 1 else "hours"
    return text.strftime(f"%#d %B %Y year %#H {hour} %#M {minute}")

print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
