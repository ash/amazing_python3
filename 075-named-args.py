def my_f(a, b):
    return a**b;

# With named arguments, you
# can change their order when
# calling a function

print(my_f(2, 3))
print(my_f(a = 2, b = 3))

# Different order
print(my_f(b = 2, a = 3))
