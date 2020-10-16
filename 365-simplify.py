# Let us simplify the code a bit!

from random import randint

pwd = ''

# The variable "n" is not used.
# Replace it with _
for _ in range(15):
    # pwd is assigned to itself plus
    # something more, let us use +=
    pwd += chr(randint(33, 127))
print(pwd)

# Good!