# Digits in the Unicode space

import re
count=0
for i in range(32, 10_000):
    ch = chr(i) # character with
    # the Unicode code i
    if re.match('\d', ch):
    # if re.match('\d', ch, re.ASCII):
        # if it is a digit
        print(ch, end='')
        count+=1
print('')
print(count)

# How many digits will be printed?