# Sort a list of lists using the
# second item in each sublist

data = [
    ["two", 2], ["one", 1],
    ["four", 4], ["three", 3]
]
# The task is to print the list
# so that it reads "one, two, three..."

data.sort(
    key = lambda d: d[1]
    # using the second (index 1)
    # item to serve as a key
)
print(data) # sorted in place