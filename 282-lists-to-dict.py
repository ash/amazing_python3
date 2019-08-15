# Create a dictionary out of 
# two lists: the list of values
# and the list of the keys

capitals = ["Paris", "Berlin"]
countries = ["France", "Germany"]

data = dict(zip(capitals, countries))
print(data)
