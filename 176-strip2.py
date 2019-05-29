# Remove newline characters from
# the strings in a list
data = [
    'alpha\n',
    'beta\n',
    'gamma\n'
]
print(data)

def strip(s):
    return s.strip()
    
# Let's use "map" this time
data = list(map(strip, data))
# map returns an object of the 
# "map" type
print(data)