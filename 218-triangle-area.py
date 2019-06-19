# Compute the area of a triangle
# (having its three sides)

import math

a = float(input('Side 1: '))
b = float(input('Side 2: '))
c = float(input('Side 3: '))

s = (a + b + c) / 2
area = math.sqrt(
    s * (s - a) * (s - b) * (s - c)
)
print(f'The area is {area}')
