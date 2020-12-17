# Using f-strings to interpolate
# the fields of a dictionary

data = {
    "name": "John",
    "age": 22,
}

print(
    f"{data['name']} is {data['age']}."
)

# Should be:
# John is 22.
