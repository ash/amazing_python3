# Passing arbitrary number of 
# arguments to a function

def my_f(*args):
    # Notice the "*"
    print(
        f'Called with {len(args)} arg(s)'
    )
    for index, value in enumerate(args):
        print(f'Arg #{index} = {value}')

my_f(5)
my_f(1, 2)
my_f('a', 'b', 'c')
