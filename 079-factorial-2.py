# Computing a factorial
# using recursion

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(5))
