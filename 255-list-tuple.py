# Convert a list of tuples
# to a list of lists

data = [
    (3, 4), (7, 8), (100, 200)
]

# Using list comprehension
data2 = [
    # "a" was a tuple here
    list(a) for a in data
]
print(data2)