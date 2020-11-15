# Creating and using a simple
# generator expression

# Count the sum of squares 
# from 1^2 to 10^2

s = sum(n * n for n in range(1, 11))
print(s)

# Prints 385, which is 
# 1 + 4 + 9 + 16 + 25 + 36 + 
# 49 + 64 + 81 + 100.

# Generator expression used:
# n * n for n in range(1, 11)
