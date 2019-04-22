# Using iterators

my_list = ['alpha', 'beta', 'gamma']

# Make the list iterable
data = iter(my_list)

a = next(data)
print(a)

a = next(data)
print(a)

a = next(data)
print(a)
