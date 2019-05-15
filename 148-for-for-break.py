# Nested "for" loops and "break"

for x in range(5):
    for y in range(5):
        if x == 3 or y == 3:
            break
        print(f'x={x}, y={y}')
