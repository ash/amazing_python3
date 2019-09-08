# Make a flat list ouf of this one:
data = [1, 3, [5, [7, 77]], 9, 11]
# Let us allow nested loops
# Should still become a flat list:
# [1, 3, 5, 7, 77, 9, 11]

def flatten(data):
    d = []
    for x in data:
        # if x is iterable, i.e. a list
        if hasattr(x, '__iter__'):
            d.extend(flatten(x))
            # called recursively
        else:
            # e.g., for integers
            d.append(x) 
    return d

print(flatten(data))

