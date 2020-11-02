# Test if all the numbers in a list
# are positive

data = [1, 2, 4, 7, 10]

if all(x > 0 for x in data):
    print('All positive ints')
else:
    print('No')
