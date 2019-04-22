# Using yield

def f():
    for i in range(100):
        yield i # not "return"

# Why do you need this assignment?
g1 = f() # generator object
g2 = f() # another generator

print(next(g1)) # value from generator 1
print(next(g2)) # from generator 2
print(next(g1)) # again 1
print(next(g2)) # ...
print(next(g1))
print(next(g2))
