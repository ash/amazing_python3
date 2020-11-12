# Let's print 10 different(!) 
# random integer numbers
# below 20

import random

used = set()
while 1:
    n = random.randrange(20)
    if not(n in used):
        used.add(n)
        print(n)
    if len(used) == 10:
        break
