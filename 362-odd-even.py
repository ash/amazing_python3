# Is the number odd?
def is_odd(n):
    return n % 2

# Check the first 10 numbers
for x in range(10):
    print(x, "is",
    "odd" if is_odd(x)
    else "even")
