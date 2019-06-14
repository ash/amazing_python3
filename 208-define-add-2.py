# Defining a "+" operator for
# your own class

class C:
    def __init__(self, value):
        self.value = value

    def __add__(self, x):
        return self.value + x

    def __radd__(self, x):
        return self.value + x

obj = C(5)
print(obj + 10) # OK, used __add__

# What if you want to do it this way:
print(10 + obj) # OK, used __radd__