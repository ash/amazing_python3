# BEFORE

from random import randint

pwd = ''

for n in range(15):
    pwd = pwd + chr(randint(33, 127))
print(pwd)
