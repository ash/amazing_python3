# Using the Monte Carlo method
# to compute the value of pi
# (approximately)

import random
import math

n = 100_000
inside = 0
for _ in range(n):
    x = random.uniform(-1, 1) # between -1, 1
    y = random.uniform(-1, 1)
    d = math.sqrt(x**2 + y**2) # distance
    # from the center of a circle
    if d <= 1:
        inside += 1

pi = 4 * inside / n
print(pi)