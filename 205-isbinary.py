# Check if the given text string
# can represent a binary number
# (in its string format, i.e. with
# regular 1 an 0 as characters)

s1 = '11010101' # OK
s2 = '10111400' # Not OK

import re # regular expressions

if re.search('[^01]', s1):
    print('s1 is not binary')

if re.search('[^01]', s2):
    print('s2 is not binary')

# [^01] - anything that is not 0 or 1