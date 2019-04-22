# Custom object formatting

class C:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

c = C(42)
print(c) # How?? # And now?