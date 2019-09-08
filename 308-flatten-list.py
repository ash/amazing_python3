# Make a flat list ouf of this one:
data = [1, 3, [5, 7], 9, 11]

# should become:
# [1, 3, 5, 7, 9, 11]

d = []
for x in data:
    # if x is iterable, i.e. a list
    if hasattr(x, '__iter__'):
        d.extend(x)
    else:
        # e.g., for integers
        d.append(x) 
print(d)