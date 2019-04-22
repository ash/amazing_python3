# Generating a series 
# of *different* random numbers

from random import randint

data = set() # Set can contain each
# value only once
while len(data) < 20:
    r = randint(0, 100)
    data.add(r) # new or existing
                # number
    
print(len(data)) # got 20 items
print(data) # all different
# Let us simplify the above