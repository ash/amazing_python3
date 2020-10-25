# "Unpacking" values

a, *b = 1, 2, 3, 4, 5
print(a) # 1
print(b) # [2, 3, 4, 5]

*c, d = 1, 2, 3, 4, 5
print(c) # [1, 2, 3, 4]
print(d) # 5
