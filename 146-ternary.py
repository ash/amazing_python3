# Need a ternary operator?
# Use conditional expression

for i in range(1, 5):
    # is i odd or even?
    oe = 'odd' if i % 2 else 'even'
    print(f'{i} is {oe}')
