# Converting a list of strings
# to a list of integers

print('Enter three numbers: ')
data = []
for _ in range(3):
    data.append(input())
    # these are strings yet
print(data) # strings

numbers = list(map(int, data))
# Converts strings to ints:
# for each item in "data",
# int(x) is called
print(numbers) # numbers