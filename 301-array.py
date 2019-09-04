# Using the "array" module at a glance

import array

a = array.array('i', [7, 9, 11])
# 'i' = integer

print(a)

# a[1] = '99' # error, as it is a string
a[1] = 99 # correct, this is integer
print(a)
