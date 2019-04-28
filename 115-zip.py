# Using the "zip" built-in
# function

colours = ['red', 'green', 'yellow']
fruits = ['apple', 'pear', 'banana']

z = zip(colours, fruits)

for x in z:
    # x is a tuple
    print(x[0] + ' ' + x[1])
