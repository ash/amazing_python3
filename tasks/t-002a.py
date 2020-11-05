# The program prints ‘fizz’ if the
# number is divisible by 3 and ‘buzz’
# if it is divisible by 5.

for i in range(5, 20):
    print(i, end=': ')
    if not(i % 15):
        print('fizzbuzz', end='')
    elif not(i % 3):
        print('fizz', end='')
    elif not(i % 5):
        print('buzz', end='')
    print('') # newline actually

    