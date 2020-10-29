# Find the most frequent item
# in a list (of integers here)

data = [10, 20, 30, 10, 20, 40, 20]
# The answer is 20

# 1. Convert the list to a set.
# 2. Find the max using the key
# where the key is the number of
# items.
# 3. Print :-)
print(
    max(set(data), key = data.count)
)
