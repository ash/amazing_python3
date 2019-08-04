# How to merge two dictionaries
# Method 2

capitals = {
    'France': 'Paris',
    'Italy': 'Rome',
}

more_capitals = {
    'Germany': 'Berlin',
}

capitals = {**capitals, **more_capitals}
# It is actually equivalent to:
# capitals = {'France': 'Paris', 'Italy':
# 'Rome', 'Germany': 'Berlin'}
# (google for "kwargs" to see what "**" is)
print(capitals)
