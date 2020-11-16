# Method 4.
# A tricky formula :-)

def sign(x):
    return (x > 0) - (x < 0)

print(sign(42))  # 1
print(sign(0))   # 0
print(sign(-42)) # -1
