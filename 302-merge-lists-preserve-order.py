# Merge two lists so that there are
# no duplicates in the output, and
# preserve the order of the items

data1 = [3, 5, 7, 9, 11]
data2 = [5, 8, 10, 11, 12]
# Both lists contain only unique
# elements 

# data = data1 + data2 # wrong, elements
# will be repeated

data = data1
for x in data2:
    if x not in data1:
        data.append(x)
print(data) # merged