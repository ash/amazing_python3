# Let's print 10 different(!) 
# random integer numbers
# below 20

import random

used = set()
while len(used) != 10:
    n = random.randrange(20)
    if not(n in used):
        used.add(n)
        print(n)
