# Using __repr__ for better
# object printing

class C:
    def __init__(self, value):
        self.v = value
    def __repr__(self):
        return "My value is " + \
                str(self.v)

c = C(42)
print(c)

d = C(43)
print(d)
