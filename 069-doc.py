# Creating simple documentation

def my_f(x):
    '''This function returns
a doubled value
of its argument'''
    return x * 2

print(my_f(15))

# Print the doc:
print(my_f.__doc__)
