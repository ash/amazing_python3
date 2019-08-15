# Check if all elements of a list
# are unique

data = [3, 5, 7, 9, 5]

# Convert it to a set
data_set = set(data)

# And check the lengths
# of the two data structures

print(len(data) == len(data_set))

# If the same, then all elems are
# unique