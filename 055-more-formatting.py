# When the new style of string
# formatting can be very handy

a, b = 10, 20
print('a + b = b + a')
print(
    '{0} + {1} = {1} + {0}'.format(
        a, b
    )
)
# {0} is replaced with a
# {1} is replaced with b
# but you only mention them once
