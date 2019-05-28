# Remove newline characters from
# the strings in a list
data = [
    'alpha\n',
    'beta\n',
    'gamma\n'
]
print(data)

data = [
    s.strip() for s in data
    # list comprehension
]
print(data)