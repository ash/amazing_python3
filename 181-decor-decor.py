# If you have two decorators.
# Which one is called first?

def decor1(f):
    print('decor1')
    return f

def decor2(f):
    print('decor2')
    return f

@decor1
@decor2
def my_func():
    print('my_func')

my_func()