# Write to a text file

f = open('t.txt', 'w')
# or:
#f = open('t.txt', mode='w')
# w = create and write
# r = read (default)
# a = append
# x = create if not existed

f.write('Hello, World!')
f.close()

