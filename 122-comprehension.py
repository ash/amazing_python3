# Demonstrating list comprehensions

def f(x):
    return x ** 2

# Create a list of squares
data = [ f(x) for x in range(10) ]

# Print the content of "data"
for x in range(10):
    print(f'{x}² = {data[x]}')
