# Adding annotations to a function

def power(a: int, b: int) -> int:
    return a ** b

# Function takes two "int"s and
# returns an "int"

print(power(2, 3))

print(power.__annotations__)
