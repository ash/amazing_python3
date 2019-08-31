# What's the difference between
# a[-1] and a[-1:]?

a = ['a', 'b', 'c', 'd', 'e', 'f']

print(a[-1]) # f
print(a[-1:]) # also f

# No difference?
# No, there is 

print(a[-2]) # e
print(a[-2:]) # e, f

print(a[-3]) # d
print(a[-3:]) # d, e, f