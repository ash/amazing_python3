# Short-circuit behaviour of
# Boolean operators

def f1():
    print('f1 called')
    return True

def f2():
    print('f2 called')
    return False

x = f1() or f2() # f2 not called
print(x)

x = f1() and f2() # f2 called too
print(x)