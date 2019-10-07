# How to read the Nth line
# of a text file

with open('lines.txt') as f:
    lines = f.readlines()
    print(lines[3]) # fourth line
