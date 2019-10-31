# Check if two lists have the same
# items in them, regardless the order.

from collections import Counter

data1 = [1, 2, 3, 4, 5]
data2 = [4, 3, 5, 1, 2]

c1 = Counter(data1)
c2 = Counter(data2)
# Count how many times each element 
# occures in a list.

print(c1 == c2)
