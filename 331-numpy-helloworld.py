# NumPy operates with N-dimensional
# data
import numpy

data = numpy.array(
    [
        [1, 3, 5, 7],
        [2, 4, 6, 8] # Two axes
    ]
)
print(data.shape) # 2 by 4
print(data.ndim) # 2 dimensions
print(data.size) # 8 elements
print(type(data)) # its class