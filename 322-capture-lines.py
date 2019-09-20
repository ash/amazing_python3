# What if you capture an output that
# takes more than one line?

import subprocess

cal = subprocess.getoutput(
    'cal oct 2019'
)

print(type(cal)) # it is still a string
# but it contains many lines separated
# by \n

print(cal)
