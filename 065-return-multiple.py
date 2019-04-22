# Solving a square equation
# and returning multiple values.
# ax² + bx + c = 0
import math
def solve(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    return x1, x2

x1, x2 = solve(1, 3, -4)
print(x1)
print(x2)
