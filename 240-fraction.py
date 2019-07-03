# Using fractions (not floating-
# point numbers)

from fractions import Fraction

a = Fraction(3, 5) # 3/5
print(a)

# You can use arithmetics with
# fractions:

b = Fraction(1, 5) # 1/5
c = a + b # 4/5
print(c) # indeed, 4/5