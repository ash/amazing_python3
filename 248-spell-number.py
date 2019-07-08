# Spelling the number

import inflect

n = 573
e = inflect.engine()
print(e.number_to_words(n))
