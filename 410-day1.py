#!/usr/bin/env python3

import itertools
import math

data = []
with open('items.txt') as f:
    data = [int(x) for x in f.readlines()]

for size in range(2, 4):
    for curr in \
        itertools.combinations(data, size):
        if sum(curr) == 2020:
            print(math.prod(curr))
            break
