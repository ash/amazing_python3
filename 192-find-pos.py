data = [
    'alpha', 'beta', 'gamma', 'delta',
    'beta', 'beta', 'epsilon'
]

# Find the positions of all 'beta's

# Using list comprehension
pos = [
    x for (x, y) in enumerate(data)
        if y == 'beta'
]
print(pos) # positions of 'beta's