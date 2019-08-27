# From Python 3.5, the "@" operator
# is implemented. It is reserved for
# the so-called matrix multiplication.
# It does not work with built-in data
# types. 

# This is a simple example. More complex
# one will be in one of the following
# posts

class C:
    def __matmul__(self, other):
        return 42 # implementating "@"
a = C()
b = C()
c = a @ b # using __matmul__
print(c) 