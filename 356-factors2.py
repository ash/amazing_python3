# List all the factors of 
# a given integer number.
# Method 2.

from math import sqrt

N = 126

factors = [
    n for n in
        range(1, int(sqrt(N)))
        if N % n == 0
]

print(factors)