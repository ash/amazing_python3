# Flatten a list of lists
data = [
    [1, 2], [3, 4], [5, 6]
]

result = []
for x in data:
    for y in x:
        result.append(y)

print(result)
