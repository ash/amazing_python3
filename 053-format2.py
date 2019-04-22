# What if you need to print
# two names?

name1, name2 = 'John', 'Karla'

# Old style
print('Hello, %s and %s!' % (
    name1, name2
))

# New style
print('Hello, {} and {}!'.format(
    name1, name2
))