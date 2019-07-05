# Getting line number N from
# a text file

import linecache

line_n = linecache.getline(
    'greek.txt', 4
)
print(line_n)
