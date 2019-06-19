# Compute the area of a triangle
# (having its three sides)
# Let's transform the code
import math

a = []
for i in range(3):
    a.append(float(input(f'Side {i+1}: ')))

s = sum(a) / 2
area = math.sqrt(
    s * math.prod( # Python 3.8
        map(
            lambda x: s - x, a
        )
    )
)
print(f'The area is {area}')
