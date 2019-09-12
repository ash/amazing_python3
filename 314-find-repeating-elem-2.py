# Find the first repeating element
# in a list, print it and quit

data = [3, 5, 7, 5, 9, 11]
# 5 is the answer

# Faster method (for big data lists)
seen = set()
for x in data:
    if x in seen:
        print(x)
        break
    seen.add(x)
