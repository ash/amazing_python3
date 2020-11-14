# Getting exchange rates and converting
# EUR to USD

import urllib.request
import json

URL = 'https://api.exchangeratesapi.io' +\
      '/latest?base=EUR'

with urllib.request.urlopen(URL) as api:
    data = json.loads(api.read().decode())
    rate = data['rates']['USD']
    print('€1.00 = $' + str(rate))
