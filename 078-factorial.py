# A possible implementation
# of a non-recursive factorial
# calculation for positive ints

def factorial(n):
    f = 1
    for m in range(1, n + 1):
        f *= m
    return f

print(factorial(5)) # should be 120
