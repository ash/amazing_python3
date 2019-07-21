# Currying in Python
# Let's make closures of this.

def a(x):
    def b(y):
        return x + y
    return b # name of function

adder_4 = a(4)
adder_10 = a(10)

print(adder_4(3)) # 4 + 3
print(adder_4(6)) # 4 + 6

print(adder_10(3)) # 10 + 3
print(adder_10(6)) # 10 + 6