# Computing the value of pi
# using the Leibnitz series:
# π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

sign = 1
pi = 0
for i in range(1, 10_000_000, 2):
    pi += sign * 1/i
    sign *= -1

print(4 * pi)
