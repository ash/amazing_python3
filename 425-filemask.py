# Matching filenames using Unix-style
# shell filename patterns

from fnmatch import fnmatch

files = ['data.txt', 'index.txt',
    'index1.txt', 'index.tar.gz']

for filename in files:
    if fnmatch(filename, 'index*.txt'):
        print(filename)
