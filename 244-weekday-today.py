# What is the day (week day) today?

import datetime

t = datetime.datetime.today()

d = t.strftime('%A')

print(f'Today is {d}')
