# What is the difference between
# the two given dates?

import datetime

date_from = datetime.date(2019, 1, 1)
date_to = datetime.date(2019, 12, 31)

diff = date_to - date_from
print(diff)

days = diff.days # diff in days
print(days)
