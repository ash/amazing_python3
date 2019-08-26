# Possible implementation of the
# __add__ method for classes
# (but this example is a bad practice,
# it is only for fun and understanding).

class C:
    def __init__(self, v):
        self.value = v
    def __add__(self, other):
        return self.value - other.value
        # notice "-" for the __add__

a = C(10)
b = C(20)
print(a + b) # -10, not 30