# Reading from a JSON file

import json

with open('capitals.json') as f:
    data = json.load(f)

    for x in data:
        print(
            x["country"], '—',
            x["capital"]
        )
