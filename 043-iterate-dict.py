# When iterating over 
# a dictionary, you get
# the keys of it

data = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}
for country in data:
    print('The capital of ' +
          country + ' is ' +
          data[country])