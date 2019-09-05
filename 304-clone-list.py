# Cloning a list

a = [3, 5, 7]
b = a # b is the same as a
b[2] = 99
print(a) # will contain 99


c = [3, 5, 9]
# Two ways of cloning:
d = c.copy() 
e = c[:]
d[2] = 77
e[2] = 88
print(c) # not modified
print(d, e)
