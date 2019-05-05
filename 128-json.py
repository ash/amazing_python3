# Saving a data structure in a file
# in JSON
import json

data = {
    "alpha" : [3, 5, 7],
    "beta"  : [4, 6, 8]
}

with open('data.json', 'w') as f:
    json.dump(data, f)

# ...
# using text format now
with open('data.json', 'r') as f:
    restored = json.load(f)
    print(restored)
