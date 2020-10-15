# Generating random passwords

from random import randint

pwd = ''

for n in range(15): # 15 characters
    pwd = pwd + chr(randint(33, 127))
print(pwd)

# 33 to 126 - ASCII code positions
