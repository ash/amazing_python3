# Transposing a matrix with NumPy
import numpy

data = numpy.array(
    [
        [1, 3, 5, 7],
        [2, 4, 6, 8] # Two axes
    ]
)
data = data.transpose()
print(data)
