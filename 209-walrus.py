# Using the new := operator
# in Python 3.8

# Read and print lines before you 
# meet STOP

with open('input.txt') as f:
    while (
        str := f.readline().strip()
    ) != 'STOP':
        print(str)