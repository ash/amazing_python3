# What if you need to compare an object
# with an integer?

class C:
    def __init__(self, i):
        self.value = i
    def __eq__(self, i):
        return self.value == i

obj = C(42)

b = 42
print(obj == 42) # ok now
print(obj == 44) # ok now