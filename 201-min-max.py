# Find the minimum and maximum
# values WITHOUT using the "min"
# and "max" functions

data = [3, 4, 77, 1, 34, 7]

min_val = data[0]
max_val = data[0]

# normally do this:
# print(min(data))
# print(max(data))

for x in data:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
print(min_val)
print(max_val)