# Imagine you have a loop over a list
data = [1, 3, 5, 7, 9]

# Let's check how many times the "range"
# function is really called.

# Define our own function instead
def f():
    print('Called f()')
    return range(len(data))

for i in f():
    print(data[i])
