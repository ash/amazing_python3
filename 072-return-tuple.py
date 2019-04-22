# What happens when you return
# two values from a function

def f():
    return 10, 11

a, b = f()
print(a)
print(b)

# What if you only take one
c = f()
print(c)
