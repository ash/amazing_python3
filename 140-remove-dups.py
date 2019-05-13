# Remove duplicates from a list
# and make sure the order is saved

data = [10, 12, 10, 33, 2, 2, 5, 2]
result = []

values = set()
for i in data:
    if i not in values:
        values.add(i)
        result.append(i)

print(result)
