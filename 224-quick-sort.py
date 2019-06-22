# Quick sort algorithm
data = [4, 7, 1, 4, 8, 9, 3, 2, 5, 6]

def quicksort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = []
    right = []

    for x in data[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quicksort(left) + \
        [pivot] + quicksort(right)

data = quicksort(data)
print(data)
