import sys

output = ['1']

def save_row(row):
    strings = [str(item) for item in row]
    strings.insert(0, '1')
    output.append(' '.join(strings))

n = int(sys.argv[1])
data = [1]
save_row(data)

for row_n in range(n - 2):
    data.insert(0, 1)
    for i in range(len(data) - 1):
        data[i] += data[i + 1]
    save_row(data)

max_width = len(output[-1])
for line in output:
    print(line.center(max_width))
