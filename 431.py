# Concatenating the elements of a list

items = ['a', 'b', 'c', 'd']

# We need to get the string "abcd"

s = ''.join(items)
# '' is the empty string that is 
# put between the items of the list
print(s) # abcd

# Not let's get this: "a b c d"
s2 = ' '.join(items)
print(s2)
