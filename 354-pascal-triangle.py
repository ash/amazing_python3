# Pascal's triangle

N = 13
data = [0] * (N + 1)
data[N//2] = 1
print(data) # start position

while data[0] == 0:
    for i in range(N//2):
        data[i] += data[i + 1]
    print(str(
        list(
            filter(
                lambda x: x != 0, data
            )
        )
    ).center(N * 3)) 