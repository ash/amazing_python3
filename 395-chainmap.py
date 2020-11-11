# Using "ChainMap"
from collections import ChainMap

# Two dictionaries
europe = {'FR': 'Paris', 'DE': 'Berlin'}
asia = {'CN': 'Beijing', 'IN': 'Delhi'}

capitals = ChainMap(europe, asia)

# Print countries
print(list(capitals.keys()))

# Print capitals
print(list(capitals.values()))
