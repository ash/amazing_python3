# Comparing two "equal" floating-
# point numbers

n1 = 0.1 + 0.2 - 0.3 # 0
n2 = 0

print(n1 == n2) # is False, as n1
# cannot be presented as an exact "0"
# when working with floating-point
# arithmetics

print(abs(n1 - n2) < 1E-15) # True
