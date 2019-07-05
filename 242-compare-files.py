# Comparing two files

import filecmp

file1 = 'file1.txt'
file2 = 'file2.txt'

print(filecmp.cmp(file1, file2))
