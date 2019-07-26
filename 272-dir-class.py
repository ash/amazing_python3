# Applyting "dir()" to a class
# and class instance:

class C:
    def method():
        print('Hi')

obj = C()

print(dir(C))
print(dir(obj)) # the same output