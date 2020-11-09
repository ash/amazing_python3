import datetime

count = 0
for year in range(1900, 2101):
    date = datetime.datetime(year, 12, 25)
    if date.weekday() == 6:
        count += 1
print('There are', count, 'Sundays')
