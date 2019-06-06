# Removing an element from a list
# (if there are more such elements)

# How to remove all "beta"s
data = [
    'alpha', 'beta', 'gamma',
    'beta', 'delta', 'beta'
] 

data = [x for x in data if x != 'beta']
print(data)
