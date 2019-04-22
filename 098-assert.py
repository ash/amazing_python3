# Using assert to break
# the program if your
# data are wrong

def divide(x, y):
    assert y != 0
    return x / y

a = divide(100, 10) # OK
print(a)

a = divide(100, 0) # Not OK
print(a) # will not be printed