# Positional-only parameters.
# Available in Python 3.8+

def s(a, b, /): # notice the /
    print(a + b)

s(10, 20) # OK
# s(a=10, b=20) # error

def s2(a, b, /, c):
    # c can be named
    print(a + b + c)

s2(10, 20, c = 30)