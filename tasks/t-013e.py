# An option for Python 2.7.
# The "cmp" function is
# not available in Python 3.

def sign(x):
    return cmp(x, 0)

print(sign(42))  # 1
print(sign(0))   # 0
print(sign(-42)) # -1
