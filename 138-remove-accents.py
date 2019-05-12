# Removing accents from characters

import unidecode

str = 'Café München'

str = unidecode.unidecode(str)
print(str)
