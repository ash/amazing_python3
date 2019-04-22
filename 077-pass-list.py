# Passing a list to a function

my_list = [10, 20, 30, 40]

def f(x):
    x[2] = 'TWO'

f(my_list)
print(my_list)
