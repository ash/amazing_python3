# Another way of cloing a list

data = [3, 5, 7]

data2 = list(data) # create a new list
# using the elements of the old list

data2[1] = 99

print(data) # unchanged old data
print(data2) # new copy, changed