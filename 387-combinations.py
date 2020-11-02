# Making all 3-item combinations
# from the items in a list

from itertools import combinations

data = [1, 3, 5, 7, 9]
for x in combinations(data, 3):
    print(x)
