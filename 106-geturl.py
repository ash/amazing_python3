# Fetching a text file from the web

import requests

url = 'https://raw.githubusercontent.com/ash/amazing_python3/master/sample.txt'                 
r = requests.get(url)

print(r.status_code) # should be 200
print(r.content) # you get a byte
                 # literal
