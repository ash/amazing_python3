# Method 1. Compare with "if".

def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

print(sign(42))  # 1
print(sign(0))   # 0
print(sign(-42)) # -1
