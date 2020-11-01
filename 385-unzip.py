# Let's "unzip" the pairs

data = [
    (1, 'a'), (2, 'b'), (3, 'c')
]

a, b = zip(*data)
print(a)
print(b)

print(type(a))