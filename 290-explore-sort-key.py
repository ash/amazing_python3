# Using your own sorting function
# to sort data
# For your curiosity, explore how Python
# calls the sorting function

def sort_func(item):
    # Print the passed item
    print(item)
    return len(item)

data = [
    'alpha', 'beta', 'gamma',
    'delta', 'epsilon'
]
data.sort(key = sort_func) # without ()
print(data)
