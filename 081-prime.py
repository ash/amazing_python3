# Print the first prime numbers
# below 20

def is_prime(n):
    for i in range(2, n):
        if not(n % i):
            # found divisor,
            # thus is not prime
            return False 
    return True # is prime

for n in range(1, 20):
    if is_prime(n):
        print(n)
