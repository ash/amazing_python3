data = [3, 5, 8, 7, 6, 0, 1, 3, 7, 0]

# Step 1. Convert a list to a set.
# Set can only host an element once.
#
# Step 2. Convert a set back to a list.

data = list(set(data))

print(data)
# [0, 1, 3, 5, 6, 7, 8]
