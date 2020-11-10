from itertools import combinations

data = [1.5, 0.4, 0.1, 2.5, 0.6, 0.2]

for choice in combinations(data, 3):
    if 1 < sum(choice) < 2:
        print(choice)
