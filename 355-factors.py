# List all the factors of a given
# number

N = 11

for x in range(1, N):
    if N % x == 0:
        print(x)
