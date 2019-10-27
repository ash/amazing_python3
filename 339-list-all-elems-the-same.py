# Tell if all elements of a list
# are the same

data1 = [4, 4, 4, 4, 4] # True
data2 = [4, 5, 4, 4, 4] # False

print(
    len(set(data1)) == 1
)

print(
    len(set(data2)) == 1
)

# Convert a list to a set. Equal
# elements will collapse.