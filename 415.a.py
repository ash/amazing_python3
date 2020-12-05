data = [
    [1, 2], [3, 4], [5, 6]
]

sum(data, [])
# Is equivalent to:
[] + data[0] + data[1] + data[2]

# Which is:
[] + [1, 2] + [3, 4] + [5, 6]
