def is_prime(n):
    if n < 2: # 1 is not prime
        return False
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

for x in range(50):
    if is_prime(x):
        print(x)
