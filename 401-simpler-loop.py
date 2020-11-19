# This is the solution of a previous
# task to find min and max without
# using built-in functions.
data = [3, 4, 6, 8, -1, -4, 0, 7]

# Let us simplify it.
max = min = data[0]
# We do not actually use n here:
for x in data:
    if x < min:
        min = x
    # Also, else will help here:
    elif x > max:
        max = x

print('Minimum =', min)
print('Maximum =', max)
