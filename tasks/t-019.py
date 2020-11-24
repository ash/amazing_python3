data = [3, 5, 7, 9, 11, 13, 15]

for i in range(len(data) // 2):
    data[i], data[-1 - i] = data[-1 - i], data[i]

print(data)
