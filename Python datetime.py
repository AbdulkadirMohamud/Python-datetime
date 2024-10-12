from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month,  year, hour ,)
print('timestamp', timestamp) 
priny(f'{day}/{month}/{year}, {hour}:{minute}:{second}')

# Formatting Date Output Using strftime 
from datetime import datetime
new_year = datetime (2020, 1, 1 )
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')

# string date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

