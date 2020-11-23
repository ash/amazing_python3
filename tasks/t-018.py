for n in range(1, 70):
    col = ''
    while n > 26:
        x = n % 26
        col = chr(x - 1 + ord('A')) + col
        n //= 26
    col = chr(n - 1 + ord('A')) + col
    print(col, end=' ')
print('')
