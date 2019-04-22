# Solving a square equation
# and returning multiple values.
# ax² + bx + c = 0
# with complex roots
# (when d < 0)
import cmath # complex math
def solve(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    return x1, x2

x1, x2 = solve(1, 2, 3)
print(x1)
print(x2)
