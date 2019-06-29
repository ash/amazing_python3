# Bubble sort

data = [4, 7, 1, 4, 8, 9, 3, 2, 5, 6]

done = 0
while not done:
    done = 1
    for n in range(1, len(data)):
        # scan left to right
        if data[n-1] > data[n]:
            # swap two adjacent items
            data[n-1], data[n] = \
                data[n], data[n-1]
            done = 0 # continue

print(data)