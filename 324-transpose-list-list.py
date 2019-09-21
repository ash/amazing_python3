# Transposing a two-dimensional list

data = [
    [1, 2], [3, 4], [5, 6], [7, 8]
]

tr_data = list(zip(*data))
# That's it.

print(tr_data)
