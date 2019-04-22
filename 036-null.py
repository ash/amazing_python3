# Testing "empty" values
# in boolean context

x = 0
if x:
    print('True')
else:
    print('False')

x = ''
if x:
    print('True')
else:
    print('False')