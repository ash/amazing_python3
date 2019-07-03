# Getting the median value

import statistics

data1 = [1, 2, 10, 20, 100]
#              ^^
# 5 items

data2 = [1, 2, 10, 20, 100, 200]
#                ^^
# 6 items

print(statistics.median(data1))
print(statistics.median(data2))