# Another way of incrementing
# all elements of a list

data = [10, 20, 30, 40, 50, 60]

# Let's use map and lambda
data = list(
    map(lambda x: x + 1, data)
)
print(data)