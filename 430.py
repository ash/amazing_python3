# You have a list of lists of numbers:

data = [
    [3, 4, 5], [8, 5, 7],
    [4], [9, 6, 3, 7, 8],
    [4, 3, 8, 3], [2, 5]
]

# Count how many times "5" appears there.

# 1. Flatten the list
# 2. Use "count"

print(sum(data, []).count(5)) # 3
