# Reading from a JSON file
# Let us improve this program a bit
import json

data = []
with open('capitals.json') as f:
    data = json.load(f)
    # Here, the file is still open

# Now the file is closed
for x in data:
    print(
        x["country"], '—',
        x["capital"]
    )
