# Using "ChainMap"
from collections import ChainMap

# Two dictionaries
europe = {'FR': 'Paris', 'DE': 'Berlin'}
asia = {'CN': 'Beijing', 'IN': 'Delhi'}

capitals = ChainMap(europe, asia)

print(capitals["FR"])
print(capitals["IN"])
