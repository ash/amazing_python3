# Project Euler Problem 1
# projecteuler.net/problem=1
# Find the sum of all numbers
# below 1000, which are multiple
# of 3 or 5 (i.e., 3, 6, 5, 9, 15, ...)

sum = 0
for n in range(0, 1000):
    if not(n % 3) or not(n % 5):
        sum += n
print(sum)
