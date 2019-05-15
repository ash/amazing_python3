# A safer way of reading values from
# a dictionary

data = {
    'France': 'Paris',
    'Italy': 'Rome'
}

# capital = data['Germany'] # error
capital = data.get('Germany') # OK
# but it returns 'None'
print(capital)

capital = data.get('Germany', '??')
print(capital) # prints "??"