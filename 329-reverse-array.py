# Different ways to reverse a list

data = [1, 3, 5, 7, 9]

# 1. Use a range with negative step
print(data[::-1])
# original list not modified

# 2. reversed function
print(list(reversed(data)))
# list not changed
# neet do convert to a list again

# Now the list will be changed in
# place
data.reverse()
print(data)