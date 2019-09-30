# How to invert a dictionary
# (how to change keys and values)

data = {
    "alpha": "a",
    "beta": "b",
    "gamma": "c"
}

# Using dictionary comprehension
new_data = {
    value: key for key, value \
        in data.items()
}

print(new_data)
