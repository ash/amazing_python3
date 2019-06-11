# Transpose a matrix

matrix = [
    [10, 20, 30],
    [40, 50, 60]
]

# Using nested list comprehensions
transposed_matrix = [
    [
        matrix[j][i] 
            for j in range(len(matrix))
    ]
    for i in range(len(matrix[0]))
]

print(transposed_matrix)