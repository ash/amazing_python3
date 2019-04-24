# Measuring the time of
# a slow piece of code

import time

def slow_code():
    time.sleep(2)

t0 = time.time() # start time
slow_code()
t = time.time() # end time

print(t - t0)
