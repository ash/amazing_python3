data = [3, 4, 6, 8, -1, -4, 0, 7]

max = min = data[0]
for n in range(1, len(data)):
    if data[n] < min:
        min = data[n]
    if data[n] > max:
        max = data[n]

print('Minimum =', min)
print('Maximum =', max)
