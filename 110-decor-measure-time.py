# Using decorator to measure time

import time

def time_measure(f): # f = function
    t0 = time.time()
    f() # call that function
    t = time.time()
    return t - t0 # duration

@time_measure # decorator
def slow_code():
    time.sleep(2)

print(slow_code) # no () 