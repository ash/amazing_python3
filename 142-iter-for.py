# Using custom iterators with a "for" loop

class Count:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def __iter__(self):
        self.n = self.min - 1
        return self
    def __next__(self):
        if self.n == self.max:
            raise StopIteration
        self.n += 1
        return self.n

c = Count(10, 15)
for i in c: # using our iterator
    print(i)