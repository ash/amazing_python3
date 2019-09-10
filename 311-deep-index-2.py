# How to get deeply located item

data = [3, 5, 7, [9, 11]]
# We need to print "11"

# Here is another way of solving the
# same task
element = data[-1][-1]
# You can count from right to left
print(element)

# [-1] gets the fourth item in data,
# which is a list [9, 11]

# [-1][-1] gets the second item in that
# list [9, 11], that is "11"