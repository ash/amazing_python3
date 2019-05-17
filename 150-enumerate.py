# Using "enumerate"

data = [
    'alpha',
    'beta',
    'gamma'
]

for index, value in enumerate(data):
    # index = number of the element
    # in the list
    # value = the item itself
    print(f'The element #{index} '
          f'is {value}')