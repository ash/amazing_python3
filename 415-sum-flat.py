# Flattening an list of lists

data = [
    [1, 2], [3, 4], [5, 6]
]

result = sum(data, [])

print(result)
# It prints the array with 
# a flat structure:
# [1, 2, 3, 4, 5, 6]
