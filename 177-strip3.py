# Remove newline characters from
# the strings in a list
data = [
    'alpha\n',
    'beta\n',
    'gamma\n'
]
print(data)

# Let's replace a separate function
# with a lambda
data = list(map(
    lambda s: s.strip(), data))
# map returns an object of the 
# "map" type
print(data)