# Sorting lists of objects

class C:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
    def __repr__(self):
        return \
            'C(' + str(self.value) + ')'

data = [
    C(10), C(2), C(42), C(-15)
]

data.sort() # will use __lt__
print(data)