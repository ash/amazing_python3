# Using precise decimal numbers

from decimal import Decimal

# Compare:
print(0.1 + 0.2 - 0.3) # Is it 0?

print(Decimal('0.1') + 
    Decimal('0.2') -
    Decimal('0.3')) # Now 0
