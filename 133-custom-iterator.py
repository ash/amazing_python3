# Creating custom iterators
class C:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        self.n += 1
        return self.n

c = C()
i = iter(c) # get an iterator

for _ in range(5):
    # use the iterator
    print(next(i))