# Normally distributed random numbers
# (Gaussian distribution)

import random

n = 10
N = 100000
hist = [0] * n
mean = 10
sigma = 2

for _ in range(N):
    r = random.gauss(mean, sigma)
    bin = int(r - mean / 2)
    if bin < 0: bin = 0
    elif bin >= n: bin = n - 1
    hist[bin] += 1

for i in range(n):
    print(hist[i])
