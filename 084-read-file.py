# Reading from a text file

for str in open('data.txt'):
    print(str, end='')

# we should not print the 
# newline after each string, 
# as "str" already contains it