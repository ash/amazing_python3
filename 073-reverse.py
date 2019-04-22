# reversed() vs .reverse()

a = ['alpha', 'beta', 'gamma']
b = reversed(a)
print(a) # original a

c = a.reverse()
print(a) # original a is broken
