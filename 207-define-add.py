# Defining a "+" operator for
# your own class

class C:
    def __init__(self, value):
        self.value = value

    # redefine "+"
    def __add__(self, x):
        return self.value + x

obj = C(5)
print(obj + 10) # OK
