# Copying lists

data = [3, 5, 7, 9]

data2 = data # the same list
data3 = data.copy() # new list 

data2.insert(1, 199) # changes
# both data and data2

data3.insert(1, 299) # only changes
# data3. data stays unchanged

print(data)
