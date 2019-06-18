# How many digits are there in
# a number

import math

n = 123456

# method 1
print(len(str(n)))
# convert a number to a string
# and take its length

# method 2 (pure mathematical)
print(1 + math.floor(math.log10(n)))
# log - base 10