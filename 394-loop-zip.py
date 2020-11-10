# Iterating over two lists
# simultaneously.

greek = ['α', 'β', 'γ', 'δ', 'ε']
latin = ['a', 'b', 'g', 'd', 'e']

# Using "zip".
# No explicit indices needed.
for gr, lat in zip(greek, latin):
    print(gr, '~', lat)

# Uncomment to see:
# print(list(zip(greek, latin)))
