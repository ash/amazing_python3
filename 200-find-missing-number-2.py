# Another way of finding a missing
# number in a list

data = [3, 8, 1, 9, 4, 10, 6, 7, 2]

s = sum(data) # sum of all items

max = len(data) + 1 # maximum number
s2 = max * (max + 1) / 2 # sum of all
# numbers from 1 to 10 including 10

print(f'{s2 - s} is missing') 
# the missing number is actually the
# difference between those two sums