# Transposing a matrix with NumPy
# The ndarray class in NumPy has the "T"
# attribute, which is a synonym of
# "transpose"
import numpy

data = numpy.array(
    [
        [1, 3, 5, 7],
        [2, 4, 6, 8] # Two axes
    ]
)
data.T # transpose
print(data)
