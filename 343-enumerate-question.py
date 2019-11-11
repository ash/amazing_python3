# How to print both
# indices and values 
# of a list?

# Here is a list:
data = ['red', 'green', 'blue']

# Let us use a built-in function
# "enumerate"
for index, value in enumerate(data):
    print('index =', index)
    print('value =', value)
