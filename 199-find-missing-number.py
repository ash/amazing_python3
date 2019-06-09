# Find a missing number in a list
data = [3, 8, 1, 9, 4, 10, 6, 7, 2]
# 5 is missing; list is not sorted

# You can also transform a list to
# a set to make the solution faster
# for bigger data arrays:
data = set(data)
for i in range(1, len(data) + 1):
    # 1..10
    if i not in data:
        print(f'{i} is missing')
        # done; it's found
        break
