import re

lines = []
with open('input.txt') as f:
    lines = f.readlines()

good = 0
for line in lines:
    m = re.search('(\d+)-(\d+) (\w): (\w+)', line)
    count = m.group(4).count(m.group(3))
    if int(m.group(1)) <= count <= int(m.group(2)):
        good += 1

print(good) # 454
