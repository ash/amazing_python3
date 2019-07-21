# Convert a list of tuples
# to a list of lists

data = [
    (3, 4), (7, 8), (100, 200)
]

# Another method
data2 = list(map(list, data))
# That's it.
print(data2)