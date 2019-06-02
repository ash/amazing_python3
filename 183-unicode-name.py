# Printing the Unicode names
# of the characters

import unicodedata

str = 'Héļļö'

for s in str:
    print(unicodedata.name(s))
