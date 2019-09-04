# Using your own sorting function
# to sort data

def sort_func(item):
    # Let us sort by length
    return len(item)

data = [
    'alpha', 'beta', 'gamma',
    'delta', 'epsilon'
]
data.sort(key = sort_func) # without ()
print(data)
