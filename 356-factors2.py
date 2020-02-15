# List all the factors of 
# a given integer number.
# Method 2.

N = 126

factors = [
    n for n in
        range(1, N//2 + 1)
        if N % n == 0
]

print(factors)