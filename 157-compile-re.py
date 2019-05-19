# Compile regular expressions to
# make them faster

import re
from time import time

count=0
t0 = time()

r = re.compile('\d') # compile it
for i in range(100_000):
    if r.match(chr(i)):
        # use that compiled one
        count+=1
print(time() - t0)
print(count)
