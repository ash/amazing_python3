# Find the first repeating element
# in a list, print it and quit

data = [3, 5, 7, 5, 9, 11]
# 5 is the answer

# "Slow" method first
for x in data:
    if data.count(x) > 1:
        print(x)
        break
    