# __repr__ vs __str__

class C:
    def __init__(self, value):
        self.v = value
    def __repr__(self):
        return "C(" + str(self.v) + ")"
    def __str__(self):
        return str(self.v)
        
c = C(42)
print(c) # __repr__ or __str__?
# __str__ is called here

d = C(43)
print(repr(d)) # Now only __repr__
