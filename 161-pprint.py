# Using "pprint" to make the output
# of data structures more readable

import pprint

data = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

# make the printer
p = pprint.PrettyPrinter(width=1)
p.pprint(data)