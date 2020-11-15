import sys

n = int(sys.argv[1])

sign = 1 if n > 0 else -1
str_n = str(abs(n))
str_n = str_n[::-1]

r = sign * int(str_n)
print(r)
