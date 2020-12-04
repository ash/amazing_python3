# Consider these two functions:
def f(a, b):
    return a + b

def g(a, /, b):
    return a + b

# Call with positional or named params
f(10, 20) # ok
f(a=10, b=20) # ok
f(10, b=20) # ok

g(10, 20) # ok
# g(a=10, b=20) # NOT OK
g(10, b=20) # ok