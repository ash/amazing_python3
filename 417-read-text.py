# Using "pathlib" library.
# Available in Python 3.4+

import pathlib

# Let's read the program itself :-)
f = pathlib.Path('417-read-text.py')
print(f.read_text())

# The file is now closed btw.