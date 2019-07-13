# From a list of lists, select all
# sublists that contain negative
# numbers

data = [
    [1, 5], [2, -3, 1], [10, -1], 
    [-8], [8], [10, 1], [-5, 4, 4, -2]
]

with_neg = [
    d for d in data if min(d) < 0
    # "d" is a sublist
]
print(with_neg)
