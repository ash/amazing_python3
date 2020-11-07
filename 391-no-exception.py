# How to supress an exception
# (for a piece of code)

from contextlib import suppress

with suppress(ZeroDivisionError):
    for n in range(-3, 3):
        print(f'42 / {n} = ', 42 /n)
print("Done?")
