# Generating a series 
# of *different* random numbers

from random import randint

data = set()
n = 0
while n < 20:
    r = randint(0, 100)
    if r not in data:
        n += 1
        data.add(r) # new number
    
print(len(data)) # got 20 items
print(data) # all different