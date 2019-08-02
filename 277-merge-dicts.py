# How to merge two dictionaries

capitals = {
    'France': 'Paris',
    'Italy': 'Rome',
}

more_capitals = {
    'Germany': 'Berlin',
}

capitals.update(more_capitals)
# Now "capitals" contains everything
print(capitals)
