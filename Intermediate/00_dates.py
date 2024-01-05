# Dates

#import datetime
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta




now = datetime.now()
timestamp = datetime.timestamp(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(now)


current_time = time(now.hour, now.minute, now.second)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date(now.year, now.month, now.day)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.today)


year = datetime(2022, 1, 1)
diff = now -year
print(diff)

start_timedelta = timedelta(200, 100,100,weeks=10)
end_timedelta = timedelta(200, 100, 100, weeks=20)
print(end_timedelta - start_timedelta)
