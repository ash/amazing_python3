# AFTER

from random import randint

pwd = ''

for _ in range(15):
    pwd += chr(randint(33, 127))
print(pwd)
