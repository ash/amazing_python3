# Caching function return values
# when you call it with the same 
# argument(s)

from functools import lru_cache
# LRU = least recently used
@lru_cache(maxsize=1000)
def factorial(n):
    if n <= 1:
        return 1
    print(f'Computing {n}!')
    return n * factorial(n - 1)

print(factorial(5)) # no cache yet
print(factorial(3)) # uses cache
print(factorial(6)) # both cache
                    # and a new
                    # computation