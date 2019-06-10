# Find the (only) duplicate
# number in the given list
# of integers

data = [3, 4, 7, 8, 1, 2, 4, 9]
# "4" to be found

seen = set()
for x in data:
    if x in seen:
        # if we already met x
        print(x)
        break
    seen.add(x) # keep collecting
else:
    print('No duplicates found')