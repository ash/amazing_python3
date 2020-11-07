e = 1
factorial = 1

for n in range(1, 20):
    factorial *= n
    e += 1 / factorial

print(e) # 2.7182818284590455
