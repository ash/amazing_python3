# Integer division without division
m = 112
n = 26

print('Must be:', m // n)

# Using subtraction instead
r = 0
while m >= n:
    m -= n
    r += 1

# Same result as above
print(r)
