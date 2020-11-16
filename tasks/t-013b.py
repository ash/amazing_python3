# Method 2. Subscript a tuple
# (1, -1) with the index 0 or 1 
# that you get from a Boolean
# condition x < 0.
# Also, returns 0 if x is 0.

def sign(x):
    return x and (1, -1)[x < 0]

print(sign(42))  # 1
print(sign(0))   # 0
print(sign(-42)) # -1
