# Tell if all elements of a list
# are the same.
# Solution 2. Using "all"

data1 = [4, 4, 4, 4, 4] # True
data2 = [4, 5, 4, 4, 4] # False

print(
    all(
        map(lambda x: x == data1[0], data1)
        # comparing all items with
        # the first one.
        # if all are true, then the list
        # contains equal eleemnts.
    )
)
print(
    all(
        map(lambda x: x == data2[0], data2)
    ))