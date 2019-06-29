# Check the quality of the generator
# of random numbers

import random

N = 10 # 10 bins in a histogram
NUMS = 10000 # repeats
MAX = 1000 # maximum random number
hist = [0] * N # histogram

for _ in range(NUMS):
    r = random.randint(0, MAX - 1)
    bin = r / (MAX / N)
    hist[int(bin)] += 1
print(hist) # all bins should be
# more or less equal