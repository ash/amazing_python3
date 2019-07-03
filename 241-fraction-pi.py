# Fractions vs decimal vs pi
# (not very serious)

import fractions
import math
import decimal

pi = fractions.Fraction.from_decimal(
    decimal.Decimal(math.pi)
)

print(pi) # many digits

# less digits:
print(pi.limit_denominator(100))
print(pi.limit_denominator(10))
