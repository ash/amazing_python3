# Accessing built-in functions
# when you (or a library) redefines 
# some of the common names

import builtins

# This clashes with the built-in sum
def sum(items):
    return 42

data = [1, 3, 5, 7]

print(sum(data)) # 42 (!!!)

# Accessing the built-in sum:
print(builtins.sum(data)) # 16
