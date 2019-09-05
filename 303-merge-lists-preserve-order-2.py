# Merge two lists so that there are
# no duplicates in the output, and
# preserve the order of the items

data1 = [3, 5, 7, 9, 11]
data2 = [5, 8, 10, 11, 12]
# Both lists contain only unique
# elements 

# Another solution using list
# comprehension

data = data1.copy()
data.extend(
    [x for x in data2 if x not in data1]
)
print(data) # merged
