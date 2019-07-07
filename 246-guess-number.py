# Guess the number

import random

while 1:
    n = random.randint(0, 10)
    while 1:
        i = int(input('Your guess: '))
        if i > n:
            print('Too big')
        elif i < n:
            print('Too small')
        else:
            print('Correct!')
            break
