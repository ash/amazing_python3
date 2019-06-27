# Calculator that parses operations

ops = { # operations
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def calc(x, y, op): # op = operator
    return ops[op](x, y)

print(calc(3, 4, '+')) # 7
print(calc(3, 4, '-')) # -1
print(calc(3, 4, '*')) # 12
print(calc(3, 4, '/')) # 0.75
