# Using yield

def f():
    for i in range(100):
        yield i # not "return"

g = f() # generator object

print(next(g)) # not g()
print(next(g))
print(next(g))
print(next(g))
