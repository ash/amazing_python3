# How to get deeply located item

data = [3, 5, 7, [9, 11]]
# We need to print "11"

element = data[3][1]
print(element)

# [3] gets the fourth item in data,
# which is a list [9, 11]

# [1] gets the second item in that
# list [9, 11], that is "11"