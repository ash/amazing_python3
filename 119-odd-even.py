# Splitting data into
# odd and even numbers

data = [
    45, 56, 67, 23, 57, 78, 67, 454
]
odd = []
even = []

for d in data:
    if d % 2:
        odd.append(d)
    else:
        even.append(d)
print(f'Odd numbers: {odd}')
print(f'Even numbers: {even}')