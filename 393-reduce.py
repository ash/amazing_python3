# A trivial case that 
# demonstrates the use of "reduce"

import functools

data = 2, 3, 5, 7, 9

def f(x, y):
    return x + y # sum :-)

# Compute the sum of all items
s = functools.reduce(f, data)
# function and data ^^^^^^^^^
print(s) # the sum
