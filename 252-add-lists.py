# Adding up the elements of
# two lists of integers (or floats,
# or even strings)

import operator
# We need "+" as a function

data1 = [1, 3, 5, 7, 9]
data2 = [2, 4, 6, 8, 10]

data3 = list(
    map(operator.add, data1, data2)
)
print(data3)
