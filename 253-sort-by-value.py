# Soring a list of dictionaries by
# values

data = [
    {
        "name": "Kevin",
        "age": 23
    },
    {
        "name": "Mary",
        "age": 22 # shoud go first 
        # by age
    }
]
data.sort(key = lambda p: p['age'])
print(data)