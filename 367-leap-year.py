# Determine if the given year
# is leap

import calendar

for year in range(2000, 2030):
    if calendar.isleap(year):
        print(year)
