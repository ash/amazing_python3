import turtle
from random import choice, randint
cho1 = ('red', 'green', 'blue')
for x in range(500):    
    turtle.pencolor(choice(cho1))
    turtle.forward(randint(1, 50))
    turtle.right(randint(33, 90))
