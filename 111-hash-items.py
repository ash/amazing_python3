# Iterating over dictionary pairs
# (both keys and values)

capitals = {
    'France': 'Paris',
    'Italy': 'Rome',
}

for country, city in capitals.items():
    # country = key
    # city = value
    print('The capital of ' + \
        country + ' is ' + city + '.')
