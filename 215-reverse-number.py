# "Reverse" a number
# for example, 12345 -> 54321

# method 1
n = 12345
r = int(str(n)[::-1])
print(r)

# method 2
r2 = 0
while n != 0:
    m = n % 10 # last digit
    r2 = r2 * 10 + m
    n //= 10 # integer division
print(r2)
