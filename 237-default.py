# Default values are calculated
# only once

import random

def f(x = random.randint(1, 10)):
    print(x)

f()
f() # the same result or not?
f()
f()
