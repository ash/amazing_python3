# Filtering ("grepping") data
# using comprehensions

data = list(range(10))
print(data)

# Now filter it.
# And select only small numbers.

data = [
    x for x in data if x < 4
]
print(data)
