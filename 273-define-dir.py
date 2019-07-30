# Defining your own dir() for
# the class

class C:
    def __dir__(self):
        return ['alpha', 'beta']

obj = C()
print(dir(obj))
# will only print 'alpha' and 'beta'