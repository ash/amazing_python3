# Passing arbitrary number
# of named arguments to a function

def my_f(**args): # two stars
    print(type(args)) # is a dict
    for k, v in args.items():
        print(f'{k} = {v}')

my_f(capital='Paris', country='France')
my_f(name='John', lastname='Smith')
