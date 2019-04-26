# Using list comprehension
# to "add up" two lists
# element by element

data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

data3 = [data1[i] + data2[i] \
    for i in range(len(data1))]
print(data3)

# data3 = [1 + 2, 3 + 4, 5 + 6, ...]