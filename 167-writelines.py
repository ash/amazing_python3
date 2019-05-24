# Be careful when using 
# "writelines"

data = [
    'alpha',
    'beta',
    'gamma'
] # some strings
with open('data2.txt', 'w') as f:
    f.writelines(data)

# No newlines will be added