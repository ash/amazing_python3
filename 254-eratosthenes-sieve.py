# Getting prime numbers below 100
# using the sieve of Eratosthenes
n = 100
s = list(range(1, n + 1))
p = 2
while p < n / 2:
    for i in range(2 * p, n + 1, p):
        s[i - 1] = 0
    for i in range(0, n):
        if s[i] > p:
            p = s[i]
            break
s = list(filter(lambda x: x != 0, s))
print(s) # done :-)